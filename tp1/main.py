######################################################################
# Auteur : Obossou Ema-Wo, Billy Bouchard, Gnaga Dogbeda Georges
# Matricule: 1780896, 1850477, 1870143
# Version Python: 3.6
######################################################################
from graph import Graph
from graph import Node
from graph import Arc
from djikstra import djikstra
import re
from six.moves import reduce
from six.moves import input

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
    ######################################################################
    # Algorithm to select the best company and if the stealing
    # should be done
    ######################################################################
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
    answer = "il faut passer par : \n\t\t" + \
        reduce(lambda x, y: x + y, solution)
    answer = re.sub(r'->$', '', answer)
    answer += "\navec" + (" une " if vehiculeType == "voiture" else " un ") + \
        vehiculeType + " de " + company
    return answer

#g = creerGraph("villes.txt")
#print(plusCourtChemin(g, 1, 20, "pick-up"))

choice = None 
g = None
depart = None
arrive = None
nomFichier= None
typeVehicule =None

while True:
    g = creerGraph("villes.txt")
    print(plusCourtChemin(g, 1, 3, "pick-up"))
    print(" veillez choisir svp le menu que vous voulez excecuter\n ")
    print("Entrez 1 pour la MisAJourCarte")
    print("Entrez 2 pour CourtCheminSecuritaire")
    print("Entrez 0 pour. Quitter")
    choice = input(" >>  ")
    if choice != "1":
        print( " \n****choix invalide svp entrez un choix valide**\n")
    if choice == "1" :
        print(choice)
        print(" entrez le nom du fichier de la carte")
        nomFichier = input(" >>  ")
        g = creerGraph(nomFichier)
        #return "ok "
        print("\nEntrez 2 pour CourtCheminSecuritaire")
        print("Entrez 0 pour. Quitter")
        choice1 = input(" >>  ")
        if choice1 != "0" or choice1 != "2":
            print(" ****** Données entrées invalides ******* ")
        if choice1 == "2" :
            print("nombre " + choice)
            print("Entrez le point du lieu de braquaque (point) ")
            depart = input(" >>  ")
            print("Entrez le point de destination apres le braquage ")
            arrive = input(" >>  ")
            print("Entrez le type de vehicule a utiliser pour le braquage ")
            typeVehicule = input(" >>  ")
            print(plusCourtChemin(g, depart, arrive, typeVehicule))
        # return "ok "
            
        if choice1 == "0" :
            print(choice)
            print("\n Quitter")
            #return"ok "

  #*  os.system('clear')
   # ch = choice.lower()
   # if ch == '':
    #    menu_actions['main_menu']()
    #else:
     #   try:
      #      menu_actions[ch]()
       # except KeyError:
        #    print(" selection invalide, veillez rechoisir svp .\n")
         #  
    #return*/
