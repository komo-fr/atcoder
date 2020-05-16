#!/usr/bin/env python3

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

# 何回で1ループするか
i = 0
done_dict = {i: -1 for i in range(N)}

route_list = []
route_len = 0
step = 1
while True:
    route_len += 1
    done_dict[i] = step
    route_list.append(i)
    next_i = a_list[i] - 1

    if done_dict[next_i] != -1:
        loop_end_i = i
        loop_start_i = next_i
        # print("loop_end_i: " + str(loop_end_i))
        # print("loop_start_i: " + str(loop_start_i))

        first_route_step = step
        # ループのステップ数
        # print("{} -> {}".format(done_dict[loop_start_i], done_dict[loop_end_i]))
        loop_len = done_dict[loop_end_i] - done_dict[loop_start_i] + 1
        # print("loop_len:" + str(loop_len))
        # print(route_list)
        break
    step += 1
    i = next_i

if K < first_route_step:
    ans = route_list[K] + 1
else:
    k = K - first_route_step
    k = k % loop_len
    ans = route_list[done_dict[loop_start_i] - 1 + k] + 1


print(ans)
