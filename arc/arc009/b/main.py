#!/usr/bin/env python3

b_list = list(map(int, input().split()))
N = int(input().split()[0])
a_list = []

for _ in range(N):
    a = int(input().split()[0])
    a_list.append(a)

otogi2real_dict = {}
for i, b in enumerate(b_list):
    otogi2real_dict[str(b)] = str(i)

real_list = []
real2otogi_dict = {}
for a in a_list:
    w = "_".join(list(str(a)))
    w = w + "_"
    for otogi_n, real_n in otogi2real_dict.items():
        w = w.replace(otogi_n + "_", otogi2real_dict[otogi_n] + "*")
    w = w.replace("*", "")
    real_list.append(int(w))
    real2otogi_dict[int(w)] = a

real_list.sort()
for real in real_list:
    print(real2otogi_dict[real])
