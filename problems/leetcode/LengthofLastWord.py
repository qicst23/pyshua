from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LengthofLastWord(LeetcodeProblem):
    def solve(self, s):
        j = len(s) - 1
        while j >= 0 and not s[j].isalpha():
            j -= 1

        i = j

        while i >= 0 and s[i].isalpha():
            i -= 1

        return j - i

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = LengthofLastWord
