#!/usr/bin/env python3
from scipy.special import comb

L = int(input().split()[0])
a = comb(L - 1, 11, exact=True)
ans = a
print(ans)
