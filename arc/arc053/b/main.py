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
    stock_n = even_len_sum
    min_len = odd_len_list[0]

    # 一番短い奇数長に合わせて、他は全部ストックに回す
    stock_n += sum([x - min_len for x in odd_len_list])

    if stock_n:
        min_len = min_len + ((stock_n // 2) // odd_n) * 2

ans = min_len
print(ans)
