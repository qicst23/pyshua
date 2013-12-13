from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class GasStation(LeetcodeProblem):
    def solve(self, gas, cost):
        s = 0
        t = 0
        index = 0
        for i in xrange(len(gas)):
            s += gas[i] - cost[i]
            t += gas[i] - cost[i]
            if t < 0:
                index = i + 1
                t = 0

        return index if s >= 0 else -1

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoIntArray
        return parseTwoIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = GasStation
