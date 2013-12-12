from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class GenerateParentheses(LeetcodeProblem):
    def solve(self, n):
        res = [{
            'l': 0,
            'r': 0,
            's': ''
        }]
        for i in xrange(2 * n):
            next = []
            for vs in res:
                if vs['l'] < n:
                    next.append({
                        'l': vs['l'] + 1,
                        'r': vs['r'],
                        's': vs['s'] + '('
                    })
                if vs['r'] < vs['l']:
                    next.append({
                        'l': vs['l'],
                        'r': vs['r'] + 1,
                        's': vs['s'] + ')'
                    })
            res = next
        return [vs['s'] for vs in res]

    def verify(self, original_input, input, s1, s2):
        s1.sort()
        s2.sort()
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.outputPath)):
            yield o[0]

problem = GenerateParentheses
