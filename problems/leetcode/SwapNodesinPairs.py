from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SwapNodesinPairs(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1, head)
        pre = fakeHead
        while pre.next and pre.next.next:
            node1 = pre.next
            node2 = pre.next.next
            next = node2.next
            pre.next = node2
            node2.next = node1
            node1.next = next
            pre = node1
        return fakeHead.next

    def verify(self, original_input, input, s1, s2):
        from DataStructure.Utils import sameList
        return sameList(s1, s2)

    def input(self):
        from Parser import parseSingleLinkedList
        return parseSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseSingleLinkedList
        for o in parseSingleLinkedList(open(self.outputPath)):
            yield o[0]

problem = SwapNodesinPairs
