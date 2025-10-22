import os
import sys
import subprocess
from .path_validator import validate_dirs
from ..utils.path_helper import find_python_in_env_or_current, resource_path

class ModelRunner:
    def __init__(self):
        # map model -> (env_folder, script_relpath)
        self.model_map = {
            "seg": ("env_seg", "models/seg_infer.py"),
            "rgb2ir": ("env_ir", "models/rgb2ir_infer.py"),
            "rgb2sar": ("env_sar", "models/rgb2sar_infer.py"),
        }

    def run_model_stream(self, model_name, input_dir, output_dir, weight_dir):
        ok, msg = validate_dirs(input_dir, output_dir, weight_dir)
        if not ok:
            yield f"[ERROR] {msg}"
            return

        if model_name not in self.model_map:
            yield f"[ERROR] 未知模型: {model_name}"
            return

        env_folder, script_rel = self.model_map[model_name]
        py_path = find_python_in_env_or_current(env_folder)
        script_path = resource_path(script_rel)

        cmd = [py_path, script_path, "--input", input_dir, "--output", output_dir, "--weight", weight_dir]
        yield f"[INFO] 调用命令: {' '.join(cmd)}"

        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in proc.stdout:
                yield line.rstrip()
            proc.wait()
            yield f"[INFO] 退出码: {proc.returncode}"
        except Exception as e:
            yield f"[EXCEPTION] {e}"
