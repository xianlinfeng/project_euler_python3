
import itertools


primes = [2, 3, 5, 7, 11, 13, 17]


def is_substring_divisible(num):
    return all((num[i+1]*100 + num[i+2]*10 + num[i+3]) % p == 0 for (i, p) in enumerate(primes))


if __name__ == "__main__":
    ans = sum(int("".join(map(str, num)))
              for num in itertools.permutations(list(range(10)))
              if is_substring_divisible(num))
    print(ans)
