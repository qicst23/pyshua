from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class AddBinary(LeetcodeProblem):
    def solve(self, a, b):
        array = []

        i = len(a) - 1
        j = len(b) - 1
        plusOne = 0

        while i >= 0 and j >= 0:
            d1 = 1 if a[i] == '1' else 0
            d2 = 1 if b[j] == '1' else 0
            d = d1 + d2 + plusOne
            plusOne = d / 2
            d %= 2
            array.append(str(d))
            i -= 1
            j -= 1

        while i >= 0:
            d1 = 1 if a[i] == '1' else 0
            d = d1 + plusOne
            plusOne = d / 2
            d %= 2
            array.append(str(d))
            i -= 1

        while j >= 0:
            d2 = 1 if b[j] == '1' else 0
            d = d2 + plusOne
            plusOne = d / 2
            d %= 2
            array.append(str(d))
            j -= 1

        if plusOne:
            array.append('1')

        array.reverse()

        return ''.join(array)

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = AddBinary
