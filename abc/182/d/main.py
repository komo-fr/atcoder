#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
max_x = 0
max_d = -float("inf")
cumsum_x = 0
appended_x = 0

x_list = [0]
d_list = []
for i, a in enumerate(a_list):
    appended_x += a
    cumsum_x += appended_x
    max_d = max([appended_x, max_d])
    this_step_max_x = x_list[-1] + max_d
    x_list.append(cumsum_x)  # ターン終了時の座標
    # print(f"{appended_x=}, {cumsum_x=}")
    max_x = max([max_x, this_step_max_x])

ans = max_x
print(ans)
