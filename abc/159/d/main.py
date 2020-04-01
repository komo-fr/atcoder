#!/usr/bin/env python3
import math
import collections


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(input().split()[0])
a_list = list(map(int, input().split()))

counter = collections.Counter(a_list)
ans_dict_1 = {}
ans_dict_2 = {}

for k, v in counter.items():
    if v >= 2:
        ans_dict_1[k] = C(v, 2)
    if v >= 3:
        ans_dict_2[k] = C(v - 1, 2)
total_w = sum(ans_dict_1.values())

for k in range(N):
    n = a_list[k]

    if counter[n] >= 3:
        w = total_w - ans_dict_1[n] + ans_dict_2[n]
    elif counter[n] >= 2:
        w = total_w - ans_dict_1[n]
    else:
        w = total_w
    print(w)

