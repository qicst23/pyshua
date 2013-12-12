from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class PalindromePartitioning(LeetcodeProblem):
    def solve(self, s):
        return self.find(s, len(s), 0, {})

    def find(self, s, n, i, cache):
        if i in cache:
            return cache[i]
        res = []
        if i == n:
            res.append([])
        else:
            for j in xrange(i, n):
                if self.isPalindrome(s, i, j):
                    ps = [s[i:j + 1]]
                    tail = self.find(s, n, j + 1, cache)
                    res += [ps + tp for tp in tail]
        cache[i] = res
        return res

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def verify(self, original_input, input, s1, s2):
        s1.sort()
        s2.sort()
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseStringArrayArrays
        for o in parseStringArrayArrays(open(self.outputPath)):
            yield o[0]

problem = PalindromePartitioning
