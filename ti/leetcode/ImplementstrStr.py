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

        pattern = self.buildPattern(needle)

        j = 0
        for i in xrange(m):
            if j == n:
                return haystack[i - j:]
            elif haystack[i] == needle[j]:
                j += 1
            else:
                while j > 0 and haystack[i] != needle[j]:
                    j = pattern[j - 1]

                if haystack[i] == needle[j]:
                    j += 1

        return haystack[-j:] if j == n else None

    def buildPattern(self, s):
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
