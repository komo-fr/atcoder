#!/usr/bin/env python3
import collections

N = int(input().split()[0])
a_list = list(map(int, input().split()))

excepted_dict = {}

if N % 2 == 0:
    n = N // 2
    expected_dict = {i * 2 + 1: 2 for i in range(n)}
else:
    n = N // 2
    expected_dict = {i * 2: 2 for i in range(n + 1)}
    expected_dict[0] = 1

counter = collections.Counter(a_list)

mod = 10 ** 9 + 7

if dict(counter) == expected_dict:
    c = 1
    for v in counter.values():
        c = ((c % mod) * (v % mod)) % mod
    ans = c
else:
    ans = 0

print(ans)
