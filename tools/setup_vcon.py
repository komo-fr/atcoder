import subprocess
from pathlib import Path
import json
import copy
import shutil

from . import config
from .contest import Problem


def update_contest_acc_json(dir_path, task_label):
    # load
    json_path = Path(dir_path / "contest.acc.json")
    with open(json_path) as f:
        setting_json = json.load(f)

    # change
    new_tasks = []
    for task in setting_json["tasks"]:
        if task["label"].lower() != task_label.lower():
            new_tasks.append(task)
            continue

        dir_info = {"path": "./", "testdir": "tests", "submit": "main.py"}
        task["directory"] = dir_info
        new_tasks.append(task)

    setting_json["tasks"] = new_tasks

    # save
    with open(json_path, "w") as f:
        json.dump(setting_json, f, indent=4)


def download_test_data(problem, root_dir: str = ".", test_dir_name: str = "tests"):
    # テストデータをダウンロードする
    test_path = Path(root_dir) / str(problem.number) / test_dir_name
    _ = subprocess.call(["oj", "dl", "-d", test_path, problem.url])


def copy_default_program_file(dst_dir_path) -> Path:
    # デフォルトのテンプレートファイルをコピーする
    template_json = config.load_default_template_config()
    file_name = template_json["task"]["program"][0]
    template_dir_path = (
        config.get_acc_config_path() / config.load_acc_config()["default-template"]
    )
    default_program_file_path = template_dir_path / file_name
    shutil.copy(default_program_file_path, dst_dir_path / file_name)


def setup_problem_dir(problem: Problem, root_dir: str = "."):
    print("コンテスト情報をダウンロード中...")
    _ = subprocess.call(["acc", "new", "--choice", "none", problem.contest_id])

    if not Path(root_dir).exists():
        Path(root_dir).mkdir(parents=True)
    temp_dir_name = "working"
    shutil.move(problem.contest_id, Path(root_dir) / temp_dir_name)

    # フォルダ名を変更
    contest_dir_path = Path(root_dir) / temp_dir_name
    contest_dir_path.rename(Path(root_dir) / str(problem.number))
    contest_dir_path = Path(root_dir) / str(problem.number)
    # コンテストの設定情報を更新
    update_contest_acc_json(contest_dir_path, problem.label)
    print("テストデータをダウンロード中...")
    test_dir_name = config.load_acc_config()["default-test-dirname-format"]
    download_test_data(problem, root_dir=root_dir, test_dir_name=test_dir_name)
    print("テンプレートファイルをコピー中...")
    copy_default_program_file(contest_dir_path)
    print("Completed.")