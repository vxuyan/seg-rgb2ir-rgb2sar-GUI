from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QMovie
from .mainwindow_ui import Ui_MainWindow
from ..utils.path_helper import resource_path

class MainWindow(QMainWindow, Ui_MainWindow):
    sig_run = Signal(str, str, str, str)  # 传递输入目录、输出目录、权重路径和模型名称

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        self.setWindowIcon(QIcon(resource_path("main_app/view/icons/app_logo.png")))

        # set icons
        self.btn_select_input.setIcon(QIcon(resource_path("main_app/view/icons/folder_icon.png")))
        self.btn_select_output.setIcon(QIcon(resource_path("main_app/view/icons/folder_icon.png")))
        self.btn_select_weight.setIcon(QIcon(resource_path("main_app/view/icons/folder_icon.png")))
        self.btn_run.setIcon(QIcon(resource_path("main_app/view/icons/run_icon.png")))

        # loading image (gif)
        movie = QMovie(resource_path("main_app/view/icons/loading.webp"))
        self.label_loading.setMovie(movie)
        self.label_loading.setMaximumHeight(20)
        self.label_loading.setAlignment(Qt.AlignCenter)
        movie.start()
        self.label_loading.setVisible(False)

    def _connect_signals(self):
        # signals
        self.btn_select_input.clicked.connect(self.select_input_dir)
        self.btn_select_output.clicked.connect(self.select_output_dir)
        self.btn_select_weight.clicked.connect(self.select_weight_dir)
        self.btn_run.clicked.connect(self.on_run_clicked)
        
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
        self.label_loading.setVisible(True)
        self.sig_run.emit(self.line_input.text(), self.line_output.text(), self.line_weight.text(), self.combo_model.currentText())

    def append_log(self, text):
        self.text_log.append(text)

    def stop_loading(self):
        self.label_loading.setVisible(False)
