import eulerlib


if __name__ == "__main__":
    nums = [0]
    primes = []
    for i in range(1, 100000):
        pivot = i * 2 + 1
        for j in range(4):
            n = pivot**2 - i*j*2
            nums.append(n)
            if eulerlib.is_prime(n):
                primes.append(n)
        print(len(primes)/len(nums))
        if len(primes)/len(nums) < 0.1:
            print(pivot)
            break
