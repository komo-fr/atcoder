#!/usr/bin/env python3
from decimal import Decimal, ROUND_HALF_UP

N = int(input().split()[0])
a_list = list(map(int, input().split()))
max_a = max(a_list)
C = 10**9
ans = [Decimal(str(C * a / max_a)).quantize(0, rounding=ROUND_HALF_UP) for a in a_list]

print(*ans)
