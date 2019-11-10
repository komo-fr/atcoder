#!/usr/bin/env python3

N, A, B = list(map(int, input().split()))
a_idx = A
b_idx = B
turn = "A"
while True:
    # 判定
    if turn == "A":
        if a_idx == 1 and b_idx == a_idx + 1:
            winner = "Borys"
            break
    else:
        if b_idx == N and a_idx == b_idx - 1:
            winner = "Alice"
            break

    if turn == "A":
        if b_idx == a_idx + 1:
            a_idx -= 1
        else:
            a_idx += 1
        turn = "B"
    else:
        if a_idx == b_idx - 1:
            b_idx += 1
        else:
            b_idx -= 1
        turn = "A"

ans = winner
print(ans)
