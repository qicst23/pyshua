from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SymmetricTree(LeetcodeProblem):
    def solve(self, root):
        if not root:
            return True

        last = [root]
        sholudContinue = True
        while sholudContinue:
            i = 0
            j = len(last) - 1
            while i < j:
                n1 = last[i]
                n2 = last[j]
                if n1 and n2:
                    if n1.val != n2.val:
                        return False
                elif n1 or n2:
                    return False
                i += 1
                j -= 1

            next = []
            sholudContinue = False
            for node in last:
                if node:
                    next.append(node.left)
                    next.append(node.right)
                    if node.left or node.right:
                        sholudContinue = True
            last = next
        return True

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = SymmetricTree
