from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LongestPalindromicSubstring(LeetcodeProblem):
    def solve(self, s):
        return self.longestPalindromic('*' + '*'.join(s) + '*')

    def longestPalindromic(self, s):
        n = len(s)
        center = 0
        r = 0
        l = [0] * n
        res = 0
        for i, c in enumerate(s):
            d = i - center
            mirror = center - d
            j = min(l[mirror], center + r - i)
            while i - j >= 0 and i + j < n and s[i + j] == s[i - j]:
                j += 1
            l[i] = j - 1
            if i + j > center + r:
                center = i
                r = j

        center = -1
        r = -1
        for i, c in enumerate(l):
            if c > r:
                center = i
                r = c

        return s[center - r + 1:center + r:2]

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for s in parseString(open(self.outputPath)):
            yield s[0]

problem = LongestPalindromicSubstring
