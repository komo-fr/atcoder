#!/usr/bin/env python3
S = input()

total = 0
for i in range(len(S)):
    if "R" * (i + 1) in S:
        total = i + 1
ans = total
print(ans)
