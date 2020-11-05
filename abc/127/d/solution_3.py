#!/usr/bin/env python3
import bisect
import numpy as np

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))
bc_list = []

for _ in range(M):
    b, c = list(map(int, input().split()))
    bc_list.append((b, c))

bc_list = sorted(bc_list, key=lambda x: x[1], reverse=True)
now_list = np.array(sorted(a_list))
fix_list = np.array([])
min_a = min(a_list)

for bc in bc_list:
    b, c = bc
    if min_a >= c:
        # もう置き換えても合計値は増えない
        break
    # cより小さい数は何個あるか？
    # 線形探索だとTLEになるので、2分探索で考える
    c_index = bisect.bisect_right(now_list, c)
    target_index = c_index if c_index < b else b

    # c_indexまでをcで置き換えても、順序の入れ替えはない
    now_list[:target_index] = c
    # c_index以前の整数は使用確定なので掃き出す
    fix_list = np.hstack([fix_list, now_list[:target_index]])
    now_list = now_list[target_index:]
    min_a = now_list[0]

fix_list = np.hstack([fix_list, now_list])
ans = fix_list.sum()
ans = int(ans)
print(ans)
