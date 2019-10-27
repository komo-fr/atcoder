#!/usr/bin/env python3

N = int(input().split()[0])
H, W = list(map(int, input().split()))

c_table = []

for _ in range(9):
    c_table += list(map(int, input().split()))

for _ in range(N):
    x = list(map(int, input().split()))
    x_list.append(x)

print(ans)
