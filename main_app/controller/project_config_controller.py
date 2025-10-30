from typing import Optional

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QFileDialog

from ..model.project_config_model import ProjectConfigModel
from ..view.project_config_window import ProjectConfigWindow


class ProjectConfigController(QObject):
    """负责协调工程配置窗口与数据模型。"""

    sig_config_applied = Signal(object)
    sig_config_cancelled = Signal()

    def __init__(self, view: ProjectConfigWindow, model: ProjectConfigModel, parent: Optional[QObject] = None):
        super().__init__(parent or view)
        self.view = view
        self.model = model

        self._init_view()
        self._connect_signals()

    def _init_view(self):
        self.view.set_form_data(**self.model.to_dict())

    def _connect_signals(self):
        self.view.sig_select_input.connect(self.on_select_input)
        self.view.sig_select_aux_input.connect(self.on_select_aux_input)
        self.view.sig_select_output.connect(self.on_select_output)
        self.view.sig_select_weight.connect(self.on_select_weight)
        self.view.sig_submit.connect(self.on_submit)
        self.view.sig_cancel.connect(self.on_cancel)

    # ---------------------------
    # 视图事件处理
    # ---------------------------
    def on_select_input(self):
        directory = QFileDialog.getExistingDirectory(
            self.view, "选择输入文件夹", self.model.input_dir or ""
        )
        if directory:
            self.model.input_dir = directory
            self.view.set_input_dir(directory)

    def on_select_aux_input(self):
        directory = QFileDialog.getExistingDirectory(
            self.view, "选择辅助输入文件夹", self.model.aux_input_dir or self.model.input_dir or ""
        )
        if directory:
            self.model.aux_input_dir = directory
            self.view.set_aux_input_dir(directory)

    def on_select_output(self):
        directory = QFileDialog.getExistingDirectory(
            self.view, "选择输出文件夹", self.model.output_dir or ""
        )
        if directory:
            self.model.output_dir = directory
            self.view.set_output_dir(directory)

    def on_select_weight(self):
        directory = QFileDialog.getExistingDirectory(
            self.view, "选择分割权重目录", self.model.weight_dir or ""
        )
        if directory:
            self.model.weight_dir = directory
            self.view.set_weight_dir(directory)

    def on_submit(self):
        self.model.update(**self.view.get_form_data())
        valid, message = self.model.validate()
        if valid:
            self.sig_config_applied.emit(self.model)
            self.view.accept()
        else:
            self.view.show_error(message)

    def on_cancel(self):
        self.sig_config_cancelled.emit()
        self.view.reject()
