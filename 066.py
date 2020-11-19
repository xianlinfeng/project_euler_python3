import math
import itertools

square = list(x**2 for x in range(100))
l = list(filter(lambda x: x not in square, range(1001)))

# right answer = 661
# ret = []
# for d in l:
#     for x in range(2, 1000):
#         y = math.sqrt((x**2 - 1)/d)
#         # print("try:", x, y)
#         if x**2 - d * int(y)**2 == 1:
#             ret.append(x)
#             print(d, x, int(y))
#             break

# print(len(ret))
# print(max(ret))
