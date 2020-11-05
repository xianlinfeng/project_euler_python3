
def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3*n + 1)


if __name__ == "__main__":
    k, m = 0, 0
    for i in range(2, 1000000):
        r = [1]
        j = i
        while j != 1:
            r.append(j)
            j = collatz(j)
        if len(r) > m:
            m = len(r)
            k = i
    print(k, m)
