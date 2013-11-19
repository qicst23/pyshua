import imp
import sys
from time import time

verbose = False


class Judge(object):
    def __init__(self):
        problemModule = imp.load_source('ProblemModule', sys.argv[1])
        self.judge(problemModule.problem())

    def judge(self, problem):
        run_time = []
        for testcase, solution in zip(problem.input(), problem.output()):
            t_start = time()
            answer = apply(problem.solve, testcase)
            if not problem.verify(testcase, answer, solution):
                print 'Wrong Answer'
                print 'Last excuted input:', testcase
                print 'Expected output:', solution
                print 'Your output:', answer
                break
            run_time.append(time() - t_start)
        print '%i testcases passed.' % len(run_time)
        if verbose:
            print 'Run time (ms):'
            print ' '.join(['{:.3f}'.format(10**6 * i) for i in run_time])

judge = Judge()
