# https://atcoder.jp/contests/abc120/tasks/abc120_c
# C - Unification
import collections

s = input().split()[0]

counter = collections.Counter(list(s))
c_0 = counter['0']
c_1 = counter['1']
step = min(c_0, c_1)
print(step * 2)
