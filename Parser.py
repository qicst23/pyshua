def parseArrayAndInt(file):
    for line in file:
        arrayString, intString = line.split('], ')
        a = [int(i) for i in arrayString.lstrip('[').split(',')]
        i = int(intString)
        yield a, i


def parseTwoInt(file):
    for line in file:
        i, j = [int(x) for x in line.split(', ')]
        yield i, j


def parseTwoArrays(file):
    for line in file:
        a, b = line.split('], [')
        a = a.lstrip('[')
        b = b.rstrip(']\n')
        if a == '':
            a = []
        else:
            a = [int(i) for i in a.split(',')]
        if b == '':
            b = []
        else:
            b = [int(i) for i in b.split(',')]
        yield a, b


def parseOneFloat(file):
    for line in file:
        f = float(line)
        yield f


def parseOneInt(file):
    for line in file:
        yield int(line)


def parseString(file):
    for line in file:
        yield line.rstrip('\n')[1:-1],
