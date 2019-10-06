# https://atcoder.jp/contests/abc034/tasks/abc034_c
# C - 経路

W, H = list(map(int, input().split()))

mod = 1000000007

N = H + W - 2
R = H - 1

fact_list = []

for i in range(1, N + 1):
    if i == 1:
        fact_n = 1 % mod
    else:
        fact_n = fact_list[i-2] * i % mod
    fact_list.append(fact_n)

fact_n_r = fact_list[N-R-1]
fact_r = fact_list[R-1]

w = pow(fact_n_r * fact_r % mod, (mod - 2), mod)
ans = fact_n * w % mod
print(ans)
