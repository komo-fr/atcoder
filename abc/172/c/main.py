#!/usr/bin/env python3
from collections import deque

N, M, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

reading_a_deque = deque([])
total = 0
count = 0


for i, a in enumerate(a_list):
    # Aを読めるだけ読む
    if total + a > K:
        break
    total += a
    count += 1
    reading_a_deque.append(a)

max_a_count = count
b_deque = deque(b_list)
reading_b_deque = deque()

while b_deque and total + b_deque[0] <= K:
    b = b_deque.popleft()
    total += b
    count += 1
    reading_b_deque.append(b)


# 初期値
max_count = count
a_count = max_a_count

# Aを1冊も読まないケース
# total <= Kの限り続ける
# b_dequeもなくなったら止める
def is_continue(reading_a_deque, total, b_deque):
    if not reading_a_deque:
        if b_deque:
            if total + b_deque[0] > K:
                return False
    if not b_deque:
        return False
    return True


while is_continue(reading_a_deque, total, b_deque):
    if reading_a_deque:
        time = reading_a_deque.pop()
        total -= time
        count -= 1

    # b_deque: 残っている本
    while b_deque and total + b_deque[0] <= K:
        b = b_deque.popleft()
        reading_b_deque.append(b)
        total += b
        count += 1
    # print(reading_b_deque)
    # print(f"{total=}")
    max_count = max(max_count, count)


ans = max_count
print(ans)
