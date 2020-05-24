#!/usr/bin/env python3

K = int(input().split()[0])
S = input()
if len(S) > K:
    ans = S[:K] + "..."
else:
    ans = S

print(ans)
