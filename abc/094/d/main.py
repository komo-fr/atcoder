#!/usr/bin/env python3

import math
import numpy as np

n = int(input().split()[0])
a_list = list(map(int, input().split()))


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


a_list = sorted(a_list)
max_comb = -float("inf")

for i, ai in enumerate(a_list):
    # aiを固定する
    # aiが偶数の場合は、ai/2、
    # aiが奇数の場合は、(ai-1)/2または(ai+1)/2に
    # 一番近い値が答えになる
    if ai % 2 == 0:
        idx = np.abs(np.asarray(a_list) - ai // 2).argmin()
        aj = a_list[idx]
    else:
        target_1 = (ai - 1) // 2
        idx_1 = np.abs(np.asarray(a_list) - target_1).argmin()
        aj = a_list[idx_1]
        target_2 = (ai + 1) // 2
        idx_2 = np.abs(np.asarray(a_list) - target_2).argmin()

        if abs(a_list[idx_1] - target_1) > abs(a_list[idx_2] - target_2):
            aj = a_list[idx_2]

    comb = C(ai, aj)
    if max_comb < comb:
        max_comb = comb
        comb_set = (ai, aj)

ans = "{} {}".format(ai, aj)
print(ans)
