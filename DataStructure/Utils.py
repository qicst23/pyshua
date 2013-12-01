def arrayToSingleLinkedList(array):
    from SingleLinkedListNode import SingleLinkedListNode
    head = None
    cur = None
    for x in array:
        node = SingleLinkedListNode(x)
        if not head:
            head = node
            cur = node
        else:
            cur.next = node
            cur = node
    return head


def arrayToBinaryTree(array):
    from TreeNode import TreeNode

    n = len(array)
    if n == 0:
        return None

    i = 0
    root = TreeNode(int(array[i]))
    i += 1
    lastLevel = [root]

    while lastLevel:
        nextLevel = []
        for node in lastLevel:
            if not node:
                continue
            if i < n:
                leftString = array[i]
                i += 1
                left = TreeNode(
                    int(leftString)) if leftString != '#' else None
                node.left = left
                nextLevel.append(left)

            if i < n:
                rightString = array[i]
                i += 1
                right = TreeNode(
                    int(rightString)) if rightString != '#' else None
                node.right = right
                nextLevel.append(right)
        lastLevel = nextLevel
    return root


def sameTree(t1, t2):
    # if t1 and t2:
    #     if t1.val != t2.val:
    #         return False
    #     return sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)
    # elif t1 or t2:
    #     return False
    # else:
    #     return True
    last1 = [t1]
    last2 = [t2]
    seenNode = True

    while seenNode:
        seenNode = False
        next1 = []
        next2 = []

        for n1, n2 in zip(last1, last2):
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                next1.append(n1.left)
                next1.append(n1.right)
                next2.append(n2.left)
                next2.append(n2.right)
                seenNode = seenNode or n1.left or n1.right
            elif n1 or n2:
                return False

        last1 = next1
        last2 = next2

    return True


def sameList(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    if l1 or l2:
        return False
    else:
        return True
