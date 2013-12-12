from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ThreeSum(LeetcodeProblem):
    def solve(self, num):
        res = []
        n = len(num)
        if n < 3:
            return res

        num.sort()
        for k in xrange(n - 2):
            if k > 0 and num[k] == num[k - 1]:
                continue
            i = k + 1
            j = n - 1
            target = -num[k]
            while i < j:
                s = num[i] + num[j]
                if s == target:
                    res.append([num[k], num[i], num[j]])
                    while i < j and num[i + 1] == num[i]:
                        i += 1
                    while j > i and num[j - 1] == num[j]:
                        j -= 1
                    i += 1
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    j -= 1

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

problem = ThreeSum
