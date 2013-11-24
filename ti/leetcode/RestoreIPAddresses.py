from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class RestoreIPAddresses(LeetcodeProblem):
    def solve(self, s):
        res = []
        ip = []
        self.restore(s, len(s), 0, res, ip)
        return res

    def restore(self, s, n, i, res, ip):
        if len(ip) == 4 and i == n:
            res.append('.'.join(map(str, ip)))
        elif len(ip) < 4 and i < n:
            if s[i] == '0':
                ip.append(0)
                self.restore(s, n, i + 1, res, ip)
                ip.pop()
            else:
                j = 0
                compo = 0
                charcode_0 = ord('0')
                while j < 3 and i + j < n:
                    d = ord(s[i + j]) - charcode_0
                    compo = compo * 10 + d
                    if compo > 255:
                        break
                    else:
                        ip.append(compo)
                        self.restore(s, n, i + j + 1, res, ip)
                        ip.pop()
                    j += 1

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.outputPath)):
            yield o[0]

problem = RestoreIPAddresses
