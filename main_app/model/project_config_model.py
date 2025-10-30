import os
from dataclasses import dataclass
from typing import Dict, Tuple

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

    def validate(self) -> Tuple[bool, str]:
        ok, message = validate_dirs(self.input_dir, self.output_dir, self.weight_dir)
        if not ok:
            return ok, message

        if self.aux_input_dir and not os.path.isdir(self.aux_input_dir):
            return False, "辅助输入文件夹无效"

        return True, "OK"
