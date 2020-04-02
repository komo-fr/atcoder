#!/usr/bin/env python3

X, Y, A, B, C = list(map(int, input().split()))
p_list = list(map(int, input().split()))  # 10 ** 5
q_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

p_list = sorted(p_list, reverse=True)
q_list = sorted(q_list, reverse=True)
r_list = sorted(r_list, reverse=True)

total = 0
for _ in range(X):
    if r_list and p_list:
        r = r_list[0]
        p = p_list[0]

        if p >= r:
            total += p_list.pop(0)
        else:
            total += r_list.pop(0)
    elif r_list:
        total += r_list.pop()
    elif p_list:
        total += p_list.pop()
    else:
        break

for _ in range(Y):
    if r_list and q_list:
        r = r_list[0]
        q = q_list[0]

        if q >= r:
            total += q_list.pop(0)
        else:
            total += r_list.pop(0)
    elif r_list:
        total += r_list.pop(0)
    elif q_list:
        total += q_list.pop(0)
    else:
        break
ans = total
print(ans)
