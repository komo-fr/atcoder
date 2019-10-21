#!/usr/bin/env python3

import math
import bisect
import numpy as np

n = int(input().split()[0])
a_list = list(map(int, input().split()))


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


a_list = sorted(a_list)
max_comb = -float("inf")
a_list = sorted(a_list, reverse=True)
ai = a_list[0]
w_list = a_list[1:]
w_list = sorted(w_list)

# 真ん中に一番近い値を取得する
if ai % 2 == 0:
    if ai // 2 in w_list:
        aj = ai // 2
    else:
        idx = bisect.bisect_left(w_list, ai // 2)
        if idx + 1 < len(a_list):
            if abs(ai // 2 - a_list[idx + 1]) < abs(ai // 2 - a_list[idx]):
                idx = idx + 1
        aj = a_list[idx]
else:
    # 奇数の場合、候補が2つある
    target_1 = (ai - 1) // 2
    idx_1 = bisect.bisect_left(w_list, target_1)
    aj = w_list[idx_1]

    target_2 = (ai + 1) // 2
    idx_2 = bisect.bisect_left(w_list, target_2)

    if abs(a_list[idx_1] - target_1) > abs(a_list[idx_2] - target_2):
        aj = w_list[idx_2]

ans = "{} {}".format(ai, aj)
print(ans)
