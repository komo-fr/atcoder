import subprocess
from pathlib import Path
import json
import shutil

# テンプレートファイルをコピー
def get_acc_config_path() -> Path:
    # atcoder-cliの設定ファイルのパスを取得する
    config_dir_path = subprocess.check_output(["acc", "config-dir"]).decode().strip()
    return Path(config_dir_path)


def load_acc_config() -> dict:
    # atcoder-cliの設定ファイルを読み込む
    config_dir_path = get_acc_config_path()
    path = config_dir_path / "config.json"
    with open(path) as f:
        config_json = json.load(f)
    return config_json


def load_default_template_config() -> dict:
    # デフォルトのテンプレートとなるファイルの設定を読み込む
    config_json = load_acc_config()
    template_dir_path = get_acc_config_path() / config_json["default-template"]
    path = template_dir_path / "template.json"
    with open(path) as f:
        template_json = json.load(f)
    return template_json