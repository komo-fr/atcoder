#!/usr/bin/env python3
N = int(input().split()[0])
abc_list = []

for _ in range(N):
    a, b, c = list(map(int, input().split()))
    abc_list.append(dict(a=a, b=b, c=c))

dp_list = [dict(a=0, b=0, c=0) for _ in range(N + 1)]

for i in range(1, N + 1):
    # i日目の行動
    scores = abc_list[i - 1]
    # その日行動Aをとる場合の最適値
    dp_list[i]["a"] = scores["a"] + max(dp_list[i - 1]["b"], dp_list[i - 1]["c"])
    # その日行動Bをとる場合の最適値
    dp_list[i]["b"] = scores["b"] + max(dp_list[i - 1]["a"], dp_list[i - 1]["c"])
    # その日行動Cをとる場合の最適値
    dp_list[i]["c"] = scores["c"] + max(dp_list[i - 1]["a"], dp_list[i - 1]["b"])

ans = max(dp_list[-1].values())

print(ans)
