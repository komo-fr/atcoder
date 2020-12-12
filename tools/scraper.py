import time
from typing import List

import chromedriver_binary  # nopa
from selenium import webdriver

from .contest import Problem, Contest


def fetch_contest(virtual_contest_url: str, waiting_sec: int = 3) -> List[Problem]:
    if not virtual_contest_url.startswith(
        "https://kenkoooo.com/atcoder#/contest/show/"
    ):
        raise ValueError(f"未対応のURL形式です. {virtual_contest_url}")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    print(f"接続中... {virtual_contest_url}")
    driver = webdriver.Chrome(options=options)
    driver.get(virtual_contest_url)
    print(f"{waiting_sec}秒待機...")
    time.sleep(waiting_sec)

    tables = driver.find_elements_by_css_selector("table")

    if len(tables) <= 3:
        # TODO: ValueErrorは適切か？
        raise ValueError("問題テーブルを取得できませんでした")

    problem_table = tables[2]  # 問題テーブル
    tr_list = problem_table.find_elements_by_tag_name("tr")
    if tr_list[0].text != "Problem Name Score":
        # TODO: ValueErrorは適切か？
        raise ValueError("問題テーブルを取得できませんでした")

    problems = []
    for tr in tr_list[1:]:  # 最初の行はタイトルなのでスキップ
        number = tr.find_elements_by_tag_name("th")[0].text.strip()
        number = int(number)
        tds = tr.find_elements_by_tag_name("td")
        name = tds[0].text.strip()
        url = tds[0].find_element_by_tag_name("a").get_attribute("href")
        score = tds[1].text.strip()
        score = int(score)
        problems.append(Problem(number, name, url, score))

    # コンテスト情報の抽出
    contest_title = driver.find_elements_by_css_selector("h1")[0].text.strip()
    description = driver.find_elements_by_css_selector("h4")[0].text.strip()
    schedule_table = tables[0]
    schedule = schedule_table.find_elements_by_tag_name("tr")[0]
    if not schedule.text.startswith("Time"):
        raise ValueError("開催日時情報の取得に失敗しました.")
    schedule = schedule.find_elements_by_tag_name("td")[0].text
    contest = Contest(
        contest_title, problems, schedule, description, virtual_contest_url
    )
    print("================")
    print(contest)
    print("================")

    driver.quit()
    return contest