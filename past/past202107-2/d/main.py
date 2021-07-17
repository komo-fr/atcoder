#!/usr/bin/env python3

N = int(input().split()[0])
S = input()
count = 0
stop_count = 0
T = []
for i, char in enumerate(S):
    # print(f"{i=}, {T=}")
    T.append(char)

    if i < 2:
        continue
    s = T[i - 2] + T[i - 1] + T[i]
    # print(f"{s=}")
    # if stop_count > 0:
    #     stop_count -= 1
    #     T.append(char)
    #     continue

    if s in ["axa", "ixi", "uxu", "exe", "oxo"]:
        count += 1
        stop_count = 3
        T[i - 2] = "."
        T[i - 1] = "."
        T[i] = "."

ans = "".join(T)
print(ans)
