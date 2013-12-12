from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class WordLadder(LeetcodeProblem):
    def solve(self, start, end, dSet):
        from string import lowercase
        dSet.add(end)
        res = 0
        cur = [start]
        while cur:
            res += 1
            next = []
            for node in cur:
                if node == end:
                    return res
                for i in xrange(len(node)):
                    for c in lowercase:
                        newString = node[:i] + c + node[i + 1:]
                        if newString in dSet:
                            next.append(newString)
                            dSet.remove(newString)
            cur = next
        return 0

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStringAndStringArray
        for o in parseTwoStringAndStringArray(open(self.inputPath)):
            yield o[0], o[1], set(o[2])

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = WordLadder
