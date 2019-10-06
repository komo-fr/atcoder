#!/usr/bin/env python3
import fractions

n = int(input().split()[0])
n = int(n)

hp_list = list(map(int, input().split()))
hp_list = [int(hp) for hp in hp_list]

hp = hp_list[0]

for h in hp_list[1:]:
    hp = fractions.gcd(hp, h)

print(hp)
