#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
start_w = a_list[0] * 2

# 一番小さいものから決めていく？
for sw in range(start_w + 1):
    w_list = []
    if a_list[0] < sw // 2:
        continue
    w_list.append(sw)
    for i in range(1, N):
        w_list.append((a_list[i - 1] - w_list[i - 1] // 2) * 2)

    if a_list[-1] == (w_list[0] + w_list[-1]) // 2:
        break

ans = " ".join([str(w) for w in w_list])
print(ans)
