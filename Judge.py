import imp
import sys
from time import time

verbose = False


class Judge(object):
    def judge(self, problem):
        run_time = []
        allRight = True
        for testcase, solution in zip(problem.input(), problem.output()):
            t_start = time()
            answer = apply(problem.solve, testcase)
            if not problem.verify(testcase, answer, solution):
                print 'Wrong Answer'
                print 'Last excuted input:', testcase
                print 'Expected output:', solution
                print 'Your output:', answer
                allRight = False
                break
            run_time.append(time() - t_start)
        print problem.__class__.__name__, ':',
        print '%i testcases passed.' % len(run_time)
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
