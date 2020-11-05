# https://atcoder.jp/contests/abc126/tasks/abc126_c
# C - Dice and Coin

import math

n, k = list(map(int, input().split()))

# 全パターン
step_1_p_list = [1 / n for x in range(1, n+1)]

# サイコロを降る回数
step_2_p_list = []

for saikoro in range(1, n+1):
    if saikoro >= k:
        step_2_p_list.append(1)
        continue

    a, b = math.modf(math.log2(k/saikoro))
    if a == 0:
        must_win_n = b
    else:
        must_win_n = b + 1
    must_win_n = int(must_win_n)
    # sprint('saikoro = {}: ({}, {}) -> {}'.format(saikoro, a, b, must_win_n))
    # print('{}: must_win_n = {}'.format(saikoro, must_win_n))
    step_2_p_list.append((1/2) ** must_win_n)

# print('step_1: {}'.format(step_1_p_list))
# print('step_2: {}'.format(step_2_p_list))

p_list = []

for step_1_p, step_2_p in zip(step_1_p_list, step_2_p_list):
    p_list.append(step_1_p * step_2_p)

# print('p_list: {}'.format(p_list))
ans = sum(p_list)
print(ans)
