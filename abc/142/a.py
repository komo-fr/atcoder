N = int(input().split()[0])

if N == 1:
    c = 1
elif N % 2 == 0:
    c = 0.5
else:
    c = ((N + 1) // 2) / N
print(c)
