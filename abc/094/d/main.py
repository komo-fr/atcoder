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
    idx = np.abs(np.asarray(w_list) - ai // 2).argmin()
    aj = w_list[idx]
else:
    t_1 = (ai - 1) // 2
    idx_1 = np.abs(np.asarray(w_list) - t_1).argmin()
    aj_1 = w_list[idx_1]

    t_2 = (ai + 1) // 2
    idx_2 = np.abs(np.asarray(w_list) - t_2).argmin()
    aj_2 = w_list[idx_2]

    if abs(t_1 - aj_1) < abs(t_2 - aj_2):
        aj = aj_1
    else:
        aj = aj_2

ans = "{} {}".format(ai, aj)
print(ans)
