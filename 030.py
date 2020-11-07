def fifthPower(x): return sum(int(c)**5 for c in str(x))


def compute():
    # As stated in the problem, 1 = 1^5 is excluded.
    # If a number has at least n >= 7 digits, then even if every digit is 9,
    # n * 9^5 is still less than the number (which is at least 10^n).
    ans = sum(i for i in range(2, 1000000) if i == fifthPower(i))
    return str(ans)


if __name__ == "__main__":
    print(compute())
