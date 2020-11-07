def compute():
    ans = 1
    for i in range(1, 10):
        for j in range(1, i):
            for k in range(1, i):
                ki = k*10 + i
                ij = i*10 + j
                if ki * j == ij * k:
                    ans *= ij / ki
    return int(ans)


if __name__ == "__main__":
    print(compute())
