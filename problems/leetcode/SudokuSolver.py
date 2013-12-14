from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SudokuSolver(LeetcodeProblem):
    def solve(self, board):
        m = n = 9
        charset = [str(i + 1) for i in xrange(9)]
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == '.':
                    for k in charset:
                        board[i][j] = k
                        if self.valid(board) and self.solve(board):
                            return True
                        board[i][j] = '.'
                    return False

        return True

    def valid(self, board):
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
        return s1 and [''.join(row) for row in input[0]] == s2

    def input(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.inputPath)):
            stringArray = o[0]
            board = [list(s) for s in stringArray]
            yield board,

    def output(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.outputPath)):
            yield o[0]

problem = SudokuSolver
