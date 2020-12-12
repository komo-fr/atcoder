#!/usr/bin/env python3
from collections import deque, namedtuple

N, C, K = list(map(int, input().split()))
t_list = []
Person = namedtuple("Person", ["at", "deadline"])

for _ in range(N):
    t = int(input().split()[0])
    t_list.append(Person(t, t + C))
person_deque = deque(sorted(t_list))

bus_count = 0
bus_deque = deque([])

# バスが定員になる
# デッドラインになる客がいる
while person_deque:
    # print(f"{len(person_deque)}, {person_deque}")
    person = person_deque.popleft()

    if bus_deque and bus_deque[0].deadline < person.at:
        # バスに人が乗っていて、出発しないと間に合わない人がいる
        # 出発
        # print(f"{bus_deque=}")
        bus_count += 1
        # 新しいバスに乗る
        bus_deque = deque([person])

        if not person_deque:
            # 最後の一人の場合、人数に関わらず出発
            bus_count += 1
        continue

    bus_deque.append(person)
    if len(bus_deque) >= C or not person_deque:
        # バスの定員に達した or 最後の一人である
        # 出発
        # print(f"{bus_deque=}")
        bus_count += 1
        bus_deque = deque([])
        continue

ans = bus_count
print(ans)
