#!/usr/bin/env python3
from collections import deque

Q, H, S, D = list(map(int, input().split()))
N = int(input().split()[0])

class Nedan:
    def __init__(self, x, amount, name):
        self.x = x
        self.amount = amount
        self.unit_x = x/(amount/0.25)
        self.name = name

    def __lt__(self, other):
        if self.unit_x == other.unit_x:
            return self.amount > other.amount
        return self.unit_x <= other.unit_x
    def __str__(self):
        text = f"{self.name}: {self.amount}リットル{self.x}円（単価{self.unit_x}）"
        return text

q = Nedan(Q, 0.25, "Q")
h = Nedan(H, 0.5, "H")
s = Nedan(S, 1, "S")
d = Nedan(D, 2, "D")

nedan_que = deque(list(sorted([q, h, s, d])))
# for nedan in list(sorted([q, h, s, d])):
#     print(nedan)

n = N  # 量
cost = 0
while n > 0:
    nedan = nedan_que.popleft()
    if n < nedan.amount:
        # 使えない
        continue
    else:
        # 買えるだけ買う
        k = n // nedan.amount
        n -= k * nedan.amount
        cost += int(nedan.x * k)
        # print(f"{nedan.name}({nedan.amount}リットル）を{k}個（{nedan.amount * k}リットル）購入({nedan.x} * {k} = {nedan.x * k})円（残り{n}リットル)")
        # print(f"値段{nedan.x * k}円")

ans = int(cost)
print(ans)
