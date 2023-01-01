#!/usr/bin/env python3

N = int(input().split()[0])
S = input().split()[0]
max_c = 0
for i in range(N):
    x = S[: i + 1]
    y = S[i + 1 :]
    max_c = max(max_c, len(set(x) & set(y)))

ans = max_c
print(ans)
