import itertools
import math


count = 0
for i in range(1, 100):
    for j in range(1, 100):
        l = len(str(i**j))
        if l == j:
            count += 1
            print("count %d: %d ** %d with length %d " % (count, i, j, l))
print(count)
