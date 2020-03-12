#!/usr/bin/env python3

N = int(input().split()[0])
x_list = list(map(int, input().split()))

min_cost = float("inf")
for i in range(1, 101):
    t = sum([(x - i) ** 2 for x in x_list])
    min_cost = min(t, min_cost)
ans = min_cost

print(ans)
