#!/usr/bin/env python3

N, M = list(map(int, input().split()))
ab_list = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

cd_list = []
for _ in range(M):
    c, d = list(map(int, input().split()))
    cd_list.append((c, d))

for ab in ab_list:
    min_d = float("inf")
    min_d_index = None
    for i, cd in enumerate(cd_list):
        m_index = i + 1
        dis = abs(ab[0] - cd[0]) + abs(ab[1] - cd[1])
        if dis < min_d:
            min_d = dis
            min_d_index = m_index
    print(min_d_index)
