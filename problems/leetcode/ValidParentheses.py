from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ValidParentheses(LeetcodeProblem):
    def solve(self, s):
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if not stack or not self.match(stack.pop(), c):
                    return False
            else:
                return False
        return not stack

    def match(self, c1, c2):
        if c1 == '(' and c2 == ')':
            return True
        if c1 == '[' and c2 == ']':
            return True
        if c1 == '{' and c2 == '}':
            return True
        return False

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = ValidParentheses
