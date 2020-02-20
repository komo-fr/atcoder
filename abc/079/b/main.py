#!/usr/bin/env python3

N = int(input().split()[0])
l_list = []

for i in range(N + 1):
    if i == 0:
        l_list.append(2)
    elif i == 1:
        l_list.append(1)
    else:
        l_list.append(l_list[i - 1] + l_list[i - 2])
ans = l_list[-1]

print(ans)
