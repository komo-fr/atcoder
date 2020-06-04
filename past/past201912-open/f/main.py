#!/usr/bin/env python3
import string

S = input()
is_end = False
sub_s = ""
sub_list = []
for i, char in enumerate(S):
    sub_s += char
    if i == 0:
        continue

    if char in string.ascii_uppercase:
        if is_end:
            is_end = False
        else:
            is_end = True
            sub_list.append(sub_s.lower())
            sub_s = ""

# ans = "".join([k for k, v in sorted(sub_dict.items(), key=lambda x: x[1])])
sub_list = sorted(sub_list)
sub_list = [s.title()[:-1] + s[-1].upper() for s in sub_list]
ans = "".join(sub_list)
print(ans)
