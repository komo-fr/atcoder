n = int(input().split()[0])

str_n = str(n)
keta = len(str_n)

c = 0
keta_list = list(range(0, 6))
keta_list.reverse()

# 1の桁
if 1 <= n < 10:
    c += n
else:
    c += 9

# 100の桁
if n >= 100:
    # 100 - 999
    if n <= 999:
        # print('100 - 999')
        c += (n - 99)
    else:
        # 1000 -
        # print('100 -')
        c += 900 # 100から999 までの数

# 10000の桁
if n >= 10000:
    if n <= 99999:
        # 10000 - 99999
        # print('10000 - 99999')
        # print('+ {}'.format(n-9999))
        c += n - 9999
    else:
        # 10000以上
        # print('10000以上')
        c += 90000 # 1000から99999までの個数

print(c)
