from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class PartitionList(LeetcodeProblem):
    def solve(self, head, x):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead1 = SingleLinkedListNode(0)
        fakeHead2 = SingleLinkedListNode(0)

        cur1 = fakeHead1
        cur2 = fakeHead2

        cur = head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur
            else:
                cur2.next = cur
                cur2 = cur
            cur = cur.next

        cur1.next = fakeHead2.next
        cur2.next = None
        return fakeHead1.next

    def verify(self, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(s1, s2)

    def input(self):
        from Parser import parseSingleLinkedListAndInt
        return parseSingleLinkedListAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = PartitionList
