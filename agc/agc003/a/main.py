#!/usr/bin/env python3
import collections

S = input()
c = collections.Counter(S)
ans = "No"

if (c["N"] > 0 and c["S"] > 0) or (c["N"] == 0 and c["S"] == 0):
    if (c["W"] > 0 and c["E"] > 0) or (c["W"] == 0 and c["E"] == 0):
        ans = "Yes"

print(ans)
