#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
a_list = list(sorted(a_list))

win_c = 0
total_size = sum(a_list)
max_size_list = []

lose_flag = False
now_size = 0
winner = -1
# 自分より左側のモンスターは確実に吸収できるので
# 自分と自分より左側のモンスターのサイズの総和で右隣のモンスターを吸収できるか考える
#

for i, a in enumerate(a_list):
    if i == N - 1:
        # 最後は確実に勝つ
        if winner == -1:
            winner = i
        break

    now_size += a
    if now_size * 2 >= a_list[i + 1]:
        # 勝てる
        if winner == -1:
            winner = i
    else:
        winner = -1
c = N - winner

ans = c
print(ans)
