from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QMessageBox

from .project_config_window_ui import Ui_ProjectConfigWindow


class ProjectConfigWindow(QDialog, Ui_ProjectConfigWindow):
    """工程配置窗口视图，负责发射用户操作信号。"""

    sig_select_input = Signal()
    sig_select_aux_input = Signal()
    sig_select_output = Signal()
    sig_select_weight = Signal()
    sig_submit = Signal()
    sig_cancel = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("工程配置")
        self._connect_internal_signals()

    def _connect_internal_signals(self):
        self.btn_select_input.clicked.connect(self.sig_select_input.emit)
        self.btn_select_input_2.clicked.connect(self.sig_select_aux_input.emit)
        self.btn_select_output.clicked.connect(self.sig_select_output.emit)
        self.btn_select_seg_weight.clicked.connect(self.sig_select_weight.emit)

        # 交由控制器决定对话框是否可以关闭
        try:
            self.buttonBox.accepted.disconnect()
        except TypeError:
            pass
        try:
            self.buttonBox.rejected.disconnect()
        except TypeError:
            pass

        self.buttonBox.accepted.connect(self.sig_submit.emit)
        self.buttonBox.rejected.connect(self.sig_cancel.emit)

    # ---------------------------
    # 数据读写接口
    # ---------------------------
    def set_form_data(self, *, input_dir="", aux_input_dir="", output_dir="", weight_dir=""):
        self.line_input.setText(input_dir)
        self.line_input_2.setText(aux_input_dir)
        self.line_output.setText(output_dir)
        self.line_seg_weight.setText(weight_dir)

    def get_form_data(self):
        return {
            "input_dir": self.line_input.text().strip(),
            "aux_input_dir": self.line_input_2.text().strip(),
            "output_dir": self.line_output.text().strip(),
            "weight_dir": self.line_seg_weight.text().strip(),
        }

    def set_input_dir(self, value: str):
        self.line_input.setText(value)

    def set_aux_input_dir(self, value: str):
        self.line_input_2.setText(value)

    def set_output_dir(self, value: str):
        self.line_output.setText(value)

    def set_weight_dir(self, value: str):
        self.line_seg_weight.setText(value)

    def show_error(self, message: str):
        QMessageBox.critical(self, "错误", message)
