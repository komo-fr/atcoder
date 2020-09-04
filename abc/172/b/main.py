#!/usr/bin/env python3

S = input()
T = input()
count = 0
for s, t in zip(S, T):
    if s != t:
        count += 1
ans = count
print(ans)
