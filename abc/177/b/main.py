#!/usr/bin/env python3

S = input()
T = input()
min_diff_count = float("inf")
for i in range(len(S)):
    if i + len(T) > len(S):
        break
    count = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            count += 1
    min_diff_count = min(min_diff_count, count)

# ans = 0 if min_diff_count == float("inf") else min_diff_count
ans = min_diff_count
print(ans)
