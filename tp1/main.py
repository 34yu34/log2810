######################################################################
# Auteur : Obossou Ema-Wo, Billy Bouchard, Gnaga Dogbeda Georges
# Matricule: 1780896, 1850477, 1870143
# Version Python: 3.6
######################################################################


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
        return "(" + str(self.node1.id) + "--" + str(self.node2.id) + " :" + str(self.time) + ")"


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

    def __getitem__(self, id):
        for node in self.node:
            if node.id == id:
                return node
        return False


def creerGraph(nomFichier):
    graph = Graph()
    fichier = open(nomFichier, "r")
    line = fichier.readline()
    while line != '\n':
        firstNumber = True
        nodeid = ""
        hasStation = ""
        for char in line:
            if char == ",":
                firstNumber = False
                continue
            if firstNumber:
                nodeid += char
            if not(firstNumber):
                hasStation += char
        nodeid = int(nodeid)
        hasStation = hasStation == '1\n'
        node = Node(nodeid, hasStation)
        graph << node
        line = fichier.readline()
    line = fichier.readline()
    while line != '':
        node1 = ""
        node2 = ""
        time = ""
        current = 0
        for char in line:
            if char == ',':
                current += 1
                continue
            elif current == 0:
                node1 += char
            elif current == 1:
                node2 += char
            elif current == 2:
                time += char
        node1 = int(node1)
        node2 = int(node2)
        time = int(time)

        arc = Arc(time, graph[node1], graph[node2])
        graph << arc
        line = fichier.readline()
    return graph


g = creerGraph("villes.txt")
for node in g.node:
    print(node)
