#!/usr/bin/env python3
import math

N, P = list(map(int, input().split()))
a_list = list(map(int, input().split()))

odd_n = 0
even_n = 0

for a in a_list:
    if a % 2 == 0:
        even_n += 1
    else:
        odd_n += 1


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if P == 0:
    odd_p = 1
    if odd_n > 0:
        # 偶数個選ぶ組み合わせ
        for i in range(2, odd_n + 1, 2):
            odd_p += C(odd_n, i)
    even_p = 2 ** even_n
    p = odd_p * even_p
else:
    odd_p = 0
    if odd_n > 0:
        # 奇数個選ぶ組み合わせ数
        for i in range(1, odd_n + 1, 2):
            odd_p += C(odd_n, i)

    even_p = 2 ** even_n
    p = odd_p * even_p

ans = p

print(ans)
