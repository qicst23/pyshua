from Problem import Problem


class TwoSum(Problem):
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
        from Parser import parseArrayAndIntInput
        import os
        inputPath = os.path.join(
            os.path.dirname(__file__),
            'data/TwoSum.input'
        )
        return parseArrayAndIntInput(open(inputPath))

    def output(self):
        from Parser import parseArrayAndIntOutput
        import os
        outputPath = os.path.join(
            os.path.dirname(__file__),
            'data/TwoSum.output'
        )
        return parseArrayAndIntOutput(open(outputPath))


problem = TwoSum
