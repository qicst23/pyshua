from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class CloneGraph(LeetcodeProblem):
    def solve(self, node):
        if not node:
            return None

        self.visited = set()
        self.copied = {}

        queue = [node]
        self.visited.add(node.label)

        while queue:
            curNode = queue.pop()
            copy = self.copy(curNode)
            for n in curNode.neighbors:
                if n.label not in self.visited:
                    self.visited.add(n.label)
                    queue.append(n)
                copy.neighbors.append(self.copy(n))

        return self.copy(node)

    def copy(self, node):
        from DataStructure.Graph import UndirectedGraphNode
        if node.label in self.copied:
            return self.copied[node.label]
        else:
            copy = UndirectedGraphNode(node.label)
            self.copied[node.label] = copy
            return copy

    def verify(self, original_input, input, s1, s2):
        if not input[0] and not s1 and not s2:
            return True

        input_queue = [input[0]]
        input_visited = set()
        answer_queue = [s1]
        answer_visited = set()
        solution_queue = [s2]
        solution_visited = set()

        while input_queue and answer_queue and solution_queue:
            input_node = input_queue.pop(0)
            answer_node = answer_queue.pop(0)
            solution_node = solution_queue.pop(0)

            if (
                id(input_node) == id(answer_node) or
                answer_node.label != solution_node.label
            ):
                return False

            for input_n in input_node.neighbors:
                if input_n.label not in input_visited:
                    input_visited.add(input_n.label)
                    input_queue.append(input_n)

            for answer_n in answer_node.neighbors:
                if answer_n.label not in answer_visited:
                    answer_visited.add(answer_n.label)
                    answer_queue.append(answer_n)

            for solution_n in solution_node.neighbors:
                if solution_n.label not in solution_visited:
                    solution_visited.add(solution_n.label)
                    solution_queue.append(solution_n)

        if input_queue or answer_queue or solution_queue:
            return False

        return True

    def input(self):
        from Parser import parseGraph
        return parseGraph(open(self.inputPath))

    def output(self):
        from Parser import parseGraph
        for o in parseGraph(open(self.outputPath)):
            yield o[0]

problem = CloneGraph
