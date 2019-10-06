# https://atcoder.jp/contests/abc094/tasks/arc095_a
# C - Many Medians
import copy

n = int(input().split()[0])
x_list = list(map(int, input().split()))
sorted_x_list = sorted(x_list)
mean_index = int((n + 1)/ 2) - 1
mean_list = []

a = sorted_x_list[mean_index]
b = sorted_x_list[mean_index + 1]
for x in x_list:
    if x <= a:
        mean_list.append(str(b))
    else:
        mean_list.append(str(a))

ans = '\n'.join(mean_list)
print(ans)