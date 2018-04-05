from automate import *
from solution import *


def creerAutomate(file_name):
    file = open(file_name, 'r')
    name = file.readline()[:-2]
    automate = Automate(name)
    for line in file:
        automate << (line.replace("\n", ""))
    return automate


def trouverMotDePasse(variantes, no):
    solver = automates[str(no)]
    for var in variantes:
        if solver.solve(var):
            return var


def traiterLesEntrees(file_name):
    file = open(file_name, 'r')
    no = file.readline().replace("\n", "")
    solution = Solution(no)
    for line in file:
        solution << line.replace("\n", "")
    return solution


def afficherLesMotsDePasse():
    for no in solutions:
        print(solutions[no])


automates = {}
automates['3'] = creerAutomate("regles3.txt")
solutions = {}
solution3 = traiterLesEntrees('variantes3.txt')
solution4 = traiterLesEntrees('variantes4.txt')
solutions[solution4.no] = solution4
solutions[solution3.no] = solution3
afficherLesMotsDePasse()
solution3.reponse = trouverMotDePasse(solution3.variantes, solution3.no)
afficherLesMotsDePasse()
