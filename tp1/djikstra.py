######################################################################
# Auteur : Obossou Ema-Wo, Billy Bouchard, Gnaga Dogbeda Georges
# Matricule: 1780896, 1850477, 1870143
# Version Python: 3.6
######################################################################
MAX = 100000


class DjikstraNode:
    ######################################################################
    # Custom made class to have every properties necessary in order
    # to make djikstra function work easily
    ######################################################################
    def __init__(self, node, startNode):
        self.node = node
        # if a node contains more fuel it is kept
        self.fuelNodeWeight = MAX if not startNode else 0
        self.fuelNodeFuel = 0 if not startNode else 100
        self.fuelNodeAncientNode = None
        self.fuelNodeAncientNodeType = "weight"
        self.fuelNodeVisited = False
        # for the weight Node
        self.weight = MAX if not startNode else 0
        self.fuel = 0 if not startNode else 100
        self.ancientNode = None
        self.ancientNodeType = "weight"
        self.visited = False

    def getWeight(self, type):
        if type == "weight":
            return self.weight
        else:
            return self.fuelNodeWeight

    def getFuel(self, type):
        if type == "weight":
            return self.fuel
        else:
            return self.fuelNodeFuel

    def ancientNode(self, type):
        if type == "weight":
            return self.ancientNode
        else:
            return self.fuelNodeAncientNode

    def ancientNodeType(self, type):
        if type == "weight":
            return self.ancientNodeType
        else:
            return self.fuelNodeAncientNodeType

    def visited(self, type):
        if type == "weight":
            return self.visited
        else:
            return self.fuelNodeVisited


def djikstra(graph, startNodeId, endNodeId, fuelConsuption):
    ######################################################################
    # Algorith tht find the smallest path through a graph givn
    # a certain fuel consuption between startNodeId and endNodeId
    ######################################################################
    endNode = graph[endNodeId]
    nodes = {}
    for node in graph:
        nodes[node] = DjikstraNode(node, node.id == startNodeId)
    currentNode, currentNodeType = selectNextNode(nodes)
    while (currentNode != endNode):
        nodes = updateNodes(nodes, currentNode,
                            currentNodeType, endNode, fuelConsuption)
        currentNode, currentNodeType = selectNextNode(nodes)
        if not(currentNode):
            break
        if currentNode.station:
            if currentNodeType == "weight":
                nodes[currentNode].fuel = 100
            else:
                nodes[currentNode].fuelNodeFuel = 100
    return getSolution(nodes, currentNode, currentNodeType)


def selectNextNode(nodes):
    ######################################################################
    # This function select the next smallest weight node and returns
    # its type
    ######################################################################
    smallest = MAX
    smallestNode = None
    smallestNodeType = "weight"
    for node in nodes:
        if (nodes[node].weight < smallest and not(nodes[node].visited)):
            smallest = nodes[node].weight
            smallestNode = node
            smallestNodeType = "weight"
        if (nodes[node].fuelNodeWeight < smallest and not(nodes[node].fuelNodeVisited)):
            smallest = nodes[node].fuelNodeWeight
            smallestNode = node
            smallestNodeType = "fuel"
    return smallestNode, smallestNodeType


def getSolution(nodes, endNode, endNodeType):
    ######################################################################
    # Functions take the nodes dictionnary and retrun the way to get to
    # the end node from the start node in a list
    ######################################################################
    solution = []
    if not(endNode):
        return []
    node = nodes[endNode]
    while True:
        solution.append(node.node)
        if endNodeType == "weight":
            if not(node.ancientNode):
                break
            node = nodes[node.ancientNode]
            endNodeType = node.ancientNodeType
        else:
            if not(node.fuelNodeAncientNode):
                break
            node = node.fuelNodeAncientNode
            endNodeType = node.fuelNodeAncientNodeType
    solution.reverse()
    return solution


def updateNodes(nodes, currentNode, currentNodeType, endNode, fuelConsuption):
    ######################################################################
    # This function update the nodes from the current node
    # it modify the weight of every node connecting to it
    ######################################################################
    nodesTime = currentNode.link()
    for node in nodesTime:
        weight = nodesTime[node] * 60 + \
            nodes[currentNode].getWeight(currentNodeType)
        nodeFuel = nodes[currentNode].getFuel(currentNodeType) - \
            nodesTime[node] * fuelConsuption
        if nodeFuel < 0:
            weight = MAX
        elif nodeFuel < 12 and (node != endNode) and not (node.station):
            weight = MAX
        if node.station:
            weight += 15
        if not(nodes[node].fuelNodeVisited) and (nodeFuel >= nodes[node].fuelNodeFuel) and (weight <= nodes[node].fuelNodeWeight):
            nodes[node].fuelNodeWeight = weight
            nodes[node].fuelNodeAncientNode = currentNode
            nodes[node].fuelNodeAncientNodeType = currentNodeType
            nodes[node].fuelNodeFuel = nodeFuel
        if not(nodes[node].visited) and (weight < nodes[node].weight):
            nodes[node].weight = weight
            nodes[node].ancientNode = currentNode
            nodes[node].ancientNodeType = currentNodeType
            nodes[node].fuel = nodeFuel
    if currentNodeType == "weight":
        nodes[currentNode].visited = True
    else:
        nodes[currentNode].fuelNodeVisited = True
    return nodes
