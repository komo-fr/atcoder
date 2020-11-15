#!/usr/bin/env python3

A, B, K = list(map(int, input().split()))
done_list = []
for i in range(A, A + K):
    if i > B:
        continue
    print(i)
    done_list.append(i)

for i in range(B - K + 1, B + 1):
    if i < A:
        continue
    if i not in done_list:
        print(i)
