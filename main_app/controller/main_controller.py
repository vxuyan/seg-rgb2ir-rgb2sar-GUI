from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QDialog

from ..model.model_runner import ModelRunner
from ..model.project_config_model import ProjectConfigModel
from ..view.main_window import MainWindow
from ..view.project_config_window import ProjectConfigWindow
from .project_config_controller import ProjectConfigController

class WorkerSignals(QObject):
    finished = Signal()
    log = Signal(str)

class RunnerThread(QThread):
    def __init__(self, model_name, input_dir, output_dir, weight_dir):
        super().__init__()
        self.model_name = model_name
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.weight_dir = weight_dir
        self.signals = WorkerSignals()

    def run(self):
        runner = ModelRunner()
        for line in runner.run_model_stream(self.model_name, self.input_dir, self.output_dir, self.weight_dir):
            self.signals.log.emit(line)
        self.signals.finished.emit()

class MainController:
    def __init__(self, view: MainWindow):
        self.view = view
        self.view.sig_run.connect(self.run_model)
        self.view.sig_open_project_config.connect(self.on_open_project_config)
        self._config_file_path = ProjectConfigModel.default_storage_path()
        self.project_config_model = ProjectConfigModel.load_from_file(self._config_file_path)

    def run_model(self, input_dir: str, output_dir: str, weight_dir: str, model_name: str):
        # spawn thread
        self.thread = RunnerThread(model_name, input_dir, output_dir, weight_dir)
        self.thread.signals.log.connect(self.view.append_log)
        self.thread.signals.finished.connect(self.view.stop_loading)
        self.thread.start()

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
