#!/usr/bin/env python3

N = int(input().split()[0])
l_list = list(map(int, input().split()))

max_l = max(l_list)
t = sum(l_list) - max_l
ans = "Yes" if max_l < t else "No"

print(ans)
