import math
N = int(input().split()[0])
c = 0
for j in range(1, N+1):
    test_list = [j % x for x in range(1, j) if x - 1 < j % x]
    if test_list:
        c += 1
if c > 0:
    print(True)
else:
    print(False)
