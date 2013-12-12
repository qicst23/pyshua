from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class BinaryTreeLevelOrderTraversalII(LeetcodeProblem):
    def solve(self, root):
        if not root:
            return []

        res = []
        last = [root]
        while last:
            res.append(last)
            next = []
            for node in last:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            last = next

        return [[node.val for node in level] for level in reversed(res)]

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = BinaryTreeLevelOrderTraversalII
