#!/usr/bin/env python3

N = int(input().split()[0])
p_list = list(map(int, input().split()))
count = 0
for i in range(N):
    index = i + 1
    if index == p_list[i]:
        if i != 0 and i != N - 1:
            if p_list[i + 1] == index + 1:
                p_list[i] = p_list[i + 1]
                p_list[i + 1] = index
            else:
                p_list[i] = p_list[i - 1]
                p_list[i - 1] = index
        elif i != 0:
            p_list[i] = p_list[i - 1]
            p_list[i - 1] = index
        elif i != N - 1:
            p_list[i] = p_list[i + 1]
            p_list[i + 1] = index

        count += 1

ans = count
print(ans)
