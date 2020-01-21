#!/usr/bin/env python3

N = int(input().split()[0])
p_list = list(map(int, input().split()))
# p_list = p_list[::-1]
min_p = p_list[0]
c = 0
for p in p_list:
    if p <= min_p:
        c += 1
        min_p = p

ans = c

print(ans)
