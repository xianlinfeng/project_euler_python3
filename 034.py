import math
from math import factorial


def compute():
    ans = sum(i for i in range(3, 999999) if i == sum(
        math.factorial(int(j)) for j in str(i)))
    return ans


if __name__ == "__main__":
    print(compute())
