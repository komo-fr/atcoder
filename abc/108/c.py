# https://atcoder.jp/contests/abc108/tasks/arc102_a
# C - Triangular Relationship
import copy
import itertools
N, K = list(map(int, input().split()))
ab_list = []

# 2 * a = (X + Y - Z) * K
# a = (X + Y - Z) * K / 2
# が成り立つ
# Kが偶数の場合は
# a = T * K または a = T * (1/2)K
# a + b = T * K なので、a, b, cのいずれか１つが a % (1/2)K == 0なら、全てそうである必要がある
# Kが偶数の場合は (1/2)*Kが整数にならないので
# a = T * K

if K % 2 == 0:
    a_list = [x for x in range(1, N + 1) if x % K == 0]
    p = len(a_list) ** 3
    a_list = [x for x in range(1, N + 1) if (x % (0.5 * K)) == 0 and not (x % K == 0)]
    p += len(a_list) ** 3
else:
    a_list = [x for x in range(1, N + 1) if x % K == 0]
    p = len(a_list) ** 3

print(p)
