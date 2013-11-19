from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class AddTwoNumbers(LeetcodeProblem):
    def solve(self, l1, l2):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        head = None
        plusOne = 0
        while l1 and l2:
            d = l1.val + l2.val + plusOne
            plusOne = d / 10
            d %= 10
            node = SingleLinkedListNode(d)
            if not head:
                head = node
                cur = node
            else:
                cur.next = node
                cur = node
            l1 = l1.next
            l2 = l2.next

        while l1:
            d = l1.val + plusOne
            plusOne = d / 10
            d %= 10
            node = SingleLinkedListNode(d)
            if not head:
                head = node
                cur = node
            else:
                cur.next = node
                cur = node
            l1 = l1.next

        while l2:
            d = l2.val + plusOne
            plusOne = d / 10
            d %= 10
            node = SingleLinkedListNode(d)
            if not head:
                head = node
                cur = node
            else:
                cur.next = node
                cur = node
            l2 = l2.next

        if plusOne:
            node = SingleLinkedListNode(1)
            if not head:
                head = node
            else:
                cur.next = node

        return head

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
        from Parser import parseTwoSingleLinkedList
        return parseTwoSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        return parseSingleLinkedList(open(self.outputPath))

problem = AddTwoNumbers
