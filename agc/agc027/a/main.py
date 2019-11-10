#!/usr/bin/env python3

N, x = list(map(int, input().split()))
a_list = list(map(int, input().split()))
a_list = sorted(a_list)
# xよりaが大きい子供にはどう頑張っても配りようがないので最初から除外する
a_list = [a for a in a_list if a <= x]
count = 0
d_list = [0] * N

# 少ない子から順に配っていく
for i, a in enumerate(a_list):
    if i == N - 1:
        # 最後の一人だったら全部押し付ける
        d_list[i] = x
        break

    if x - a >= 0:
        d_list[i] = a
        x -= a
    else:
        d_list[i] = x
        break

ans = len([a for a, d in zip(a_list, d_list) if a == d])

print(ans)
