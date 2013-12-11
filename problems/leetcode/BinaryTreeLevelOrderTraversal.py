from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class BinaryTreeLevelOrderTraversal(LeetcodeProblem):
    def solve(self, root):
        if not root:
            return []

        nodes = []
        lastLevel = [root]
        while lastLevel:
            nodes.append(lastLevel)
            nextLevel = []
            for node in lastLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            lastLevel = nextLevel

        return [map(lambda n: n.val, level) for level in nodes]

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = BinaryTreeLevelOrderTraversal
