#!/usr/bin/env python3
import collections

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
            # これがないとrandom_11.txtとrandom_12.txtでREになる
            i, j = min(i, j), max(i, j)

            # 別の家族だったら養子に迎える
            self.parents[j] = i


uf = UnionFind(N)

for _ in range(M):
    s, t = list(map(int, input().split()))
    uf.union(s - 1, t - 1)

group = [uf.find(i) for i in range(N)]
counter = collections.Counter(group)
ans = counter.most_common()[0][1]

print(ans)
