if __name__ == "__main__":
    for i in range(1, 1000):
        for j in range(i, 1000):
            for k in range(j, 1000):
                if i+j+k == 1000 and i*i + j*j == k*k:
                    print(i*j*k)
