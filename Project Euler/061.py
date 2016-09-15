# https://projecteuler.net/problem=61

class Chain:
    def __init__(self, chain, product):
        self.chain = chain
        self.product = product
        self.firstTwo = chain[0] / 100
        self.lastTwo = chain[-1] % 100

    def __str__(self):
        return self.chain.__str__()

    def __repr__(self):
        return self.__str__()


def addToDic(dic, values):
    keys = [2, 3, 5, 7, 11, 13]
    if 1 not in dic:
        dic[1] = {}
    for index, value in enumerate(values):
        if 1000 <= value < 10000:
            if keys[index] in dic[1]:
                dic[1][keys[index]].append(Chain([value], keys[index]))
            else:
                dic[1][keys[index]] = [Chain([value], keys[index])]


'''

'''
def getValidNumbers():
    # 19 is the point below which the largest function, octagonal, yields 3-digit numbers
    i = 19
    dic = {}

    # 141 is the point above which the smallest function, triangular, yields 5-digit numbers
    while i < 142:
        values = []
        values.append(i*(i + 1)/2)    # triangular
        values.append(i*i)            # square
        values.append(i*(3*i - 1)/2)  # pentagonal
        values.append(i*(2*i - 1))    # hexagonal
        values.append(i*(5*i- 3)/2)   # heptagonal
        values.append(i*(3*i - 2))    # octagonal
        addToDic(dic, values)
        i += 1
    return dic

'''

'''
def buildChains():
    return None


'''

'''
def cyclicalFigurate():
    dic = getValidNumbers()
    print dic


cyclicalFigurate()
