# https://atcoder.jp/contests/abc056/tasks/arc070_a
# C - Go Home
X = int(input().split()[0])
total = 0
for x in range(1, X+1):
    total += x
    if total >= X:
        break

ans = x

print(ans)
