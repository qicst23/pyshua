from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MergekSortedLists(LeetcodeProblem):
    def solve(self, lists):
        n = len(lists)
        if n == 0:
            return None
        while n > 1:
            lists = [
                self.mergeTwo(
                    lists[i], lists[i + 1] if i + 1 < n else None
                ) for i in xrange(0, n, 2)
            ]
            n = (n + 1) / 2
        return lists[0]

    def mergeTwo(self, l1, l2):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        if not l1 or not l2:
            return l1 or l2

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

    def verify(self, original_input, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(s1, s2)

    def input(self):
        from Parser import parseSingleLinkedListArray
        return parseSingleLinkedListArray(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = MergekSortedLists
