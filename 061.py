import itertools


class Number:
    """
    class to store a middle-stage data 
    """

    def __init__(self, start, belong, end, value):
        """
        docstring
        """
        self.start = start      # the previous list which share the first two digits with self.value
        self.belong = belong    # the self.value is belong to which list
        self.end = end          # the after list which share the last two digits with self.value
        self.value = value      # the value of the number

    def __str__(self):
        return '%s,%s,%s : %d' % (self.start, self.belong, self.end, self.value)


def prepareData():
    # Triangle Numbers:
    l3 = list(filter(lambda x: 1000 <= x <= 9999, list(int(n * (n + 1)/2)
                                                       for n in range(9999))))
    # Square Numbers:
    l4 = list(filter(lambda x: 1000 <= x <= 9999, list(int(n*n)
                                                       for n in range(9999))))
    # Pentagonal Numbers:
    l5 = list(filter(lambda x: 1000 <= x <= 9999, list(int(n * (3 * n - 1)/2)
                                                       for n in range(9999))))
    # Hexagonal Numbers:
    l6 = list(filter(lambda x: 1000 <= x <= 9999, list(n*(2*n - 1)
                                                       for n in range(9999))))
    # Heptagonal Numbers:
    l7 = list(filter(lambda x: 1000 <= x <= 9999, list(int(n*(5*n-3)/2)
                                                       for n in range(9999))))
    # Octagonal Numbers:
    l8 = list(filter(lambda x: 1000 <= x <= 9999, list(n*(3*n - 2)
                                                       for n in range(9999))))
    data = {}
    data['l3'] = l3
    data['l4'] = l4
    data['l5'] = l5
    data['l6'] = l6
    data['l7'] = l7
    data['l8'] = l8
    return data  # the original data collection to be computed


def getShareDigits(a, b: list):
    """
    from two list find the shared two digits between last two digits of a and first two digits of b 
    """
    la = sorted(set(int(str(x)[-2:]) for x in a))
    lb = sorted(set(filter(lambda x: len(str(x)) == 2,
                           list(int(str(x)[:2]) for x in b))))
    return list(set(la) & set(lb))  # set intersection


def combin(s1, s2, d1: list):
    """
    combine two shared list(every element has two digits) into four-digits integer, and return them if the integer is in the list of d1
    """
    ret = []
    for i in s1:
        for j in s2:
            n = int(str(i)+str(j))
            if n in d1:
                ret.append(n)
    return ret


def dataFilter(data):
    """
    filter the original dataset, find the data which shared both head and tail with other list,and store them as the object of Number class in the list named "collect"
    """
    collect = []
    for d in itertools.permutations(data, 3):  # pertutate the original dataset
        # print(d) == ('l3', 'l4', 'l5')
        k1 = d[0]
        v1 = data[k1]
        k2 = d[1]
        v2 = data[k2]
        k3 = d[2]
        v3 = data[k3]

        s12 = getShareDigits(v1, v2)
        s23 = getShareDigits(v2, v3)

        ret2 = combin(s12, s23, v2)
        for r in ret2:
            num = Number(k1, k2, k3, r)
            collect.append(num)
    return collect
    # print the tmp collect
    # for c in collect:
    #     print(c)  # l3,l4,l7 : 5625


def isMatch(n1: Number, n2: Number):
    """
    check if two Number object is math, here is an example
    l3,l4,l7 : 5625 
    l4,l7,l8 : 2512
    """
    s1 = str(n1.value)
    s2 = str(n2.value)
    if n1.belong == n2.start and n1.end == n2.belong and s1[-2:] == s2[:2]:
        return True
    return False


def compute(pool):
    answers = []  # used to store the result to return
    selected = []   # used to store the Number.belong which has being selected to avoid double select
    for a in pool:
        selected.clear()    # clear it every new begining
        selected.append(a.belong)   # add a into selected
        print(a)
        for b in pool:
            # if a and b matched and b.belong is not in selected
            if isMatch(a, b) and b.belong not in selected:
                selected.append(b.belong)  # add b.belong into selected
                print(a, b)
                for c in pool:   # the same logic with b until we find six answers
                    if isMatch(b, c) and c.belong not in selected:
                        selected.append(c.belong)
                        print(a, b, c)
                        for d in pool:
                            if isMatch(c, d) and d.belong not in selected:
                                selected.append(d.belong)
                                print(a, b, c, d)
                                for e in pool:
                                    if isMatch(d, e) and e.belong not in selected:
                                        selected.append(e.belong)
                                        print(a, b, c, d, e)
                                        for f in pool:
                                            if isMatch(e, f) and isMatch(f, a) and f.belong not in selected:
                                                print(a, b, c, d, e, f)
                                                answers.extend(
                                                    [a, b, c, d, e, f])
                                                return answers
                                        # also need to remove them when this iteration is finished
                                        selected.remove(e.belong)
                                selected.remove(d.belong)
                        selected.remove(c.belong)
                selected.remove(b.belong)


if __name__ == "__main__":
    data = prepareData()    # get the original dataset
    collect = dataFilter(data)  # filter the data
    ans = compute(collect)  # find the integers we need
    sum = sum(a.value for a in ans)  # add them together
    print(sum)
