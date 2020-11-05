#!/usr/bin/env python3
import collections

N, K, Q = list(map(int, input().split()))
a_list = []

ls
for _ in range(Q):
    a = int(input().split()[0])
    a_list.append(a)

p_list = [K] * N
a_counter = collections.Counter(a_list)
result_list = []

count_dict = {i + 1: 0 for i in range(N)}
count_dict.update(dict(a_counter))

for winner in range(1, N + 1):
    # 負けた回数
    win_count = count_dict[winner]
    l_count = Q - win_count
    result = "Yes" if l_count < K else "No"
    result_list.append(result)

ans = "\n".join(result_list)
print(ans)
