from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class UniqueBinarySearchTrees(LeetcodeProblem):
    def solve(self, n):
        return self.count(1, n, {})

    def count(self, low, high, cache):
        diff = high - low
        if diff in cache:
            return cache[diff]
        else:
            res = 0
            if low > high:
                res = 1
            else:
                for i in xrange(low, high + 1):
                    res += (
                        self.count(low, i - 1, cache) *
                        self.count(i + 1, high, cache)
                    )
            cache[diff] = res
            return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = UniqueBinarySearchTrees
