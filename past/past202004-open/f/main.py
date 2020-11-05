#!/usr/bin/env python3
from collections import defaultdict, deque
import bisect

N = int(input().split()[0])
ab_list = []

day2p_dict = defaultdict(lambda: deque([]))

for _ in range(N):  # 2 * 10**5
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))
    if day2p_dict[a]:
        bisect.insort_right(day2p_dict[a], b)
    else:
        day2p_dict[a] = deque([b])
# print(day2p_dict)
total = 0
for i in range(N):  # 2 * 10 ** 5
    d = i + 1
    max_point = -float("inf")
    max_point_day = -1
    # print(f"day={i}")
    for j in range(d + 1):
        if day2p_dict[j]:
            if day2p_dict[j][0] > max_point:
                max_point = day2p_dict[j][0]
                max_point_day = j
    p = day2p_dict[max_point_day].pop()
    total += p
    print(total)
