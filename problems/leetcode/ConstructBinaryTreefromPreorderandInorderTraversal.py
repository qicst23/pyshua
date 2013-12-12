from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ConstructBinaryTreefromPreorderandInorderTraversal(LeetcodeProblem):
    def solve(self, preorder, inorder):
        return self.construct(
            preorder,
            0,
            len(preorder) - 1,
            inorder,
            0,
            len(inorder) - 1
        )

    def construct(self, preorder, plow, phigh, inorder, ilow, ihigh):
        from DataStructure.TreeNode import TreeNode

        if plow > phigh:
            return None
        else:
            rootVal = preorder[plow]

            i = -1
            for j, x in enumerate(inorder):
                if x == rootVal:
                    i = j
                    break

            return TreeNode(
                rootVal,
                self.construct(
                    preorder,
                    plow + 1,
                    plow + i - ilow,
                    inorder,
                    ilow,
                    i - 1
                ),
                self.construct(
                    preorder,
                    plow + i - ilow + 1,
                    phigh,
                    inorder,
                    i + 1,
                    ihigh
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

problem = ConstructBinaryTreefromPreorderandInorderTraversal
