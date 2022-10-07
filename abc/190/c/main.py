#!/usr/bin/env python3
import itertools

N, M = list(map(int, input().split()))
ab_list = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

K = int(input().split()[0])
cd_list = []

for _ in range(K):
    c, d = list(map(int, input().split()))
    cd_list.append((c, d))

p_gen = itertools.product([0, 1],repeat=3)
max_count = 0
for pattern in p_gen:  # 65536
    cond_list = [dict(a=False, b=False) for _ in range(K)] 
    for h_index, p in enumerate(pattern):  # 16
        done = False
        for c_index, cond in enumerate(cond_list):  # 100
            if (ab_list[c_index][0] == cd_list[h_index][p]):
                cond_list[c_index]["a"] = True
                # print(f"人{h_index+1}が条件{c_index+1}のA（皿{ab_list[c_index][0]}）にボールをおきました: {cond_list}")

            if (ab_list[c_index][1] == cd_list[h_index][p]):
                cond_list[c_index]["b"] = True
                # print(f"人{h_index+1}が条件{c_index+1}のB（皿{ab_list[c_index][1]}）にボールをおきました: {cond_list}")
                
    count = sum([c["a"] and c["b"] for c in cond_list])
    max_count = max([max_count, count])
    # print(f"{max_count=}===================")

ans = max_count
print(ans)
