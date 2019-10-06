#!/usr/bin/env python3
import fractions
import itertools

a, b = list(map(int, input().split()))
c = min(a, b)
d = max(a, b)


def factorize(n: int) -> list:
    # 試し割り法
    f_list = []
    while n % 2 == 0:
        f_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            f_list.append(f)
            n //= f
        else:
            # 偶数はすでにチェックしているので+2ずつカウントアップ
            f += 2

    if n != 1:
        f_list.append(n)
    return f_list


a_list = factorize(a)
b_list = factorize(b)

common = (set(a_list) & set(b_list)) | {1}
count = len(common)

print(count)
