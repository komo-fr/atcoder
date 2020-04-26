#!/usr/bin/env python3
import collections

N = int(input().split()[0])
a_list = list(map(int, input().split()))
c = collections.Counter(a_list)
ans = ""
for i in range(N):
    ans += str(c[i + 1]) + "\n"
print(ans)
