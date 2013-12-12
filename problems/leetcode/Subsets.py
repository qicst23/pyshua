from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class Subsets(LeetcodeProblem):
    def solve(self, s):
        return self.subset(s, len(s), 0)

    def subset(self, s, n, i):
        if n == i:
            return [[]]
        else:
            e = [s[i]]
            tail = self.subset(s, n, i + 1)
            return tail + [e + s for s in tail]

    def verify(self, input, s1, s2):
        for a in s1:
            a.sort()
        for a in s2:
            a.sort()
        s1.sort()
        s2.sort()
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = Subsets
