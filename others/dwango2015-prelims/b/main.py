#!/usr/bin/env python3

S = input()
N = len(S)
is_seq = False
count25 = 0
sub25_len = 0
for i in range(1, N):
    ss = S[i - 1] + S[i]
    if ss == "25":
        is_seq = True
        sub25_len += 1
    elif is_seq and ss == "52":
        continue
    else:
        if is_seq:
            count25 += sum(list(range(sub25_len + 1)))
        is_seq = False
        sub25_len = 0

if is_seq:
    count25 += sum(list(range(sub25_len + 1)))
ans = count25

print(ans)
