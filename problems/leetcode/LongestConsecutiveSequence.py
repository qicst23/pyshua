from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LongestConsecutiveSequence(LeetcodeProblem):
    def solve(self, num):
        record = {}
        for x in num:
            record[x] = True
        res = 0
        for x in num:
            if x in record:
                del record[x]
                c = 1
                i = 1
                while x + i in record:
                    del record[x + i]
                    c += 1
                    i += 1
                i = 1
                while x - i in record:
                    del record[x - i]
                    c += 1
                    i += 1
                if res < c:
                    res = c

        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = LongestConsecutiveSequence
