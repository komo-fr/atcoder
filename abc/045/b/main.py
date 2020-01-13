#!/usr/bin/env python3

a_list = list(input().split()[0])
b_list = list(input().split()[0])
c_list = list(input().split()[0])

turn = "a"
card_dict = dict(a=a_list, b=b_list, c=c_list)

while card_dict["a"] and card_dict["b"] and card_dict["c"]:
    turn = card_dict[turn].pop()

for k, v in card_dict.items():
    if v:
        continue
    else:
        ans = k.upper()

print(ans)
