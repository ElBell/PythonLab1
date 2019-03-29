i, a, b, total = 0, 0, 1, 0

while a < 4000000:
    current = a + b
    a = b
    b = current
    if current % 2 == 0:
        total += current
print(total)
