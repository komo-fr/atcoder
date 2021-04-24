#!/usr/bin/env python3

S = input()
count = 0
ans = "none"
for i, _ in enumerate(S):
    if i % 4 == 0:
        count += 1
        # print(S[i:i+4])
        if S[i:i+4] == "post":
            ans = count
            break
print(ans)
