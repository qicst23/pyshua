from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class ConvertSortedArraytoBinarySearchTree(LeetcodeProblem):
    def solve(self, num):
        return self.build(num, 0, len(num) - 1)

    def build(self, num, low, high):
        from DataStructure.TreeNode import TreeNode
        if low > high:
            return None
        middle = low + (high - low) / 2
        root = TreeNode(
            num[middle],
            self.build(num, low, middle - 1),
            self.build(num, middle + 1, high)
        )
        return root

    def verify(self, input, s1, s2):
        from DataStructure.Utils import sameTree
        return sameTree(s1, s2)

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseBinaryTree
        for o in parseBinaryTree(open(self.outputPath)):
            yield o[0]

problem = ConvertSortedArraytoBinarySearchTree
