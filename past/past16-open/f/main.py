#!/usr/bin/env python3
import sys
sys.set_int_max_str_digits(0)

s_list = input().split("*")
C = 998244353
r = 1
for s in s_list:
    r *= int(s)
    r %= C

ans = r % C
print(ans)
