#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_set = set(list(map(int, input().split())))
b_set = set(list(map(int, input().split())))

ans = " ".join([str(x) for x in sorted(a_set & b_set)])
print(ans)
