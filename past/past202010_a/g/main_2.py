#!/usr/bin/env python3

N, M = list(map(int, input().split()))
s_table = []

for _ in range(N):
    s_list = list(input())
    s_table.append(s_list)


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, i):
        if self.parents[i] == i:
            # 自分自身だったらそのまま返す
            return i
        else:
            # 自分の祖先を、自分の祖先の祖先で更新する
            # こうすることで、途中を飛ばすことができる
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i != j:
            i, j = min(i, j), max(i, j)

            # 別の家族だったら養子に迎える
            self.parents[j] = i


group_table = [["X"] * M for _ in range(N)]
group_no = -1
g2nodes = {}

for i, s_list in enumerate(s_table):
    group_list = []
    for j, s in enumerate(s_list):
        my_info = dict(s=s)
        if s == ".":
            group_kouho_list = []
            if i != 0 and s_table[i - 1][j] == ".":  # 上
                group_kouho_list.append(group_table[i - 1][j]["group"])
            if j != 0 and s_table[i][j - 1] == ".":  # 左
                group_kouho_list.append(group_list[j - 1]["group"])

            if group_kouho_list:
                group_kouho_set_list = list(set(group_kouho_list))
                if len(group_kouho_set_list) == 1:
                    # 候補が一つしかない場合
                    group_no = group_kouho_set_list[0]
                    my_info["group"] = group_no
                    g2nodes[group_no] += [(i, j)]
                else:
                    # 候補が複数ある場合は統合
                    group_no = group_kouho_set_list[0]
                    my_info["group"] = group_no
                    g2nodes[group_no] += [(i, j)]

                    sub_no = group_kouho_set_list[1]
                    print(f"{g2nodes=}")
                    for node_id in g2nodes[sub_no]:
                        print(f"統合される側={g2nodes[sub_no]}")
                        print(f"{node_id=}")
                        group_table[node_id[0]][node_id[1]] = group_no
                    g2nodes[group_no] += g2nodes[sub_no]
                    g2nodes[sub_no] = []
            else:
                # 新しいグループ
                group_no += 1
                my_info["group"] = group_no
                g2nodes[group_no] = [(i, j)]

        else:
            my_info["group"] = "X"

        print(f"{i=}, {j=}, {s=}, group={my_info['group']}, {g2nodes=}")

        group_list.append(my_info)
    group_table.append(group_list)

for group_list in group_table:
    text = ""
    for g in group_list:
        text += str(g["group"])
    print(text)

kouho_count = 0
for i, group_list in enumerate(group_table):
    for j, my_info in enumerate(group_list):
        if my_info == ".":
            continue

        adj_group_list = []
        if i != 0 and s_table[i - 1][j] == ".":  # 上
            adj_group_list.append(group_table[i - 1][j]["group"])

        if j != 0 and s_table[i][j - 1]:  # 左
            adj_group_list.append(group_table[i][j - 1]["group"])

        if i < N - 1 and s_table[i + 1][j] == ".":  # 下
            adj_group_list.append(group_table[i + 1][j]["group"])

        if j < M - 1 and s_table[i][j - 1]:  # 右
            adj_group_list.append(group_table[i][j + 1]["group"])

        adj_set = set(adj_group_list)
        print(f"{i=}, {j=}, {adj_set=}")

    if len(adj_set) == group_no:
        kouho_count += 1

ans = kouho_count
print(ans)
