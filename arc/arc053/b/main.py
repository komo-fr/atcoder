#!/usr/bin/env python3
import collections

S = input()
counter = collections.Counter(S)

odd_len_list = []
even_n = 0
odd_n = 0
even_len_sum = 0

for c in counter.values():
    if c % 2 == 0:
        even_n += 1
        even_len_sum += c
    else:
        odd_n += 1
        odd_len_list.append(c)

odd_len_list = sorted(odd_len_list)

if odd_n < 2:
    min_len = len(S)
else:
    even_len = even_len_sum
    min_len = odd_len_list[0]

    for i, x in enumerate(odd_len_list[:-1]):
        if even_len < 1:
            break
        next_len = odd_len_list[i + 1]
        d = next_len - x

        # 奇数長の差をなるべく埋めていく
        if d > 0:
            if even_len >= d:
                even_len -= d
                min_len = next_len
            else:
                min_len = x + even_len
                even_len = 0
    if even_len:
        # まだ残っている場合、なるべく均等になるように割り振る
        min_len = min_len + ((even_len // 2) // odd_n) * 2

ans = min_len
print(ans)
