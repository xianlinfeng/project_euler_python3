
def sumDigits(n: int):
    ans = sum(int(x) for x in str(n))
    return ans


if __name__ == "__main__":
    m = 0
    for a in range(1, 100):
        for b in range(1, 100):
            ans = sumDigits(a ** b)
            if ans > m:
                m = ans
    print(m)
