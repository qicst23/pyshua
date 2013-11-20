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

        for f in allPyFiles:
            problemModule = imp.load_source(
                'ProblemModule', join(leetcodePath, f))
            problem = getattr(problemModule, 'problem', None)
            if problem:
                self.assertTrue(self.judge.judge(problem()))

if __name__ == '__main__':
    unittest.main()
