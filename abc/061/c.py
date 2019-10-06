# https://atcoder.jp/contests/abc061/tasks/abc061_c
# C - Big Array

N, K = list(map(int, input().split()))
ab_list = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

ab_list = sorted(ab_list, key=lambda x: x[0])
c = 0
for a, b in ab_list:
    c += b
    if c >= K:
        ans = a
        break

print(ans)

