from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class EvaluateReversePolishNotation(LeetcodeProblem):
    def solve(self, tokens):
        stack = []
        for s in tokens:
            if s in ['+', '-', '*', '/']:
                i2 = stack.pop()
                i1 = stack.pop()
                n = None
                if s == '+':
                    n = i1 + i2
                elif s == '-':
                    n = i1 - i2
                elif s == '*':
                    n = i1 * i2
                else:
                    # vary important difference between python and c
                    sign = 1 if i1 * i2 > 0 else -1
                    n = sign * (abs(i1) / abs(i2))
                stack.append(n)
            else:
                stack.append(int(s))

        return stack.pop()

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseStringArray
        return parseStringArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = EvaluateReversePolishNotation
