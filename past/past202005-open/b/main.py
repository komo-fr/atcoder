#!/usr/bin/env python3
from collections import defaultdict

N, M, Q = list(map(int, input().split()))

counter = defaultdict(int)
done_dict = defaultdict(lambda: [])
score_dict = defaultdict(int)

for _ in range(Q):
    s = list(map(int, input().split()))
    if len(s) == 2:
        _, n = s
        score = sum([score_dict[m] for m in done_dict[n]])
        print(score)

    else:
        _, n, m = s
        counter[m] += 1
        score_dict[m] = N - counter[m]
        done_dict[n].append(m)

