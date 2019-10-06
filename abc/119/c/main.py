#!/usr/bin/env python3

N, A, B, C = list(map(int, input().split()))
l_list = []

for _ in range(N):
    l = int(input().split()[0])
    l_list.append(l)


def cost(no, a_len, b_len, c_len):
    if no == N:
        # 最後のノードでは
        # 差分を延長魔法 or 短縮魔法で補う
        if min(a_len, b_len, c_len) <= 0:
            # 竹の長さを0以下にすることはできないので
            # このパターンはありえない
            return float("inf")

        a_cost = abs(a_len - A)
        b_cost = abs(b_len - B)
        c_cost = abs(c_len - C)
        # 最初にA,B,Cを選ぶときは余分に+10されているので、減らす
        return sum([a_cost, b_cost, c_cost]) - 30

    l = l_list[no]
    a_cost = 10 + cost(no + 1, a_len + l, b_len, c_len)
    b_cost = 10 + cost(no + 1, a_len, b_len + l, c_len)
    c_cost = 10 + cost(no + 1, a_len, b_len, c_len + l)
    d_cost = cost(no + 1, a_len, b_len, c_len)

    # このノードより上（以前）のルートは同じなので、
    # この時点で最小のものを1つだけ返せば良い
    return min([a_cost, b_cost, c_cost, d_cost])


ans = cost(0, 0, 0, 0)
print(ans)
