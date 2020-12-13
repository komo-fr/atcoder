#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
p_tuple = tuple(map(int, input().split()))
q_tuple = tuple(map(int, input().split()))

l = range(1, N + 1)
patterns = list(itertools.permutations(l))
patterns = list(sorted(patterns))

a = patterns.index(p_tuple)
b = patterns.index(q_tuple)

ans = abs(a - b)
print(ans)
