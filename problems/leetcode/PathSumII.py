from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class PathSumII(LeetcodeProblem):
    def solve(self, root, target):
        res = []
        self.go(root, [], target, res)
        return res

    def go(self, node, path, target, res):
        if node:
            path.append(node.val)
            if node.val == target and not node.left and not node.right:
                res.append(path[:])
            else:
                self.go(node.left, path, target - node.val, res)
                self.go(node.right, path, target - node.val, res)
            path.pop()

    def verify(self, original_input, input, s1, s2):
        s1.sort()
        s2.sort()
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTreeAndInt
        return parseBinaryTreeAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = PathSumII
