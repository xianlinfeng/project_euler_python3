import eulerlib
import math
# if __name__ == "__main__":
#     primes = list(x for x in range(2, 1000000) if eulerlib.is_prime(x))
#     n = 0
#     primeSum = []
#     for x in primes:
#         n += x
#         if n < 1000000:
#             if n in primes:
#                 primeSum.append(n)
#         else:
#             break
#     print(primeSum)

# Returns a list of True and False indicating whether each number is prime.
# For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise.


def list_primality(n):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def compute():
    ans = 0
    isprime = list_primality(999999)
    primes = list(x for x in range(2, 999999) if eulerlib.is_prime(x))
    consecutive = 0
    for i in range(len(primes)):
        sum = primes[i]
        consec = 1
        for j in range(i + 1, len(primes)):
            sum += primes[j]
            consec += 1
            if sum >= len(isprime):
                break
            if isprime[sum] and consec > consecutive:
                ans = sum
                consecutive = consec
    return str(ans)


if __name__ == "__main__":
    print(compute())
