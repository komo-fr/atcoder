#!/usr/bin/env python3
import collections
R, C, K = list(map(int, input().split()))
N = int(input().split()[0])
rc_list = []
for _ in range(N):
    r, c = list(map(int, input().split()))
    rc_list.append((r, c))

r_n_list = [0 for _ in range(R)]
c_n_list = [0 for _ in range(C)]

# 各行、各列の飴の合計
for rc in rc_list:
    r, c = rc
    r_n_list[r-1] += 1
    c_n_list[c-1] += 1

r_n_counter = collections.Counter(r_n_list)
c_n_counter = collections.Counter(c_n_list)

comb_n = 0
for a in range(K + 1):
    r_n = r_n_counter[a]
    c_n = c_n_counter[K-a]

    comb_n += c_n * r_n

for rc in rc_list:
    r, c = rc
    if r_n_list[r-1] + c_n_list[c-1] == K:
        # 重複しているので、引く
        comb_n -= 1
    if r_n_list[r-1] + c_n_list[c-1] == K + 1:
        # 数え漏れているので、足す
        comb_n += 1

print(comb_n)
