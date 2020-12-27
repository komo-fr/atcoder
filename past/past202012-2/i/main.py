#!/usr/bin/env python3
from collections import defaultdict, deque

N, M, K = list(map(int, input().split()))
h_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

edge_list = []
# 隣接ノードの情報 key=node_id, value=隣接するノードのリスト
neighbor_dict = defaultdict(lambda: [])

for _ in range(M):
    a, b = list(map(int, input().split()))
    a_h, b_h = h_list[a - 1], h_list[b - 1]
    if a_h < b_h:
        neighbor_dict[a].append(b)
    else:
        neighbor_dict[b].append(a)

# 探索済みのノード情報
# 1からの距離が入っている。1から到達できない場合は-1
step_dict = defaultdict(lambda: -1)

# start_node_id = 1
for c in c_list:
    # 避難所は全部0
    step_dict[c] = 0
# 次の探索対象が入ったキュー
work_queue = deque(c_list)

while work_queue:
    # 今いるノード
    current_id = work_queue.popleft()
    for neighbor_id in neighbor_dict[current_id]:
        # 今いるノードに隣接するノードを巡回する
        if step_dict[neighbor_id] != -1:
            # 経由済のノードはスキップする
            # 今いるノードと同じ階層にいるノードは、
            # これの1つ前のステップで既に距離が更新されている=巡回済の扱いになっているのでスキップされる
            continue
        # 距離を更新（現在値 + 1）
        step_dict[neighbor_id] = step_dict[current_id] + 1
        # 次の巡回対象
        work_queue.append(neighbor_id)

for i in range(1, N + 1):
    print(step_dict[i])

# ans =
# print(ans)
