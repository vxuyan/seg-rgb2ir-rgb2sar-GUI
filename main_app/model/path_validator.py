import os

def validate_dirs(input_dir, output_dir, weight_dir):
    if not input_dir or not os.path.isdir(input_dir):
        return False, "输入文件夹无效"
    if not output_dir:
        return False, "输出文件夹未填写"
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except Exception as e:
            return False, f"无法创建输出文件夹: {e}"
    if not weight_dir or not os.path.isdir(weight_dir):
        return False, "权重目录无效（可用空文件夹占位）"
    return True, "OK"
