# https://atcoder.jp/contests/abc130/tasks/abc130_b
# B - Bounding

n, x = list(map(int, input().split()))
l_list = list(map(int, input().split()))

c = 1
d = 0

for i in range(n):
    d += l_list[i]
    if d <= x:
        c += 1
    else:
        break

print(c)
