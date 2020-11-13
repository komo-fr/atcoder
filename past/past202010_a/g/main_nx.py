#!/usr/bin/env python3
import networkx as nx

N, M = list(map(int, input().split()))
s_table = []

for _ in range(N):
    s_list = list(input())
    s_table.append(s_list)

group_table = []
G = nx.Graph()
for i in range(N):
    group_list = []
    for j in range(M):
        if s_table[i][j] == ".":
            G.add_node((i, j))
        group_list.append("X")
    group_table.append(group_list)

for i, s_list in enumerate(s_table):
    for j, s in enumerate(s_list):
        if s == ".":
            if i != 0 and s_table[i - 1][j] == ".":  # 上
                G.add_edge((i, j), (i - 1, j))
            if j != 0 and s_table[i][j - 1] == ".":  # 左
                G.add_edge((i, j), (i, j - 1))

# print(group_table)

compo = list(nx.connected_components(G))
for group_id, com in enumerate(compo):
    for node_id in com:
        group_table[node_id[0]][node_id[1]] = group_id

group_n = len(compo)

kouho_count = 0
kouho_list = []
for i, group_list in enumerate(group_table):

    for j, my_group in enumerate(group_list):
        if s_table[i][j] == ".":
            continue

        adj_group_list = []
        debug = ""
        if i != 0 and s_table[i - 1][j] == ".":  # 上
            adj_group_list.append(group_table[i - 1][j])
            # debug += f"上: {group_table[i - 1][j]} "

        if j != 0 and s_table[i][j - 1]:  # 左
            adj_group_list.append(group_table[i][j - 1])
            # debug += f"左: {group_table[i][j-1]} "

        if i < N - 1 and s_table[i + 1][j] == ".":  # 下
            adj_group_list.append(group_table[i + 1][j])
            # debug += f"下: {group_table[i + 1][j]} "

        if j < M - 1 and s_table[i][j - 1]:  # 右
            adj_group_list.append(group_table[i][j + 1])
            # debug += f"右: {group_table[i][j+1]} "

        adj_set = set(adj_group_list) - set("X")
        # print(f"{i=}, {j=}, {adj_set=}, len(adj_set)={len(adj_set)}")

        if len(adj_set) == group_n:
            kouho_count += 1
            kouho_list.append((i, j))
            # print(
            #     f"{i=}, {j=}, {adj_set=}, len(adj_set)={len(adj_set)}, {adj_group_list=}, {debug=}"
            # )
# print(kouho_list)
ans = kouho_count
print(ans)
