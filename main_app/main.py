import sys
from PySide6.QtWidgets import QApplication
from .view.main_window import MainWindow
from .controller.main_controller import MainController

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    controller = MainController(window)
    window.show()
    sys.exit(app.exec())