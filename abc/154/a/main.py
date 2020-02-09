#!/usr/bin/env python3

s, t = list(input().split())
a, b = list(map(int, input().split()))
u = input()
ab_list = [a, b]
n_list = [s, t]

ab_list[n_list.index(u)] = ab_list[n_list.index(u)] - 1
ans = " ".join([str(x) for x in ab_list])

print(ans)
