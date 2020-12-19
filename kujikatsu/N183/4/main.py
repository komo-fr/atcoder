#!/usr/bin/env python3
from collections import defaultdict

N, X, Y = list(map(int, input().split()))
counter = defaultdict(lambda: 0)

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if i == X and j == Y:
            d = 1
        elif (i <= X and j <= X) or (i >= Y and j >= Y):
            d = j - i
        else:
            d_0 = j - i
            d_1 = abs(i - X) + abs(j - Y) + 1
            d_2 = abs(i - Y) + abs(j - X) + 1
            d = min([d_0, d_1, d_2])
        counter[d] += 1

for k in range(1, N):
    print(counter[k])