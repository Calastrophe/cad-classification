
class DiGraph:
    def __init__(self):
        self.nodes: dict[Node, list[Node]]


class Node:
    def __init__(self, id, type, parameters):
        self.id = id
        self.type = type
        self.parameters = parameters