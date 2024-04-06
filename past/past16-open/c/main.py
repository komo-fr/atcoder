#!/usr/bin/env python3
from collections import Counter

N = int(input().split()[0])
a_list = list(map(int, input().split()))
c = Counter(a_list)
n = min(c.values())
ans = n if len(c) == 8 else 0
print(ans)
