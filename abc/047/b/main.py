#!/usr/bin/env python3
W, H, N = list(map(int, input().split()))
min_x, min_y = 0, 0
max_x, max_y = W, H

for _ in range(N):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        min_x = max([x, min_x])
    elif a == 2:
        max_x = min([x, max_x])
    elif a == 3:
        min_y = max([y, min_y])
    else:
        max_y = min([y, max_y])

if max_x <= 0 or min_x >= W or max_y <= 0 or min_y >= H:
    ans = 0
else:
    ans = max([(max_x - min_x) * (max_y - min_y), 0])
print(ans)
