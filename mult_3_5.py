"""
    Sum multiples of 3 or 5 between [1 and 100)
"""

sum = 0

for i in range(1, 1000):
    if (i % 3) == 0 or (i % 5) == 0:
        sum += i


print(f"Sum {sum}")