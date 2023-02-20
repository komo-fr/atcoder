#!/usr/bin/env python3
# しゃくとり法で求める方法

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

total = 0
r = 1
for i in range(N - 1):
    # Aj - Ai <= Kを満たすギリギリまで伸ばす
    for j in range(r, N):
        if a_list[j] - a_list[i] <= K:
            if r < N - 1:
                # 末尾の場合はこれ以上増やさない
                r += 1
        else:
            # 超えたときは進みすぎなのでインデックスを1引く
            r -= 1
            break
    # Ajのインデックス - Aiのインデックス が組み合わせの数
    total += r - i

ans = total
print(ans)
