# https://atcoder.jp/contests/abc029/tasks/abc029_c
# C - Brute-force Attack
import itertools
N = int(input().split()[0])

p_gen = itertools.product('abc', repeat=N)
ans_list = []
for p in p_gen:
    ans_list.append(''.join(list(p)))

ans_list = sorted(ans_list)
ans = '\n'.join(ans_list)
print(ans)
