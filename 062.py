import itertools

data = {}  # a dictionary to store the data
for i in itertools.count(1):
    s = "".join(sorted(str(i**3)))  # get the sorted result of i**3
    # add it into data
    if s in data:
        data[s] += 1
    else:
        data[s] = 1

    if data[s] == 5:  # achieve the target
        print("got the answer")
        for j in range(1, i):
            if "".join(sorted(str(j**3))) == "".join(sorted(str(i**3))):
                print(j**3)  # find the smallest one
                break
        break
