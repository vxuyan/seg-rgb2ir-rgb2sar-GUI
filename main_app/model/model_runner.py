import os
from datetime import datetime
from typing import List, Optional, Tuple

from .path_validator import validate_dirs
from ..utils.path_helper import resource_path

class ModelRunner:
    """统一准备模型推理可执行文件命令并格式化日志输出。"""
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

    def format_log(self, message: str) -> str:
        return self._log(message)

    def prepare_model_command(
        self, model_name: str, input_dir: str, output_dir: str, weight_dir: str
    ) -> Tuple[Optional[List[str]], List[str]]:
        """
        验证路径和模型名称，并返回可执行命令及预先需要输出的日志。

        Args:
            model_name: 模型名称 key。
            input_dir: 输入目录。
            output_dir: 输出目录。
            weight_dir: 权重目录。

        Returns:
            (command, logs) 二元组。若验证失败，command 为 None，logs 中包含错误信息。
        """

        logs: List[str] = []

        ok, msg = validate_dirs(input_dir, output_dir, weight_dir)
        if not ok:
            logs.append(self._log(f"[ERROR] {msg}"))
            return None, logs

        if model_name not in self.model_map:
            logs.append(self._log(f"[ERROR] 未知模型: {model_name}"))
            return None, logs

        exe_rel = self.model_map[model_name]
        exe_path = resource_path(exe_rel)

        if not os.path.exists(exe_path):
            logs.append(self._log(f"[ERROR] 找不到可执行文件: {exe_path}"))
            return None, logs

        cmd = [exe_path, input_dir, output_dir, weight_dir]
        logs.append(self._log(f"[INFO] 调用命令: {' '.join(cmd)}"))
        return cmd, logs
