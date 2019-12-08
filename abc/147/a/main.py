#!/usr/bin/env python3

a1, a2, a3 = list(map(int, input().split()))

if a1+a2+a3 >= 22:
    ans = 'bust'
else:
    ans = 'win'
print(ans)
