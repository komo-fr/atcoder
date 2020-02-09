#!/usr/bin/env python3

N, K = list(map(int, input().split()))
p_list = list(map(int, input().split()))
c_list = []

k_list = []
total = 0
for x in range(1001):
    total += x
    if x == 0:
        k_list.append(0)
    else:
        k_list.append(total / x)

max_t = -float("inf")
max_kp = -float("inf")
kp_list = []
t_list = []
for i, p in enumerate(p_list):  # 200000
    kp = k_list[p]
    if i != 0:
        c_list.append(c_list[i - 1] + p)
        kp_list.append(kp_list[i - 1] + kp)
    else:
        c_list.append(p)
        kp_list.append(kp)

    if i >= K - 1:
        if i - K < 0:
            t = c_list[i]
        else:
            t = c_list[i] - c_list[i - K]
        t_list.append(t)

        if t > max_t:
            if i - K < 0:
                max_kp = kp_list[i]
            else:
                max_kp = kp_list[i] - kp_list[i - K]
            max_t = t

ans = max_kp
print(ans)
