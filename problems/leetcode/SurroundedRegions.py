from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SurroundedRegions(LeetcodeProblem):
    def solve(self, board):
        self.m = len(board)
        if self.m == 0:
            return

        self.n = len(board[0])
        self.board = board

        self.visited = set()

        self.queue = []

        for i in xrange(self.m):
            self.add(i, 0)
            self.add(i, self.n - 1)

        for j in xrange(self.n):
            self.add(0, j)
            self.add(self.m - 1, j)

        while self.queue:
            x, y = self.queue.pop(0)
            self.go(x, y)

        for i in xrange(self.m):
            for j in xrange(self.n):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        return

    def go(self, x, y):
        if self.board[x][y] == 'O' or self.board[x][y] == '.':
            self.board[x][y] = '.'
            self.add(x - 1, y)
            self.add(x + 1, y)
            self.add(x, y - 1)
            self.add(x, y + 1)

    def add(self, x, y):
        if 0 <= x < self.m and 0 <= y < self.n and (x, y) not in self.visited:
            self.queue.append((x, y))
            self.visited.add((x, y))

    def verify(self, original_input, input, s1, s2):
        return [''.join(row) for row in input[0]] == s2

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

problem = SurroundedRegions
