#!/usr/bin/env python3
from decimal import Decimal

N = int(input().split()[0])

s_list = []


class S:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        # self < other
        if int(self.x) != int(other.x):
            return int(self.x) <= int(other.x)
        else:
            # return self.x <= other.x
            return len(self.x) >= len(other.x)


for _ in range(N):
    s = input()
    s = S(s)
    s_list.append(s)

for s in sorted(s_list):
    print(s.x)
