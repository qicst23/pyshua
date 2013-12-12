from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SearchInsertPosition(LeetcodeProblem):
    def solve(self, a, target):
        low = 0
        if target <= a[low]:
            return low

        high = len(a) - 1

        if target > a[high]:
            return high + 1

        while low <= high:
            middle = low + (high - low) / 2
            if target <= a[middle] and target > a[middle - 1]:
                return middle
            elif target > a[middle]:
                low = middle + 1
            else:
                high = middle - 1

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseArrayAndInt
        return parseArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = SearchInsertPosition
