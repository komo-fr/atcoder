#!/usr/bin/env python3
from collections import defaultdict
from re import A
import sys

sys.setrecursionlimit(10 ** 5)
n, x, y = list(map(int, input().split()))
edge_dict = defaultdict(lambda: [])

for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    edge_dict[u].append(v)
    edge_dict[v].append(u)

cur = x
done_dict = defaultdict(lambda: False)
path_list = []
end = False


def search(cur):
    done_dict[cur] = True
    global end
    if cur == y:
        end = True
    for node in edge_dict[cur]:
        if end:
            break
        if done_dict[node]:
            continue
        search(cur=node)
        if end:
            path_list.append(node)
            break


search(cur=cur)
path_list += [x]
print(*reversed(path_list))
