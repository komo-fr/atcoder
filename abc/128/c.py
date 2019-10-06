# https://atcoder.jp/contests/abc128/tasks/abc128_c
# C - Switches
from itertools import product

n, m = list(map(int, input().split()))
k_list = []
s_list_list = []

for _ in range(m):
    k, *s = list(map(int, input().split()))
    k_list.append(k)
    s_list_list.append(s)

p_list = list(map(int, input().split()))

# スイッチの点灯の組み合わせは最大で100
s_p_list = product([0, 1], repeat=n)
c = 0
match_list = []
for s_p in s_p_list:

    is_match = True
    for i, s_list in enumerate(s_list_list):
        w = sum([s_p[s-1] for s in s_list])
        if w % 2 != p_list[i]:
            is_match = False
            break
    if is_match:
        c += 1
        match_list.append(s_p)

print(c)
