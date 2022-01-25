#!/usr/bin/env python3

N = int(input().split()[0])

k = len(str(N))
c = 0
if k % 2 == 0 and k != 2:
    # 偶数桁
    k_1 = k - 2
    a, b = int(str(N)[:k//2]), int(str(N)[k//2:])

    for i in range(1, a+1):
        x = i * 10 ** (k // 2) + i
        if x <= N:
            c += 1
elif k == 2:
    a, b = str(N)
    c = min([a, b])
elif k == 1:
    # 奇数桁
    c = 0
else:
    # 奇数桁
    k_1 = (k - 1) // 2
    c = int("9" * k_1)

ans = c
print(ans)
