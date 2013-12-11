from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class InsertionSortList(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode

        fakeHead = SingleLinkedListNode(-1, head)

        pre = fakeHead
        cur = head
        while cur:
            preNode = fakeHead
            node = fakeHead.next

            while node.val < cur.val:
                preNode = node
                node = node.next

            if node != cur:
                pre.next = cur.next
                preNode.next = cur
                cur.next = node
                cur = pre

            pre = cur
            cur = cur.next
        return fakeHead.next

    def verify(self, input, s1, s2):
        while s1 and s2:
            if s1.val != s2.val:
                return False
            s1 = s1.next
            s2 = s2.next

        if s1 or s2:
            return False
        else:
            return True

    def input(self):
        from Parser import parseSingleLinkedList
        return parseSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = InsertionSortList
