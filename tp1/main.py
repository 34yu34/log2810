######################################################################
# Auteur : Obossou Ema-Wo, Billy Bouchard, Gnaga Dogbeda Georges
# Matricule: 1780896, 1850477, 1870143
# Version Python: 3.6
######################################################################
from graph import Graph
from graph import Node
from graph import Arc
from djikstra import djikstra
from six.moves import reduce

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
    variables = ["", "", ""]
    current = 0
    for char in line:
        if char == ',':
            current += 1
            continue
        variables[current] += char
    node1 = int(variables[0])
    node2 = int(variables[1])
    time = int(variables[2])
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
    for nodeId, node in graph.nodes.items():
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


def plusCourtChemin(graph, startNodeId, endNodeId, vehiculeType):
    if vehiculeType == "voiture":
        solution = djikstra(graph, startNodeId, endNodeId, 5)
        company = "Cheap Car"
        if solution == []:
            solution = djikstra(graph, startNodeId, endNodeId, 3)
            company = "Super Car"
            if solution == []:
                return "ne pas faire le braquage"
    if vehiculeType == "pick-up":
        solution = djikstra(graph, startNodeId, endNodeId, 7)
        company = "Cheap Car"
        if solution == []:
            solution = djikstra(graph, startNodeId, endNodeId, 4)
            company = "Super Car"
            if solution == []:
                return "ne pas faire le braquage"
    if vehiculeType == "fourgon":
        solution = djikstra(graph, startNodeId, endNodeId, 8)
        company = "Cheap Car"
        if solution == []:
            solution = djikstra(graph, startNodeId, endNodeId, 6)
            company = "Super Car"
            if solution == []:
                return "ne pas faire le braquage"
    solution = map(lambda x: str(x.id) + "->", solution)
    answer = "il faut passer par : " + reduce(lambda x, y: x + y, solution)
    answer += "avec un " + vehiculeType + " de " + company
    return answer


g = creerGraph("villes.txt")
print(plusCourtChemin(g, 1, 15, "voiture"))

list
