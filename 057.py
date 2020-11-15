from typing import Counter


if __name__ == "__main__":
    a, b = 3, 2
    count = 0
    for n in range(0, 1000):
        # print(a, b)
        if len(str(a)) > len(str(b)):
            count += 1
        a, b = a+2*b, a+b
    print(count)
