from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class RemoveDuplicatesfromSortedList(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-float('inf'), head)

        pre = fakeHead
        cur = head
        curVal = fakeHead.val

        while cur:
            if cur.val != curVal:
                pre.next = cur
                pre = cur
                curVal = cur.val
            cur = cur.next

        # important don't forget this
        pre.next = None

        return fakeHead.next

    def verify(self, input, s1, s2):
        while s1 and s2:
            if s1.val != s2.val:
                return False
            s1 = s1.next
            s2 = s2.next
        if s1 or s2:
            return False
        return True

    def input(self):
        from Parser import parseSingleLinkedList
        return parseSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = RemoveDuplicatesfromSortedList
