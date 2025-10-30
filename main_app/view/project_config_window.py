from PySide6.QtWidgets import QDialog
from .project_config_window_ui import Ui_ProjectConfigWindow

class ProjectConfigWindow(QDialog, Ui_ProjectConfigWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("工程配置")
