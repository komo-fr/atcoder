#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# 後ろからみていく
# ・dp_list[i] = dp_list[i-1] + a
# ・dp_list[i] = dp_list[i-2] + b
# のうち、小さい方を採用する
dp_list = []

for i in range(N):
    if i == 0:
        dp_list.append(0)
    elif i == 1:
        dp_list.append(dp_list[i - 1] + a_list[i - 1])
    else:
        a = dp_list[i - 1] + a_list[i - 1]
        b = dp_list[i - 2] + b_list[i - 2]
        dp_list.append(min([a, b]))

# 後ろから見ていく
route_list = [N]
next_index = N - 1
while next_index > 0:
    index = next_index
    if index == 1:
        route_list.append(1)
        break
    else:
        a = dp_list[index - 1] + a_list[index - 1]
        b = dp_list[index - 2] + b_list[index - 2]
        if a < b:
            next_index = index - 1
            route_list.append(next_index + 1)
        else:
            next_index = index - 2
            route_list.append(next_index + 1)


ans = " ".join([str(i) for i in reversed(route_list)])
print(len(route_list))
print(ans)
