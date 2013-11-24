from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class ImplementstrStr(LeetcodeProblem):
    def solve(self, haystack, needle):
        # kmp
        n = len(needle)
        if n == 0:
            return haystack

        m = len(haystack)
        if m < n:
            return None

        pattern = self.buildPatter(needle)

        j = 0
        i = 0
        while i < m:
            while i < m and j < n and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == n:
                return haystack[i - j:]
            if i == m:
                return None

            while j > 0 and haystack[i] != needle[j]:
                j = pattern[j - 1]

            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:  # j must be zero
                i += 1

        return None

    def buildPatter(self, s):
        n = len(s)
        p = [0] * n
        for i in xrange(1, n):
            k = p[i - 1]
            while k > 0 and s[k] != s[i]:
                k = p[k - 1]
            if s[k] == s[i]:
                k += 1
            p[i] = k
        return p

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseStringOrNull
        for o in parseStringOrNull(open(self.outputPath)):
            yield o[0]

problem = ImplementstrStr
