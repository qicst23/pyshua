from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SubsetsII(LeetcodeProblem):
    def solve(self, num):
        if not num:
            return []

        num.sort()
        cur = num[0]
        count = 0
        parts = []
        partsCount = []
        for x in num:
            if x == cur:
                count += 1
            else:
                parts.append(cur)
                partsCount.append(count)
                cur = x
                count = 1
        parts.append(cur)
        partsCount.append(count)
        return self.construct(parts, partsCount, len(parts), 0)

    def construct(self, parts, partsCount, n, i):
        if i == n:
            return [[]]
        else:
            x = parts[i]
            count = partsCount[i]
            res = []
            tail = self.construct(parts, partsCount, n, i + 1)
            for c in xrange(count + 1):
                thisPart = [x] * c
                for tailPart in tail:
                    res.append(thisPart + tailPart)
            return res

    def verify(self, original_input, input, s1, s2):
        s1.sort()
        s2.sort()
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = SubsetsII
