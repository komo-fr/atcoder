# https://atcoder.jp/contests/abc134/tasks/abc134_c
# C - Exception Handling
import copy

n = int(input().split()[0])
a_list = []

for _ in range(n):
    a_list.append(int(input().split()[0]))

kouho_list = sorted(a_list)
max_n = max(kouho_list)
second_max_n = kouho_list[-2]

max_list = [str(max_n) if x != max_n else str(second_max_n) for x in a_list]
max_str = '\n'.join(max_list)

print(max_str)
