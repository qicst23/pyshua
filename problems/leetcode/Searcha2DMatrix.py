from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class Searcha2DMatrix(LeetcodeProblem):
    def solve(self, matrix, target):
        matrix = [m for m in matrix if m]
        low = 0
        high = len(matrix) - 1
        row = -1
        while low <= high:
            middle = low + (high - low) / 2
            if (
                middle == high or
                matrix[middle][0] <= target < matrix[middle + 1][0]
            ):
                row = middle
                break
            elif target < matrix[middle][0]:
                high = middle - 1
            else:
                low = middle + 1
        if row == -1:
            return False
        else:
            low = 0
            high = len(matrix[row]) - 1
            while low <= high:
                middle = low + (high - low) / 2
                if matrix[row][middle] == target:
                    return True
                elif matrix[row][middle] < target:
                    low = middle + 1
                else:
                    high = middle - 1
            return False

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArrayArraysAndInt
        return parseIntArrayArraysAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = Searcha2DMatrix
