class SingleLinkedListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        array = []
        cur = self
        while cur:
            array.append(cur.val)
            cur = cur.next
        return '{' + ', '.join([str(val) for val in array]) + '}'
