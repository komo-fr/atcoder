import itertools
N = int(input().split()[0])

p_gen = itertools.product(list(range(0, N)), repeat=3)
ans = len(list(p_gen))
print(ans)
