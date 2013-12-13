from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class TextJustification(LeetcodeProblem):
    def solve(self, words, l):
        res = []

        n = len(words)
        i = 0

        curRow = []
        curL = 0
        curCount = 0

        while i < n:
            w = words[i]
            wl = len(w)
            if curL + curCount + wl <= l:
                curRow.append(w)
                curCount += 1
                curL += wl
                i += 1
            else:
                rowS = ''
                if curCount == 1:
                    rowS = curRow[0] + ' ' * (l - curL)
                else:
                    sc = (l - curL) / (curCount - 1)
                    rest = l - curL - (curCount - 1) * sc
                    for j in xrange(rest):
                        curRow[j] += ' '
                    rowS = (' ' * sc).join(curRow)
                res.append(rowS)
                curRow = []
                curL = 0
                curCount = 0

        res.append(' '.join(curRow) + ' ' * (l - curL - curCount + 1))
        return res

    def verify(self, original_input, input, s1, s2):
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                print c1, c2
                return False
        return True

    def input(self):
        from Parser import parseStringArrayAndInt
        return parseStringArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.outputPath)):
            yield o[0]

problem = TextJustification
