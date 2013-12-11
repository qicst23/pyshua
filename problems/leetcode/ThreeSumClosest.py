from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ThreeSumClosest(LeetcodeProblem):
    def solve(self, num, target):
        num.sort()

        n = len(num)
        res = float('inf')
        for k, x in enumerate(num):
            newTarget = target - x
            i = k + 1
            j = n - 1
            while i < j:
                s = num[i] + num[j]

                if s == newTarget:
                    return target
                elif s < newTarget:
                    i += 1
                else:
                    j -= 1

                if abs(s - newTarget) < abs(res - target):
                    res = s + x

        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseArrayAndInt
        return parseArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = ThreeSumClosest
