#!/usr/bin/env python3

S = input()
s_list = [int(x) for x in S.split("*")]
C = 998244353
r = s_list[0] % C
for s in s_list[1:]:
    r *= s % C

ans = r % C
print(ans)
