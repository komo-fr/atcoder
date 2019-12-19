#!/usr/bin/env python3

s = input()
ans = ""
for c in s:
    if c in ["0", "1"]:
        ans += c
    elif ans:
        ans = ans[:-1]

print(ans)
