from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class ConvertSortedListtoBinarySearchTree(LeetcodeProblem):
    def solve(self, head):
        self.cur = head

        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        return self.build(0, n - 1)

    def build(self, low, high):
        from DataStructure.TreeNode import TreeNode
        if low > high:
            return None
        middle = low + (high - low) / 2

        left = self.build(low, middle - 1)

        root = TreeNode(self.cur.val, left)
        self.cur = self.cur.next

        right = self.build(middle + 1, high)
        root.right = right

        return root

    def verify(self, input, s1, s2):
        from DataStructure.Utils import sameTree
        return sameTree(s1, s2)

    def input(self):
        from Parser import parseSingleLinkedList
        return parseSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseBinaryTree
        for o in parseBinaryTree(open(self.outputPath)):
            yield o[0]

problem = ConvertSortedListtoBinarySearchTree
