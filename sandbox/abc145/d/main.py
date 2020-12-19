#!/usr/bin/env python3

X, Y = list(map(int, input().split()))
mod = 10 ** 9 + 7

# a + 2b = X
# 2a + b = Y
b = (2 * X - Y) / 3  # 上2右1移動の回数
a = X - 2 * b  # 上1右2移動の回数

if int(a) != a or int(b) != b:
    ans = 0
elif a < 0 or b < 0:
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