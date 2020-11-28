#!/usr/bin/env python3
from collections import defaultdict

N = int(input().split()[0])
a_list = list(map(int, input().split()))
friend_dict = defaultdict(lambda: False)
count = 0
for i, a in enumerate(a_list):
    b = i + 1
    key = tuple(sorted([a, b]))
    if friend_dict[key]:
        count += 1
    else:
        friend_dict[key] = True
ans = count
print(ans)
