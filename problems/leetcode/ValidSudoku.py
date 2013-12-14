from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ValidSudoku(LeetcodeProblem):
    def solve(self, board):
        ord_zero = ord('0')
        m = n = 9

        for i in xrange(m):
            occured = [False] * 10
            for j in xrange(n):
                if board[i][j] == '.':
                    continue
                d = ord(board[i][j]) - ord_zero
                if occured[d]:
                    return False
                else:
                    occured[d] = True

        for j in xrange(n):
            occured = [False] * 10
            for i in xrange(m):
                if board[i][j] == '.':
                    continue
                d = ord(board[i][j]) - ord_zero
                if occured[d]:
                    return False
                else:
                    occured[d] = True

        for i in xrange(0, m, 3):
            for j in xrange(0, n, 3):
                occured = [False] * 10
                for x in xrange(3):
                    for y in xrange(3):
                        if board[i + x][j + y] == '.':
                            continue

                        d = ord(board[i + x][j + y]) - ord_zero
                        if occured[d]:
                            return False
                        else:
                            occured[d] = True

        return True

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseStringArray
        return parseStringArray(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = ValidSudoku
