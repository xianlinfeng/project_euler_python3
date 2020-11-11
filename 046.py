import eulerlib
from eulerlib.prime_numbers import is_prime


if __name__ == "__main__":
    oddComposite = list(i for i in range(2, 10000) if i %
                        2 != 0 and not eulerlib.is_prime(i))
    primes = list(i for i in range(2, max(oddComposite))
                  if eulerlib.is_prime(i))
    for i in oddComposite:
        equl = any((j, k)for j in primes
                   for k in range(1, i//2) if j < i and i == j + 2 * k * k)
        if not equl:
            print(i)
            break
