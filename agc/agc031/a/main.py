#!/usr/bin/env python3

N = int(input().split()[0])
S = input()

start_idx, end_idx = 0, 0
is_reversed = False
sub_s = S[0]
count = 1
mod = 10 ** 9 + 7


while True:

    if len(set(sub_s)) == len(sub_s):
        count += 1
        is_ok = True
    else:
        is_ok = False

    # 次の更新
    if not is_reversed:
        if end_idx != N - 1:
            if is_ok:
                end_idx += 1
            else:
                is_reversed = True
                start_idx += 1
        else:
            is_reversed = True
            start_idx += 1
    else:
        if end_idx != start_idx:
            end_idx -= 1
        else:
            is_reversed = False
            start_idx += 1

    if start_idx == N or end_idx == N or start_idx > end_idx:
        break

ans = count % mod
print(ans)
