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
        yield f,


def parseOneInt(file):
    for line in file:
        yield int(line),


def parseString(file):
    for line in file:
        yield line.rstrip('\n')[1:-1],


def parseSingleLinkedList(file):
    from DataStructure.SingleLinkedListNode import SingleLinkedListNode
    from DataStructure.Utils import arrayToSingleLinkedList
    for line in file:
        array = [int(i) for i in line.strip('{}\n').split(',')]
        yield arrayToSingleLinkedList(array),


def parseTwoSingleLinkedList(file):
    from DataStructure.SingleLinkedListNode import SingleLinkedListNode
    from DataStructure.Utils import arrayToSingleLinkedList
    for line in file:
        a1, a2 = line.split('}, {')
        a1 = a1.lstrip('{')
        if a1 == '':
            l1 = None
        else:
            l1 = arrayToSingleLinkedList([int(x) for x in a1.split(',')])

        a2 = a2.rstrip('}\n')
        if a2 == '':
            l2 = None
        else:
            l2 = arrayToSingleLinkedList([int(x) for x in a2.split(',')])
        yield l1, l2


def parseTupleList(file):
    for line in file:
        line = line.strip('[]\n')
        a = []
        if line != '':
            tupleStringList = [ts.strip('()') for ts in line.split('),(')]
            a = [tuple(
                [int(i) for i in ts.split(',')]) for ts in tupleStringList]
        yield a,
