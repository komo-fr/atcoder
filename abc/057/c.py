# https://atcoder.jp/contests/abc057/tasks/abc057_c
# C - Digits in Multiplication

N = int(input().split()[0])
c = 0
for i in range(int(N ** (1/2)), 0, -1):
    if N % i == 0:
        a = int(N / i)
        d = (i, a)
        break

ans = len(str(max(d)))
print(ans)
