class UndirectedGraphNode(object):
    def __init__(self, label):
        self.label = label
        self.neighbors = []

    def __str__(self):
        return ','.join(
            map(
                str,
                [self.label] + [n.label for n in self.neighbors]
            )
        )

    def __repr__(self):
        queue = [self]
        nodeStrings = []
        visited = set()
        while queue:
            node = queue.pop(0)
            visited.add(node.label)
            nodeStrings.append(str(node))
            for n in node.neighbors:
                if n.label not in visited:
                    queue.append(n)

        return '#'.join(nodeStrings)
