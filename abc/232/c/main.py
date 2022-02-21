#!/usr/bin/env python3
import itertools

N, M = list(map(int, input().split()))
ab_list = []
ab_table = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))
    ab_table[a - 1][b - 1] = 1
    ab_table[b - 1][a - 1] = 1

cd_list = []
cd_table = [[0] * N for _ in range(N)]

for _ in range(M):
    c, d = list(map(int, input().split()))
    cd_list.append((c, d))
    cd_table[c - 1][d - 1] = 1
    cd_table[d - 1][c - 1] = 1

# ノードの対応パターン
l = list(range(1, N + 1))
p_gen = itertools.permutations(l, N)
total_is_ok = False
for pattern in p_gen:
    is_ok = True
    ab2cd_map = {}
    cd2ab_map = {}
    for i, p in enumerate(pattern):
        ab2cd_map[i + 1] = p
        cd2ab_map[p] = i + 1

    for a, b in ab_list:
        c = ab2cd_map[a]
        d = ab2cd_map[b]
        if cd_table[c - 1][d - 1] != 1:
            is_ok = False
            break
    if is_ok:
        for c, d in cd_list:
            a = cd2ab_map[c]
            b = cd2ab_map[d]
            if ab_table[a - 1][b - 1] != 1:
                is_ok = False
                break
    if is_ok:
        total_is_ok = True

ans = "Yes" if total_is_ok else "No"
print(ans)
