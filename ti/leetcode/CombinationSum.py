from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class CombinationSum(LeetcodeProblem):
    def solve(self, candidates, target):
        candidates.sort()
        res = []
        self.find(candidates, len(candidates), 0, target, res, [])

        return res

    def find(self, candidates, n, low, target, res, solution):
        if target == 0:
            res.append(solution)
        else:
            for i in xrange(low, n):
                x = candidates[i]
                if x > target:
                    break
                else:
                    self.find(
                        candidates,
                        n,
                        i,
                        target - x,
                        res,
                        solution + [x]
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

problem = CombinationSum
