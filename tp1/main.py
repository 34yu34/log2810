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
        ######################################################################
        # Operator << overloading to add item to the graph
        # return self is for cascade
        ######################################################################
        self.arcs.append(arc)
        return self

    def __str__(self):
        ######################################################################
        # Overload the str function for printing
        ######################################################################
        return str(self.id) + ". " + str(self.station) + ": " + reduce(lambda x, y: x + ", " + y, map(lambda x: str(x), self.arcs))


class Arc:
    def __init__(self, time, node1, node2):
        self.time, self.node1, self.node2 = time, node1, node2
        node1 << self
        node2 << self

    def __str__(self):
        ######################################################################
        # Overload the str function for printing
        ######################################################################
        return "(" + str(self.node1.id) + "--" + str(self.node2.id) + " :" + str(self.time) + ")"


class Graph:
    def __init__(self):
        self.arcs = []
        self.node = {}
        self.current_node = 0

    def __lshift__(self, elem):
        ######################################################################
        # Add << operator to add arc or node to their respective array
        # self return is for cascade
        ######################################################################
        if isinstance(elem, Node):
            self.node[elem.id] = elem
        elif isinstance(elem, Arc):
            self.arcs.append(elem)
        return self

    def __getitem__(self, nodeId):
        ######################################################################
        # return a node from a node id
        ######################################################################
        return self.node[nodeId]


def readNodeLine(line):
    ######################################################################
    # This function read a line of the style "1,2\n" and returns
    # a node object from it
    ######################################################################
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
    return Node(nodeid, hasStation)


def readArcLine(line, graph):
    ######################################################################
    # this function read a line of format : "1,4,7\n" and return an arc
    # object out of it. It needs a group of preexisting node to work
    ######################################################################
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
    return Arc(time, graph[node1], graph[node2])


def creerGraph(nomFichier):
    ######################################################################
    # This function read a file and generate a graph from it
    ######################################################################
    graph = Graph()
    fichier = open(nomFichier, "r")
    line = fichier.readline()
    while line != '\n':
        graph << readNodeLine(line)
        line = fichier.readline()
    line = fichier.readline()
    while line != '':
        graph << readArcLine(line, graph)
        line = fichier.readline()
    return graph


def lireGraph(graph):
    ######################################################################
    # This function print a formated string to look like the graph
    ######################################################################
    text = ''
    for nodeId, node in graph.node.items():
        text += '(noeud, ' + str(nodeId) + ', ('
        i = False
        for arc in node.arcs:
            if i:
                text += ', '
            else:
                i = True
            text += "(" + str(arc.node1.id if arc.node1.id !=
                              nodeId else arc.node2.id) + ', ' + str(arc.time) + ')'
        text += '))\n'
    print(text)


g = creerGraph("villes.txt")
lireGraph(g)
