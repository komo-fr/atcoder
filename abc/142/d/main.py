#!/usr/bin/env python3
import fractions
import itertools

a, b = list(map(int, input().split()))
c = min(a, b)
d = max(a, b)


def get_divisor(n: int) -> list:
    d_list = []
    for i in range(1, int(n ** 1 / 2) + 1):
        if n % i == 0:
            a = int(n / i)
            d_list += [a, i]
    d_list = list(set(d_list))
    return d_list


w_list = get_divisor(c)
# 正の公約数
# 以下のリストから任意の数を選ぶ
koyaku_list = [w for w in w_list if d % w == 0]




    # if fractions.gcd(x, y) == 1:
    #     count += 1

print(count)
