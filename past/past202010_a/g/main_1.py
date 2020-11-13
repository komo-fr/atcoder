#!/usr/bin/env python3

N, M = list(map(int, input().split()))
s_table = []

for _ in range(N):
    s_list = list(input())
    s_table.append(s_list)

group_table = []
group_no = -1
for i, s_list in enumerate(s_table):
    group_list = []
    for j, s in enumerate(s_list):
        my_info = dict(s=s)
        if s == ".":
            if i != 0 and s_table[i - 1][j] == ".":  # 上
                my_info["group"] = group_table[i - 1][j]["group"]
            elif j != 0 and s_table[i][j - 1] == ".":  # 左
                my_info["group"] = group_list[j - 1]["group"]
            else:
                group_no += 1
                my_info["group"] = str(group_no)
        else:
            my_info["group"] = "X"

        # print(f"{i=}, {j=}, {s=}, group={my_info['group']}")

        group_list.append(my_info)
    group_table.append(group_list)

for group_list in group_table:
    text = ""
    for g in group_list:
        text += g["group"]
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
