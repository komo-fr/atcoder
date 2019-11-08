#!/usr/bin/env python3

N, C, K = list(map(int, input().split()))
t_list = []

for _ in range(N):
    t = int(input().split()[0])
    t_list.append(t)

waiting_n = 0
dead_line_t = float("inf")
bus_count = 0
t_list = sorted(t_list)

for i, t in enumerate(t_list):
    if waiting_n == 0:
        dead_line_t = t + K

    waiting_n += 1

    if waiting_n >= C:
        # 定員に達したので出発する
        waiting_n = 0
        bus_count += 1
        continue

    if i == len(t_list) - 1:
        # 最後の一人はどのみち乗せるしかない
        bus_count += 1
        break

    if t_list[i + 1] > dead_line_t:
        # 出発しないと怒り出す客がいる
        waiting_n = 0
        bus_count += 1
        continue


ans = bus_count
print(ans)
