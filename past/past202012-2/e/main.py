#!/usr/bin/env python3
import numpy as np

H, W = list(map(int, input().split()))
s_table = []
t_table = []

for _ in range(H):
    s = input()
    s = list(s)
    s_table.append(s)

for i in range(H):
    t = input()
    t = list(t)
    t_table.append(t)
# trim
is_space = False
for i in range(H - 1, -1, -1):
    if "#" in t_table[i]:
        if is_space:
            t_table = t_table[: i + 1]
        break
    else:
        is_space = True
# print("Trim0--------")
# print(t_table)
is_space = False

for i in range(len(t_table)):
    if "#" in t_table[i]:
        if is_space:
            t_table = t_table[i:]
        break
    else:
        is_space = True
# print("Trim1--------")
# print(t_table)

t_table = np.rot90(t_table)
# print("Rotate------")
# print(t_table)

is_space = False
for i in range(W - 1, -1, -1):
    if "#" in t_table[i]:
        if is_space:
            t_table = t_table[: i + 1]
        break
    else:
        is_space = True

# print("Trim2--------")
# print(t_table)
is_space = False

for i in range(len(t_table)):
    if "#" in t_table[i]:
        if is_space:
            t_table = t_table[i:]
        break
    else:
        is_space = True
# print("Trim3--------")
# print(t_table)

t_table_0 = t_table.copy()
t_table_1 = np.rot90(t_table_0)
t_table_2 = np.rot90(t_table_1)
t_table_3 = np.rot90(t_table_2)

t_patterns = [t_table_0, t_table_1, t_table_2, t_table_3]
is_found = False


def print_t(table):
    for t in table:
        print(t)


for t_table in t_patterns:

    # print("=============")
    # print_t(t_table)
    # print("============")

    t_h = len(t_table)
    t_w = len(t_table[0])
    if t_h > H or t_w > W:
        # はみ出てしまう
        continue
    for start_y in range((H - t_h) + 1):
        for start_x in range((W - t_w) + 1):

            # この場所で一致しているか確認
            is_ok = True
            for relative_y in range(t_h):
                for relative_x in range(t_w):
                    x = start_x + relative_x
                    y = start_y + relative_y
                    # print(f"t_table[{relative_y}][{relative_x}] =? s_table[{y}][{x}]")
                    # print(f"{s_table=}")
                    # print(s_table[y])
                    # print(s_table[y][x])
                    if t_table[relative_y][relative_x] == "#" and s_table[y][x] == "#":
                        # 衝突
                        is_ok = False
                        break
                if not is_ok:
                    # 衝突
                    break

            if is_ok:
                is_found = True
                break
    if is_found:
        break

ans = "Yes" if is_found else "No"
print(ans)
