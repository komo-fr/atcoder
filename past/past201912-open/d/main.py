#!/usr/bin/env python3
import collections
import itertools

N = int(input().split()[0])
a_list = []

counter = collections.defaultdict(int)
dup_counter = collections.defaultdict(int)
for _ in range(N):
    a = int(input().split()[0])
    counter[a] += 1
    a_list.append(a)

no_set = set(set(range(1, N + 1)) - set(a_list))
ans_txt = ""
if no_set:
    dup_list = list(
        itertools.chain.from_iterable([[k] * v for k, v in counter.items() if v > 1])
    )

    for i, x in enumerate(no_set):
        y = dup_list[i]
        ans_txt += "{} {}\n".format(y, x)
else:
    ans_txt = "Correct"
ans = ans_txt
print(ans)
