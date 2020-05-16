#!/usr/bin/env python3
S = input()
T = input()
is_ok = False

if len(S) + 1 == len(T):
    if S == T[:-1]:
        is_ok = True
ans = "Yes" if is_ok else "No"
print(ans)
