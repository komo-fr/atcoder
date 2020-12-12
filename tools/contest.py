import dataclasses
import string
from typing import List


@dataclasses.dataclass
class Problem:
    # 問題クラス
    number: int
    name: str
    url: str
    score: int

    @property
    def formatted_name(self):
        if " / " in self.name:
            # 日英表示の場合は日本語部分のみを抽出する
            after_name = self.name.split(" / ")[0]
        else:
            after_name = self.name

        # 問題の区分は「A.」 ->「A -」に変更する
        prefix = after_name[:2]
        prefix = f"{prefix[0]} -"
        after_name = prefix + after_name[2:]
        return after_name

    @property
    def contest_url(self):
        return f"https://atcoder.jp/contests/{self.contest_id}"

    @property
    def contest_id(self):
        return self.url.replace("https://atcoder.jp/contests/", "").split("/")[0]

    @property
    def task_id(self):
        return self.url.replace("https://atcoder.jp/contests/", "").split("/")[2]

    @property
    def label(self):
        label = self.task_id.split("_")[-1]
        if label not in string.ascii_lowercase:
            label = self.name.split(".")[0]
        return label

    def __str__(self):
        desc = f"{self.number}: {self.name} ({self.contest_id.upper()})"
        return desc


@dataclasses.dataclass
class Contest:
    title: str
    problems: List[Problem]
    schedule: str
    description: str
    url: str

    @property
    def date(self):
        return self.schedule[: len("YYYY-MM-DD")]

    @property
    def start_at(self):
        raise NotImplementedError()

    @property
    def end_at(self):
        raise NotImplementedError()

    def __str__(self):
        desc = f"title: {self.title}"
        desc += f"\nurl: {self.url}"
        desc += f"\nschedule: {self.schedule}"
        for p in self.problems:
            desc += f"\n{p.__str__()}"
        return desc