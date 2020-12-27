#!/usr/bin/env python3

N = int(input().split()[0])
S = input()
after = S
for char in S:
    after = after.replace(char, "") + char

ans = after
print(ans)
