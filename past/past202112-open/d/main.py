#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))


class Score:
    def __init__(self, i, a, b):
        self.a = a
        self.b = b
        self.i = i

    def __lt__(self, other):
        # self < other
        if self.a + self.b != other.a + other.b:
            return self.a + self.b < other.a + other.b
        elif self.a != other.a:
            return self.a < other.a
        else:
            return self.i > other.i


s_list = []
for i, ab in enumerate(zip(a_list, b_list)):
    a, b = ab
    score = Score(i + 1, a, b)
    s_list.append(score)

s_list = sorted(s_list, reverse=True)
r_list = []
for s in s_list:
    r_list.append(str(s.i))
ans = " ".join(r_list)
print(ans)
