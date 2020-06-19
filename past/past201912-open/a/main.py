#!/usr/bin/env python3

S = input()
is_ok = True
ok_list = [str(i) for i in range(10)]

for i in range(3):
    if S[i] not in ok_list:
        is_ok = False

ans = str(int(S) * 2) if is_ok else "error"

print(ans)
