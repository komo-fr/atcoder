#!/usr/bin/env python3
import math
N = int(input().split()[0])

d = math.floor(math.log2(N)) + 1

TAKAHASHI = 1
AOKI = 0

if d % 2 == 0:
    left_player = TAKAHASHI
    right_player = AOKI
else:
    left_player = AOKI
    right_player = TAKAHASHI

def go_left(x):
    return x * 2

def go_right(x):
    return x * 2 + 1

x = 1

for i in range(1, d + 1):
    player = i % 2
    if player == left_player:
        x = go_left(x)
    else:
        x = go_right(x)
    if x > N:
        break

# オーバーした時のplayerが負け
ans = 'Aoki' if player == TAKAHASHI else 'Takahashi'
print(ans)
