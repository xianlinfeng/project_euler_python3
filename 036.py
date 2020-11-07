import eulerlib


if __name__ == "__main__":
    ans = sum(i for i in range(1, 1000000) if eulerlib.is_palindrome(
        i) and eulerlib.is_palindrome(i, 2))
    print(ans)
