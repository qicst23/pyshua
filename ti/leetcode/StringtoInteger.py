from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class StringtoInteger(LeetcodeProblem):
    def solve(self, s):
        n = len(s)

        i = 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        sign = 1
        if s[i] in ['+', '-']:
            sign = 1 if s[i] == '+' else -1
            i += 1

        res = 0
        mag = 0
        charcode_0 = ord('0')
        while i < n:
            d = ord(s[i]) - charcode_0
            if 0 <= d <= 9:
                if sign == 1 and (res > 214748364 or (
                        res == 214748364 and d > 7)):
                    return 2147483647
                elif sign == -1 and (res > 214748364 or (
                        res == 214748364 and d > 8)):
                    return -2147483648
                else:
                    res = res * 10 + d
            else:
                break
            i += 1
        return sign * res * (10 ** mag)

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = StringtoInteger
