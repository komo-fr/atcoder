#!/usr/bin/env python3
import numpy as np

N = int(input().split()[0])
ans = np.base_repr(N, 36)
print(ans)
