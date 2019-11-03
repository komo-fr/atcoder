#!/usr/bin/env python3

S = input()
s_list = list(S)
w_list = [0]
min_n = 0
s_l = len(s_list)
totsu_list = [False]

if s_list[0] == "<":
    ou_list = [True]
else:
    ou_list = [False]

t_list = []
if ou_list[0]:
    t_list = ["ou"]
else:
    t_list = ["totsu"]

for i, char in enumerate(s_list):
    # 凹であるかどうか
    is_ou = False
    is_totsu = False
    if i == s_l - 1:
        if char == ">":
            is_ou = True
    else:
        if s_list[i] == "<" and s_list[i + 1] == ">":
            is_totsu = True
        elif s_list[i] == ">" and s_list[i + 1] == "<":
            is_ou = True

    ou_list.append(is_ou)
    totsu_list.append(is_totsu)
    if is_ou:
        t = "ou"
    elif is_totsu:
        t = "totsu"
    elif char == "<":
        t = "up"
    else:
        t = "down"
    t_list.append(t)

    if char == "<":
        w_list.append(w_list[i] + 1)
    else:
        w_list.append(w_list[i] - 1)
        min_n = min(w_list[i] - 1, min_n)

x_list = []
d = abs(min_n)
w_len = len(w_list)
for i, w in enumerate(w_list):
    t = t_list[i]
    if t == "ou":
        x = 0
    elif t == "up" or i == w_len - 1:
        x = x_list[i - 1] + 1
    else:
        x = w_list[i] + d
    x_list.append(x)

x_len = len(x_list)
y_list = x_list[:]

total = 0

for i in range(x_len):
    idx = x_len - (i + 1)
    t = t_list[idx]
    if t == "down":
        y_list[idx] = y_list[idx + 1] + 1
    elif t == "ou" or t == "down":
        pass
    elif t == "totsu":
        if idx == 0 or idx == x_len:
            pass
        else:
            a = y_list[idx - 1]
            b = y_list[idx + 1]
            y_list[idx] = max(a, b) + 1
    total += y_list[idx]

if len(y_list) >= 3:
    if t_list[0] == "totsu":
        total -= y_list[0]
        total += y_list[1] + 1
    if t_list[-1] == "totsu":
        total -= y_list[-1]
        total += y_list[-2] + 1

# ans = sum(z_list)
ans = total
print(ans)
