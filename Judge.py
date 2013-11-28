import imp
import sys
from time import time

verbose = False
sys.setrecursionlimit(5000)


class Judge(object):
    def judge(self, problem):
        run_time = []
        allRight = True
        for orig_testcase, testcase, solution in zip(
            problem.input(), problem.input(), problem.output()
        ):
            t_start = time()
            answer = apply(problem.solve, testcase)
            if not problem.verify(testcase, answer, solution):
                print 'Wrong Answer'
                print 'Last excuted input:', orig_testcase
                print 'Expected output:', solution
                print 'Your output:', answer
                allRight = False
                break
            run_time.append(time() - t_start)
        print problem.__class__.__name__, ':',
        print '%i testcases passed ... %s' % (
            len(run_time), 'Accepted' if allRight else 'Wrong Answer'
        )
        if verbose:
            print 'Run time (ms):'
            print ' '.join(['{:.3f}'.format(10**6 * i) for i in run_time])

        return allRight


def main():
    judge = Judge()
    problemModule = imp.load_source('ProblemModule', sys.argv[1])
    judge.judge(problemModule.problem())

if __name__ == '__main__':
    main()
