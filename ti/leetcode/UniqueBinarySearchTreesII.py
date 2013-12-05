from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class UniqueBinarySearchTreesII(LeetcodeProblem):
    def solve(self, n):
        res = self.build(1, n)
        return res

    def build(self, low, high):
        from DataStructure.TreeNode import TreeNode

        res = []
        if low > high:
            res.append(None)
        else:
            for rootVal in xrange(low, high + 1):
                for left in self.build(low, rootVal - 1):
                    for right in self.build(rootVal + 1, high):
                        root = TreeNode(rootVal, left, right)
                        res.append(root)
        return res

    def verify(self, input, s1, s2):
        from DataStructure.Utils import sameTree
        for b1, b2 in zip(s1, s2):
            if not sameTree(b1, b2):
                return False
        return True

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseBinaryTreeArray
        for o in parseBinaryTreeArray(open(self.outputPath)):
            yield o[0]

problem = UniqueBinarySearchTreesII
