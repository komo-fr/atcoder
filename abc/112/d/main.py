#!/usr/bin/env python3

N, M = list(map(int, input().split()))


def factorize(n: int) -> list:
    # 試し割り法
    f_list = []
    while n % 2 == 0:
        f_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            f_list.append(f)
            n //= f
        else:
            # 偶数はすでにチェックしているので+2ずつカウントアップ
            f += 2

    if n != 1:
        f_list.append(n)
    return f_list


p_list = list(sorted(factorize(M), reverse=True))
print(p_list)
k = 1
for p in p_list:
    k *= p
    if M // k < N:
        continue
    else:
        break

k = p
ans = k

print(ans)
