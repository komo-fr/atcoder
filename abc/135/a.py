# n = int(input().split()[0])
a, b = list(map(int, input().split()))

ans = 'IMPOSSIBLE'
if a == b:
    k = 0
elif (a + b) % 2 == 0:
    k = int((a+b) / 2)
else:
    k = 'IMPOSSIBLE'
print(k)
