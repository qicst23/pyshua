from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LinkedListCycle(LeetcodeProblem):
    def solve(self, head):
        from DataStructure.SingleLinkedListNode import SingleLinkedListNode
        fakeHead = SingleLinkedListNode(-1, head)

        slow = fakeHead
        quick = fakeHead
        met = 0
        while quick:
            slow = slow.next

            if quick.next == slow:
                met += 1
                if met == 2:
                    return True
            quick = quick.next

            if not quick:
                return False
            else:
                if quick.next == slow:
                    met += 1
                    if met == 2:
                        return True
                quick = quick.next
        return False

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseCyclicSingleLinkedList
        return parseCyclicSingleLinkedList(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = LinkedListCycle
