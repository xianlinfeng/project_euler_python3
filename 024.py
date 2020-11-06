import itertools


def next(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i-1] < nums[i]:
            _, j = min((v, j)
                       for (j, v) in enumerate(nums[i:]) if v > nums[i-1])
            nums[i-1], nums[i+j] = nums[i+j], nums[i-1]
            nums[i:] = sorted(nums[i:])
            return nums
        else:
            pass
    return None


def compute():
    """ method 2 """
    arr = list(range(10))
    temp = itertools.islice(itertools.permutations(arr), 999999, None)
    return "".join(str(x) for x in next(temp))


if __name__ == "__main__":
    List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1, 1000000):
        List = next(List)
    print(List)
