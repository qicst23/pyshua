from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ConstructBinaryTreefromInorderandPostorderTraversal(LeetcodeProblem):
    def solve(self, inorder, postorder):
        return self.construct(
            inorder, 0, len(inorder) - 1,
            postorder, 0, len(postorder) - 1
        )

    def construct(self, inorder, ilow, ihigh, postorder, plow, phigh):
        from DataStructure.TreeNode import TreeNode

        if ilow > ihigh:
            return None
        else:
            rootVal = postorder[phigh]

            i = ilow
            while i <= ihigh:
                if inorder[i] == rootVal:
                    break
                i += 1

            return TreeNode(
                rootVal,
                self.construct(
                    inorder, ilow, i - 1,
                    postorder, plow, plow + i - 1 - ilow
                ),
                self.construct(
                    inorder, i + 1, ihigh,
                    postorder, plow + i - ilow, phigh - 1
                )
            )

    def verify(self, original_input, input, s1, s2):
        from DataStructure.Utils import sameTree
        return sameTree(s1, s2)

    def input(self):
        from Parser import parseTwoArrays
        return parseTwoArrays(open(self.inputPath))

    def output(self):
        from Parser import parseBinaryTree
        for o in parseBinaryTree(open(self.outputPath)):
            yield o[0]

problem = ConstructBinaryTreefromInorderandPostorderTraversal
