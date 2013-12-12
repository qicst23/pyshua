from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MinimumWindowSubstring(LeetcodeProblem):
    def solve(self, s, t):
        m = len(s)
        n = len(t)
        if m < n or m == 0:
            return ''

        occur = {}
        diffCharCount = 0
        for c in t:
            if c not in occur:
                diffCharCount += 1
                occur[c] = 0
            occur[c] += 1

        a = b = 0
        minCount = float('inf')
        res = ''
        while b < m:
            while b < m:
                c = s[b]
                if c in occur:
                    occur[c] -= 1
                    if occur[c] == 0:
                        diffCharCount -= 1
                        if diffCharCount == 0:
                            break
                b += 1
            if b < m:
                while a <= b:
                    c = s[a]
                    if c in occur:
                        occur[c] += 1
                        if occur[c] > 0:
                            diffCharCount += 1
                            break
                    a += 1
                if minCount > b - a + 1:
                    minCount = b - a + 1
                    res = s[a:b + 1]
                a += 1
            b += 1
        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = MinimumWindowSubstring
