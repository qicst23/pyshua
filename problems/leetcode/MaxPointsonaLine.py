from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MaxPointsonaLine(LeetcodeProblem):
    def solve(self, points):
        n = len(points)

        res = 0
        for i in range(n):
            p1 = points[i]
            lines = {}
            samePointCount = 1
            localMaxCount = 0
            specialLinePointCount = 0
            for j in xrange(i + 1, n):
                p2 = points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    samePointCount += 1
                elif p1.x == p2.x:
                    specialLinePointCount += 1
                    if specialLinePointCount > localMaxCount:
                        localMaxCount = specialLinePointCount
                else:
                    k = float(p1.y - p2.y) / (p1.x - p2.x)
                    c = 1
                    if k in lines:
                        c = lines[k] + 1
                    lines[k] = c
                    if c > localMaxCount:
                        localMaxCount = c
            localMaxCount += samePointCount

            if localMaxCount > res:
                res = localMaxCount

        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTupleList
        from DataStructure.Point import Point

        for s in parseTupleList(open(self.inputPath)):
            tuples = s[0]
            yield [Point(pair[0], pair[1]) for pair in tuples],

    def output(self):
        from Parser import parseOneInt

        for s in parseOneInt(open(self.outputPath)):
            yield s[0]

problem = MaxPointsonaLine
