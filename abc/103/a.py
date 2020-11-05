# https://atcoder.jp/contests/abc103/tasks/abc103_a
# A - Task Scheduling Problem

a_list = list(map(int, input().split()))

sorted_list = sorted(a_list, reverse=True)
x_list = []

for i, a1 in enumerate(sorted_list[:-1]):
    a2 = sorted_list[i+1]
    x = abs(a1-a2)
    x_list.append(x)

ans = sum(x_list)
print(ans)

