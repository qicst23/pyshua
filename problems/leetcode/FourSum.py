from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class FourSum(LeetcodeProblem):
    def solve(self, num, target):
        num.sort()

        res = []
        n = len(num)
        for i in xrange(n):
            if i > 0 and num[i] == num[i - 1]:
                continue
            for j in xrange(i + 1, n):
                if j > i + 1 and num[j] == num[j - 1]:
                    continue
                else:
                    newTarget = target - num[i] - num[j]
                    l = j + 1
                    r = n - 1
                    while l < r:
                        s = num[l] + num[r]
                        if s == newTarget:
                            res.append([num[k] for k in [i, j, l, r]])
                            while l < r and num[l + 1] == num[l]:
                                l += 1
                            while r > l and num[r] == num[r - 1]:
                                r -= 1
                            l += 1
                            r -= 1
                        elif s < newTarget:
                            l += 1
                        else:
                            r -= 1
        return res

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

problem = FourSum
