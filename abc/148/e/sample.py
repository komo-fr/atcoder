#!/usr/bin/env python3

#!/usr/bin/env python3

N = int(input().split()[0])
t = 1
for i in range(N, 0, -2):
    if i < 2:
        t *= 1
    else:
        t *= i
c = 0
for x in reversed(list(str(t))):
    if x == "0":
        c += 1
    else:
        break
ans = c
print(t)
print(ans)
