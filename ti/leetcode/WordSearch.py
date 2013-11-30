from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class WordSearch(LeetcodeProblem):
    def solve(self, board, word):
        l = len(word)
        if l == 0:
            return True

        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False

        for i in xrange(m):
            for j in xrange(n):
                if self.go(board, word, m, n, i, j, l, 0):
                    return True
        return False

    def go(self, board, word, m, n, x, y, l, k):
        if k == l:
            return True
        else:
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[k]:
                board[x][y] = '*'
                res = False
                if (
                    self.go(board, word, m, n, x + 1, y, l, k + 1) or
                    self.go(board, word, m, n, x, y + 1, l, k + 1) or
                    self.go(board, word, m, n, x - 1, y, l, k + 1) or
                    self.go(board, word, m, n, x, y - 1, l, k + 1)
                ):
                    res = True

                board[x][y] = word[k]
                return res
            else:
                return False

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseStringArrayAndString
        for board, word in parseStringArrayAndString(open(self.inputPath)):
            board = [list(w) for w in board]
            yield board, word

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = WordSearch
