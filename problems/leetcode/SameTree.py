from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SameTree(LeetcodeProblem):
    def solve(self, p, q):
        if p and q:
            return (
                p.val == q.val and
                self.solve(p.left, q.left) and
                self.solve(p.right, q.right)
            )
        elif p or q:
            return False
        else:
            return True

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoBinaryTree
        return parseTwoBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = SameTree
