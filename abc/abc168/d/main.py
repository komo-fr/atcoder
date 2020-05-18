#!/usr/bin/env python3
import collections

N, M = list(map(int, input().split()))

# 隣の部屋の辞書
# node2nb_dict = {i + 1: [] for i in range(N)}  # 2 * 10** 5
node2nb_dict = collections.defaultdict(lambda: [])

for _ in range(M):  # 2 * 10** 5
    a, b = list(map(int, input().split()))
    node2nb_dict[a].append(b)
    node2nb_dict[b].append(a)

# 幅優先でいく
route_dict = {}
done_set = {1}


def f(next_targets, node_a):
    w_next_targets = {}
    for node in next_targets:
        # 巡回済みノードの更新
        global done_set
        done_set = done_set | {node}

        # 次の探索対象
        my_next_targets = list(set(node2nb_dict[node]) - done_set - set(next_targets))
        w_next_targets[node] = my_next_targets
        route_dict[node] = node_a

        for next_node in my_next_targets:
            # 次の探索対象も確定させる
            route_dict[next_node] = node
            # done_set = done_set | {next_node}  # 巡回済みノードの更新
    return w_next_targets


node_a = 1
next_targets = {node_a: node2nb_dict[1]}

while next_targets:
    for node_a, next_list in next_targets.items():
        next_targets = f(next_list, node_a)

if len(route_dict.keys()) == N - 1:
    ans = "Yes\n"
    for i in range(2, N + 1):
        ans += str(route_dict[i]) + "\n"
else:
    ans = "No"

# print(route_dict)
print(ans)
