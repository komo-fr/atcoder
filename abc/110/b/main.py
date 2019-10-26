#!/usr/bin/env python3

N, M, X, Y = list(map(int, input().split()))
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

if max(x_list) < min(y_list) and max(x_list) > X and min(y_list) <= Y:
    ans = "No War"
else:
    ans = "War"

print(ans)
