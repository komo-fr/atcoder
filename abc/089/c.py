# https://atcoder.jp/contests/abc089/tasks/abc089_c
# C - March
import itertools
import collections

n = int(input().split()[0])
s_list = []

for _ in range(n):
    s = input().split()[0]
    s_list.append(s)

target_list = [s[0] for s in s_list if s[0] in list('MARCH')]
counter = collections.Counter(target_list)
c = 0

if len(set(target_list)) < 3:
    ans = 0
else:
    p_list = itertools.combinations(set(target_list), 3)

    for p in p_list:
        c += counter[p[0]] * counter[p[1]] * counter[p[2]]
    ans = c
print(c)
