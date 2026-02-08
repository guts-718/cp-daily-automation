import yaml
import sys
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent / "config.yaml"
    if not config_path.exists():
        print("[ERROR] config.yaml not found")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    cfg = load_config()
    # Print values PowerShell needs, one per line
    print(cfg["repos"]["target"])
    print(cfg["logging"]["dir"])
