#!/usr/bin/env python3

N = int(input().split()[0])
S = input()

if N % 2 == 0:
    if S == S[: N // 2] + S[: N // 2]:
        ans = "Yes"
    else:
        ans = "No"
else:
    ans = "No"

print(ans)
