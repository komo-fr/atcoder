#!/usr/bin/env python3

N = int(input().split()[0])
x_list = list(map(int, input().split()))
sorted_list = sorted(x_list)

l_mid = sorted_list[N // 2 - 1]
r_mid = sorted_list[N // 2]

for x in x_list:
    if x <= l_mid:
        print(r_mid)
    else:
        print(l_mid)
