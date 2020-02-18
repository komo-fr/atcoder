#!/usr/bin/env python3
import collections

S = input()
a = S[0] == "A"
b = collections.Counter(S[2:-1])["C"] == 1
c = S.replace("A", "").replace("C", "").islower()

ans = "AC" if a and b and c else "WA"

print(ans)
