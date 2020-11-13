v_list = list(map(int, input().split()))
s = "ABC"
index = sorted(v_list)[1]
ans = s[v_list.index(index)]
print(ans)