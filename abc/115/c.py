# https://atcoder.jp/contests/abc115/tasks/abc115_c
# C - Christmas Eve
import itertools

n, k = list(map(int, input().split()))
h_list = []

for _ in range(n):
    h_list.append(int(input().split()[0]))

h_list = sorted(h_list)

min_value = float('inf')

for i, v in enumerate(h_list[:-k+1]):
    diff_h = h_list[i+k-1] - v
    if diff_h < min_value:
        min_value = diff_h

print(min_value)
