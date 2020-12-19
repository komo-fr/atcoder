#!/usr/bin/env python3
import math

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))

a_list = list(sorted(a_list))
min_d = float("inf")
d_list = []
# print(f"{a_list=}")

for i, a in enumerate(a_list):  # O(M)
    if i == 0 and a != 1:
        # 左端に白がある場合
        min_d = a - 1
        d_list.append(a - 1)
        continue
    elif i == 0:
        # 左端が青の場合
        continue

    # print(f"{i=}, {a_list[i]} - {a_list[i-1]}")
    d = a_list[i] - a_list[i - 1] - 1
    d_list.append(d)
    if d != 0:
        min_d = min([min_d, d])
else:
    # 右端が白の場合
    if a_list and a_list[-1] != N:
        d = N - a_list[-1]
        min_d = min([min_d, d])
        d_list.append(d)

if a_list:
    if min_d is None:
        k = 1
    else:
        k = min_d
    # print(f"{d_list=}")
    # print(f"{k=}")
    count = 0
    for i, d in enumerate(d_list):  # O(M)
        count += math.ceil(d / k)
else:
    count = 1

ans = count
print(ans)
