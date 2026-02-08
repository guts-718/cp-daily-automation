import os
from datetime import datetime

def get_log_path(base_dir: str) -> str:
    date = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(base_dir, exist_ok=True)
    return os.path.join(base_dir, f"cp_bot_{date}.log")
