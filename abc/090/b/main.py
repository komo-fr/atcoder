#!/usr/bin/env python3

A, B = list(map(int, input().split()))
pn_list = []
for i in range(10000, 999999):
    S = str(i)
    T = S[::-1]
    if S == T:
        pn_list.append(int(S))
c = 0
for i in pn_list:
    if A <= i <= B:
        c += 1


ans = c
print(ans)
