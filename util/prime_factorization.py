# 試し割り法で素因数分解する

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

N = int(input().split()[0])
print(factorize(N))
