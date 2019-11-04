#!/usr/bin/env python3
import collections

N = int(input().split()[0])
S = input()
counter = collections.Counter(S)
count = 1
mod = 10 ** 9 + 7
for _, v in counter.items():
    # その文字数の数 + 1ケース（選ばないケース)
    count = count * (v + 1) % mod

# 空文字列も含まれるので1引く
ans = (count - 1) % mod
print(ans)
