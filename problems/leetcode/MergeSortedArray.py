from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MergeSortedArray(LeetcodeProblem):
    def solve(self, a, m, b, n):
        k = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if a[i] > b[j]:
                a[k] = a[i]
                i -= 1
            else:
                a[k] = b[j]
                j -= 1
            k -= 1
        while i >= 0:
            a[k] = a[i]
            i -= 1
            k -= 1
        while j >= 0:
            a[k] = b[j]
            j -= 1
            k -= 1
        return a

    def verify(self, original_input, input, s1, s2):
        return input[0] is s1 and s1 == s2

    def input(self):
        from Parser import parseTwoArrays
        for a, b in parseTwoArrays(open(self.inputPath)):
            m = len(a)
            n = len(b)
            a = a + (['space'] * (n))
            yield a, m, b, n

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = MergeSortedArray
