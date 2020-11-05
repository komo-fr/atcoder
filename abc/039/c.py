# https://atcoder.jp/contests/abc039/tasks/abc039_c
# C - ピアニスト高橋君

S = input().split()[0]

shi_index = S.find('WWBWBWW')
pattern = ['Do', 'Do', 'Re', 'Re', 'Mi', 'Fa', 'Fa', 'So', 'So', 'La', 'La', 'Si'] * 2
pattern = list(reversed(pattern))

print(pattern[shi_index])
