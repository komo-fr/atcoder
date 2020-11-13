#!/usr/bin/env python3
import numpy as np

N, Q = list(map(int, input().split()))
h_list = list(map(int, input().split()))
h_array = np.array(h_list)
h_array2 = np.roll(h_array, -1)[:-1]
h_array = h_array[:-1]

q_list = []

for _ in range(Q):
    q = list(map(int, input().split()))
    # print(f"{q=}")
    if q[0] == 1:
        # 奇数をvだけ増やす
        v = q[1]
        h_array[::2] = h_array[::2] + v
        h_array2[1::2] = h_array2[1::2] + v
    elif q[0] == 2:
        # 偶数をvだけ増やす
        v = q[1]
        h_array[1::2] = h_array[1::2] + v
        h_array2[::2] = h_array2[::2] + v
    else:
        # uをvだけ増やす
        u, v = q[1], q[2]
        u = u - 1
        # print(f"{u=}")
        # print(f"{h_array}")
        if u < N - 1:
            h_array[u] = h_array[u] + v
        if u != 0:
            h_array2[u - 1] = h_array2[u - 1] + v
    diff = h_array - h_array2
    count = np.count_nonzero(diff == 0)
    print(count)
