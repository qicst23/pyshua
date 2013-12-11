from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SearchinRotatedSortedArray(LeetcodeProblem):
    def solve(self, a, target):
        low = 0
        high = len(a) - 1
        while low <= high:
            middle = low + (high - low) / 2
            if a[middle] == target:
                return middle
            elif a[middle] < a[high]:
                if a[middle] < target <= a[high]:
                    low = middle + 1
                else:
                    high = middle - 1
            else:
                if a[low] <= target < a[middle]:
                    high = middle - 1
                else:
                    low = middle + 1

        return -1

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseArrayAndInt
        return parseArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = SearchinRotatedSortedArray
