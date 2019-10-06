# https://atcoder.jp/contests/abc137/tasks/abc137_c
# C - Green Bin
import collections
import itertools
import math

n = int(input().split()[0])
s_list = []


for _ in range(n):
    s = input().split()[0]
    s_list.append(''.join(sorted(s)))

counter = collections.Counter(s_list)

def C(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

p_list = [C(value, 2) for key, value in counter.items() if value > 1]
ans = int(sum(p_list))

print(ans)
