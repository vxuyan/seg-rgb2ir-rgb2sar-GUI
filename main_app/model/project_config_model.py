import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple

from .path_validator import validate_dirs


@dataclass
class ProjectConfigModel:
    """工程配置数据模型，用于存储和校验路径配置。"""

    input_dir: str = ""
    aux_input_dir: str = ""
    output_dir: str = ""
    weight_dir: str = ""

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)

    def to_dict(self) -> Dict[str, str]:
        return {
            "input_dir": self.input_dir,
            "aux_input_dir": self.aux_input_dir,
            "output_dir": self.output_dir,
            "weight_dir": self.weight_dir,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "ProjectConfigModel":
        return cls(
            input_dir=data.get("input_dir", ""),
            aux_input_dir=data.get("aux_input_dir", ""),
            output_dir=data.get("output_dir", ""),
            weight_dir=data.get("weight_dir", ""),
        )

    # ---------------------------
    # 文件读写
    # ---------------------------
    @staticmethod
    def default_storage_path() -> Path:
        """返回默认的配置文件路径。"""
        return Path.home() / ".seg_gui_project_config.json"

    @classmethod
    def load_from_file(cls, path: Optional[os.PathLike] = None) -> "ProjectConfigModel":
        """从本地文件读取配置，无法读取时返回默认实例。"""
        config_path = Path(path) if path is not None else cls.default_storage_path()
        try:
            with config_path.open("r", encoding="utf-8") as fp:
                data = json.load(fp)
                if isinstance(data, dict):
                    return cls.from_dict(data)
        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, OSError):
            # 读取失败时回退到默认值
            pass
        return cls()

    def save_to_file(self, path: Optional[os.PathLike] = None) -> None:
        """将当前配置写入本地文件。"""
        config_path = Path(path) if path is not None else self.default_storage_path()
        try:
            config_path.parent.mkdir(parents=True, exist_ok=True)
            with config_path.open("w", encoding="utf-8") as fp:
                json.dump(self.to_dict(), fp, ensure_ascii=False, indent=2)
        except OSError:
            # 写入失败时静默忽略，避免阻塞 UI
            pass

    def validate(self) -> Tuple[bool, str]:
        ok, message = validate_dirs(self.input_dir, self.output_dir, self.weight_dir)
        if not ok:
            return ok, message

        if self.aux_input_dir and not os.path.isdir(self.aux_input_dir):
            return False, "辅助输入文件夹无效"

        return True, "OK"
