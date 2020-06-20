#!/usr/bin/env python3

N, M = list(map(int, input().split()))
sc_list = []
for _ in range(M):
    s, c = list(map(int, input().split()))
    sc_list.append((s, c))

sc_set = set(sc_list)
start = 10 ** (N - 1)
end = 10 ** N

is_ok = True

if len(sc_set) > N:
    is_ok = False

answer = -1
if is_ok:
    for i in range(start, end):
        is_sub_ok = True
        str_number = str(i)
        for sc in sc_set:
            s, c = sc
            if str_number[s - 1] != str(c):
                is_sub_ok = False
                continue
        if is_sub_ok:
            answer = i
            break
ans = answer
print(ans)
