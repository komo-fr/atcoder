#!/usr/bin/env python3

S, T = list(input().split())
x_list = "B9,B8,B7,B6,B5,B4,B3,B2,B1,1F,2F,3F,4F,5F,6F,7F,8F,9F".split(",")

ans = abs(x_list.index(S) - x_list.index(T))
print(ans)
