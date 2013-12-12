from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class Permutations(LeetcodeProblem):
    def solve(self, num):
        return self.permutation(num, len(num), 0)

    def permutation(self, num, n, i):
        if i == n:
            return [[]]
        else:
            e = [num[i]]
            res = []
            for p in self.permutation(num, n, i + 1):
                res += [p[:j] + e + p[j:] for j in xrange(n - i)]
            return res

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

problem = Permutations
