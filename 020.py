import math

if __name__ == "__main__":
    n = math.factorial(100)
    ans = sum(int(i) for i in str(n))
    print(ans)
