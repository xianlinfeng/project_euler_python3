import eulerlib


def is_truncatable_primes(n):
    s = str(n)
    # for i in range(len(s)):
    #     if not eulerlib.is_prime(int(s[i:])):
    #         return False
    #     if i >= 1 and not eulerlib.is_prime(int(s[:i])):
    #         return False
    # return True
    return all(eulerlib.is_prime(int(s[i:])) for i in range(len(s))) and all(eulerlib.is_prime(int(s[:i])) for i in range(1, len(s)))


if __name__ == "__main__":
    ans = sum(i for i in range(10, 1000000) if is_truncatable_primes(i))
    print(ans)
    # print(is_truncatable_primes(3797))
