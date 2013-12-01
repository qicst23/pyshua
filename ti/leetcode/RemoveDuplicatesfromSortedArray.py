from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class RemoveDuplicatesfromSortedArray(LeetcodeProblem):
    def solve(self, a):
        n = len(a)
        if n == 0:
            return 0

        curVal = a[0]
        curIndex = 1
        for i in xrange(1, n):
            x = a[i]
            if x != curVal:
                curVal = x
                a[curIndex] = curVal
                curIndex += 1
        return curIndex

    def verify(self, input, s1, s2):
        print input[0][0:10], s2[0:10]
        return input[0][0:s1] == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = RemoveDuplicatesfromSortedArray
