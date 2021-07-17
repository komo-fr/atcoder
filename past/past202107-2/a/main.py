#!/usr/bin/env python3

S = input()
# a = sum([int(S[i]) * 3 if (i + 1) % 2 == 1 else int(S[i]) for i in range(15)]) % 10
a = sum([int(S[i]) * 3 for i in range(14) if (i + 1) % 2 == 1])
b = sum([int(S[i]) for i in range(14) if (i + 1) % 2 == 0])
c = (a + b) % 10

ans = "Yes" if c == int(S[-1]) else "No"
# print(a, b, c)
print(ans)
