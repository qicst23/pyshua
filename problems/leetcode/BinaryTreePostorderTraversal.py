from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class BinaryTreePostorderTraversal(LeetcodeProblem):
    def solve(self, root):
        if not root:
            return []

        res = []
        stack = [root]
        pre = None
        cur = root
        while stack:
            cur = stack[-1]
            if not pre or pre.left == cur or pre.right == cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
            elif cur.left == pre:
                if cur.right:
                    stack.append(cur.right)
            else:
                res.append(cur.val)
                cur = stack.pop()
            pre = cur
        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = BinaryTreePostorderTraversal
