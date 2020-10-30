def isPalindromic(n):
    """
    A palindromic number reads the same both ways. such as 9009
    """
    s = str(n)
    r = s[::-1]
    if s == r:
        return True
    else:
        return False


if __name__ == "__main__":
    max = 0
    for i in range(100, 999):
        for j in range(100, 999):
            p = i*j
            if isPalindromic(p):
                if p > max:
                    max = p
    print(max)
