#!/usr/bin/env python3

H, W = list(map(int, input().split()))
x_table = []

for _ in range(H):
    x_list = list(map(int, input().split()))
    x_table.append(x_list)

Q = int(input().split()[0])
q_list = []
for _ in range(Q):
    a, b, c, d = list(map(int, input().split()))
    q_list.append((a, b, c, d))

# 横方向の累積和をとる
_cumsum_table = []
for i in range(H):
    x_list = x_table[i]
    _cumsum_list = []
    for j, x in enumerate(x_list):
        if j == 0:
            _cumsum_list.append(x)
            continue
        _cumsum_list.append(_cumsum_list[j - 1] + x)
    _cumsum_table.append(_cumsum_list)

# 二次元の累積和を計算する
cumsum_table = []
for i in range(H):
    cumsum_list = []
    if i == 0:
        # 一番上の行
        cumsum_table.append(_cumsum_table[0])
        continue
    for j in range(W):
        cumsum_list.append(cumsum_table[i - 1][j] + _cumsum_table[i][j])
    cumsum_table.append(cumsum_list)

# 長方形を計算する
for abcd in q_list:
    # 右上(a, b)、左下(c, d)
    # 問題文のインデックスは1始まりなので、-1する
    a, b, c, d = [x - 1 for x in abcd]
    z_0 = cumsum_table[a - 1][b - 1] if a - 1 >= 0 and b - 1 >= 0 else 0
    z_1 = cumsum_table[a - 1][d] if a - 1 >= 0 else 0
    z_2 = cumsum_table[c][b - 1] if b - 1 >= 0 else 0
    z_3 = cumsum_table[c][d]
    z = z_0 + z_3 - z_1 - z_2
    print(z)
