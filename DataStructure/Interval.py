class Interval(object):
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __repr__(self):
        return str([self.start, self.end])
