def parseArrayAndIntInput(file):
    for line in file:
        arrayString, intString = line.split('], ')
        a = [int(i) for i in arrayString.lstrip('[').split(',')]
        i = int(intString)
        yield a, i


def parseArrayAndIntOutput(file):
    for line in file:
        i, j = [int(x) for x in line.split(', ')]
        yield i, j
