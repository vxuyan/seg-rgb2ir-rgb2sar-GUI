from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
from .mainwindow_ui import Ui_MainWindow
from ..utils.path_helper import resource_path

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path("main_app/view/icons/app_logo.png")))

        # set icons
        self.btn_select_input.setIcon(QIcon(resource_path("main_app/view/icons/folder_icon.png")))
        self.btn_select_output.setIcon(QIcon(resource_path("main_app/view/icons/folder_icon.png")))
        self.btn_select_weight.setIcon(QIcon(resource_path("main_app/view/icons/folder_icon.png")))
        self.btn_run.setIcon(QIcon(resource_path("main_app/view/icons/run_icon.png")))

        # loading image (static)
        self.label_loading.setPixmap(QPixmap(resource_path("main_app/view/icons/loading.png")))
        self.label_loading.setVisible(False)

        # signals
        self.btn_select_input.clicked.connect(self.select_input_dir)
        self.btn_select_output.clicked.connect(self.select_output_dir)
        self.btn_select_weight.clicked.connect(self.select_weight_dir)
        self.btn_run.clicked.connect(self.on_run_clicked)

        self.controller = None

    def bind_controller(self, controller):
        self.controller = controller

    def select_input_dir(self):
        path = QFileDialog.getExistingDirectory(self, "选择输入文件夹")
        if path:
            self.line_input.setText(path)

    def select_output_dir(self):
        path = QFileDialog.getExistingDirectory(self, "选择输出文件夹")
        if path:
            self.line_output.setText(path)

    def select_weight_dir(self):
        path = QFileDialog.getExistingDirectory(self, "选择权重文件夹")
        if path:
            self.line_weight.setText(path)

    def on_run_clicked(self):
        if not self.controller:
            QMessageBox.warning(self, "提示", "控制器未绑定")
            return
        self.label_loading.setVisible(True)
        self.controller.handle_run_clicked()

    def append_log(self, text):
        self.text_log.append(text)

    def stop_loading(self):
        self.label_loading.setVisible(False)
