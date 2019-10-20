
#!/usr/bin/env python3
import bisect


N = int(input().split()[0])
l_list = list(map(int, input().split()))
l_list = sorted(l_list)
p_list = []

for a_i, a in enumerate(l_list):
    for b_i, b in enumerate(l_list):
        if a_i == b_i:
            continue

        c_kouho = a + b
        c_i = bisect.bisect_left(l_list, c_kouho)
        p_list += [
            sorted([a, b, c])
            for c_i, c in enumerate(l_list[: c_i + 1])
            if c_i != a_i and c_i != b_i and abs(b - c) < a < b + c
        ]

p_list = ["{}_{}_{}".format(p[0], p[1], p[2]) for p in p_list]
ans = len(set(p_list))

print(ans)
