#!/usr/bin/env python3
import heapq

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))

# Pythonのheapqは最小値しかとれないので、負の値に変換して扱う
a_list = list(map(lambda x: x * (-1), a_list))
heapq.heapify(a_list)

for _ in range(M):
    max_value = -heapq.heappop(a_list)
    heapq.heappush(a_list, -(max_value // 2))

ans = -sum(a_list)
print(ans)
