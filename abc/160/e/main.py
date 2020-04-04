#!/usr/bin/env python3

X, Y, A, B, C = list(map(int, input().split()))
p_list = list(map(int, input().split()))  # 10 ** 5
q_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

p_list = list(sorted(p_list, reverse=True))
q_list = list(sorted(q_list, reverse=True))
# r_list = sorted(r_list, reverse=True)

p_list = p_list[:X]
q_list = q_list[:Y]

all_list = p_list + q_list + r_list
all_list = list(sorted(all_list, reverse=True))
total = sum(all_list[: X + Y])


ans = total
print(ans)
