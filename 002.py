a, b = 1, 2
sum = 0
while True:
    a, b = b, a + b
    if a < 4000000:
        if a % 2 == 0:
            sum += a
    else:
        break
print(sum)
