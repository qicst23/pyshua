from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class NextPermutation(LeetcodeProblem):
    def solve(self, num):
        n = len(num)
        s = 0
        for i in xrange(n - 1, 0, -1):
            if num[i] > num[i - 1]:
                j = i
                while j < n and num[j] > num[i - 1]:
                    j += 1
                num[j - 1], num[i - 1] = num[i - 1], num[j - 1]
                s = i
                break
        e = n - 1
        while s < e:
            num[s], num[e] = num[e], num[s]
            s += 1
            e -= 1
        return num

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = NextPermutation
