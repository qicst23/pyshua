from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class MedianofTwoSortedArrays(LeetcodeProblem):
    def solve(self, a, b):
        n = len(a)
        m = len(b)
        if (n + m) % 2 == 0:
            return (self.find(a, 0, n - 1, b, 0, m - 1, (n + m) / 2) +
                    self.find(a, 0, n - 1, b, 0, m - 1, (n + m) / 2 + 1)) / 2.0
        else:
            return self.find(a, 0, n - 1, b, 0, m - 1, (n + m) / 2 + 1)

    def find(self, a, aLow, aHigh, b, bLow, bHigh, k):
        if aLow > aHigh:
            return b[bLow + k - 1]
        if bLow > bHigh:
            return a[aLow + k - 1]
        if k == 1:
            return min(a[aLow], b[bLow])

        # # this way for setting ac and bc also works
        # if (aHigh - aLow + 1) <= k / 2:
        #     ac = aHigh - aLow + 1
        #     bc = k - ac
        # elif (bHigh - bLow + 1) <= k / 2:
        #     bc = bHigh - bLow + 1
        #     ac = k - bc
        # else:
        #     ac = k / 2
        #     bc = k - ac

        if (aHigh - aLow > bHigh - bLow):
            bc = min(bHigh - bLow + 1, k / 2)
            ac = k - bc
        else:
            ac = min(aHigh - aLow + 1, k / 2)
            bc = k - ac

        x = a[aLow + ac - 1]
        y = b[bLow + bc - 1]

        if x == y:
            return x
        elif x < y:
            return self.find(a, aLow + ac, aHigh, b, bLow, bHigh, k - ac)
        else:
            return self.find(a, aLow, aHigh, b, bLow + bc, bHigh, k - bc)

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoArrays
        return parseTwoArrays(open(self.inputPath))

    def output(self):
        from Parser import parseOneFloat
        return parseOneFloat(open(self.outputPath))

problem = MedianofTwoSortedArrays
