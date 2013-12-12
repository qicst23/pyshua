from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LinkedListCycle(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1, head)

        slow = fakeHead
        quick = fakeHead
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseCyclicSingleLinkedList
        return parseCyclicSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = LinkedListCycle
