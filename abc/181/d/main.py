#!/usr/bin/env python3
import collections

S = input()
is_found = False
if S == "8":
    ans = "Yes"
elif len(S) == 2:
    s_counter = collections.Counter(S)
    counter_list = [collections.Counter(str(i * 8)) for i in range(2, 13)]

    for c in counter_list:
        is_ok = True
        for k, v in c.items():
            if s_counter[k] < v:
                is_ok = False
                # print(f"No: {c}")
                break

        if is_ok:
            is_found = True
            # print(f"Yes: {c}")
            break
    ans = "Yes" if is_found else "No"
else:
    s_counter = collections.Counter(S)
    counter_list = [collections.Counter(str(i * 8)) for i in range(13, 125)]

    for c in counter_list:
        is_ok = True
        for k, v in c.items():
            if s_counter[k] < v:
                is_ok = False
                # print(f"No: {c}")
                break

        if is_ok:
            is_found = True
            # print(f"Yes: {c}")
            break
    ans = "Yes" if is_found else "No"
print(ans)
