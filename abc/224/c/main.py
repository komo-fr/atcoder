#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
xy_list = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    xy_list.append((x, y))

count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x_list = [xy_list[i][0], xy_list[j][0], xy_list[k][0]]
            y_list = [xy_list[i][1], xy_list[j][1], xy_list[k][1]]
            if len(set(x_list)) == 1 or len(set(y_list)) == 1:
                continue
            elif len(set(x_list)) == 2 or len(set(y_list)) == 2:
                count += 1
                continue
            abc_list = sorted([xy_list[i], xy_list[j], xy_list[k]])

            ab = (abc_list[1][0] - abc_list[0][0]) / (abc_list[1][1] - abc_list[0][1])
            bc = (abc_list[2][0] - abc_list[1][0]) / (abc_list[2][1] - abc_list[1][1])
            if ab != bc:
                count += 1


ans = count
print(ans)
