def findFactorsLen(n):
    factors = []
    if n % 2 != 0 or n % 3 != 0 or n % 5 != 0 or n % 7 != 0 or n % 11 != 0 or n % 13 != 0:
        return 0
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return len(factors)


if __name__ == "__main__":
    triangle = 0
    for i in range(1, 30000):
        triangle += i
        if findFactorsLen(triangle) > 500:
            print(triangle)
            break
