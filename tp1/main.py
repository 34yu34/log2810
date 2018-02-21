class Node:
    def __init__(self, id, hasStation):
        self.station = hasStation
        self.arcs = []
        self.id = id

    def __lshift__(self, arc):
        self.arcs.append(arc)

    def __str__(self):
        return str(self.id) + ". " + str(self.station) + ": " + reduce(lambda x, y: x + ", " + y, map(lambda x: str(x), self.arcs))


class Arc:
    def __init__(self, time, node1, node2):
        self.time, self.node1, self.node2 = time, node1, node2
        node1 << self
        node2 << self

    def __str__(self):
        return "(" + str(self.node1.id) + "--" + str(self.time) + "--" + str(self.node2.id) + ")"


class Graph:
    def __init__(self):
        self.arcs = []
        self.node = []
        self.current_node = 0

    def __lshift__(self, elem):
        if isinstance(elem, Node):
            self.node.append(elem)
        elif isinstance(elem, Arc):
            self.arcs.append(elem)
        return self


a = Node(1, True)
b = Node(2, False)
c = Node(3, True)

ab = Arc(7, a, b)
ac = Arc(4, a, c)

g = Graph()

g << a << b << ab

print(g.arcs)
print(a)
