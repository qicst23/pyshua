from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LongestSubstringWithoutRepeatingCharacters(LeetcodeProblem):
    def solve(self, s):
        n = len(s)

        charCount = 26
        occur = [False] * charCount

        res = i = j = 0

        a_charcode = ord('a')

        while j < n:
            code = ord(s[j]) - a_charcode
            if occur[code]:
                res = max(j - i, res)
                while i < j:
                    if ord(s[i]) == ord(s[j]):
                        i += 1
                        break
                    else:
                        occur[ord(s[i]) - a_charcode] = False
                        i += 1
            else:
                occur[code] = True
            j += 1
        res = max(j - i, res)
        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = LongestSubstringWithoutRepeatingCharacters
