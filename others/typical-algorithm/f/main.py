#!/usr/bin/env python3
import networkx as nx

N, M = list(map(int, input().split()))

edge_list = []

for _ in range(M):
    u, v, c = list(map(int, input().split()))
    edge_list.append((u, v, c))

g = nx.Graph()
g.add_weighted_edges_from(edge_list)
edges = nx.minimum_spanning_edges(g, algorithm="prim")

cost = 0
for edge in edges:
    cost += edge[2]["weight"]

ans = cost
print(cost)
