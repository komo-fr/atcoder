#!/usr/bin/env python3
import copy

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

a_list = sorted(a_list)


def judge(w_list, k):
    w_list = sorted(w_list)

    for i in range(len(w_list) - 1):
        w_list += [abs(w_list[i] - w_list[i + 1])]

    if k in w_list:
        return True, w_list
    w_list = sorted(list(set(w_list)))
    ww_list = set([w + K for w in w_list])
    if ww_list & set(w_list):
        return True, w_list
    else:
        return False, w_list


w_list = a_list

while True:
    org_w_list = copy.copy(w_list)
    is_ok, w_list = judge(w_list, K)
    if is_ok:
        break
    else:
        if abs(w_list[0] - w_list[-1]) < K:
            # 操作によって作れる差分よりKの方が大きいので
            # これ以上操作してもKを作れない
            break
        if w_list == org_w_list:
            # これ以上操作しても変化がない
            break

ans = "POSSIBLE" if is_ok else "IMPOSSIBLE"

print(ans)
