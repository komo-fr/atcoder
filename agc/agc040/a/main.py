#!/usr/bin/env python3

S = input()
s_list = list(S)
s_l = len(s_list)
N = s_l + 1
t_list = ["ou"] if s_list[0] == "<" else ["totsu"]

# 1回目のループ: 凹凸↗︎↘︎を判定する
for i, char in enumerate(s_list):
    # 凹であるかどうか
    is_ou = False
    is_totsu = False
    if i == s_l - 1:
        if char == ">":
            is_ou = True
        else:
            is_totsu = True
    else:
        if s_list[i] == "<" and s_list[i + 1] == ">":
            is_totsu = True
        elif s_list[i] == ">" and s_list[i + 1] == "<":
            is_ou = True

    if is_ou:
        t = "ou"
    elif is_totsu:
        t = "totsu"
    elif char == "<":
        t = "up"
    else:
        t = "down"
    t_list.append(t)

# 2回目のループ: 凹と↗︎部分の値を確定させる
x_list = []
for i, t in enumerate(t_list):
    if t == "ou":
        x = 0
    elif t == "up" or i == N - 1:
        x = x_list[i - 1] + 1
    else:
        x = None
    x_list.append(x)

# 3回目のループ: 末尾から見ていって、凸と↘︎部分を確定させる
total = 0

for i in range(N):
    idx = N - (i + 1)
    t = t_list[idx]
    if t == "down":
        x_list[idx] = x_list[idx + 1] + 1
    elif t == "ou" or t == "down":
        pass
    elif t == "totsu":
        if idx == 0:
            x_list[0] = x_list[1] + 1
        elif idx == N - 1:
            x_list[idx] = x_list[idx - 1] + 1
        else:
            a = x_list[idx - 1]
            b = x_list[idx + 1]
            x_list[idx] = max(a, b) + 1
    total += x_list[idx]

ans = total
print(ans)
