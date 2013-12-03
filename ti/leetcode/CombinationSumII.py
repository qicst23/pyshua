from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class CombinationSumII(LeetcodeProblem):
    def solve(self, num, target):
        num.sort()

        parts = []
        partsLength = []

        curVal = num[0]
        count = 0
        for x in num:
            if x == curVal:
                count += 1
            else:
                parts.append(curVal)
                partsLength.append(count)
                curVal = x
                count = 1
        parts.append(curVal)
        partsLength.append(count)

        res = []
        self.find(parts, partsLength, len(parts), 0, target, res, [])

        return res

    def find(self, parts, partsLength, n, low, target, res, solution):
        if target == 0:
            res.append(solution)
        else:
            for i in xrange(low, n):
                x = parts[i]
                for j in xrange(1, partsLength[i] + 1):
                    newTarget = target - j * x
                    if newTarget < 0:
                        break
                    else:
                        self.find(
                            parts,
                            partsLength,
                            n,
                            i + 1,
                            newTarget,
                            res,
                            solution + [x] * j
                        )

    def verify(self, input, s1, s2):
        s1Set = set([tuple(l) for l in s1])
        if len(s1) != len(s1Set):
            return False
        return s1Set == set([tuple(l) for l in s2])

    def input(self):
        from Parser import parseArrayAndInt
        return parseArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = CombinationSumII
