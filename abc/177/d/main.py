#!/usr/bin/env python3
import networkx as nx

N, M = list(map(int, input().split()))
edge_list = []
G = nx.Graph()
for _ in range(M):
    s, t = list(map(int, input().split()))
    edge_list.append((s, t))
    G.add_edge(s, t)

# NetworkXを使う場合
max_size = -float("inf")
for compo in nx.connected_components(G):
    max_size = max(len(compo), max_size)

ans = max_size
print(ans)
