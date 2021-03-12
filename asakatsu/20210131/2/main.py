#!/usr/bin/env python3
import numpy as np

c_table = []
for _ in range(4):
    c_list = list(input().split())
    c_table.append(c_list)

c_table = np.array(c_table)
# c_table = np.fliplr(c_table)
c_table = np.rot90(c_table)
c_table = np.rot90(c_table)

for c_list in c_table:
    c = " ".join(c_list)
    print(c)
