#!/usr/bin/env python3

N, Q = list(map(int, input().split()))
s_list = []

for _ in range(Q):
    s = list(map(int, input().split()))
    s_list.append(s)

# f_table = [[0] * N for _ in range(N)]
f_map = {i + 1: set() for i in range(N)}  # keyがフォローしているユーザ
ff_map = {i + 1: set() for i in range(N)}  # keyをフォローしているユーザ
for s in s_list:  # 500
    if s[0] == 1:
        source, target = s[1], s[2]
        f_map[source] = f_map[source] | {target}
        ff_map[target] = ff_map[target] | {source}
    elif s[0] == 2:
        source = s[1]
        for target in ff_map[source]:
            f_map[source] = f_map[source] | {target}
            ff_map[target] = ff_map[target] | {source}
    elif s[0] == 3:
        source = s[1]
        additional = set()
        for f in f_map[source]:
            additional = additional | f_map[f]
        f_map[source] = f_map[source] | additional
        for target in additional:
            ff_map[target] = ff_map[target] | {source}

f_table = [["N"] * N for _ in range(N)]

for i in range(N):  # フォロー元
    for j in range(N):
        if (j + 1) in f_map[i + 1]:
            f_table[i][j] = "Y"

for f in f_table:
    print("".join(f))
