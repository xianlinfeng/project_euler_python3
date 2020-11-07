import math


def compute():
    ans = sum(i for i in range(10000) if product(i))
    return str(ans)


def product(n):
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n//i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False


if __name__ == "__main__":
    print(compute())
