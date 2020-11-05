# https://atcoder.jp/contests/abc063/tasks/arc075_a
# C - Bugged

n = int(input().split()[0])
s_list = []

for _ in range(n):
    s_list.append(int(input().split()[0]))

total = sum(s_list)
if total % 10 == 0:
    work_list = [s for s in s_list if s % 10 != 0]
    if work_list:
        total -= min(work_list)
    else:
        total = 0

print(total)
