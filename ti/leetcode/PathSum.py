from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class PathSum(LeetcodeProblem):
    def solve(self, root, target):
        cur = root
        stack = []
        pathSum = 0
        while stack or cur:
            if cur:
                pathSum += cur.val
                if pathSum == target and not cur.left and not cur.right:
                    return True
                stack.append((cur, pathSum))
                cur = cur.left
            else:
                cur, pathSum = stack.pop()
                cur = cur.right

        return False

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTreeAndInt
        return parseBinaryTreeAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = PathSum
