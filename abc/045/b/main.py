#!/usr/bin/env python3

a_list = list(input().split()[0])
b_list = list(input().split()[0])
c_list = list(input().split()[0])

turn = "a"
card_dict = dict(a=a_list, b=b_list, c=c_list)
while True:
    if card_dict[turn]:
        turn = card_dict[turn].pop(0)
    else:
        break

ans = turn.upper()
print(ans)
