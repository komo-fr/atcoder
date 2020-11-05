# https://atcoder.jp/contests/abc123/tasks/abc123_b
# B - Five Dishes

time_list = []

for _ in range(5):
    time_list.append(int(input().split()[0]))

# 10の倍数からの差が一番大きいやつを最後に頼んだ方が良い
ichi_list = [int(str(x)[-1]) for x in time_list]
sabun_list = [10 - int(str(x)[-1]) if int(str(x)[-1]) != 0 else 0 for x in time_list]

# print(ichi_list)
# print(sabun_list)

last_order_time = max(sabun_list)
last_order_time_index = sabun_list.index(last_order_time)

total = 0
i = last_order_time_index 
total = sum(time_list[:i] + time_list[i+1:])
total += sum(sabun_list[:i] + sabun_list[i+1:])
total += time_list[i]
print(total)