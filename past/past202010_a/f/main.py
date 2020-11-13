#!/usr/bin/env python3
import collections

N, K = list(map(int, input().split()))
s_list = []

for _ in range(N):
    s = input()
    s_list.append(s)

counter = collections.Counter(s_list)
w = counter.most_common()[K - 1]
# print(w)
# print(counter)
counter_2 = collections.Counter(counter.values())
# print(counter_2)
if counter_2[w[1]] >= 2:
    ans = "AMBIGUOUS"
else:
    ans = w[0]

print(ans)
