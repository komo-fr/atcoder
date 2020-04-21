#!/usr/bin/env python3
import collections
import copy

N = int(input().split()[0])
S = input()

counter = collections.Counter(S)
total = 0
done_list = []

for i, ch in enumerate(S[::-1]):  # 3 * 10 ** 4
    if ch in done_list:
        counter[ch] = counter[ch] - 1
        if counter[ch] < 1:
            del counter[ch]
        continue
    sub_done_list = []
    counter[ch] = counter[ch] - 1
    if counter[ch] < 1:
        del counter[ch]
    sub_counter = copy.copy(counter)

    for ch_2 in S[N - (i + 1) - 1 :: -1]:  # 3 * 10 ** 4
        if ch_2 in sub_done_list:
            sub_counter[ch_2] = sub_counter[ch_2] - 1
            if sub_counter[ch_2] < 1:
                del sub_counter[ch_2]
            continue
        sub_done_list.append(ch_2)
        sub_counter[ch_2] = sub_counter[ch_2] - 1
        if sub_counter[ch_2] < 1:
            del sub_counter[ch_2]
        total += len(sub_counter.keys())

    done_list.append(ch)

ans = total

print(ans)
