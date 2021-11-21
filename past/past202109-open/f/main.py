#!/usr/bin/env python3
from collections import deque

N = int(input().split()[0])
S = input()
x_list = []
zero_count = S.count("0")
if zero_count == 1:
    ans = -1
elif zero_count == 0:
    ans = " ".join([str(i + 1) for i in range(N)])
else:
    # 使える数字を集める
    c_list = []
    for i, char in enumerate(S):
        if char == "0":
            c_list.append(i + 1)
    ans_list = []
    c_list = [c_list[-1]] + c_list[:-1]
    index = 0
    for i, char in enumerate(S):
        if char == "1":
            ans_list.append(str(i + 1))
        else:
            num = c_list[index]
            ans_list.append(str(num))
            index += 1
    ans = " ".join(ans_list)
print(ans)
