#!/usr/bin/env python3

A, B = list(map(int, input().split()))

after_A = str(A)
after_B = str(B)
if A != 999:
    for i in range(3):
        if str(A)[i] != "9":
            after_A = str(A)[:i] + "9"
            if i != 2:
                after_A += str(A)[i + 1 :]
            break
if B != 100:
    if str(B)[0] != "1":
        after_B = "1" + str(B)[1:]
    else:
        if str(B)[1] != "0":
            after_B = str(B)[0] + "0" + str(B)[2]
        elif after_B[2] != 0:
            after_B = str(B)[:2] + "0"

ans = max(int(after_A) - B, A - int(after_B))
print(ans)
