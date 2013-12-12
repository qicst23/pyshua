from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class BinaryTreeZigzagLevelOrderTraversal(LeetcodeProblem):
    def solve(self, root):
        res = []
        if root:
            cur = [root]
            leftFirst = False
            while cur:
                res.append(cur)

                next = []
                if leftFirst:
                    for node in reversed(cur):
                        if node.left:
                            next.append(node.left)
                        if node.right:
                            next.append(node.right)
                else:
                    for node in reversed(cur):
                        if node.right:
                            next.append(node.right)
                        if node.left:
                            next.append(node.left)

                leftFirst = not leftFirst
                cur = next
        return [[node.val for node in level] for level in res]

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = BinaryTreeZigzagLevelOrderTraversal
