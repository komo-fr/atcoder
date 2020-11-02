# https://atcoder.jp/contests/abc073/tasks/abc073_c
# C - Write and Erase
import collections

n = int(input().split()[0])
a_list = []

for _ in range(n):
    a_list.append(int(input().split()[0]))

counter = collections.Counter(a_list)
no_list = [k for k, c in counter.items() if c % 2 == 1]
ans = len(no_list)
print(ans)
