#!/usr/bin/env python3
import math
import itertools

N, K = list(map(int, input().split()))

mod = 10 ** 9 + 7

fact_list = []

for i in range(1, N + 1):
    if i == 1:
        fact_n = 1 % mod
    else:
        fact_n = fact_list[i - 2] * i % mod
    fact_list.append(fact_n)

# for r in range(K, N + 1):
#     fact_n_r = fact_list[N - r - 1]
#     fact_r = fact_list[r - 1]
#     w = pow(fact_n_r * fact_r % mod, (mod - 2), mod)
#     w = (10 ** 100) * r % mod + (fact_n * w) % mod
#     w = w % mod
#     t += w
#     t = t % mod


r = K
fact_n_r = fact_list[N - r - 1]
fact_r = fact_list[r - 1]
w = pow(fact_n_r * fact_r % mod, (mod - 2), mod)
# w = (10 ** 100) * r % mod + (fact_n * w) % mod
w = fact_n * w % mod

ans = w
print(ans)


# def C(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


print(C(N, K) % mod)
