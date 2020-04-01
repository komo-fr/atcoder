#!/usr/bin/env python3

a = int(input().split()[0])
b = int(input().split()[0])
c = int(input().split()[0])

p_list = sorted([a, b, c], reverse=True)
for x in [a, b, c]:
    print(p_list.index(x) + 1)
