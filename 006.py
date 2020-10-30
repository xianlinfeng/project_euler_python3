import math

if __name__ == "__main__":
    sum = 0
    sumSquare = 0
    for i in range(1, 101):
        sum += i
        sumSquare += i**2
    squareSum = sum ** 2
    difference = abs(squareSum - sumSquare)
    print(difference)
