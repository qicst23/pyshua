from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class WordLadderII(LeetcodeProblem):
    def solve(self, start, end, dSet):
        from string import lowercase

        pathNodes = {}
        dSet.add(end)
        last = set([start])
        while last:
            if end in last:
                break
            else:
                next = set([])
                toRemove = set([])
                for word in last:
                    n = len(word)
                    for i in xrange(n):
                        for c in lowercase:
                            if word[i] == c:
                                continue
                            newWord = word[:i] + c + word[i + 1:]
                            if newWord in dSet:
                                toRemove.add(newWord)
                                next.add(newWord)
                                if newWord not in pathNodes:
                                    pathNodes[newWord] = []
                                pathNodes[newWord].append(word)
                if not next:
                    return []
                dSet.difference_update(toRemove)
                last = next
        res = []
        self.buildPath(pathNodes, start, [end], res)
        return res

    def buildPath(self, pathNodes, start, path, res):
        node = path[-1]
        if node == start:
            res.append(path[::-1])
        else:
            for preNode in pathNodes[node]:
                path.append(preNode)
                self.buildPath(pathNodes, start, path, res)
                path.pop()

    def verify(self, input, s1, s2):
        s1Set = set([tuple(l) for l in s1])
        if len(s1) != len(s1Set):
            return False
        return s1Set == set([tuple(l) for l in s2])

    def input(self):
        from Parser import parseTwoStringAndStringArray
        for o in parseTwoStringAndStringArray(open(self.inputPath)):
            yield o[0], o[1], set(o[2])

    def output(self):
        from Parser import parseStringArrayArrays
        for o in parseStringArrayArrays(open(self.outputPath)):
            yield o[0]

problem = WordLadderII
