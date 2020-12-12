#!/usr/bin/env python3
from collections import defaultdict, deque

N = int(input().split()[0])
neighbor_dict = defaultdict(lambda: [])
org_edge_list = []

for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    neighbor_dict[a].append(b)
    neighbor_dict[b].append(a)
    org_edge_list.append(tuple(sorted([a, b])))

color_dict = defaultdict(lambda: -1)

start_node_id = 1

# 次の探索対象が入ったキュー
work_queue = deque([start_node_id])

edge_dict = defaultdict(lambda: None)
color_dict = defaultdict(lambda: None)
color_dict[start_node_id] = 0  # ダミー
max_color = 1
while work_queue:
    # 今いるノード
    current_id = work_queue.popleft()
    current_color = color_dict[current_id]
    color = 1

    for neighbor_id in neighbor_dict[current_id]:
        # 今いるノードに隣接するノードを巡回する
        edge = tuple(sorted([current_id, neighbor_id]))

        if edge_dict[edge] is not None:
            continue

        if color == current_color:
            color += 1
        color_dict[neighbor_id] = color
        edge_dict[edge] = color
        max_color = max([max_color, color])
        color += 1
        # 次の巡回対象
        work_queue.append(neighbor_id)

print(max_color)
for edge in org_edge_list:
    print(edge_dict[edge])
