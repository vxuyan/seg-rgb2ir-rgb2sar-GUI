import os
from PySide6.QtCore import QThread, Signal, QObject
from ..model.model_runner import ModelRunner

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
    def __init__(self, view):
        self.view = view
        self.view.bind_controller(self)

    def handle_run_clicked(self):
        model_name = self.view.combo_model.currentText()
        input_dir = self.view.line_input.text()
        output_dir = self.view.line_output.text()
        weight_dir = self.view.line_weight.text()

        # spawn thread
        self.thread = RunnerThread(model_name, input_dir, output_dir, weight_dir)
        self.thread.signals.log.connect(self.view.append_log)
        self.thread.signals.finished.connect(self.view.stop_loading)
        self.thread.start()
