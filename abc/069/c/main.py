#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
c = {'odd': 0,
     'even': 0,
     'four': 0,
     'even_not_four': 0}

for x in a_list:
    if x % 2 == 0:
        c['even'] += 1
    else:
        c['odd'] += 1

    if x % 4 == 0:
        c['four'] += 1

ans = 'No'

if c['even'] == N:
    ans = 'Yes'
else:
    if c['odd'] == 1:
        if c['four'] >= 1:
            ans = 'Yes'
    else:
        if c['even'] - c['four'] >= 1:
            if c['four'] >= c['odd']:
                ans = 'Yes'
        else:
            if c['four'] >= c['odd'] - 1:
                ans = 'Yes'

print(ans)
