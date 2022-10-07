#!/usr/bin/env python3
import random
from dataclasses import dataclass
from collections import defaultdict, deque


@dataclass
class P:
    x: int
    y: int

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            return self.x <= other.x
        else:
            return False


@dataclass
class L:
    a: P
    b: P

    def __init__(self, ax, ay, bx, by):
        self.a = P(ax, ay)
        self.b = P(bx, by)

    def print(self):
        print(self.a.x, self.a.y, self.b.x, self.b.y)


@dataclass
class A:
    a: int
    d: int

    def __lt__(self, other):
        return self.d < other.d


# 入力
# N=苺の数、K=カット回数
N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    b_list.append(P(x=x, y=y))
a_list_ = []
a_dict = defaultdict(lambda: 0)
for i, a in enumerate(a_list):
    a_list_.append(A(a=a, d=i + 1))
    a_dict[i+1] = a

a_list = sorted(a_list_, reverse=True)

c_list = []
for a in a_list:
    c_list += [a.d] * a.a

b_list = sorted(b_list)

# debug
# b_list = []
# for _ in range(3):
#     b_list.append(P(1, 1))
# for _ in range(3):
#     b_list.append(P(1, 2))
# for _ in range(3):
#     b_list.append(P(1, 4))
# for _ in range(3):
#     b_list.append(P(1, 6))

# yの位置にある最初のイチゴのインデックス
b_y2index_dict = defaultdict(lambda: -1)
for i, b in enumerate(b_list):
    y = b.y
    if b_y2index_dict[y] == -1:
        b_y2index_dict[y] = i
# print(b_list)
# print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

# print(b_y2index_dict)
# print("🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰🍰")

y2n_dict = {}
berry_cumsum = 0
now_index = 0

for i, i_y in enumerate(range(10 ** 4 * (-1), 10 ** 4 * +1)):
    # y上にある苺の最初のインデックス
    if i == 0:
        continue
    elif i == 1:
        n = b_y2index_dict[i_y]
        n = 0 if n == -1 else n
        y2n_dict[i_y - 1] = n
        now_index = 0
        continue
    # 1つ前の直線で得られる苺の数
    j_0 = now_index
    j_1 = b_y2index_dict[i_y]
    if j_1 == -1:
        j_1 = j_0
    additional_n = j_1 - j_0
    y2n_dict[i_y - 1] = y2n_dict[i_y - 2] + additional_n
    now_index = j_1
    # print(i)
    # print(y2n_dict)
    # print("-------------------")
    if i_y >= b_list[-1].y:
        break

# print(y2n_dict)

# l_list = []
# index = 0
# for c in c_list:
#     # イチゴがc個のケーキを切りたい
#     if len(b_list) - 1 < index + c or len(l_list) >= 100:
#         break
#     count = 0
#     # 前回の線と直線がかぶっている場合は飛ばす
#     if len(l_list) != 0:
#         pre_l = l_list[-1]

#     p = b_list[index + c]
#     x0 = 10 ** 4 * (-1)
#     y0 = p.y + 1
#     x1 = 10 ** 4
#     y1 = p.y + 1
#     l = L(x0, y0, x1, y1)
#     l_list.append(l)
#     index += c

# print(len(l_list))
# for l in l_list:
#     l.print()
