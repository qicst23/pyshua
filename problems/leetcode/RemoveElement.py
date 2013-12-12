from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class RemoveElement(LeetcodeProblem):
    def solve(self, a, elem):
        n = len(a)
        i = 0
        for x in a:
            if x != elem:
                a[i] = x
                i += 1
        return i

    def verify(self, original_input, input, s1, s2):
        s1List = input[0][:s1]
        s1List.sort()
        s2.sort()
        return s1List == s2

    def input(self):
        from Parser import parseArrayAndInt
        return parseArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = RemoveElement
