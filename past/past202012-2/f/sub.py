#!/usr/bin/env python3
from collections import defaultdict, Counter

N, M = list(map(int, input().split()))
abc_list = []
abc_set_list = []

for _ in range(M):
    a, b, c = list(map(int, input().split()))
    abc = list(sorted([a, b, c]))
    abc_set_list.append((a, b, c))

# abc_set_list = set(abc_set_list)

for abc in abc_set_list:
    a, b, c = abc
    abc_list.append((a, b))
    abc_list.append((b, c))
    abc_list.append((a, c))

counter = Counter(abc_list)
ng_list = []
count = 0

for maze_set in counter.most_common():
    # print(f"{abc_list=}")
    # print(f"{maze_set=}")
    if maze_set[0][0] in ng_list or maze_set[0][1] in ng_list:
        # この組み合わせはもう使えない
        # print("continue")
        continue
    next_list = []
    for abc in abc_set_list:
        # print(f"{abc=}")
        # print(f"{maze_set[0][0]}, {maze_set[0][1]}")
        if maze_set[0][0] in abc and maze_set[0][1] in abc:
            # 爆発寸前
            count += 1
            for x in abc:
                if maze_set[0] != x and maze_set[1] != x:
                    ng_list.append(x)
        else:
            # 爆発寸前ではない
            next_list.append(abc)

    # done_list.append(maze_set[0])
    # done_list.append(maze_set[1])
    abc_set_list = next_list
ans = count
print(ans)
