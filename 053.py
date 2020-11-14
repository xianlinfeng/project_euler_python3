from math import factorial
import eulerlib


def combination(n: int, r: int):
    return factorial(n)//(factorial(r)*factorial(n-r))


if __name__ == "__main__":
    count = 0
    for r in range(1, 101):
        for n in range(r, 101):
            if combination(n, r) > 1000000:
                count += 1
    print(count)
