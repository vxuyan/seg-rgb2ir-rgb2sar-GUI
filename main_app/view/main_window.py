from pathlib import Path
from typing import Optional

from PySide6.QtCore import QDir, QModelIndex, Signal, Qt
from PySide6.QtWidgets import QFileSystemModel, QMainWindow
from PySide6.QtGui import QIcon, QPixmap, QMovie
from .mainwindow_ui import Ui_MainWindow
from ..utils.path_helper import resource_path

class MainWindow(QMainWindow, Ui_MainWindow):
    sig_run = Signal(str, str, str, str)  # 传递输入目录、输出目录、权重路径和模型名称
    sig_open_project_config = Signal()  # 打开工程配置窗口的信号

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._file_model: Optional[QFileSystemModel] = None
        self._current_pixmap: Optional[QPixmap] = None
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

        self._init_file_browser()

    def _init_file_browser(self):
        self._file_model = QFileSystemModel(self)
        root_path = QDir.rootPath()
        root_index = self._file_model.setRootPath(root_path)
        self.tree_file_browser.setModel(self._file_model)
        self.tree_file_browser.setRootIndex(root_index)
        for column in range(1, self._file_model.columnCount()):
            self.tree_file_browser.hideColumn(column)
        self.tree_file_browser.setSortingEnabled(True)

        home_index = self._file_model.index(QDir.homePath())
        if home_index.isValid():
            self.tree_file_browser.expand(home_index)
            self.tree_file_browser.setCurrentIndex(home_index)
            self.tree_file_browser.scrollTo(home_index)

        selection_model = self.tree_file_browser.selectionModel()
        if selection_model is not None:
            selection_model.currentChanged.connect(self._on_browser_selection_changed)
        self.tree_file_browser.doubleClicked.connect(self._on_browser_double_clicked)

    def _on_browser_selection_changed(self, current: QModelIndex, _previous: QModelIndex):
        if not current.isValid() or self._file_model is None:
            return
        path = self._file_model.filePath(current)
        self.statusbar.showMessage(path)

    def _on_browser_double_clicked(self, index: QModelIndex):
        if not index.isValid() or self._file_model is None:
            return
        path = Path(self._file_model.filePath(index))
        if path.is_dir():
            if not self.tree_file_browser.isExpanded(index):
                self.tree_file_browser.expand(index)
            else:
                self.tree_file_browser.collapse(index)
            return

        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp", ".tif", ".tiff"}:
            self._load_image_from_path(path)
        else:
            self.statusbar.showMessage(str(path))

    def _connect_signals(self):
        self.btn_config.clicked.connect(self.sig_open_project_config)

    def append_log(self, text):
        self.text_log.append(text)

    def stop_loading(self):
        self.label_loading.setVisible(False)

    def _load_image_from_path(self, path: Path):
        pixmap = QPixmap(str(path))
        if pixmap.isNull():
            self.statusbar.showMessage(f"无法加载图像: {path}")
            return
        self._current_pixmap = pixmap
        self._update_image_preview()
        self.statusbar.showMessage(str(path))
        self.append_log(f"已加载图像: {path}")

    def _update_image_preview(self):
        if not self._current_pixmap:
            return
        scaled = self._current_pixmap.scaled(
            self.label_input.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.label_input.setPixmap(scaled)
        self.label_input.setText("")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_image_preview()
