from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class IntegertoRoman(LeetcodeProblem):
    def solve(self, num):
        table = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '*', '*']
        res = []

        for i in xrange(3, -1, -1):
            m = 10 ** i
            d = num / m
            one = table[2 * i]
            five = table[2 * i + 1]
            ten = table[2 * i + 2]

            if 1 <= d <= 3:
                for j in xrange(d):
                    res.append(one)
            elif d == 4:
                res.append(one)
                res.append(five)
            elif 5 <= d <= 8:
                res.append(five)
                for j in xrange(d - 5):
                    res.append(one)
            elif d == 9:
                res.append(one)
                res.append(ten)

            num %= m

        return ''.join(map(str, res))

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = IntegertoRoman
