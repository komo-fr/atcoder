# https://atcoder.jp/contests/abc090/tasks/arc091_a
# C - Flip,Flip, and Flip......

N, M = list(map(int, input().split()))

if N == 1 and M == 1:
    c = 1
elif N == 1 or M == 1:
    c = max(N, M) - 2
else:
    c = (M - 2) * (N - 2)

print(c)
