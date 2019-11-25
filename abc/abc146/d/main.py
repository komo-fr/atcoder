#!/usr/bin/env python3
from collections import deque

N = int(input().split()[0])

# ノードの情報
node_dict = {i + 1: dict(parent=None, children=[]) for i in range(N)}

a_list = []
b_list = []
edge_dict = {}
edge_list = []

# エッジの情報
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    edge_list.append((a, b))
    edge_dict[(a, b)] = dict(a=a, b=b, color=None)
    a_list.append(a)
    b_list.append(b)

    node_dict[a]["children"].append(b)
    node_dict[b]["parent"] = a

# ルートを探す
root = list(set(a_list) - set(b_list))[0]

max_color_degree = -float("inf")

# 最悪で10 ** 5
for k, v in node_dict.items():
    d = len(v["children"])
    # 親がいない場合は、親の数も含める
    d = d + 1 if v["parent"] else d
    max_color_degree = max(max_color_degree, d)

COLOR_LIST = list(range(max_color_degree))


def color_edge(parent):
    next_node_list = node_dict[parent]["children"]
    parent_parent = node_dict[parent]["parent"]
    parent_edge_color = edge_dict[(parent_parent, parent)]["color"]
    ng_color = parent_edge_color

    # 最悪で10 ** 5
    color_index = 0
    for child in next_node_list:
        color = COLOR_LIST[color_index]
        if color == ng_color:
            color_index += 1
            color = COLOR_LIST[color_index]

        edge_dict[(parent, child)]["color"] = color
        color_index += 1
    return


parent = root
next_node_list = node_dict[root]["children"]
next_next_node_list = []

# 最悪で10 ** 5
color_index = 0
for node in next_node_list:
    color = COLOR_LIST[color_index]
    color_index += 1
    edge_dict[(parent, node)]["color"] = color

# 最悪で10 ** 5
while next_node_list:
    next_parent_list = []
    # 最悪で10 ** 5
    for node in next_node_list:
        color_edge(node)
        next_parent_list += node_dict[node]["children"]
    # コピーはO(N)
    next_node_list = next_parent_list

color_list_str = ""
for edge in edge_list:
    a, b = edge
    color_list_str += str(edge_dict[(a, b)]["color"] + 1) + "\n"

print(max_color_degree)
print(color_list_str)
