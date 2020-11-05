# https://atcoder.jp/contests/abc076/tasks/abc076_b
# B - Addition and Multiplication
c = 1
n = int(input().split()[0])
k = int(input().split()[0])

for _ in range(n):
    if c + k < c * 2:
        c = c + k
    else:
        c = c * 2

print(c)

