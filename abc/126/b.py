# https://atcoder.jp/contests/abc126/tasks/abc126_b
# B - YYMM or MMYY

s = input().split()[0]

# YYMMの可能性がある
format_list = []

if 1 <= int(s[:2]) <= 12:
    format_list.append('MMYY')

if 1 <= int(s[2:]) <= 12:
    format_list.append('YYMM')

if not format_list:
    ans = 'NA'
elif len(format_list) > 1:
    ans = 'AMBIGUOUS'
else:
    ans = format_list[0]

print(ans)
