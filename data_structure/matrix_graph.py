class MatrixGraph:

    def __init__(self, vertices):
        self.vertices = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.len = vertices

    def append(self, vertex, target, edge):
        self.vertices[vertex][target] = edge

    def edges(self, index):
        return self.vertices[index]
