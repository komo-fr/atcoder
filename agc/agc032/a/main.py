#!/usr/bin/env python3

N = int(input().split()[0])
b_list = list(map(int, input().split()))
w_list = b_list[:]

# 引いていく方法で考える
is_ok = True
ans_list = []

# 深さ優先探索か？
# 候補が複数ある場合が考えられる
while w_list:
    kouho_list = [i for i, w in enumerate(w_list) if w == i + 1]
    if kouho_list:
        del_i = kouho_list[0]
        ans_list.append(w_list[del_i])
        del w_list[del_i]
    else:
        is_ok = False
        break

if is_ok:
    ans_list = reversed(ans_list)
    ans = "\n".join(ans_list)
else:
    ans = -1
print(ans)
