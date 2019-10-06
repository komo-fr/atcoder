#!/usr/bin/env python
K, X = list(map(int, input().split()))

l = X - K + 1
r = X + K - 1

ans_list = []
for i in range(l, r + 1):
    ans_list.append(str(i))

print(' '.join(ans_list))
