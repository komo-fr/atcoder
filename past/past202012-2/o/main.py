#!/usr/bin/env python3
from collections import defaultdict

N, M = list(map(int, input().split()))

neighbor_dict = defaultdict(lambda: [])
edge_dict = defaultdict(lambda: False)

for _ in range(M):
    a, b = list(map(int, input().split()))
    neighbor_dict[a].append(b)
    neighbor_dict[a].append(a)
    edge_dict[(a, b)] = True
    edge_dict[(b, a)] = True

q_list = list(map(int, input().split()))
Q = q_list[0]
n_list = []
done_q_dict = defaultdict(lambda: 0)
n_idx = 0
for q_idx in range(Q):  # 10 ** 5
    # print(f"{q_idx=}, {n_list=}")
    q = list(map(int, input().split()))
    t, x = q
    if t == 1:
        n_idx += 1
        n_list.append(x)
    else:
        count = 0
        for y in n_list[done_q_dict[x] :]:  # 10 ** 5
            if edge_dict[(x, y)] or edge_dict[(y, x)]:
                count += 1
        done_q_dict[x] = n_idx
        print(count)
