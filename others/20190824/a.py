import itertools
M, D = list(map(int, input().split()))

p = itertools.product(range(1, M+1), range(1, D+1))
c = 0
t_list = []
for m, d in p:
    d_10, d_1 = str(d).zfill(2)
    if int(d_10) == 1 or int(d_1) == 1:
        continue
    if m == int(d_10) * int(d_1):
        c += 1
        t_list.append((m, d_10, d_1))
print(c)