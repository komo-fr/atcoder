#!/usr/bin/env python3
from collections import deque, defaultdict

N, M = list(map(int, input().split()))

neighbor_dict = defaultdict(lambda: [])

for _ in range(M):  # 2 * 10** 5
    a, b = list(map(int, input().split()))
    neighbor_dict[a].append(b)
    neighbor_dict[b].append(a)

# 作業用キュー
start_node_id = 1
work_queue = deque([start_node_id])
# 探索済ノード
sign_dict = defaultdict(lambda: None)
sign_dict[start_node_id] = -1

while work_queue:
    current_id = work_queue.popleft()
    neighbors = neighbor_dict[current_id]
    for neighbor_id in neighbors:
        if sign_dict[neighbor_id]:
            # 探索済みはスキップ
            continue
        sign_dict[neighbor_id] = current_id
        work_queue.append(neighbor_id)

# Noになるケースはない
ans = "Yes"
print(ans)

for i in range(2, N + 1):
    print(sign_dict[i])
