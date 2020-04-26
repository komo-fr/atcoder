#!/usr/bin/env python3
from collections import deque

S = input()
N = len(S)
sub_s = ""
d = deque()
total = 0
# s_list = []

for l in range(N):  # 200000
    if l % 2 == 0:
        # 左から右に伸ばしていく
        d = deque([S[l]])
        sub_s = "".join(d)
        # s_list.append(sub_s)  # TODO

        if int(sub_s) % 2019 == 0:
            total += 1
        r = l + 1
        while r < N:  # 末尾N-1まで
            d.append(S[r])
            sub_s = "".join(d)
            # s_list.append(sub_s)  # TODO
            if int(sub_s) % 2019 == 0:
                total += 1
                # print((l, r))
                # print(sub_s)
            r += 1
    else:
        # 右を縮めていく
        r = N  # 末尾から
        d.popleft()
        sub_s = "".join(d)
        # s_list.append(sub_s)  # TODO
        if not sub_s:
            break
        if int(sub_s) % 2019 == 0:
            total += 1

        while r > l:
            d.pop()
            sub_s = "".join(d)
            # s_list.append(sub_s)  # TODO

            if not sub_s:
                break
            if int(sub_s) % 2019 == 0:
                total += 1
                # print((l, r))
                # print(sub_s)
            # r -= 1
            r += 1
    # print("--------")

ans = total

print(ans)
