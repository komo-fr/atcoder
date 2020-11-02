#!/usr/bin/env python3

N = int(input().split()[0])
s_table = []

for _ in range(N):
    s = list(input())
    s_table.append(s)

# print(s_table)
s_table = [list(x) for x in zip(*s_table)]
# print(s_table)
found_flag = False
for s_list in s_table:
    r_s_list = list(reversed(s_list))
    # print(s_list)
    # print(r_s_list)
    if s_list == r_s_list:
        print("".join(s_list))
        found_flag = True
        break

if not found_flag:
    print(-1)
