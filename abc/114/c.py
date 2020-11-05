# https://atcoder.jp/contests/abc114/tasks/abc114_c
# C - 755
import itertools

n = int(input().split()[0])
k = len(str(n))
c = 0

if k >= 3:
    for j in range(3, k+1):
        p_gen = itertools.product([3, 5, 7], repeat=j)
        for p in p_gen:
            x = 0
            for k_i in range(j):
                x += p[k_i] * 10**k_i
            if x <= n and len(set(list(str(x)))) == 3:
                c += 1

print(c)