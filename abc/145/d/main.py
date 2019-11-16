#!/usr/bin/env python3

X, Y = list(map(int, input().split()))

# a + 2b = X
# 2a + b = Y
b = (2 * X - Y) / 3  # 下2、右1移動の回数
a = X - 2 * b  # 下1、右2移動の回数
mod = 10 ** 9 + 7

if int(b) != b or int(a) != a:
    ans = 0
elif b < 0 or a < 0:
    ans = 0
else:
    fact_list = []
    N = int(a + b)
    R = int(min(a, b))

    if R != 0:
        for i in range(1, N + 1):
            if i == 1:
                fact_n = 1 % mod
            else:
                fact_n = fact_list[i - 2] * i % mod
            fact_list.append(fact_n)

        fact_n_r = fact_list[N - R - 1]
        fact_r = fact_list[R - 1]

        w = pow(fact_n_r * fact_r % mod, (mod - 2), mod)

        ans = fact_n * w % mod
    else:
        ans = 1 % mod

print(ans)
