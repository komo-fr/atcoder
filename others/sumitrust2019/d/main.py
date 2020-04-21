#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
S = input()

index_list = [i for i in range(N)]
p_list = []

for pattern in itertools.combinations(index_list, 3):
    a, b, c = list(sorted(list(pattern)))

    s = S[a] + S[b] + S[c]
    p_list.append(s)

ans = len(set(p_list))

print(ans)
