from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class InsertInterval(LeetcodeProblem):
    def solve(self, intervals, newInterval):
        points = []
        n = 0
        for inter in intervals:
            points.append(inter.start)
            points.append(inter.end)
            n += 2
        left = self.insertIndex(points, n, newInterval.start)
        if left % 2 == 1:
            newInterval.start = points[left - 1]

        right = self.insertIndex(points, n, newInterval.end)
        if right % 2 == 1:
            newInterval.end = points[right]
            right += 2
        elif right + 1 < n and newInterval.end == points[right]:
            newInterval.end = points[right + 1]
            right += 2

        intervals[left / 2:right / 2] = [newInterval]

        return intervals

    def insertIndex(self, a, n, target):
        if n == 0:
            return 0

        if target <= a[0]:
            return 0
        if a[n - 1] < target:
            return n

        low = 0
        high = n - 1
        while low <= high:
            middle = low + (high - low) / 2
            if a[middle] < target and a[middle + 1] >= target:
                return middle + 1
            elif a[middle] >= target:
                high = middle - 1
            else:
                low = middle + 1

    def verify(self, original_input, input, s1, s2):
        for i1, i2 in zip(s1, s2):
            if i1.start != i2.start or i1.end != i2.end:
                return False
        return True

    def input(self):
        from Parser import parseIntArrayArraysAndIntArray
        from DataStructure.Interval import Interval
        for aa, a in parseIntArrayArraysAndIntArray(open(self.inputPath)):
            aa = [Interval(start, end) for start, end in aa]
            a = Interval(a[0], a[1])
            yield aa, a

    def output(self):
        from Parser import parseIntArrayArrays
        from DataStructure.Interval import Interval
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield [Interval(start, end) for start, end in o[0]]

problem = InsertInterval
