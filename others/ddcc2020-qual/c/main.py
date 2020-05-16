#!/usr/bin/env python3

H, W, K = list(map(int, input().split()))
table = []

for _ in range(H):
    w_list = input()
    table.append(w_list)

cut_table = []
k_no = 1
first_cut_str = ""
skip_count = 0
for h, w_list in enumerate(table):
    cut_str = ""
    cake_count = 0
    if "#" not in w_list:
        # 1列上にケーキが1個もない場合
        if first_cut_str:
            # 上の段までにすでにケーキが登場している場合
            # 上の段の区切りに合わせる
            cut_str = cut_table[-1]
            cut_table.append(cut_str)
        else:
            # 未登場の場合、下の段に合わせる
            # 後からスキップした回数分追加する
            skip_count += 1
        continue

    for w, item in enumerate(w_list):

        if item == "#":
            cake_count += 1
            if cake_count >= 2:
                k_no += 1
        cut_str += str(k_no) + " "
    cut_str = cut_str.rstrip() + "\n"
    if not first_cut_str:
        first_cut_str = cut_str
    k_no += 1
    cut_table.append(cut_str)

cut_table_str = "".join(cut_table)

if skip_count > 0:
    cut_table_str = first_cut_str * skip_count + cut_table_str

ans = cut_table_str
print(ans)
