from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ValidNumber(LeetcodeProblem):
    def solve(self, s):
        import string

        n = len(s)

        i = 0
        while i < n and s[i].isspace():
            i += 1

        j = n
        while j > i and s[j - 1].isspace():
            j -= 1

        if i == j:
            return False

        if s[i] == '-' or s[i] == '+':
            i += 1

        if i == j:
            return False

        needDigit = True
        seenDot = False
        seenE = False
        seenSign = False

        while i < j:
            c = s[i]
            if c in string.digits:
                needDigit = False

            elif c == 'e' or c == 'E':
                if seenE or needDigit:
                    return False
                seenE = True
                needDigit = True
                if i + 1 < j and (s[i + 1] == '+' or s[i + 1] == '-'):
                    i += 1

            elif c == '.':
                if seenDot or seenE:
                    return False
                seenDot = True

            else:
                return False

            i += 1

        return not needDigit

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = ValidNumber
