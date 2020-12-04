#!/usr/bin/env python3
from collections import Counter

S = input()
N = len(S)
counter = Counter(S)
c_counter = Counter(counter.values())
n = N // 3

if N == 1:
    ans = "YES"
elif N == 2:
    ans = "YES" if len(counter) == 2 else "NO"
else:
    if N % 3 == 0:
        ans = "YES" if c_counter[n] == 3 else "NO"
    elif N % 3 == 1:
        ans = "YES" if c_counter[n] == 2 and c_counter[n + 1] == 1 else "NO"
    else:
        ans = "YES" if c_counter[n + 1] == 2 and c_counter[n] == 1 else "NO"
print(ans)
