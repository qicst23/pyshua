from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ReorderList(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1, head)
        slow = fakeHead
        quick = fakeHead
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next

        pre = None
        cur = slow.next
        slow.next = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        end = pre
        head = fakeHead.next
        self.mixTwoList(head, end)

    def mixTwoList(self, l1, l2):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1)
        cur = fakeHead
        while l1 and l2:
            l1next = l1.next
            l2next = l2.next

            cur.next = l1
            cur = cur.next
            cur.next = l2
            cur = cur.next

            l1 = l1next
            l2 = l2next

        if l1:
            cur.next = l1
            cur = cur.next
        elif l2:
            cur.next = l2
            cur = cur.next

        cur.next = None

        return fakeHead.next

    def verify(self, original_input, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(input[0], s2)

    def input(self):
        from Parser import parseSingleLinkedList
        return parseSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = ReorderList
