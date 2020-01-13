#!/usr/bin/env python3

N, M = list(map(int, input().split()))
ps_list = [[] for _ in range(N)]

for _ in range(M):
    p, s = list(input().split())
    p = int(p) - 1
    ps_list[p].append(s)

wa_c = 0
ac_c = 0
total_wa_c = 0

for i, ss in enumerate(ps_list):
    wa_c = 0
    for s in ss:
        if s == "WA":
            wa_c += 1
        else:
            ac_c += 1
            total_wa_c += wa_c
            break

ans = "{} {}".format(ac_c, total_wa_c)
print(ans)
