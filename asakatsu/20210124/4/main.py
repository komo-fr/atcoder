#!/usr/bin/env python3
import bisect

N = int(input().split()[0])
s_list = []

for _ in range(N):
    s = int(input().split()[0])
    s_list.append(s)

Q = int(input().split()[0])
k_list = []

for _ in range(Q):
    k = int(input().split()[0])
    k_list.append(k)

s_list = list(sorted(s_list, reverse=True))
border_list = []
for i, k in enumerate(k_list):
    # 収容人数はk人
    # k+1番目の点数の人はoutにしたい
    # print(f"{k=}, s_list[{k}]={s_list[k]}")
    if k >= N:
        border = s_list[0] + 1
        border_list.append(0)
        continue

    border = s_list[k] + 1
    if s_list[k] == 0:
        border = 0
    border_list.append(border)


for b in border_list:
    print(b)