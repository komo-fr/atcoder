#!/usr/bin/env python3

N, K = list(map(int, input().split()))
mod = 10 ** 9 + 7
total = 0


def sum_seq(start: int, end: int) -> int:
    n = end - start + 1
    result = n * (start + end) // 2
    return int(result)


item_N = N + 1
for k in range(K, item_N + 1):
    # k選ぶときの組み合わせの数を求める
    # 最小
    start = sum_seq(0, k - 1)
    end = sum_seq(N - k + 1, N)
    c_n = end - start + 1
    total += c_n % mod
    # print(f"{k=}, {c_n=}")


ans = total % mod
print(ans)
