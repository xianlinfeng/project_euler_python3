import eulerlib
if __name__ == "__main__":
    ans = max(i for i in range(1234567, 7654322)
              if eulerlib.is_pandigital(i, 1, 7) and eulerlib.is_prime(i))
    print(ans)
