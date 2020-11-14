import itertools

if __name__ == "__main__":
    for x in itertools.count(1):
        if sorted(str(x)) == sorted(str(2*x)) == sorted(str(3*x)) == sorted(str(4*x)) == sorted(str(5*x)) == sorted(str(6*x)):
            print(x)
            break
