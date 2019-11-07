#!/usr/bin/env python3

N, A, B, C, D = list(map(int, input().split()))
S = input()

is_ok = True

for i in range(A, max(C, D) - 1):
    if S[i] == "#" and S[i + 1] == "#":
        is_ok = False
        break

if is_ok:
    if C > D:
        is_ok = False
        for i in range(B, D - 1):
            if S[i] == "." and S[i + 1] == "." and S[i + 2] == ".":
                is_ok = True
                break

ans = "Yes" if is_ok else "No"

print(ans)
