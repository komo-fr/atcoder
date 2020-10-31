#!/usr/bin/env python3
import collections

S = input()
counter = collections.Counter(S)
ans = counter.most_common()[0][0]
print(ans)
