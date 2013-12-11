from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SortColors(LeetcodeProblem):
    def solve(self, a):
        pivot = 1
        i = 0
        j = -1
        k = len(a) - 1
        while j < k:
            x = a[k]
            if x <= pivot:
                j += 1
                a[j], a[k] = a[k], a[j]
                if x < pivot:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            else:
                k -= 1
        return a

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = SortColors
