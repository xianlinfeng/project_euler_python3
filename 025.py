def compute():
    a = 1
    b = 1
    i = 1
    while True:
        if len(str(a)) == 1000:
            break
        a, b = b, a+b
        i += 1
    return i


if __name__ == "__main__":
    print(compute())
