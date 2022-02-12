#!/usr/bin/env python3

N, X = list(map(int, input().split()))
a_table = []
l_list = []
for _ in range(N):
    l, *a_list = list(map(int, input().split()))
    a_table.append(a_list)
    l_list.append(l)


def select(i, pre_x, count):
    if i > N - 1:
        return count
    for j in range(l_list[i]):
        now_x = pre_x * a_table[i][j]
        if i == N - 1:
            if now_x == X:
                count += 1
        count = select(i + 1, now_x, count)
    return count


count = 0
for a in a_table[0]:
    count = select(1, a, count)

ans = count
print(ans)
