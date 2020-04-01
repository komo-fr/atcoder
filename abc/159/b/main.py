#!/usr/bin/env python3

S = input()
N = len(S)
a = S[: int((N - 1) / 2)]
b = S[int((N + 3) / 2) - 1 :]
ans = "Yes" if S == S[::-1] and a == a[::-1] and b == b[::-1] else "No"

print(ans)
