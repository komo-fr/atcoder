#!/usr/bin/env python3
from collections import defaultdict

N = int(input().split()[0])
boss_dict = defaultdict(lambda: defaultdict(lambda: False))

for i in range(N):
    p = int(input())
    boss_dict[p][i + 1] = True

Q = int(input().split()[0])

for _ in range(Q):
    a, b = list(map(int, input().split()))
    # ab_list.append((a, b))
    text = "Yes" if boss_dict[b][a] else "No"
    print(text)

print(boss_dict)
