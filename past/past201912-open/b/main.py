#!/usr/bin/env python3

N = int(input().split()[0])
a_list = []
ans_txt = ""
for i in range(N):
    a = int(input().split()[0])
    a_list.append(a)
    if i == 0:
        continue
    if a == a_list[i - 1]:
        ans_txt += "stay\n"
    elif a > a_list[i - 1]:
        ans_txt += "up {}\n".format(a - a_list[i - 1])
    else:
        ans_txt += "down {}\n".format(a_list[i - 1] - a)
ans = ans_txt
print(ans)
