#!/usr/bin/env python3
import collections

N = int(input().split()[0])
S = input()

index2count_dict = collections.defaultdict(int)
left_black_count = 0
for i, char in enumerate(S):
    index2count_dict[i] = left_black_count
    if char == "#":
        left_black_count += 1

right_white_count = 0
min_count = float("inf")
for i in range(N):
    index = N - (i + 1)
    count = index2count_dict[index] + right_white_count
    min_count = min(min_count, count)
    if S[index] == ".":
        right_white_count += 1

ans = min_count
print(ans)
