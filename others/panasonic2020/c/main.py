#!/usr/bin/env python3
from decimal import Decimal

a, b, c = list(map(int, input().split()))

# ans = "Yes" if (math.sqrt(a) + math.sqrt(b)) < math.sqrt(c) else "No"
root = Decimal("0.5")
ans = "Yes" if ((a ** root) + (b ** root)) < (c ** root) else "No"


print(ans)
