#!/usr/bin/env python3
import math

A, B, N = list(map(int, input().split()))

# Test
max_score = -float("inf")
for i in range(1, N + 1):
    if i > B:
        break
    f_1 = math.floor(A * i / B)
    f_2 = A * math.floor(i / B)

    score = f_1 - f_2
    max_score = max(score, max_score)
    # print(f"x = {i}: {f_1} - {f_2} = {p}")
    # print(f"A * x / B = {A * i} / {B} = {A* i/B}")
    # print(f"x / B     = {i / B}")
    # print("========================")

ans = max_score
print(ans)
