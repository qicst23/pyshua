def parseArrayAndInt(file):
    for line in file:
        arrayString, intString = line.split('], ')
        a = []
        arrayString = arrayString.lstrip('[')
        if arrayString != '':
            a = [int(i) for i in arrayString.split(',')]
        i = int(intString)
        yield a, i


def parseTwoIntArray(file):
    for line in file:
        a1S, a2S = line.rstrip('\n')[1:-1].split('], [')

        a1 = []
        if a1S != '':
            a1 = [int(s) for s in a1S.split(',')]

        a2 = []
        if a2S != '':
            a2 = [int(s) for s in a2S.split(',')]

        yield a1, a2


def parseIntArrayArraysAndInt(file):
    for line in file:
        stringAA, stringI = line.split('], ')

        stringI = stringI.rstrip('\n')
        intI = int(stringI)

        stringAA = stringAA.strip('[]').split('],[')
        intAA = []
        if stringAA != ['']:
            for sa in stringAA:
                ia = [int(i) for i in sa.split(',')]
                intAA.append(ia)
        yield intAA, intI


def parseIntArrayArraysAndIntArray(file):
    for line in file:
        stringAA, stringA = line.split('], ')

        stringA = stringA.rstrip(']\n').lstrip('[')
        intA = []
        if stringA != '':
            intA = [int(s) for s in stringA.split(',')]

        stringAA = stringAA.strip('[]').split('],[')
        intAA = []
        if stringAA != ['']:
            for sa in stringAA:
                ia = [int(i) for i in sa.split(',')]
                intAA.append(ia)
        yield intAA, intA


def parseStringAndInt(file):
    for line in file:
        s, i = line.split('", ')
        s = s.lstrip('"')
        i = int(i.rstrip('\n'))
        yield s, i


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


def parseOneFloatAndOneInt(file):
    for line in file:
        fS, iS = line.rstrip('\n').split(', ')
        yield float(fS), int(iS)


def parseString(file):
    for line in file:
        yield line.rstrip('\n')[1:-1],


def parseCylicDescription(file):
    for line in file:
        yield line.rstrip('\n'),


def parseTwoStrings(file):
    for line in file:
        s1, s2 = line.split('", "')
        yield s1[1:], s2.strip('\n')[:-1]


def parseThreeStrings(file):
    for line in file:
        s1, s2, s3 = line.split('", "')
        yield s1[1:], s2, s3.rstrip('\n')[:-1]


def parseSingleLinkedList(file):
    from DataStructure.Utils import arrayToSingleLinkedList
    for line in file:
        line = line.strip('{}\n')
        array = []
        if line != '':
            array = [int(i) for i in line.split(',')]
        yield arrayToSingleLinkedList(array),


def parseCyclicSingleLinkedList(file):
    from DataStructure.Utils import arrayToSingleLinkedList
    for line in file:
        line = line.rstrip('\n')
        listS, cycleS = line.split(', ')

        listS = listS.strip('{}')
        array = []
        if listS != '':
            array = [int(i) for i in listS.split(',')]
        head = arrayToSingleLinkedList(array)

        if cycleS != 'no cycle':
            i = int(cycleS[-1])
            cur = head
            for j in xrange(i):
                cur = cur.next
            ith = cur
            while cur.next:
                cur = cur.next
            tail = cur
            tail.next = ith
        yield head,


def parseSingleLinkedListAndOneInt(file):
    from DataStructure.Utils import arrayToSingleLinkedList
    for line in file:
        listS, iS = line.split('}, ')

        i1 = int(iS.rstrip('\n'))

        listS = listS.strip('{}')
        array = []
        if listS != '':
            array = [int(i) for i in listS.split(',')]
        yield arrayToSingleLinkedList(array), i1


def parseSingleLinkedListAndTwoInt(file):
    from DataStructure.Utils import arrayToSingleLinkedList
    for line in file:
        listS, twoIntS = line.split('}, ')

        i1, i2 = [int(s) for s in twoIntS.rstrip('\n').split(', ')]

        listS = listS.strip('{}')
        array = []
        if listS != '':
            array = [int(i) for i in listS.split(',')]
        yield arrayToSingleLinkedList(array), i1, i2


def parseSingleLinkedListArray(file):
    from DataStructure.Utils import arrayToSingleLinkedList
    for line in file:
        line = line[1:-2]
        array = []
        if line != '':
            arrayString = line.split('},{')
            for linkedListString in arrayString:
                linkedList = None
                linkedListString = linkedListString.strip('{}')
                if linkedListString != '':
                    linkedList = arrayToSingleLinkedList(
                        [int(i) for i in linkedListString.split(',')]
                    )
                array.append(linkedList)
        yield array,


def parseSingleLinkedListAndInt(file):
    from DataStructure.Utils import arrayToSingleLinkedList
    for line in file:
        linkedListString, iString = line.split(', ')

        iString = iString.rstrip('\n')
        i = int(iString)

        linkedListString = linkedListString[1:-1]
        array = []
        if linkedListString != '':
            array = [int(j) for j in linkedListString.split(',')]

        yield arrayToSingleLinkedList(array), i


def parseTwoSingleLinkedList(file):
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


def parseBinaryTree(file):
    from DataStructure.Utils import arrayToBinaryTree
    for line in file:
        line = line.strip('{}\n')
        nodeArray = line.split(',')
        if nodeArray[0] == '':
            nodeArray = []
        root = arrayToBinaryTree(nodeArray)
        yield root,


def parseTwoBinaryTree(file):
    from DataStructure.Utils import arrayToBinaryTree
    for line in file:
        t1S, t2S = line.rstrip('\n').split('}, {')

        t1S = t1S[1:]
        t1NodeArray = t1S.split(',')
        if t1NodeArray[0] == '':
            t1NodeArray = []
        t1 = arrayToBinaryTree(t1NodeArray)

        t2S = t2S[:-1]
        t2NodeArray = t2S.split(',')
        if t2NodeArray[0] == '':
            t2NodeArray = []
        t2 = arrayToBinaryTree(t2NodeArray)
        yield t1, t2


def parseBinaryTreeArray(file):
    from DataStructure.Utils import arrayToBinaryTree
    for line in file:
        line = line.strip('[{}]\n')
        array = []
        if line != '':
            bStringArray = line.split('},{')
            for s in bStringArray:
                a = []
                if s != '':
                    a = s.split(',')
                array.append(arrayToBinaryTree(a))
        yield array,


def parseBinaryTreeAndInt(file):
    from DataStructure.Utils import arrayToBinaryTree
    for line in file:
        arrayString, iString = line.split('}, ')
        i = int(iString.rstrip('\n'))
        array = arrayString.lstrip('{').split(',')
        if array[0] == '':
            array = []
        root = arrayToBinaryTree(array)
        yield root, i


def parseBoolean(file):
    for line in file:
        line = line.rstrip('\n')
        yield line == 'true',


def parseIntArrayArrays(file):
    for line in file:
        stringAA = line.lstrip('[').rstrip(']\n').split('],[')
        intAA = []
        if stringAA != ['']:
            for sa in stringAA:
                ia = [int(i) for i in sa.split(',')] if sa != '' else []
                intAA.append(ia)
        yield intAA,


def parseIntArray(file):
    for line in file:
        line = line.strip('[]\n')
        array = []
        if line != '':
            array = [int(i) for i in line.split(',')]
        yield array,


def parseStringOrNull(file):
    for line in file:
        line = line.rstrip('\n')
        s = None
        if line != 'null':
            s = line[1:-1]
        yield s,


def parseStringArray(file):
    for line in file:
        line = line.strip('[]\n')
        array = []
        if line != '':
            array = [s for s in line[1:-1].split('","')]
        yield array,


def parseStringArrayArrays(file):
    for line in file:
        stringAA = line.lstrip('[').rstrip(']\n').split('],[')
        array = []
        if stringAA != ['']:
            for sa in stringAA:
                array.append([s[1:-1] for s in sa.split(',')])
        yield array,


def parseStringArrayAndInt(file):
    for line in file:
        aS, iS = line.rstrip('\n').split(', ')

        i = int(iS)

        aS = aS[1:-1]
        a = []
        if aS != '':
            a = [s for s in aS[1:-1].split('","')]

        yield a, i


def parseStringAndStringArray(file):
    for line in file:
        sString, arrayString = line.split(', [')
        s = sString[1:-1]
        arrayString = arrayString[:-2]  # remove \n and ]
        array = []
        if arrayString != '':
            array = [sString[1:-1] for sString in arrayString.split(',')]
        yield s, array


def parseStringArrayAndString(file):
    for line in file:
        arrayString, sString = line.split('], ')

        s = sString[1:-2]

        arrayString = arrayString[1:]  # remove [
        array = []
        if arrayString != '':
            array = [sString[1:-1] for sString in arrayString.split(',')]

        yield array, s


def parseTwoStringAndStringArray(file):
    for line in file:
        twoString, arrayString = line.split(', [')
        s1, s2 = [s.strip('"') for s in twoString.split('", "')]
        arrayString = arrayString[:-2]  # remove \n and ]
        array = []
        if arrayString != '':
            array = [sString[1:-1] for sString in arrayString.split(',')]
        yield s1, s2, array


def parseGraph(file):
    from DataStructure.Graph import UndirectedGraphNode
    for line in file:
        line = line.rstrip('\n')[1:-1]

        root = None
        if line != '':
            nodesIntRepr = [map(int, s.split(',')) for s in line.split('#')]

            nodesIntMap = {}
            for intRepr in nodesIntRepr:
                label = intRepr[0]
                nodesIntMap[label] = UndirectedGraphNode(label)

            for intRepr in nodesIntRepr:
                label = intRepr[0]
                node = nodesIntMap[label]

                node.neighbors = [nodesIntMap[l] for l in intRepr[1:]]

                root = nodesIntMap[nodesIntRepr[0][0]]

        yield root,
