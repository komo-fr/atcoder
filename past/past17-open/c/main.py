#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
p_list = list(map(int, input().split()))
x_list = []

ans = sum([p_list[a - 1] for a in a_list])
print(ans)
