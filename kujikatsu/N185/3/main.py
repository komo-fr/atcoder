#!/usr/bin/env python3
from collections import Counter

N = int(input().split()[0])
c_list = input()


counter = Counter(c_list)
red_n = counter["R"]

left_w_n = Counter(c_list[:red_n])["W"]
ans = left_w_n
print(ans)
