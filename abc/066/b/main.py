#!/usr/bin/env python3

S = input().split()[0]

for i in range(len(S)):
    s = S[: i + 1]
    n = len(s)
    if n % 2:
        continue
    if s[: n // 2] == s[n // 2 :]:
        ans = n
        break

print(ans)
