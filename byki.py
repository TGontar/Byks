def byks(a, b):
    a = list(str(a))
    b = list(str(b))
    if a[0] == '0':
        return 'Nelzya 0 v nacahle'
    if len(a) != 4:
        return 'Nuzhno 4 znachnoe chislo'
    for i in range(len(a)):
        if a.count(a[i]) >1:
            return 'Tsifri ne dolzhny povtoryatsa'
    byki = []
    korovi = []
    for i in range(len(a)):
        if a[i] == b[i]:
            byki.append([a[i], i])
            b[i] = 'bebra'
    for i in range(len(a)):
        k = [a[i], i]
        if (k not in byki) and (a[i] in b):
            korovi.append(a[i])
    if len(byki) == 4:
        return 'HAROSH TI POBEDIL'
    else:
        return 'Y vas ' + str(len(byki)) + ' bykov i ' + str(len(korovi)) + ' korov'


# import random
#
# numbers = random.sample(range(1, 10), 4)
# ans = ''.join(map(str, numbers))
# print(ans)
# print(byks(ans, 1234))
