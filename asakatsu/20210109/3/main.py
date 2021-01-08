#!/usr/bin/env python3
from collections import Counter

S = input()
s = S.replace("W", "0")
s = s.replace("B", "1")

s_list = [int(char) for char in s]
N = len(s_list)
count = 0
for i in range(N):
    for j in range(N - i - 1):
        if s_list[j] > s_list[j + 1]:
            count += 1
            s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
ans = count
print(ans)
