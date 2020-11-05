#!/usr/bin/env python3

n = int(input().split()[0])
ab_list = []
min_paint = float("inf")
max_paint = -float("inf")

for _ in range(n):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))
    min_paint = min(min_paint, a)
    max_paint = max(max_paint, b)

work_list = [0] * (max_paint + 2)

for ab in ab_list:
    a, b = ab
    work_list[a] += 1
    work_list[b + 1] -= 1

cumsum_list = []

for i in range(max_paint + 1):
    if i == 0:
        cumsum_list.append(work_list[i])
    else:
        cumsum_list.append(cumsum_list[i - 1] + work_list[i])

ans = max(cumsum_list)
print(ans)
