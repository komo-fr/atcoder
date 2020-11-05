# https://atcoder.jp/contests/abc075/tasks/abc075_c
# C - Bridge
import copy
import itertools

N, M = list(map(int, input().split()))
edge_list = []
for _ in range(M):
    a, b = list(map(int, input().split()))
    edge_list.append((a, b))

all_edge_list = sorted(edge_list, key=lambda x: (x[0], x[1]))
all_node_list = list(set(list(itertools.chain.from_iterable(edge_list))))

bridge_list = []

for removed_edge in all_edge_list:  # 50
    r_a, r_b = removed_edge[0], removed_edge[1]

    # 当該エッジを除去した後のエッジリスト
    w_edge_list = copy.copy(all_edge_list)
    w_edge_list.remove((r_a, r_b))

    # 最初のエッジ
    a, b = w_edge_list[0]
    done_node_list = []
    done_node_list.append(a)
    done_node_list.append(b)

    done_edge_list = []
    done_edge_list.append((a, b))

    while True:
        # 探索済ノードから伸びているエッジを探す
        connected_edges = [edge for edge in w_edge_list if edge[0] in done_node_list or edge[1] in done_node_list]
        new_edges = set(connected_edges) - set(done_edge_list)
        for edge in new_edges:
            # 新しく見つかったエッジ
            done_edge_list.append(edge)
            done_node_list.append(edge[0])
            done_node_list.append(edge[1])
            done_node_list = list(set(done_node_list))
        if not new_edges:
            break

    if len(done_node_list) != len(all_node_list):
        # 全てのノードを探索し尽くしていない
        bridge_list.append((r_a, r_b))

ans = len(bridge_list)
print(ans)
