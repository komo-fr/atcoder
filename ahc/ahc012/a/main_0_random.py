#!/usr/bin/env python3
import random
from collections import namedtuple
from dataclasses import dataclass


@dataclass
class P:
    x: int
    y: int


@dataclass
class L:
    a: P
    b: P

    def __init__(self, ax, ay, bx, by):
        self.a = P(ax, ay)
        self.b = P(bx, by)

    def print(self):
        print(self.a.x, self.a.y, self.b.x, self.b.y)


# N=苺の数、K=カット回数
N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_table = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    b_table.append(P(x=x, y=y))

# ベースライン: ランダムに出力する
random.seed(0)
l_list = []
for _ in range(K):
    x0 = random.randint(10 ** 4 * (-1), 10 ** 4)
    y0 = random.randint(10 ** 4 * (-1), 10 ** 4)
    x1 = random.randint(10 ** 4 * (-1), 10 ** 4)
    y1 = random.randint(10 ** 4 * (-1), 10 ** 4)
    l = L(x0, y0, x1, y1)
    l_list.append(l)

# print(ans)
print(len(l_list))
for l in l_list:
    l.print()
