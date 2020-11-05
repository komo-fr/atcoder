# https://atcoder.jp/contests/abc111/tasks/abc111_a
# A - AtCoder Beginner Contest 999

n = int(input().split()[0])
n = str(n)
n = n.replace('1', 'x')
n = n.replace('9', '1')
n = n.replace('x', '9')

print(n)