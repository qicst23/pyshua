from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LongestCommonPrefix(LeetcodeProblem):
    def solve(self, strs):
        if not strs:
            return ''

        n = min([len(s) for s in strs])
        first = strs[0]
        for i in xrange(n):
            c = first[i]
            for s in strs:
                if s[i] != c:
                    return first[:i]
        return first[:n]

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseStringArray
        return parseStringArray(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = LongestCommonPrefix
