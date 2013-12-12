from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class CountandSay(LeetcodeProblem):
    def solve(self, n):
        res = [1]
        i = 1
        while i < n:
            nextRes = []

            curVal = res[0]
            count = 0
            for x in res:
                if x == curVal:
                    count += 1
                else:
                    nextRes.append(count)
                    nextRes.append(curVal)
                    curVal = x
                    count = 1
            nextRes.append(count)
            nextRes.append(curVal)

            res = nextRes
            i += 1

        return ''.join([str(i) for i in res])

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = CountandSay
