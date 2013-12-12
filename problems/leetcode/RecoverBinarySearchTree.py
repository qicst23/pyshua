from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class RecoverBinarySearchTree(LeetcodeProblem):
    def solve(self, root):
        self.earlier = self.later = None
        self.pre = None
        self.go(root)
        self.earlier.val, self.later.val = self.later.val, self.earlier.val
        return root

    def go(self, node):
        if node:
            self.go(node.left)
            if self.pre and self.pre.val > node.val:
                if not self.earlier:
                    self.earlier = self.pre
                self.later = node
            self.pre = node
            self.go(node.right)

    def verify(self, original_input, input, s1, s2):
        from DataStructure.Utils import sameTree
        return sameTree(s1, s2)

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseBinaryTree
        for o in parseBinaryTree(open(self.outputPath)):
            yield o[0]

problem = RecoverBinarySearchTree
