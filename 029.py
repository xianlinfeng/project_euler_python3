def compute():
    ans = set(a**b for a in range(2, 101) for b in range(2, 101))
    return len(ans)


if __name__ == "__main__":
    print(compute())
