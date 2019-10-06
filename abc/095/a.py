# https://atcoder.jp/contests/abc095/tasks/abc095_a
# A - Something on It

s = input().split()[0]

c = 700
for char in s:
    if char == 'o':
        c += 100

print(c)