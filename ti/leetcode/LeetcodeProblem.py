from Problem import Problem
import os


class LeetcodeProblem(Problem):
    def __init__(self):
        self.inputPath = os.path.join(
            os.path.dirname(__file__),
            'data',
            self.__class__.__name__ + '.input'
        )
        self.outputPath = os.path.join(
            os.path.dirname(__file__),
            'data',
            self.__class__.__name__ + '.output'
        )

problem = None
