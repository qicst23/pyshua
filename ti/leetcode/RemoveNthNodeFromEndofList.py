from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class RemoveNthNodeFromEndofList(LeetcodeProblem):
    def solve(self, head, n):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(0, head)
        quick = fakeHead
        for i in xrange(n + 1):
            quick = quick.next
        pre = fakeHead
        cur = head
        while quick:
            pre = cur
            cur = cur.next
            quick = quick.next
        pre.next = cur.next
        return fakeHead.next

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

problem = RemoveNthNodeFromEndofList
