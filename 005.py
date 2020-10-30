
if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    s = 1
    m = 1
    for i in range(1, 21):
        if i in primes:
            s *= i
            m *= i
        elif m % i == 0:
            pass
        elif m % i != 0:
            j = m
            while True:
                j += s
                if j % i == 0:
                    m = j
                    s = j
                    break
    print(m)
