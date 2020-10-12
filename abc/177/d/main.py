#!/usr/bin/env python3
import collections

N, M = list(map(int, input().split()))


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            # 自分自身だったらそのまま返す
            return i
        else:
            # 自分の祖先を、自分の祖先の祖先で更新する
            # こうすることで、途中を飛ばすことができる
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        self.parent[j] = i


union = UnionFind(N)

for _ in range(M):
    s, t = list(map(int, input().split()))
    union.union(s - 1, t - 1)

group = [union.find(i) for i in range(N)]
counter = collections.Counter(group)
ans = counter.most_common()[0][1]

print(ans)
