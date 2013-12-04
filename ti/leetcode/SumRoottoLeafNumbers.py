from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class SumRoottoLeafNumbers(LeetcodeProblem):
    def solve(self, root):
        self.res = 0
        self.go(root, 0)
        return self.res

    def go(self, node, s):
        if node:
            s = s * 10 + node.val
            if node.left and node.right:
                self.go(node.left, s)
                self.go(node.right, s)
            elif node.left or node.right:
                self.go(node.left or node.right, s)
            else:
                self.res += s

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = SumRoottoLeafNumbers
