import imp
import sys
from time import time
from os import path

hr = ''
verbose = False
sys.setrecursionlimit(5000)


class Judge(object):
    def judge(self, problem):
        run_time = []
        allRight = True
        for original_testcase, testcase, solution in zip(
            problem.input(), problem.input(), problem.output()
        ):
            errorInfo = ''
            try:
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
                    errorTitle = 'Wrong Answer'
                    errorInfo = '\n'.join([
                        'Expected output: ' + solution_repr,
                        'Your output: ' + answer_repr
                    ])
                    raise Exception(errorTitle)

                run_time.append(duration)
            except Exception as e:
                allRight = False
                errorTitle = e.message
                break

        print hr
        if not allRight:
            print 'Error:', errorTitle
            print ''
            print 'Last excuted input:', testcase_repr
            if errorInfo:
                print errorInfo
            print ''

        print problem.__class__.__name__, ':',
        print '%i testcases passed ... %s' % (
            len(run_time), 'Accepted' if allRight else 'Failed'
        )

        if verbose:
            print 'Run time (ms):'
            print ' '.join(['{:.3f}'.format(10**6 * i) for i in run_time])

        print hr

        return allRight


def main():
    if len(sys.argv) < 3:
        print 'Usage: python Judge.py library problem'
        sys.exit()
    judge = Judge()
    problemModule = imp.load_source(
        'ProblemModule',
        path.join('problems', sys.argv[1], sys.argv[2] + '.py')
    )
    judge.judge(problemModule.problem())

if __name__ == '__main__':
    main()
