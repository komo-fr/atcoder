#!/usr/bin/env python3

a, b = list(map(int, input().split()))
n = min([len(str(a)), len(str(b))])

is_kuriagari = False

for i in range(1, n+1):
    x = int(str(a)[-i])
    y = int(str(b)[-i])
    if x + y >= 10:
        is_kuriagari = True
        break

ans = "Hard" if is_kuriagari else "Easy"
print(ans)
