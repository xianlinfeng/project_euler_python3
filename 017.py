digit = {
    1: 3,  # one
    2: 3,  # two
    3: 5,  # three
    4: 4,  # four
    5: 4,  # five
    6: 3,  # six
    7: 5,  # seven
    8: 5,  # eight
    9: 4  # nine
}

ten = {
    11: 6,  # eleven
    12: 6,  # twelve
    13: 8,  # thirteen
    14: 8,  # fourteen
    15: 7,  # fifteen
    16: 7,  # sixteen
    17: 9,  # seventeen
    18: 8,  # eighteen
    19: 8,  # nineteen
    1:  3,  # ten
    2:  6,  # twenty
    3:  6,  # thirty
    4:  5,  # forty
    5:  5,  # fifty
    6:  5,  # sixty
    7:  7,  # seventy
    8:  6,  # eighty
    9:  6,  # ninety
}


def getLetters(n):
    if n in digit:  # 1,2,3,4
        return digit[n]
    elif n in ten:  # 11, 12, 13 ,14
        return ten[n]
    elif n == 1000:
        return 3 + 8  # one thousand
    elif n % 100 == 0:  # 100, 200, 300
        return digit[n / 100] + 7  # hundred
    elif n > 100:  # 102, 120
        return digit[n / 100] + 7 + 3 + getLetters(n % 100)  # hundred and
    elif n % 10 == 0:
        return ten[n/10]  # 10, 20 ,30
    else:
        return ten[n/10] + digit[n % 10]  # 23


if __name__ == "__main__":
    sum = 0
    for i in range(1, 1001):
        sum += getLetters(i)
    print(sum)
