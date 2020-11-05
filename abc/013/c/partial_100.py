#!/usr/bin/env python3
N, H = list(map(int, input().split()))
cost_a, eat_b, cost_c, eat_d, no_eat_e = list(map(int, input().split()))

min_cost = float("inf")

for normal_c in range(N + 1):
    # normal_c: 普通の食事を食べる回数
    for simple_c in range(N + 1 - normal_c):
        # simple_c: 質素な食事を食べる回数
        h = H
        cost = 0

        h += eat_b * normal_c
        h += eat_d * simple_c
        no_eat_c = N - (normal_c + simple_c)
        h -= no_eat_e * no_eat_c
        if h > 0:
            cost = cost_a * normal_c + cost_c * simple_c
            min_cost = min(min_cost, cost)

ans = min_cost
print(ans)
