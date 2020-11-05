#!/usr/bin/env python3
from collections import defaultdict, deque
import bisect

N = int(input().split()[0])

day2p_dict = defaultdict(lambda: [])

for _ in range(N):  # 2 * 10**5
    a, b = list(map(int, input().split()))
    if day2p_dict[a]:
        day2p_dict[a].append(b)
    else:
        day2p_dict[a] = [b]

total = 0
p_deque = deque([])
for i in range(N):
    d = i + 1
    for p in day2p_dict[d]:
        bisect.insort_right(p_deque, p)
    total += p_deque.pop()
    print(total)
