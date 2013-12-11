from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class FlattenBinaryTreetoLinkedList(LeetcodeProblem):
    def solve(self, root):
        if not root:
            return None

        stack = []
        pre = None
        cur = root

        while stack or cur:
            if cur:
                if pre:
                    pre.right = cur
                    pre = cur
                else:
                    pre = cur

                if cur.right:
                    stack.append(cur.right)

                left = cur.left
                cur.left = None
                cur = left

            else:
                cur = stack.pop()

        return root

    def verify(self, input, s1, s2):
        from DataStructure.Utils import sameTree
        return sameTree(s1, s2)

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseBinaryTree
        for o in parseBinaryTree(open(self.outputPath)):
            yield o[0]

problem = FlattenBinaryTreetoLinkedList
