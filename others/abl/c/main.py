#!/usr/bin/env python3
from collections import defaultdict

N, M = list(map(int, input().split()))


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


uf = UnionFind(N)

for _ in range(M):
    a, b = list(map(int, input().split()))
    uf.union(a - 1, b - 1)

ans = len(set([uf.find(i - 1) for i in range(N)])) - 1
print(ans)
