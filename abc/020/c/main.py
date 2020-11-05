#!/usr/bin/env python3
import math
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

H, W, T = list(map(int, input().split()))
s_table = []

for _ in range(H):
    s = input()
    s_table.append(list(s))

# 隣接行列を作る
adj = [[0] * H * W for _ in range(H * W)]
start = (0, 0)
end = (0, 0)
x_list = []

lo = 1
hi = T
c = 0
while True:
    x = (lo + hi) // 2
    for h in range(H):
        for w in range(W):
            if s_table[h][w] in [".", "S", "G"]:
                cost = 1
            else:
                cost = x
            if s_table[h][w] == "S":
                start = (h, w)
            if s_table[h][w] == "G":
                end = (h, w)
            index = h * W + w
            if index + 1 < H * W and (index + 1) % W != 0:
                # 右隣
                adj[index + 1][index] = cost
            if index - 1 >= 0 and (index + 1) % W != 1:
                # 左隣
                adj[index - 1][index] = cost
            if index + W < H * W:
                # 下
                adj[index + W][index] = cost
            if index - W >= 0:
                # 上
                adj[index - W][index] = cost

    # AtCoder上のScipyのバージョンは0.13.3
    # このバージョンのshortest_pathには不具合があり、
    # csr＿matrix変換後の疎行列を渡すと
    # エラーになることがある（入力例2)
    # https://github.com/scipy/scipy/issues/3466
    # そのため、隣接行列をnumpy配列の形で渡すこと
    # csr = csr_matrix(adj)
    # d_matrix = shortest_path(csr)
    d_matrix = shortest_path(np.array(adj))
    start_index = start[0] * W + start[1]
    end_index = end[0] * W + end[1]
    if d_matrix[start_index][end_index] <= T:
        x_list.append(x)
        lo = x
    else:
        hi = x

    if c >= math.log2(T):
        break
    c += 1

ans = max(x_list)

print(ans)
