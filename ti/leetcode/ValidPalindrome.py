from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class ValidPalindrome(LeetcodeProblem):
    def solve(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = ValidPalindrome
