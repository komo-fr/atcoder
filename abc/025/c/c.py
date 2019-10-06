#!/usr/bin/env python
max_score = 0

# 縦方向に一致していた場合の配点
b_table = []
for _ in range(2):
    b_list = list(map(int, input().split()))
    b_table.append(b_list)
    max_score += sum(b_list)

# 横方向に一致していた場合の配点
c_table = []
for _ in range(3):
    c_list = list(map(int, input().split()))
    c_table.append(c_list)
    max_score += sum(c_list)

memo_dict = {}

def calc_score(board_table):
    # 縦方向の得点のチェック
    score = 0
    for j in range(2):
        for i in range(3):
            if board_table[j][i] == board_table[j+1][i]:
                score += b_table[j][i]
    # 横方向の得点のチェック
    for j in range(3):
        for i in range(2):
            if board_table[j][i] == board_table[j][i+1]:
                score += c_table[j][i]
    return score

def dfs(turn_n, board_table):
    if turn_n == 10:
        return calc_score(board_table)

    player = turn_n % 2  # 1 = ○ 0 = x

    if str(board_table) in memo_dict:
        # 同じ状況を既に知っている
        return memo_dict[str(board_table)]

    score_list = []
    for j in range(3):
        for i in range(3):
            if board_table[j][i] is not None:
                # 既に置いてある
                continue
            board_table[j][i] = player
            next_score = dfs(turn_n + 1, board_table)
            score_list.append(next_score)

            board_table[j][i] = None

    best_choice_score = max(score_list) if player % 2 == 1 else min(score_list)
    memo_dict[str(board_table)] = best_choice_score
    return best_choice_score

board_table = [[None] * 3 for _ in range(3)]
chokudai_score = dfs(1, board_table)
naoko_score = max_score - chokudai_score
print(chokudai_score)
print(naoko_score)
# print(memo_dict)