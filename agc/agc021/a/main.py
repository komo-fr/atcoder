#!/usr/bin/env python3

N = int(input().split()[0])
n_list = [int(char) for char in str(N)]

if N % 10 == 0:
    ans = 9 * len(n_list[1:])
else:
    total_1 = sum(n_list)
    n_list_2 = n_list[:]
    target_idx = -1
    for i, n in enumerate(n_list):
        if n == 9:
            continue
        else:
            if n != 0:
                target_idx = i
            break
    if target_idx != -1:
        if target_idx == 0:
            n_list_2[0] = n_list[0] - 1
            if len(n_list) > 2:
                n_list_2[1:] = [9] * len(n_list_2[1:])
        else:
            n_list_2[target_idx - 1] = n_list[target_idx - 1] - 1
            n_list_2[target_idx:] = [9] * len(n_list_2[target_idx:])
    total_2 = sum(n_list_2)
    ans = max(total_2, total_1)

print(ans)
