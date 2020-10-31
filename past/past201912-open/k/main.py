#!/usr/bin/env python3
from collections import defaultdict
import sys

N = int(input().split()[0])
sys.setrecursionlimit(N + 10)

p_dict = {}
root_id = None
child_dict = defaultdict(lambda: defaultdict(lambda: None))


for i in range(N):  # 150000
    p = int(input())
    child = i + 1
    if p == -1:
        root_id = child
        continue
    if child_dict[p]:
        child_dict[p].append(child)
    else:
        child_dict[p] = [child]

# route = []
appear_dict = {}
count = 0


def walk(node_id: int):
    global count
    count += 1
    # global route
    # route.append(node_id)
    global appear_dict
    appear_dict[node_id] = dict(first=count, end=None)
    for child_node_id in child_dict[node_id]:
        walk(child_node_id)
    count += 1
    # route.append(node_id)
    appear_dict[node_id]["last"] = count


walk(root_id)
Q = int(input().split()[0])

for _ in range(Q):  # 100000
    a, b = list(map(int, input().split()))
    if (
        appear_dict[b]["first"]
        <= appear_dict[a]["first"]
        <= appear_dict[a]["last"]
        <= appear_dict[b]["last"]
    ):
        print("Yes")
    else:
        print("No")