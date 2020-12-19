#!/usr/bin/env python3
from collections import Counter

S = input()
c = Counter(S)

ans = 700 + c["o"] * 100
print(ans)
