#!/usr/bin/env python3
import itertools

x, y = list(map(int, input().split()))
m_table = []
for _ in range(3):
    m_list = list(input())
    m_table.append(m_list)

done_dict = {(i, j): False for i, j in itertools.product(range(9), range(9))}
count = 0


def go(i, j):
    if not ((0 <= i < 9) and (0 <= j < 9)):
        return
    if done_dict[(i, j)]:
        # 巡回済
        return
    done_dict[(i, j)] = True
    # print((i, j))
    global count
    count += 1
    # 上段
    if m_table[0][0] == "#":
        # print("左上")
        # 左上
        go(i - 1, j - 1)
    if m_table[0][1] == "#":
        # 上
        # print("上")
        go(i - 1, j)
    if m_table[0][2] == "#":
        # 右上
        # print("右上")
        go(i - 1, j + 1)
    # 中段
    if m_table[1][0] == "#":
        # 左
        # print("左")
        go(i, j - 1)
    if m_table[1][2] == "#":
        # 右
        # print("右")
        go(i, j + 1)
    # 下段
    if m_table[2][0] == "#":
        # 左下
        # print("左下")
        go(i + 1, j - 1)
    if m_table[2][1] == "#":
        # 下
        # print("下")
        go(i + 1, j)
    if m_table[2][2] == "#":
        # 右下
        # print("右下")
        go(i + 1, j + 1)


go(x - 1, y - 1)


# def print_table(table):
#     print((len(table), len(table[0])))
#     for line in table:
#         print(line)

# m_table = []
# for i in range(9):
#     m_list = []
#     for j in range(9):
#         m_list.append("#" if done_dict[(i, j)] else ".")
#     m_table.append(m_list)

# print_table(m_table)
ans = count
print(ans)
