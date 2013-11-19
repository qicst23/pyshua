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
