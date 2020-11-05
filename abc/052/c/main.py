#!/usr/bin/env python3
import math
import collections

N = int(input().split()[0])

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

mod = 10**9 + 7
c = 1
d_list = []
counter = collections.Counter()

for i in range(1, N+1):
    f_list = factorize(i)
    c = collections.Counter(f_list)
    counter += c

x = 1

for k, v in counter.items():
    x *= (v + 1) % mod

ans = x % mod
print(ans)
