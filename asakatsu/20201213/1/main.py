#!/usr/bin/env python3
from collections import Counter

ab_list = []
node_list = []
for _ in range(3):
    a, b = list(map(int, input().split()))
    ab = tuple(list(sorted([a, b])))
    ab_list.append(ab)
    node_list.append(a)
    node_list.append(b)

counter = Counter(node_list)
is_ok = False
if len(set(ab_list)) >= 3:
    if len(counter) == 4:
        w_list = [v[1] for v in counter.most_common()]
        if w_list == [2, 2, 1, 1]:
            is_ok = True

ans = "YES" if is_ok else "NO"
print(ans)
