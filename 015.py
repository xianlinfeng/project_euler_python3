def move(i, j):
    if i == 20 or j == 20:
        return 1
    else:
        return move(i+1, j) + move(i, j+1)


if __name__ == "__main__":
    print(move(0, 0))
