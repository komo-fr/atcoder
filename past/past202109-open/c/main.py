#!/usr/bin/env python3

N, X = list(map(int, input().split()))
a_list = list(map(int, input().split()))

count = 0

for a in a_list:
    if a == X:
        count += 1
ans = count
print(ans)
