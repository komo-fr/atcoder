#!/usr/bin/env python3

a_list = list(input())
c = len(set(a_list))

if c == 1:
    ans = 1
elif c == 2:
    ans = 3
else:
    ans = 6

print(ans)
