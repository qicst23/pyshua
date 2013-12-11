from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class TwoSum(LeetcodeProblem):
    def solve(self, numbers, target):
        copy = numbers[:]
        numbers.sort()
        i = 0
        j = len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                break
            elif s > target:
                j -= 1
            else:
                i += 1

        if numbers[i] != numbers[j]:
            i, j = copy.index(numbers[i]), copy.index(numbers[j])
        else:
            i = copy.index(numbers[i])
            j = copy.index(numbers[j], i + 1)
        return (min(i, j) + 1, max(i, j) + 1)

    def verify(self, input, s1, s2):
        return s1[0] == s2[0] and s1[1] == s2[1]

    def input(self):
        from Parser import parseArrayAndInt
        return parseArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseTwoInt
        return parseTwoInt(open(self.outputPath))


problem = TwoSum
