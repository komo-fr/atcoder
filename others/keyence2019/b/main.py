#!/usr/bin/env python3

S = input()
N = len(S)
is_ok = False
for l in range(N):
    for r in range(N):
        if S[:l] + S[r+1:] == "keyence":
            is_ok = True

ans = "YES" if is_ok else "NO"
print(ans)
