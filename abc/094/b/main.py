#!/usr/bin/env python3

N, M, X = list(map(int, input().split()))
a_list = list(map(int, input().split()))
zero2x = 0
x2m = 0
for i in range(N):
    if i in a_list:
        if i < X:
            zero2x += 1
        else:
            x2m += 1

ans = min(zero2x, x2m)
print(ans)
