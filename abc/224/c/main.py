#!/usr/bin/env python3

N = int(input().split()[0])
xy_list = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    xy_list.append((x, y))

count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            area = (xy_list[j][0] - xy_list[i][0]) * (xy_list[k][1] - xy_list[i][1]) - (
                xy_list[k][0] - xy_list[i][0]
            ) * (xy_list[j][1] - xy_list[i][1])
            if area != 0:
                count += 1

ans = count
print(ans)
