from os import listdir
from os.path import join
from Judge import Judge
import imp
import unittest


class LeetcodeTest(unittest.TestCase):
    def setUp(self):
        self.judge = Judge()

    def testAllProblems(self):
        leetcodePath = 'ti/leetcode/'
        allPyFiles = filter(lambda f: f.endswith('py'), listdir(leetcodePath))
        pCount = 0
        for f in allPyFiles:
            problemModule = imp.load_source(
                'ProblemModule', join(leetcodePath, f))
            problem = getattr(problemModule, 'problem', None)
            if problem:
                self.assertTrue(self.judge.judge(problem()))
                pCount += 1
        print '%i problems verified.' % pCount
if __name__ == '__main__':
    unittest.main()
