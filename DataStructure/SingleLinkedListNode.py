class SingleLinkedListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __hash__(self):
        return id(self)

    def __repr__(self):
        array = []
        record = set()
        cyclicInfo = ''
        cur = self
        while cur:
            if cur not in record:
                record.add(cur)
                array.append(cur)
                cur = cur.next
            else:
                cyclicInfo = ''.join([
                    ' --- tail connects to node index ',
                    str(array.index(cur))
                ])
                break
        return ''.join([
            '{',
            ', '.join([str(node.val) for node in array]),
            '}',
            cyclicInfo
        ])
