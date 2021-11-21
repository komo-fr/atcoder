#!/usr/bin/env python3
import itertools


def get_divisor(n: int) -> list:
    d_list = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            a = int(n / i)
            d_list.append([i, a])
    return d_list


X, Y = list(map(int, input().split()))
x_list = get_divisor(X)
y_list = get_divisor(Y)
x_list = set(itertools.chain.from_iterable(x_list))
y_list = set(itertools.chain.from_iterable(y_list))
if len(x_list) == len(y_list):
    ans = "Z"
elif len(x_list) < len(y_list):
    ans = "Y"
else:
    ans = "X"

print(ans)
