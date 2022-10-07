#!/usr/bin/env python3
from collections import defaultdict

N = int(input().split()[0])
xy_list = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    xy_list.append((x, y))


def get_neighbors(i, j):
    neighbors = [
        (i - 1, j - 1),
        (i - 1, j),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]
    return neighbors


group_dict = defaultdict(lambda: [])  # キーがグループ番号、値がノードのリスト
node2group_dict = defaultdict(lambda: -1)  # -1は白マス、それ以外は所属するグループ番号
group_count = 0

for x, y in xy_list:
    # print("=====================")
    # print("ノード:", (x, y))
    n_list = get_neighbors(x, y)
    # 隣接するノードが黒マスの場合
    n_group_list = []
    for i, j in n_list:
        g = node2group_dict[(i, j)]
        if g != -1:
            n_group_list.append(g)
    if n_group_list:
        n_group_list = list(set(n_group_list))
        group = n_group_list[0]
        node2group_dict[(x, y)] = group
        group_dict[group] += [(x, y)]
        if len(n_group_list) > 1:
            # 他のグループも連結されるので更新
            for _g in n_group_list[1:]:
                # 統合
                group_dict[group] += group_dict[_g]
                for _n in group_dict[_g]:
                    # 更新
                    node2group_dict[_n] = group
                group_dict[_g] = []
                group_count -= 1
    else:
        # 新しいグループ
        group = len(group_dict.keys())
        node2group_dict[(x, y)] = group
        group_dict[group] += [(x, y)]
        group_count += 1
    # print(group_dict)

ans = group_count
print(ans)
