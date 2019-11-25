#!/usr/bin/env python3

N = int(input().split()[0])

a_list = []
b_list = []
edge_dict = {}
edge_list = []

for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    edge_list.append((a, b))
    edge_dict[(a, b)] = dict(a=a, b=b, color=None)
    a_list.append(a)
    b_list.append(b)

# ルートを探す
root = list(set(a_list) - set(b_list))[0]

node_dict = {}
for node_id in list(set(a_list) | set(b_list)):
    node_data = dict(node_id=node_id, parent=None, children=[])
    node_dict[node_id] = node_data

for edge in edge_list:
    p, c = edge
    node_dict[p]["children"].append(c)
    node_dict[c]["parent"] = p

max_color_degree = -float("inf")
for k, v in node_dict.items():
    d = len(v["children"])
    # 親がいない場合は、親の数も含める
    d = d + 1 if v["parent"] else d
    max_color_degree = max(max_color_degree, d)

COLOR_SET = set(range(max_color_degree))


def color_edge(parent):
    next_node_list = node_dict[parent]["children"]
    parent_parent = node_dict[parent]["parent"]
    parent_edge_color = edge_dict[(parent_parent, parent)]["color"]
    ng_color_set = set([parent_edge_color])
    ok_color_list = list(COLOR_SET - ng_color_set)

    for child in next_node_list:
        color = ok_color_list.pop(0)
        edge_dict[(parent, child)]["color"] = color
    return


parent = root
next_node_list = node_dict[root]["children"]
ng_color_set = set()
ok_color_list = list(COLOR_SET - ng_color_set)
next_next_node_list = []

for child in next_node_list:
    color = ok_color_list.pop(0)
    edge_dict[(parent, child)]["color"] = color
    next_next_node_list += node_dict[child]["children"]

while next_node_list:
    next_next_node_list = []
    for child in next_node_list:
        color_edge(child)
        next_next_node_list += node_dict[child]["children"]
    next_node_list = next_next_node_list

color_list = []
for edge in edge_list:
    a, b = edge
    color_list.append(edge_dict[(a, b)]["color"])

ans = "\n".join([str(x + 1) for x in color_list])

print(len(COLOR_SET))
print(ans)
