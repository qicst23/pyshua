from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SortList(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1, head)
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        i = 1
        while i <= n:
            pre = fakeHead
            cur = pre.next
            while cur:
                l1 = cur
                for j in xrange(i):
                    if cur:
                        cur = cur.next
                    else:
                        break
                l2 = cur
                for j in xrange(i):
                    if cur:
                        cur = cur.next
                    else:
                        break
                start, end = self.merge(l1, l2, l2, cur)
                pre.next = start
                end.next = cur
                pre = end
            i *= 2

        return fakeHead.next

    def merge(self, l1, l2, l1end, l2end):
        head = cur = None
        while l1 != l1end and l2 != l2end:
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next
            if head:
                cur.next = node
                cur = node
            else:
                head = node
                cur = node

        while l1 != l1end:
            node = l1
            l1 = l1.next
            if head:
                cur.next = node
                cur = node
            else:
                head = node
                cur = node

        while l2 != l2end:
            node = l2
            l2 = l2.next
            if head:
                cur.next = node
                cur = node
            else:
                head = node
                cur = node
        cur.next = None
        return head, cur

    def verify(self, input, s1, s2):
        while s1 and s2:
            if s1.val != s2.val:
                return False
            s1 = s1.next
            s2 = s2.next

        if s1 or s2:
            return False
        else:
            return True

    def input(self):
        from Parser import parseSingleLinkedList
        return parseSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = SortList
