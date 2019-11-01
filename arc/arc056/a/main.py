#!/usr/bin/env python3

A, B, K, L = list(map(int, input().split()))

if K % L == 0:
    n = K // L
    cost = B * n
else:
    b_set_n = K // L
    a_n = K - L * b_set_n
    cost_1 = B * b_set_n + A * a_n
    cost_2 = B * (b_set_n + 1)
    cost = min(cost_1, cost_2)

ans = cost
print(ans)
