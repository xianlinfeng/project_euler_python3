import math


def isPrime(n):
    """
    check if the input number n is a prime number or not
    """
    if n <= 3:
        return n > 1
    if n % 6 != 1 and n % 6 != 5:
        return False

    sqrt = math.sqrt(n)
    for i in range(5, int(sqrt)+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


def findFactors(n):
    """
    find the all the factors of a number n
    """
    factors = []
    while True:
        for i in range(n+1):
            if isPrime(i):
                if n % i == 0:
                    factors.append(i)
                    n = int(n / i)
                    break
        if n == 1:
            break
    return factors


if __name__ == "__main__":
    factors = findFactors(600851475143)
    print(max(factors))
