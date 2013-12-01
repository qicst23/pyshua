from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class DivideTwoIntegers(LeetcodeProblem):
    def solve(self, dividend, divisor):
        if divisor == 0:
            return float('inf')

        sign = 1
        if dividend > 0:
            sign = -sign
            dividend = -dividend

        if divisor > 0:
            sign = -sign
            divisor = -divisor

        res = 0
        rest = dividend
        while rest <= divisor:
            newDivisor = divisor
            fac = 1
            while rest - newDivisor <= newDivisor:
                newDivisor += newDivisor
                fac += fac
            rest -= newDivisor
            res += fac
        return sign * res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoInt
        return parseTwoInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = DivideTwoIntegers
