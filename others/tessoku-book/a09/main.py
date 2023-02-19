#!/usr/bin/env python3

H, W, N = list(map(int, input().split()))
abcd_list = []

for _ in range(N):
    abcd = list(map(int, input().split()))
    abcd_list.append(abcd)

diff_table = [[0] * W for _ in range(H)]


# デバッグ用の表示関数
def print_table(table):
    print((len(table), len(table[0])))
    for line in table:
        print(line)


# 差分テーブルを作成
for abcd in abcd_list:
    # 問題文ではインデックスが1始まりなので-1する
    a, b, c, d = [x - 1 for x in abcd]
    diff_table[a][b] += 1
    if d + 1 < W:
        diff_table[a][d + 1] -= 1
    if c + 1 < H:
        diff_table[c + 1][b] -= 1
    if d + 1 < W and c + 1 < H:
        diff_table[c + 1][d + 1] += 1

# 横方向の累積和をとる
_cumsum_table = []
for i in range(H):
    _cumsum_list = [diff_table[i][0]]
    for j in range(1, W):
        d = _cumsum_list[j - 1] + diff_table[i][j]
        _cumsum_list.append(d)
    _cumsum_table.append(_cumsum_list)

# 縦方向に足して2次元の累積和をとる
cumsum_table = [_cumsum_table[0]]
for i in range(1, H):
    cumsum_list = []
    for j in range(W):
        cumsum_list.append(cumsum_table[i - 1][j] + _cumsum_table[i][j])
    cumsum_table.append(cumsum_list)

for cumsum_list in cumsum_table:
    print(" ".join([str(x) for x in cumsum_list]))
