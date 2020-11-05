S = input().split()[0]
T = input().split()[0]

c = 0

for s, t in zip(S, T):
    if s == t:
        c += 1
print(c)
