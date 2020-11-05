# https://atcoder.jp/contests/abc080/tasks/abc080_c
# C - Shopping Street
import itertools
N = int(input().split()[0])
f_list_list = []

for _ in range(N):
    f_list_list.append(list(map(int, input().split())))

p_list_list = []

for _ in range(N):
    p_list_list.append(list(map(int, input().split())))

p_gen = itertools.product([0, 1], repeat=10)
max_p = -float('inf')

for pattern in p_gen:  # 1024
    if sum(pattern) == 0:
        continue
    counter = {k: 0 for k in range(N)}
    for t_i, is_open in enumerate(pattern):  # 10
        if is_open == 0:
            continue
        for n_i in range(N):  # 100
            if f_list_list[n_i][t_i] == 1:
                counter[n_i] += 1
    total_p = 0
    for k, c in counter.items():  # 100
        total_p += p_list_list[k][c]
    max_p = max(total_p, max_p)

print(max_p)
