from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class PermutationsII(LeetcodeProblem):
    def solve(self, num):
        n = len(num)
        if n == 0:
            return []

        num.sort()

        used = [False] * n
        res = []
        self.go(num, n, used, res, [])
        return res

    def go(self, num, n, used, res, path):
        if len(path) == n:
            res.append(path[:])
        else:
            for i in xrange(n):
                if not used[i] and (
                    i == 0 or num[i] != num[i - 1] or used[i - 1]
                ):
                    used[i] = True
                    path.append(num[i])
                    self.go(num, n, used, res, path)
                    path.pop()
                    used[i] = False

    def verify(self, original_input, input, s1, s2):
        s1Set = set([tuple(l) for l in s1])
        if len(s1) != len(s1Set):
            return False
        return s1Set == set([tuple(l) for l in s2])

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = PermutationsII
