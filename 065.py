def compute():
    numer = 1  # 分子
    denom = 0  # 分母
    for i in range(100):
        numer, denom = e_contfrac_term(i) * numer + denom, numer
        # this formula can only meet the specification of the molecular(分子)，
        # we cannot use this formula to get the right value of Denominator
    ans = sum(int(c) for c in str(numer))
    return str(ans)


def e_contfrac_term(i):
    if i == 0:
        return 2
    elif i % 3 == 2:
        return i // 3 * 2 + 2
    else:
        return 1


if __name__ == "__main__":
    print(compute())
