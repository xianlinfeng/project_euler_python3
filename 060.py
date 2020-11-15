import itertools
import eulerlib


def compute():
    """
        this is an three-step work flow. 
    """
    primes = eulerlib.primes(
        10000)  # a guess of maximum prime number in the answer
    primes.remove(2)  # 2,5 is invalid in the end of a prime number
    primes.remove(5)

    # step 1: generate two number of primes, which meat the requiement of the problem, such as [3, 7, 109], [3, 7, 229], [3, 7, 541]
    for l1 in itertools.combinations(primes, 3):
        threePrimes = all(eulerlib.is_prime(int("".join(str(x) for x in j)))
                          for j in itertools.permutations(l1, 2))
        # step 2: add another prime number in the previous result, and verify it to generate three elements list, such as [3, 7, 109, 673], [3, 7, 541, 4159], [3, 11, 701, 8747]
        if threePrimes:
            print(l1)
            for i in primes:
                if i > max(l1):
                    l2 = list(l1)
                    l2.append(i)
                    fourPrimes = all(eulerlib.is_prime(int("".join(str(x) for x in j)))
                                     for j in itertools.permutations(l2, 2))
                    # step 3: same as step two, add another prime into the previous list which is generated in step two. the result is [13, 5197, 5701, 6733, 8389], takes 2m34s in 2019 macbook pro.
                    if fourPrimes:
                        print(l2)
                        for j in primes:
                            if j > max(l2):
                                l3 = list(l2)
                                l3.append(j)
                                fourPrimes = all(eulerlib.is_prime(int("".join(str(x) for x in j)))
                                                 for j in itertools.permutations(l3, 2))
                                if fourPrimes:
                                    print(l3)
                                    return
    print("done")


if __name__ == "__main__":
    compute()
    # answer = 26033 where list = [13, 5197, 5701, 6733, 8389]
