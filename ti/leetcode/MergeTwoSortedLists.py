from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class MergeTwoSortedLists(LeetcodeProblem):
    def solve(self, l1, l2):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1)
        cur = fakeHead

        while l1 and l2:
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next
            cur.next = node
            cur = node

        while l1:
            cur.next = l1
            cur = l1
            l1 = l1.next

        while l2:
            cur.next = l2
            cur = l2
            l2 = l2.next

        return fakeHead.next

    def verify(self, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(s1, s2)

    def input(self):
        from Parser import parseTwoSingleLinkedList
        return parseTwoSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = MergeTwoSortedLists
