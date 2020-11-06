import math
import eulerlib
import itertools


def count_consecutive_primes(ab):
    a, b = ab  # it will pass (a,b) into this funciton
    for i in itertools.count():
        n = i*i + a * i + b
        if not eulerlib.is_prime(n):
            return i


def compute():
    ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
              key=count_consecutive_primes)
    return str(ans[0] * ans[1])


if __name__ == "__main__":
    print(compute())
