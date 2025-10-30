from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QMovie
from .mainwindow_ui import Ui_MainWindow
from ..utils.path_helper import resource_path

class MainWindow(QMainWindow, Ui_MainWindow):
    sig_run = Signal(str, str, str, str)  # 传递输入目录、输出目录、权重路径和模型名称
    sig_open_project_config = Signal()  # 打开工程配置窗口的信号

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        self.setWindowIcon(QIcon(resource_path("main_app/view/icons/app_logo.png")))

        # loading image (gif)
        movie = QMovie(resource_path("main_app/view/icons/loading.webp"))
        self.label_loading.setMovie(movie)
        self.label_loading.setMaximumHeight(20)
        self.label_loading.setAlignment(Qt.AlignCenter)
        movie.start()
        self.label_loading.setVisible(False)

    def _connect_signals(self):
        self.btn_config.clicked.connect(self.sig_open_project_config)

    def append_log(self, text):
        self.text_log.append(text)

    def stop_loading(self):
        self.label_loading.setVisible(False)
