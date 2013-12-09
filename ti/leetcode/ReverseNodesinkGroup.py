from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class ReverseNodesinkGroup(LeetcodeProblem):
    def solve(self, head, k):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1, head)
        last = fakeHead
        while last.next:
            start = last.next
            end = last.next
            for i in xrange(1, k):
                end = end.next
                if not end:
                    return fakeHead.next

            nextHead = end.next

            pre = start
            cur = start.next
            for i in xrange(1, k):
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

            last.next = end
            start.next = nextHead
            last = start

        return fakeHead.next

    def verify(self, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(s1, s2)

    def input(self):
        from Parser import parseSingleLinkedListAndOneInt
        return parseSingleLinkedListAndOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = ReverseNodesinkGroup
