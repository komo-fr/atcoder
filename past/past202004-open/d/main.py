#!/usr/bin/env python3
import string
import collections

S = input()

chars = "." + string.ascii_lowercase

N = len(S)

if N == 1:
    ans = 2
elif N == 2:
    ans = 6 if S[0] == S[1] else 7
elif N >= 3:
    all_list = []
    count_1 = 1 + len(collections.Counter(S).keys())

    kouho_list = []
    for i, s in enumerate(S):
        t_list = []
        if i == 0:
            s_0 = s
            continue
        t_list.append(s_0 + ".")
        t_list.append("." + s)
        t_list.append(s_0 + s)
        # print(f"{i}: {t_list}")
        s_0 = s
        kouho_list += t_list
    count_2 = 1 + len(set(kouho_list))
    all_list = list(set(kouho_list))
    kouho_list = []
    for i, s in enumerate(S):
        t_list = []
        if i == 0:
            s_0 = s
            continue
        if i == 1:
            s_1 = s
            continue
        t_list.append(s_0 + s_1 + ".")
        t_list.append(s_0 + "." + s)
        t_list.append("." + s_1 + s)

        t_list.append(s_0 + "..")
        t_list.append("." + s_1 + ".")
        t_list.append(".." + s)
        t_list.append(s_0 + s_1 + s)
        # print(f"{i}: {t_list}")
        kouho_list += t_list

        s_0 = s_1
        s_1 = s

    count_3 = 1 + len(set(kouho_list))
    # print(f"{count_1=}")
    # print(f"{count_2=}")
    # print(f"{count_3=}")

    ans = count_1 + count_2 + count_3

    all_list += list(set(kouho_list))
    # for t in all_list:
    #     print(t)

print(ans)
