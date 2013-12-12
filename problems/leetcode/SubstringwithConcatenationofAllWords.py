from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SubstringwithConcatenationofAllWords(LeetcodeProblem):
    def solve(self, s, L):
        wc = len(L)
        if wc == 0:
            return []

        wl = len(L[0])
        n = len(s)

        wordCountMap = {}
        for word in L:
            if word not in wordCountMap:
                wordCountMap[word] = 0
            wordCountMap[word] += 1

        res = []
        for i in xrange(0, len(s) - wc * wl + 1):
            realWordCountMap = {}
            found = True
            k = i
            for j in xrange(wc):
                word = s[k:k + wl]
                if word not in wordCountMap:
                    found = False
                    break
                if word not in realWordCountMap:
                    realWordCountMap[word] = 0
                realWordCountMap[word] += 1
                if realWordCountMap[word] > wordCountMap[word]:
                    found = False
                    break
                k += wl
            if found:
                res.append(i)

        return res

    def verify(self, original_input, input, s1, s2):
        s1.sort()
        return s1 == s2

    def input(self):
        from Parser import parseStringAndStringArray
        return parseStringAndStringArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = SubstringwithConcatenationofAllWords
