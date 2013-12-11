from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LetterCombinationsofaPhoneNumber(LeetcodeProblem):
    def solve(self, s):
        n = len(s)
        table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return self.combi(s, n, 0, table)

    def combi(self, s, n, i, table):
        if i == n:
            return ['']
        else:
            res = []
            tail = self.combi(s, n, i + 1, table)
            for solution in tail:
                for c in table[s[i]]:
                    res.append(c + solution)
            return res

    def verify(self, input, s1, s2):
        s1.sort()
        s2.sort()
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.outputPath)):
            yield o[0]

problem = LetterCombinationsofaPhoneNumber
