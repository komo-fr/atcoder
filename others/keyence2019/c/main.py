#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

if sum(a_list) < sum(b_list):
    count = -1
else:
    need_c_list = [b - a for a, b in zip(a_list, b_list) if a < b]
    need_c = sum(need_c_list)
    count = len(need_c_list)
    over_c_list = sorted([a - b for a, b in zip(a_list, b_list) if a > b], reverse=True)

    if need_c > 0:
        for over in over_c_list:
            need_c -= over
            count += 1
            if need_c <= 0:
                break

ans = count
print(ans)
