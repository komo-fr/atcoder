#!/usr/bin/env python3
from collections import defaultdict

N, M = list(map(int, input().split()))
xy_list = []
src2dst_map = defaultdict(lambda: [])
dst2src_map = defaultdict(lambda: [])

for _ in range(M):
    x, y = list(map(int, input().split()))
    src2dst_map[x].append(y)
    dst2src_map[y].append(x)

done = defaultdict(lambda: False)
longest_path_dict = dict()


def calc_longest_path(node_id):
    global done
    # global longest_path_dict

    if done[node_id]:
        return longest_path_dict[node_id]

    longest_path = 0
    for dst_node_id in src2dst_map[node_id]:
        longest_path = max(longest_path, calc_longest_path(dst_node_id) + 1)

    done[node_id] = True
    longest_path_dict[node_id] = longest_path
    return longest_path


total_longest_path = 0
for node_id in range(1, N + 1):
    if not dst2src_map[node_id]:
        total_longest_path = max(total_longest_path, calc_longest_path(node_id))

# print(longest_path_dict)
ans = total_longest_path
print(ans)
