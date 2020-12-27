#!/usr/bin/env python3
import networkx as nx

# H, W = list(map(int, input().split()))

H, W = list(map(int, input().split()))
s_table = []
for y in range(H):
    s = input()
    s_table.append(s)
G = nx.Graph()
for y, s in enumerate(s_table):
    for x, char in enumerate(s):
        # ひとつ前、ひとつ上と道があったらつなぐ
        if x != 0:
            if s[x - 1] == "#" and char == "#":
                G.add_edge((y + 1, x + 1), (y + 1, x - 1 + 1))
        if y != 0:
            if s_table[y - 1][x] == "#" and char == "#":
                G.add_edge((y + 1, x + 1), (y - 1 + 1, x + 1))

print(G.edges())

route = list(nx.eulerian_circuit(G))
print(len(route))
for r in route:
    print(r[0], r[1])

# s_table = []
# target_list = []
# k = 0
# for h in range(H):
#     s = input()
#     for w, char in enumerate(s):
#         if char == "#":
#             k += 1
#             target_list.append((h + 1, w + 1))
# print(k)
# for t in target_list:
#     print(f"{t[0]} {t[1]}")
