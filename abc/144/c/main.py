#!/usr/bin/env python3

N = int(input().split()[0])


def get_divisor(n: int) -> list:
    d_list = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            a = int(n / i)
            d_list.append((i, a))
    return d_list


min_d = float("inf")

for d_set in get_divisor(N):
    x, y = d_set
    min_d = min(abs(1 - x) + abs(1 - y), min_d)

ans = min_d
print(ans)
