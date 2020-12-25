#!/usr/bin/env python3

a_list = list(map(int, input().split()))
a_list = list(sorted(a_list))

if set(a_list) == 1:
    ans = 0
elif a_list[1] == a_list[2]:
    d = a_list[2] - a_list[0]
    if d % 2 == 0:
        ans = d // 2
    else:
        ans = (d // 2) + 2
else:
    count = 0
    d_0 = a_list[2] - a_list[0]
    d_1 = a_list[2] - a_list[1]
    d = d_0 - d_1
    count += d_1
    if d % 2 == 0:
        count += d // 2
    else:
        count += (d // 2) + 2
    ans = count
print(ans)
