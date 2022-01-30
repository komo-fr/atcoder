#!/usr/bin/env python3

N = int(input().split()[0])
ok_list = []
for i in range(2, int(N ** (1 / 2)) + 2):
    for j in range(2, int(N ** (1 / 2)) + 2):
        if i ** j > N:
            break
        # print(f"{i} ** {j} = {i ** j}")
        ok_list.append(i ** j)
# print(len(ok_list))
ans = N - len(set(ok_list))
# print(len(set(ok_list)))

print(ans)
