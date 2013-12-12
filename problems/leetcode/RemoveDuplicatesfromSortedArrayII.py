from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class RemoveDuplicatesfromSortedArrayII(LeetcodeProblem):
    def solve(self, a):
        n = len(a)
        if n == 0:
            return 0

        cur = a[0]
        count = 0
        i = 0
        for x in a:
            if x == cur:
                count += 1
            else:
                a[i] = cur
                i += 1
                if count > 1:
                    a[i] = cur
                    i += 1
                cur = x
                count = 1
        a[i] = cur
        i += 1
        if count > 1:
            a[i] = cur
            i += 1
        return i

    def verify(self, original_input, input, s1, s2):
        return input[0][:s1] == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = RemoveDuplicatesfromSortedArrayII
