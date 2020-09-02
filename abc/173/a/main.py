#!/usr/bin/env python3

N = int(input().split()[0])
ans = int(str(10000 - N)[-min(3, len(str(10000 - N))) :])
print(ans)
