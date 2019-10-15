#!/usr/bin/env python3
import collections

N = int(input().split()[0])
a_list = list(map(int, input().split()))

counter = collections.Counter(a_list)

# 4種類以上だと、どうしようもない
is_ok = True
if len(counter) > 4:
    is_ok = False
elif len(counter) == 3:
    v_list = list(counter.values())
    if len(set(v_list)) != 1:
        # 全部同じ数ではない
        is_ok = False

    if is_ok:
        k_list = list(counter.keys())
        if k_list[0] ^ k_list[1] != k_list[2]:
            is_ok = False
elif len(counter) == 2:
    v_list = list(counter.values())
    if min(v_list) * 2 == max(v_list):
        a = [k for k, v in counter.items() if v == max(v_list)][0]
        b = [k for k, v in counter.items() if v == min(v_list)][0]
        if a ^ a != b:
            is_ok = False
    else:
        is_ok = False
else:
    for k in counter.keys():
        if k != 0:
            is_ok = False
            break

ans = "Yes" if is_ok else "No"

print(ans)
