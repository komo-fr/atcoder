#!/usr/bin/env python3

import collections

N = int(input().split()[0])
c_input = input()

counter = collections.Counter(c_input)
red_n = counter["R"]
counter = collections.Counter(c_input[:red_n])
left_white_n = counter["W"]
ans = left_white_n
print(ans)
