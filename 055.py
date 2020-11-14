import eulerlib

# eulerlib.is_palindrome()


def addPalin(n):
    return n + int(str(n)[::-1])


if __name__ == "__main__":
    count = 0
    for n in range(1, 10000):
        ret = n
        for i in range(50):
            ret = addPalin(ret)
            if eulerlib.is_palindrome(ret):
                break
        else:
            count += 1
    print(count)
