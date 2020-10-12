#!/usr/bin/env python3
import networkx as nx

N, M = list(map(int, input().split()))
edge_set = set()
# edge_set = []
for _ in range(M):
    s, t = list(map(int, input().split()))
    s, t = min(s, t), max(s, t)
    edge_set = edge_set | {(s, t)}
    # edge_set.append((s, t))

group_list = []
group_dict = {i + 1: None for i in range(N)}

for edge in edge_set:  # 10 ** 5
    s, t = edge
    # print(f"edge={edge}")
    if (group_dict[s] is None) and (group_dict[t] is None):
        group_list.append({s, t})
        new_group = len(group_list) - 1
        group_dict[s] = new_group
        group_dict[t] = new_group
    elif group_dict[s] is not None:
        group_index = group_dict[s]
        group_list[group_index] = group_list[group_index] | {s, t}
        if group_dict[t] is not None:
            other_group_index = group_dict[t]
            if other_group_index == group_index:
                continue

            other_group = group_list[other_group_index]
            group_list[group_index] = group_list[group_index] | other_group
            for i in group_list[other_group_index]:
                group_dict[i] = group_index
            group_list[other_group_index] = set()
        group_dict[t] = group_index
    else:
        group_index = group_dict[t]
        group_list[group_index] = group_list[group_index] | {s, t}
        group_dict[s] = group_index

    # print(group_list)
    # print(group_dict)
    # print("----------")

max_group_size = 1
for group in group_list:
    max_group_size = max(len(group), max_group_size)

ans = max_group_size

print(ans)
