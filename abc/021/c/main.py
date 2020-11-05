#!/usr/bin/env python3
N = int(input().split()[0])
A, B = list(map(int, input().split()))
M = int(input().split()[0])

# 隣接ノード
neighbors_dict = {i + 1: [] for i in range(N)}
for _ in range(M):
    x, y = list(map(int, input().split()))
    neighbors_dict[x] += [y]
    neighbors_dict[y] += [x]

# index = 0は未使用
# index = 0にノード1を詰めても良いが、
# ノード番号&辞書のキーとリストのindexがずれてややこしいので
# ノード番号・辞書キーとリストのindexを統一させて使う
dist_list = [float('inf')] * (N + 1)  # 最短経路長
pattern_list = [0] * (N + 1)  # 最短経路のパターン

# 始点の設定
dist_list[A] = 0
pattern_list[A] = 1
q = [A]

mod = 10**9 + 7

# BFSで最短経路を求める
while q:
    me = q.pop(0)
    for neighbor in neighbors_dict[me]:
        if dist_list[me] + 1 < dist_list[neighbor]:
            # 最短経路を更新
            dist_list[neighbor] = dist_list[me] + 1
            pattern_list[neighbor] = pattern_list[me]
            q.append(neighbor)
        elif dist_list[me] + 1== dist_list[neighbor]:
            pattern_list[neighbor] += pattern_list[me]

ans = pattern_list[B] % mod
print(ans)
