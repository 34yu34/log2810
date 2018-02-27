MAX = 100000


class DjikstraNode:
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
                nodes[currentNode].weight += 15
            else:
                nodes[currentNode].fuelNodeFuel = 100
                nodes[currentNode].fuelNodeWeight += 15
    return getSolution(nodes, currentNode, currentNodeType)


def selectNextNode(nodes):
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


def getSolution(nodes, currentNode, currentNodeType):
    solution = []
    if not(currentNode):
        return []
    node = nodes[currentNode]
    while True:
        solution.append(node.node)
        if currentNodeType == "weight":
            if not(node.ancientNode):
                break
            node = nodes[node.ancientNode]
            currentNodeType = node.ancientNodeType
        else:
            if not(node.fuelNodeAncientNode):
                break
            node = node.fuelNodeAncientNode
            currentNodeType = node.fuelNodeAncientNodeType
    solution.reverse()
    return solution


def updateNodes(nodes, currentNode, currentNodeType, endNode, fuelConsuption):
    nodesTime = currentNode.link()
    for node in nodesTime:
        weight = nodesTime[node] * 60 + \
            nodes[currentNode].getWeight(currentNodeType)
        nodeFuel = nodes[currentNode].getFuel(currentNodeType) - \
            nodesTime[node] * fuelConsuption
        if nodeFuel < 12 and (node != endNode) and not (node.station):
            weight = MAX
        if nodeFuel < 0:
            weight = MAX
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
