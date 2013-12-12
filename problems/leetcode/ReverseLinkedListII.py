from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ReverseLinkedListII(LeetcodeProblem):
    def solve(self, head, m, n):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1, head)
        pre = fakeHead
        cur = head
        i = 1
        while i < m:
            pre = cur
            cur = cur.next
            i += 1
        mth_pre = pre

        while i < (n + 1):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            i += 1

        mth_pre.next.next = cur
        mth_pre.next = pre

        return fakeHead.next

    def verify(self, original_input, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(s1, s2)

    def input(self):
        from Parser import parseSingleLinkedListAndTwoInt
        return parseSingleLinkedListAndTwoInt(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = ReverseLinkedListII
