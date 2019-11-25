#!/usr/bin/env python3
import string

N = int(input().split()[0])
S = input()

s_list = list(string.ascii_uppercase + string.ascii_uppercase)
r = ""
for c in list(S):
    n = s_list.index(c)
    r += s_list[n + N]

ans = r
print(ans)
