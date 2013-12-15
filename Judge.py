import imp
import sys
from time import time
from os import path

verbose = False
sys.setrecursionlimit(5000)


class Judge(object):
    def judge(self, problem):
        run_time = []
        allRight = True
        for original_testcase, testcase, solution in zip(
            problem.input(), problem.input(), problem.output()
        ):
            testcase_repr = repr(testcase)
            solution_repr = repr(solution)

            t_start = time()
            answer = apply(problem.solve, testcase)
            duration = time() - t_start

            answer_repr = repr(answer)

            if not problem.verify(
                original_testcase,
                testcase,
                answer,
                solution
            ):
                print 'Wrong Answer'
                print 'Last excuted input:', testcase_repr
                print 'Expected output:', solution_repr
                print 'Your output:', answer_repr
                allRight = False
                break
            run_time.append(duration)
        print problem.__class__.__name__, ':',
        print '%i testcases passed ... %s' % (
            len(run_time), 'Accepted' if allRight else 'Wrong Answer'
        )
        if verbose:
            print 'Run time (ms):'
            print ' '.join(['{:.3f}'.format(10**6 * i) for i in run_time])

        return allRight


def main():
    if len(sys.argv) < 3:
        print 'Usage: python Jude.py library problem'
        sys.exit()
    judge = Judge()
    problemModule = imp.load_source(
        'ProblemModule',
        path.join('problems', sys.argv[1], sys.argv[2] + '.py')
    )
    judge.judge(problemModule.problem())

if __name__ == '__main__':
    main()
