from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class LongestValidParentheses(LeetcodeProblem):
    def solve(self, s):
        stack = []
        s = list(s)
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    l = stack.pop()
                    s[l] = '*'
                    s[i] = '*'
        res = 0
        count = 0
        for c in s:
            if c == '*':
                count += 1
            else:
                if count > res:
                    res = count
                count = 0

        if count > res:
            res = count

        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = LongestValidParentheses
