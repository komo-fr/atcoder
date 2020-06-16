#!/usr/bin/env python3

N = int(input().split()[0])
even_sum = sum([int(x) for i, x in enumerate(reversed(str(N))) if (i + 1) % 2 == 0])
odd_sum = sum([int(x) for i, x in enumerate(reversed(str(N))) if (i + 1) % 2 == 1])

print(even_sum, odd_sum)
