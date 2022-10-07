#!/usr/bin/env python3
import random
from dataclasses import dataclass


@dataclass
class P:
    x: int
    y: int

    def __lt__(self, other):
        if self.y > other.y:
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
for i, a in enumerate(a_list):
    a_list_.append(A(a=a, d=i + 1))

a_list = sorted(a_list_, reverse=True)

c_list = []
for a in a_list:
    c_list += [a.d] * a.a

b_list = sorted(b_list)

# 単純な方法: 上から切っていく  19397021
# 同一線上にイチゴが複数並んでいる場合、数がずれる可能性がある
# 直線上のイチゴのことは考慮していない

l_list = []
index = 0
for c in c_list:
    if len(b_list) - 1 < index + c or len(l_list) >= 100:
        break
    p = b_list[index + c]
    x0 = 10 ** 4 * (-1)
    y0 = p.y + 1
    x1 = 10 ** 4
    y1 = p.y + 1
    l = L(x0, y0, x1, y1)
    l_list.append(l)
    index += c

print(len(l_list))
for l in l_list:
    l.print()
