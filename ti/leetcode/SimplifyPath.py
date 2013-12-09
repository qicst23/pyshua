from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class SimplifyPath(LeetcodeProblem):
    def solve(self, path):
        stack = []
        components = path.split('/')
        for c in components:
            if c == '.' or c == '':
                pass
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return '/' + '/'.join(stack)

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = SimplifyPath
