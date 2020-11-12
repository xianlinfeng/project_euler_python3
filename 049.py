import eulerlib


def compute():
    for a in range(1000, 9999):
        for step in range(1, 8999):
            if sorted(str(a)) == sorted(str(a + step)) == sorted(str(a + step * 2)):
                if eulerlib.is_prime(a) and eulerlib.is_prime(a+step) and eulerlib.is_prime(a + step * 2):
                    if a != 1487:
                        print(str(a)+str(a + step)+str(a + step * 2))
                        return
    return "not found"


if __name__ == "__main__":
    compute()
