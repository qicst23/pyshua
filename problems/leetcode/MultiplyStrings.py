from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MultiplyStrings(LeetcodeProblem):
    def solve(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            num1, num2 = num2, num1
        res = '0'
        for i, c in enumerate(reversed(num2)):
            res = self.addNum(res, self.mul(num1, c) + '0' * i)
        return res

    def mul(self, num1, d):
        i = ord(d[0]) - ord('0')
        if i == 0:
            return '0'
        else:
            plus = 0
            res = []
            for c in reversed(num1):
                d2 = ord(c) - ord('0')
                p = d2 * i + plus
                plus = p / 10
                res.append(p % 10)
            if plus:
                res.append(plus)
            return ''.join([str(digit) for digit in reversed(res)])

    def addNum(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            num1 = ('0' * (l2 - l1)) + num1
        elif l2 < l1:
            num2 = ('0' * (l1 - l2)) + num2

        res = []
        plus = 0
        ord_zero = ord('0')
        for c1, c2 in zip(reversed(num1), reversed(num2)):
            d1 = ord(c1) - ord_zero
            d2 = ord(c2) - ord_zero
            d = d1 + d2 + plus
            plus = d / 10
            res.append(d % 10)
        if plus:
            res.append(plus)
        return ''.join([str(digit) for digit in reversed(res)])

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = MultiplyStrings
