import math
import eulerlib


primes = list(i for i in range(150000) if eulerlib.is_prime(i))


def getFactors(n):
    factors = set()
    while n > 1:
        for i in primes:
            if n >= i and n % i == 0:
                factors.add(i)
                n //= i
                break
            elif n < i:
                break
    return factors


def getLenFactors(n):
    return len(getFactors(n))


if __name__ == "__main__":
    nums = list(getLenFactors(x) for x in range(150000))
    for i in range(len(nums)-2):
        if nums[i] == nums[i+1] == nums[i+2] == nums[i+3] == 4:
            # if nums[i] == nums[i+1] == nums[i+2] == 3:
            print(i)
            break
