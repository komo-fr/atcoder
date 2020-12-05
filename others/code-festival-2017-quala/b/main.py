#!/usr/bin/env python3

N, M, K = list(map(int, input().split()))
is_ok = False
for h in range(N+1):
    for w in range(M+1):
        if w *h + (M-w) *(N-h) == K:
            is_ok = True
            break

ans = "Yes" if is_ok else "No"
print(ans)
