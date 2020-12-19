#!/usr/bin/env python3

N, K = list(map(int, input().split()))


def comb(n, k):
    c = min(k - 1, 2 * n + 1 - k)
    return c


def m_comb(n, k):
    c = k if n > abs(k) else 0
    return c


total = 0
for i in range(2, 2 * N + 1):
    # a+ b = i で固定したときの組み合わせ数
    if K > 0:
        comb_y = comb(N, i - K)
    else:
        comb_y = m_comb(N, i - K)
    # aとbでxを作る時の組み合わせ数
    comb_i = comb(N, i)
    total += comb_y * comb_i

ans = total
print(ans)
