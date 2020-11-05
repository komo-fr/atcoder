#!/usr/bin/env python3
import math
import itertools

N = int(input().split()[0])

# 6を使うパターンを列挙
i = 0
p_6_list = []
while 6 ** i <= N:
    p_6_list.append(6 ** i)
    i += 1

p_9_list = []
i = 0
while 9 ** i <= N:
    p_9_list.append(9 ** i)
    i += 1

p_6_gen = list(itertools.product(range(0, 6), repeat=len(p_6_list)))
min_count = float("inf")

for p_6 in p_6_gen:
    x = sum([x * i for x, i in zip(p_6_list, list(p_6))])
    c = sum(list(p_6))

    if c >= min_count:
        # この時点ですでに最小記録更新できないとわかるので、
        # あとの計算は実施しない
        continue

    balance = N - x
    if balance < 0:
        continue

    for y in reversed(p_9_list):
        # 大きい方から払えるだけ払う
        y_count = balance // y
        balance -= y * y_count
        c += y_count
        if balance == 0:
            break

    min_count = min(min_count, c)

ans = min_count
print(ans)
