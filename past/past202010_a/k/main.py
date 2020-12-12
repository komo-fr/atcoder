#!/usr/bin/env python3
from collections import deque

K = int(input().split()[0])
# a_list = list(map(int, input().split()))

# a_list = []

a_list_list = deque()
a_dict = {}

for i in range(K):
    n = input()
    a_list = list(map(int, input().split()))
    a_dict[i + 1] = a_list

Q = int(input().split()[0])
b_list = list(map(int, input().split()))


count = 0
count_i = 0
count_char = 0
for b in b_list:
    a_list = a_dict[b]
    # print(a_list)

    for j, a in enumerate(a_list):
        # print("hoge")
        if count_char == 0:
            before_0 = a
            count_char += 1
            continue
        # if count_char == 1:
        #     before_1 = a
        #     count_char += 1
        #     continue

        # print(f"{before_0=}, {before_1=}, {a=}")

        if before_0 <= a:
            count += 1

        # before_0 = before_1
        # before_1 = a
        before_0 = a

    count_i += 1

mod = 10 ** 9

ans = count % mod
print(ans)
