#!/usr/bin/env python3
import itertools

N, H = list(map(int, input().split()))
cost_a, eat_b, cost_c, eat_d, no_eat_e = list(map(int, input().split()))

p_gen = itertools.product("cde", repeat=N)
min_cost = float("inf")

for patterns in p_gen:
    cost = 0
    h = H
    is_ok = True
    for p in patterns:
        if p == "c":
            h += eat_b
            cost += cost_a
        elif p == "d":
            h += eat_d
            cost += cost_c
        else:
            h -= no_eat_e
        if h <= 0:
            is_ok = False
            break
    if is_ok:
        min_cost = min(min_cost, cost)

ans = min_cost
print(ans)
