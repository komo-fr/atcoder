#!/usr/bin/env python3
import string

S = input()
all_s_list = list(string.ascii_lowercase)
remain_s_list = [x for x in all_s_list if x not in S]

s_dict = {c: i + 1 for i, c in enumerate(all_s_list)}

if remain_s_list:
    ans = S + remain_s_list[0]
else:
    last_s = "".join(reversed(all_s_list))
    if S == last_s:
        ans = -1
    else:
        tail_list = []
        for i in range(1, len(all_s_list) + 1):
            char = S[-i]
            w_list = [x for x in tail_list if s_dict[char] < s_dict[x]]
            w_list = sorted(w_list)
            if w_list:
                if i != len(all_s_list):
                    ans = S[:-i] + w_list[0]
                else:
                    ans = w_list[0]
                break
            tail_list.append(char)

print(ans)
