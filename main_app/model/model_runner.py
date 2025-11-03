import os
import subprocess
from .path_validator import validate_dirs
from ..utils.path_helper import resource_path
from datetime import datetime

class ModelRunner:
    '''在一个多模型的项目中，用统一接口来调用不同模型的推理可执行文件，并实时地将运行日志（包括命令、输出、错误等）以流的形式输出。'''
    def __init__(self):
        # map model -> executable relative path
        self.model_map = {
            "seg": "models/seg_infer.exe",
            "rgb2ir": "models/rgb2ir_infer.exe",
            "rgb2sar": "models/rgb2sar_infer.exe",
        }

    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _log(self, msg: str):
        return f"[{self._timestamp()}] {msg}"

    def run_model_stream(self, model_name: str, input_dir: str, output_dir: str, weight_dir: str):
        ok, msg = validate_dirs(input_dir, output_dir, weight_dir)
        if not ok:
            yield self._log(f"[ERROR] {msg}")
            return

        if model_name not in self.model_map:
            yield self._log(f"[ERROR] 未知模型: {model_name}")
            return

        exe_rel = self.model_map[model_name]
        exe_path = resource_path(exe_rel)

        if not os.path.exists(exe_path):
            yield self._log(f"[ERROR] 找不到可执行文件: {exe_path}")
            return

        cmd = [exe_path, "--input", input_dir, "--output", output_dir, "--weight", weight_dir]
        yield self._log(f"[INFO] 调用命令: {' '.join(cmd)}")

        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in proc.stdout:
                yield self._log(line.rstrip())
            proc.wait()
            yield self._log(f"[INFO] 退出码: {proc.returncode}")
            # 在一次执行结束后产出一个空行，便于两次执行日志之间有空行间隔
            yield ""
        except Exception as e:
            yield self._log(f"[EXCEPTION] {e}")
            # 即使发生异常，也在结束时产出一个空行
            yield ""
