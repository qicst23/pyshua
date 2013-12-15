class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        stringArray = []
        if self:
            lastLevel = [self]
            while lastLevel:
                nextLevel = []
                for node in lastLevel:
                    if node:
                        stringArray.append(str(node.val))
                        nextLevel.append(node.left)
                        nextLevel.append(node.right)
                    else:
                        stringArray.append('#')
                lastLevel = nextLevel
            lastIndex = -1
            for i, s in enumerate(stringArray):
                if s != '#':
                    lastIndex = i
        return '{' + ', '.join(stringArray[:lastIndex + 1]) + '}'


class TreeLinkNode(object):
    def __init__(self, x, left=None, right=None, next=None):
        self.val = x
        self.left = left
        self.right = right
        self.next = next
