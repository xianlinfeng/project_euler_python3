import eulerlib


primes = list(i for i in range(9999) if eulerlib.is_prime(i))


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


def test_getFactors():
    assert getFactors(230) == {2, 5, 23}
    assert getFactors(231) == {11, 3, 7}
    assert getFactors(232) == {2, 29}
    assert getFactors(644) == {2, 23, 7}


def test_getLenFactors():
    assert getLenFactors(14) == 2
    assert getLenFactors(15) == 2
    assert getLenFactors(230) == 3
    assert getLenFactors(231) == 3
    assert getLenFactors(232) == 2
    assert getLenFactors(644) == 3
    assert getLenFactors(646) == 3
    assert getLenFactors(646) == 3
