import os, sys

def resource_path(relative_path):
    """兼容 PyInstaller 的资源路径解析"""
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def find_python_in_env_or_current(env_folder):
    """尝试在指定 env_folder 下找到 Python；找不到则回退到当前解释器"""
    if os.name == "nt":
        candidate = os.path.join(env_folder, "Scripts", "python.exe")
    else:
        candidate = os.path.join(env_folder, "bin", "python")
    abs_candidate = resource_path(candidate)
    if os.path.exists(abs_candidate):
        return abs_candidate
    return sys.executable
