# https://atcoder.jp/contests/abc120/tasks/abc120_b
# B - K-th Common Divisor

a, b, k = list(map(int, input().split()))

def koyaku(x):
    i = 1
    koyaku_list = []
    while i * i <= x:
        if x % i == 0:
            koyaku_list.append(i)
            koyaku_list.append(x // i)
        i += 1
    return list(set(koyaku_list))

a_koyaku = koyaku(a)
b_koyaku = koyaku(b)

common_koyaku = set(a_koyaku).intersection(set(b_koyaku))
ans = sorted(common_koyaku, reverse=True)[k-1]

print(ans)
