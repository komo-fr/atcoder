#!/usr/bin/env python3
import itertools

N = int(input().split()[0])

def get_divisor(n: int) -> list:
    d_list = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            a = int(n / i)
            d_list.append((i, a))
    return d_list
d_list = get_divisor(N)
d_list = set(list(itertools.chain.from_iterable(d_list)))
d_list = sorted(list(d_list))
d_list = [str(d) for d in d_list]
ans = "\n".join(d_list)
print(ans)
