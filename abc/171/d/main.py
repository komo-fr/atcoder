#!/usr/bin/env python3
import collections

N = int(input().split()[0])
a_list = list(map(int, input().split()))
Q = int(input().split()[0])
bc_list = []

for _ in range(Q):
    b, c = list(map(int, input().split()))
    bc_list.append((b, c))

counter = collections.Counter(a_list)
total = 0
for k, v in counter.items():
    total += k * v

for b, c in bc_list:
    b_count = counter[b]
    total -= b * b_count
    counter[b] = 0

    counter[c] += b_count
    total += c * b_count
    print(total)
