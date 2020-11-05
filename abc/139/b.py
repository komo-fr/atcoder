A, B = list(map(int, input().split()))
c = -1
x = 1

while x < B:
    c += 1
    x = (A - 1) * (c - 1) + A

c = max(0, c)
print(c)
