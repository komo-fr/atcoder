#!/usr/bin/env python3

N, M = list(map(int, input().split()))

sc_list = ["dummy"]

for _ in range(M):
    s, c = list(input().split())
    c = int(c)
    # 集合を変換する
    s_bit = s.replace("Y", "1").replace("N", "0")
    s_int = int(s_bit, 2)  # 集合を整数で表現する
    sc_list.append((s_int, c))

# cost[i][j] := i番目の品物まで見たときに、揃った部品の集合がjであるときの最小コスト
set_n = 1 << N  # 集合の個数
cost = [[float("inf")] * set_n for _ in range(M+1)]
cost[0][0] = 0  # 初期化

def print_table(table):
    print((len(table), len(table[0])))
    for line in table:
        print(line)

for i in range(1, M+1):  # セットの個数
    # セットiについて買う/買わないを考える
    for j in range(set_n):
        # 揃っている品物の集合j
        # セットiを買わない
        cost[i][j] = min([cost[i-1][j], cost[i][j]])
        
        # セットiを買う
        s = sc_list[i][0]  # セットiで揃う品物の集合
        c = sc_list[i][1]  # セットiのコスト
        # print(f"{j}|{s} = {j | s}")
        kouho_0 = cost[i-1][j | s]  # セットiを買わなくても揃う時のコスト
        kouho_1 = cost[i-1][j] + c  # セットiを買って揃える時のコスト
        kouho_2 = cost[i][j | s]  # 現在持っているコスト
        # print(f"{i=}, {j=}, kouho_0=cost[{i-1}][{j | s}]={kouho_0}, {kouho_1=}, {kouho_2=}")
        cost[i][j | s] = min([kouho_0, kouho_1, kouho_2])
        # print(f"cost[{i}][{j|s}] = {cost[i][j | s]}")
        # print("=============")

# print_table(cost)

ans = -1 if cost[-1][-1] == float("inf") else cost[-1][-1]
print(ans)
