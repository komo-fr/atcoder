#!/usr/bin/env python3
from collections import defaultdict

N = int(input().split()[0])
boss_dict = defaultdict(lambda: defaultdict(lambda: False))
p_dict = {}
for i in range(N):  # 150000
    p = int(input())
    p_dict[i + 1] = p

Q = int(input().split()[0])

for _ in range(Q):  # 100000
    a, b = list(map(int, input().split()))
    me = a
    is_boss = False
    while me != -1:
        me = p_dict[me]
        if me == b:
            is_boss = True
            break

    text = "Yes" if is_boss else "No"
    print(text)
