#!/usr/bin/env python3

X, N = list(map(int, input().split()))
p_list = list(map(int, input().split()))


if p_list:
    max_p = max(p_list)
    min_diff = float("inf")
    ans_list = []
    for i in range(-max_p, max_p + 2):
        if i in p_list:
            continue

        if abs(X - i) < min_diff:
            min_diff = abs(X - i)
            ans_list = [i]
        elif abs(X - i) == min_diff:
            ans_list.append(i)
    ans = min(ans_list)
else:
    ans = X

print(ans)
