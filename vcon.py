from pathlib import Path
import fire
from tqdm import tqdm
from tools import setup_vcon, scraper


def main(url: str, dir_path: str = None):
    contest = scraper.fetch_contest(url)

    if contest.title.startswith("あさかつ"):
        dir_name = contest.date.replace("-", "")
        dir_path = Path("asakatsu") / dir_name

    if contest.title.startswith("くじかつ"):
        title = contest.title
        number = title.split("#")[-1]
        dir_name = f"N{number}" if "NORMAL" in title else f"A{number}"
        dir_path = Path("kujikatsu") / dir_name

    dir_path = dir_path if dir_path else "."

    for p in tqdm(contest.problems):
        print(f"{p.number}: {p.name}")
        setup_vcon.setup_problem_dir(p, dir_path)
    print(f"cd {dir_path}")


if __name__ == "__main__":
    fire.Fire(main)