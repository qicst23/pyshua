from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LinkedListCycleII(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1, head)
        slow = fakeHead
        quick = fakeHead
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                meetPoint = slow
                slow = fakeHead
                while slow != quick:
                    slow = slow.next
                    quick = quick.next
                return slow
        return None

    def verify(self, input, s1, s2):
        if s1:
            if s2 == 'no cycle':
                return False
            i = int(s2[-1])
            cur = input[0]  # head
            j = 0
            while cur and j < i:
                cur = cur.next
                j += 1
            if j < i:
                return False
            return cur == s1
        else:
            return s2 == 'no cycle'

    def input(self):
        from Parser import parseCyclicSingleLinkedList
        return parseCyclicSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseCylicDescription
        for o in parseCylicDescription(open(self.outputPath)):
            yield o[0]

problem = LinkedListCycleII
