
l3 = list(filter(lambda x: 1000 <= x <= 9999, list(int(n * (n + 1)/2)
                                                   for n in range(9999))))

l4 = list(filter(lambda x: 1000 <= x <= 9999, list(int(n*n)
                                                   for n in range(9999))))

l5 = list(filter(lambda x: 1000 <= x <= 9999, list(int(n * (3 * n - 1)/2)
                                                   for n in range(9999))))

l6 = list(filter(lambda x: 1000 <= x <= 9999, list(n*(2*n - 1)
                                                   for n in range(9999))))

l7 = list(filter(lambda x: 1000 <= x <= 9999, list(int(n*(5*n-3)/2)
                                                   for n in range(9999))))

l8 = list(filter(lambda x: 1000 <= x <= 9999, list(n*(3*n - 2)
                                                   for n in range(9999))))


def getShareDigits(a, b: list):
    la = sorted(set(int(str(x)[-2:]) for x in a))
    lb = sorted(set(filter(lambda x: len(str(x)) == 2,
                           list(int(str(x)[:2]) for x in b))))
    return list(set(la) & set(lb))


# print(getShareDigits(l3, l5))
# print(getShareDigits(l4, l3))
# print(getShareDigits(l5, l4))
s35 = getShareDigits(l3, l5)
s43 = getShareDigits(l4, l3)
s54 = getShareDigits(l5, l4)


def combin(s1, s2, d1: list):
    ret = []
    for i in s1:
        for j in s2:
            n = int(str(i)+str(j))
            if n in d1:
                ret.append(n)
    return ret


print(s43)
print(s35)
print(combin(s43, s35, l3))


# def compute(pool):
#     for a in pool:
#         selected = []
#         selected.append(a.belong)
#         for b in pool:
#             if isMatch(a, b) and b.belong not in selected:
#                 selected.append(b.belong)
#                 for c in pool:
#                     if isMatch(b, c) and c.belong not in selected:
#                         selected.append(c.belong)
#                         print(a, b, c)
#                         for d in pool:
#                             if isMatch(c, d) and d.belong not in selected:
#                                 selected.append(d.belong)
#                                 print(a, b, c, d)
#                                 for e in pool:
#                                     if isMatch(d, e) and e.belong not in selected:
#                                         selected.append(e.belong)
#                                         print(a, b, c, d, e)
#                                         for f in pool:
#                                             if isMatch(e, f) and isMatch(f, a) and f.belong not in selected:
#                                                 selected.append(f.belong)
#                                                 print(a, b, c, d, e, f)
#                                                 return
