from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SearchforaRange(LeetcodeProblem):
    def solve(self, a, target):
        n = len(a)

        low = 0
        high = n - 1
        left = -1
        while low <= high:
            middle = low + (high - low) / 2
            if a[middle] == target and (middle == 0 or a[middle - 1] < target):
                left = middle
                break
            elif a[middle] < target:
                low = middle + 1
            else:
                high = middle - 1

        low = 0
        high = n - 1
        right = -1
        while low <= high:
            middle = low + (high - low) / 2
            if a[middle] == target and (
                middle == n - 1 or a[middle + 1] > target
            ):
                right = middle
                break
            elif a[middle] <= target:
                low = middle + 1
            else:
                high = middle - 1
        return [left, right]

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseArrayAndInt
        return parseArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = SearchforaRange
