# https://atcoder.jp/contests/abc054/tasks/abc054_a
# A - One Card Poker
a, b = list(map(int, input().split()))

if a == 1:
    a = 100
if b == 1:
    b = 100

if a == b:
    answer = 'Draw'
elif a < b:
    answer = 'Bob'
elif a > b:
    answer = 'Alice'

print(answer)
