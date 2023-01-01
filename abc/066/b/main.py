#!/usr/bin/env python3

S = input().split()[0]

for i in range(1, len(S)):
    s = S[: len(S) - i]
    n = len(s)
    if n % 2:
        continue
    if s[: n // 2] == s[n // 2 :]:
        ans = n
        break

print(ans)
