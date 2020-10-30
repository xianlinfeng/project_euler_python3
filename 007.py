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


if __name__ == "__main__":
    i, j = 0, 1
    while True:
        if isPrime(j):
            i += 1
        if i == 10001:
            print(j)
            break
        j += 1
