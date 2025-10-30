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
        self.project_config_model = ProjectConfigModel()

    def run_model(self, input_dir: str, output_dir: str, weight_dir: str, model_name: str):
        # spawn thread
        self.thread = RunnerThread(model_name, input_dir, output_dir, weight_dir)
        self.thread.signals.log.connect(self.view.append_log)
        self.thread.signals.finished.connect(self.view.stop_loading)
        self.thread.start()

    def on_open_project_config(self):
        dialog = ProjectConfigWindow(self.view)  # 传入主窗口作为父级
        # 需要保持控制器的引用，避免被垃圾回收导致信号失效
        self._project_config_controller = ProjectConfigController(
            dialog, self.project_config_model
        )
        result = dialog.exec()
        # 对话框关闭后不再需要控制器实例
        self._project_config_controller = None
        if result == QDialog.Accepted:
            # 未来可以在此处处理配置更新，例如刷新主界面显示
            pass
