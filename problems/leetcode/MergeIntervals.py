from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MergeIntervals(LeetcodeProblem):
    def solve(self, intervals):
        from DataStructure.Interval import Interval
        intervals.sort(key=lambda i: i.start)

        res = []
        if not intervals:
            res = []
        else:
            cur = intervals[0]
            for i in intervals:
                if i.start <= cur.end:
                    cur = Interval(cur.start, max(cur.end, i.end))
                else:
                    res.append(cur)
                    cur = i
            res.append(cur)
        return res

    def verify(self, original_input, input, s1, s2):
        for i1, i2 in zip(s1, s2):
            if i1.start != i2.start or i1.end != i2.end:
                return False
        return True

    def input(self):
        from Parser import parseIntArrayArrays
        from DataStructure.Interval import Interval
        for o in parseIntArrayArrays(open(self.inputPath)):
            intervals = [Interval(start, end) for start, end in o[0]]
            yield intervals,

    def output(self):
        from Parser import parseIntArrayArrays
        from DataStructure.Interval import Interval
        for o in parseIntArrayArrays(open(self.outputPath)):
            intervals = [Interval(start, end) for start, end in o[0]]
            yield intervals

problem = MergeIntervals
