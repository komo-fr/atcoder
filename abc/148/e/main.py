#!/usr/bin/env python3

#!/usr/bin/env python3

N = int(input().split()[0])

if N % 2 == 0:
    n = (N // 2) // 5
    total_n = n
    count = 2
    while n >= 5:
        p = (N // 2) // (5 ** count)
        total_n += p
        count += 1
        if p <= 0:
            break
        # n_w = n // 5
        # # n_amari = n_w % 5 if n_w % 5 != 0 else 4
        # n_amari = n_w % 5
        # n_f = (n_w - 1) * 5 + (n_amari + 1)
        # # total_n += count * (n_amari + 1)
        # # total_n += (n_amari + 1) + (n_w - 1) * 5
        # n = n // 5
        # count += 1
        # total_n += 1
    ans = total_n
else:
    ans = 0

print(ans)
