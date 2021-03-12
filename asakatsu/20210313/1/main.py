#!/usr/bin/env python3
from collections import Counter

N = int(input().split()[0])
s_list = input().split()

ans = "Three" if len(Counter(s_list)) == 3 else "Four"
print(ans)
