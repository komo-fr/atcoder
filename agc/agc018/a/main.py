#!/usr/bin/env python3
import copy

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

a_list = sorted(a_list)


def judge(w_list, k):
    w_list = sorted(w_list)

    for i in range(len(w_list) - 1):
        w_list += [abs(w_list[i] - w_list[i + 1])]

    w_list = sorted(list(set(w_list)))

    if k in w_list:
        return True, w_list
    elif 1 in w_list:
        return True, w_list
    elif abs(w_list[0] - w_list[-1]) < K:
        return False, w_list
    elif k % 2 == 0 and 2 in w_list:
        return True, w_list
    else:
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
            break
        if w_list == org_w_list:
            break

ans = "POSSIBLE" if is_ok else "IMPOSSIBLE"

print(ans)
