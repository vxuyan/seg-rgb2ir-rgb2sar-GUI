from typing import Optional

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QDialog

from ..model.model_runner import ModelRunner
from ..model.project_config_model import ProjectConfigModel
from ..view.main_window import MainWindow
from ..view.project_config_window import ProjectConfigWindow
from .project_config_controller import ProjectConfigController

class MainController:
    def __init__(self, view: MainWindow):
        self.view = view
        self.view.sig_run.connect(self.run_model)
        self.view.sig_open_project_config.connect(self.on_open_project_config)
        self.view.sig_seg_clicked.connect(self.on_seg_clicked)
        self._config_file_path = ProjectConfigModel.default_storage_path()
        self.project_config_model = ProjectConfigModel.load_from_file(self._config_file_path)
        self._runner = ModelRunner()
        self._process: Optional[QProcess] = None
        self._stdout_buffer: str = ""

    def run_model(self, input_dir: str, output_dir: str, weight_dir: str, model_name: str):
        if self._process and self._process.state() != QProcess.NotRunning:
            self.view.append_log("[WARN] 上一次任务仍在执行，请稍候...")
            return

        self._cleanup_process()

        command, pre_logs = self._runner.prepare_model_command(
            model_name, input_dir, output_dir, weight_dir
        )
        for message in pre_logs:
            self.view.append_log(message)

        if not command:
            # 已在 pre_logs 中记录错误信息
            self.view.stop_loading()
            self.view.statusbar.showMessage("模型执行失败")
            return

        self.view.start_loading()
        self.view.statusbar.showMessage("正在执行模型...")

        process = QProcess(self.view)
        process.setProcessChannelMode(QProcess.MergedChannels)
        process.readyReadStandardOutput.connect(self._handle_process_output)
        process.errorOccurred.connect(self._handle_process_error)
        process.finished.connect(self._handle_process_finished)
        process.start(command[0], command[1:])

        self._process = process

    def on_seg_clicked(self):
        valid, message = self.project_config_model.validate()
        if not valid:
            self.view.append_log(f"[ERROR] {message}")
            self.view.statusbar.showMessage(message)
            return

        input_dir = self.project_config_model.input_dir
        output_dir = self.project_config_model.output_dir
        weight_dir = self.project_config_model.weight_dir

        self.view.append_log("[INFO] 开始执行分割模型")
        self.view.statusbar.showMessage("正在执行分割模型...")
        self.view.sig_run.emit(input_dir, output_dir, weight_dir, "seg")

    def on_open_project_config(self):
        dialog = ProjectConfigWindow(self.view)  # 传入主窗口作为父级
        controller = ProjectConfigController(
            dialog, self.project_config_model, parent=dialog
        )
        controller.sig_config_applied.connect(self.on_project_config_applied)
        controller.sig_config_cancelled.connect(self.on_project_config_cancelled)
        result = dialog.exec()
        dialog.deleteLater()
        if result == QDialog.Accepted:
            # 未来可以在此处处理配置更新，例如刷新主界面显示
            pass

    def on_project_config_applied(self, model: ProjectConfigModel):
        """在配置对话框确认后触发，可用于刷新主界面状态。"""
        # 当前主界面尚未展示配置概览，因此暂时不需要额外操作。
        # 该方法提供了扩展点，未来可以在此处更新 UI 或持久化配置。
        self.project_config_model = model
        self.project_config_model.save_to_file(self._config_file_path)

    def on_project_config_cancelled(self):
        """配置对话框取消时触发，预留给未来扩展。"""
        pass

    def _cleanup_process(self):
        if self._process:
            if self._process.state() != QProcess.NotRunning:
                self._process.kill()
            self._process.deleteLater()
            self._process = None
        self._stdout_buffer = ""

    def _handle_process_output(self):
        if not self._process:
            return

        raw_bytes = self._process.readAllStandardOutput()
        if not raw_bytes:
            return

        text = bytes(raw_bytes).decode(errors="replace")
        self._stdout_buffer += text
        lines = self._stdout_buffer.splitlines(keepends=True)

        if lines and not lines[-1].endswith(("\n", "\r")):
            self._stdout_buffer = lines[-1]
            lines = lines[:-1]
        else:
            self._stdout_buffer = ""

        for line in lines:
            clean = line.rstrip("\r\n")
            if clean:
                self.view.append_log(self._runner.format_log(clean))
            else:
                self.view.append_log("")

    def _handle_process_finished(self, exit_code: int, _status):
        if self._stdout_buffer:
            trailing = self._stdout_buffer.rstrip("\r\n")
            if trailing:
                self.view.append_log(self._runner.format_log(trailing))
            self._stdout_buffer = ""

        self.view.append_log(self._runner.format_log(f"[INFO] 退出码: {exit_code}"))
        self.view.append_log("")

        self.view.stop_loading()
        self.view.statusbar.showMessage("模型执行已结束")
        self._cleanup_process()

    def _handle_process_error(self, error):
        message_map = {
            QProcess.FailedToStart: "[ERROR] 进程启动失败，请检查可执行文件是否存在及权限是否正确",
            QProcess.Crashed: "[ERROR] 进程异常退出",
            QProcess.Timedout: "[ERROR] 进程启动超时",
            QProcess.WriteError: "[ERROR] 向进程写入数据失败",
            QProcess.ReadError: "[ERROR] 读取进程输出失败",
        }
        text = message_map.get(error, f"[ERROR] 未知的进程错误: {error}")
        self.view.append_log(self._runner.format_log(text))
        if error == QProcess.FailedToStart:
            self.view.stop_loading()
            self.view.statusbar.showMessage("模型执行失败")
            self._cleanup_process()
