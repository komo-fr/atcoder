#!/usr/bin/env python3

N, M = list(map(int, input().split()))
edge_list = []C - 友達の友達
friend_dict = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = list(map(int, input().split()))
    friend_dict[a].append(b)
    friend_dict[b].append(a)

ff_n_list = []

for i in range(1, N + 1):
    friend_list = friend_dict[i]
    ff_list = []
    for f in friend_list:
        ff_list += friend_dict[f]
    ff = set(ff_list) - set(friend_dict[i]) - set([i])
    ff_n_list.append(str(len(list(ff))))

ans = "\n".join(ff_n_list)

print(ans)
