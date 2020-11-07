import eulerlib


def is_circular_prime(n):
    s = str(n)
    return all(eulerlib.is_prime(int(s[i:] + s[:i])) for i in range(len(s)))


def compute():
    ans = sum(1 for i in range(1, 1000000) if is_circular_prime(i))
    return ans


if __name__ == "__main__":
    print(compute())
