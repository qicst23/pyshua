from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class RemoveDuplicatesfromSortedListII(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode

        if not head:
            return None

        fakeHead = SingleLinkedListNode(-float('inf'), head)
        lastValidNode = fakeHead
        pre = fakeHead
        cur = head
        curVal = head.val
        curCount = 0
        while cur:
            if cur.val == curVal:
                curCount += 1
            else:
                if curCount == 1:
                    lastValidNode.next = pre
                    lastValidNode = pre

                curVal = cur.val
                curCount = 1
            pre = cur
            cur = cur.next

        if curCount == 1:
            lastValidNode.next = pre
            lastValidNode = pre

        lastValidNode.next = None

        return fakeHead.next

    def verify(self, original_input, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(s1, s2)

    def input(self):
        from Parser import parseSingleLinkedList
        return parseSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = RemoveDuplicatesfromSortedListII
