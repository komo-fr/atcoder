#!/usr/bin/env python3

N = int(input().split()[0])

keta = len(str(N))

if keta <= 3:
    count = 0
else:
    count = 0
    for k in range(4, keta + 1):
        d = 10 ** (k - 1) - 1
        if k == keta:
            count += (N - d) * ((k - 1) // 3)
        else:
            count += ((10 ** k - 1) - d) * ((k - 1) // 3)
        # print(f"{count=}")

ans = count
print(ans)
