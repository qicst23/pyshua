from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class RotateList(LeetcodeProblem):
    def solve(self, head, n):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode

        if n == 0 or not head:
            return head

        fakeHead = SingleLinkedListNode(-1, head)

        cur = fakeHead
        l = 0
        while cur.next:
            l += 1
            cur = cur.next

        n %= l

        quick = fakeHead

        for i in xrange(n):
            if not quick:
                return head
            else:
                quick = quick.next

        slow = fakeHead
        end = quick
        while end.next:
            end = end.next
            slow = slow.next

        end.next = fakeHead.next
        fakeHead.next = slow.next
        slow.next = None

        return fakeHead.next

    def verify(self, original_input, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(s1, s2)

    def input(self):
        from Parser import parseSingleLinkedListAndInt
        return parseSingleLinkedListAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = RotateList
