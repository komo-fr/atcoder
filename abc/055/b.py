# https://atcoder.jp/contests/abc055/tasks/abc055_b
# B - Training Camp

n = int(input().split()[0])
warukazu = 10 ** 9 + 7
x = 1
for i in range(1, n+1):
    x = (x * i) % warukazu

print(x % warukazu)