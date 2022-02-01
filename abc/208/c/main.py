#!/usr/bin/env python3

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
at_list = []
for i, a in enumerate(a_list):
    at_list.append((a, i))
at_list = sorted(at_list)

x = K // N
y = K % N
c_list = []
for i, at in enumerate(at_list):
    if i + 1 <= y:
        count = x + 1
    else:
        count = x
    c_list.append((at[1], count))
c_list = sorted(c_list)

for c in c_list:
    print(c[1])
