from automate import *
from solution import *


def creerAutomate(file_name):
    file = open(file_name, 'r')
    name = file.readline().replace("\n", "")
    automate = Automate(name)
    for line in file:
        automate << (line.replace("\n", ""))
    return automate


def trouverMotDePasse(variantes, no):
    solver = automates[no]
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


def menu(erreur):
    get = None
    if erreur:
        print("Cette fonction n'existe pas!")
    print("Que voulez vous faire?")
    print("  (a) Creer l'automates")
    print("  (b) Traiter des requetes")
    print("  (c) Afficher les mots de passe valides obtenus")
    print("  (d) Quitter")
    return input("")


def ln():
    print("\n" * 80)


automates = {}
solutions = {}
get = ""
erreur = False
while get != "d":
    get = menu(erreur)
    if get == 'a':
        erreur = False
        file_name = input("\nQuel est le nom du fichier de regles : ")
        while 'regles' not in file_name:
            print("\nil ne s'agit pas d'un fichier de regles")
            file_name = input("Quel est le nom du fichier de regles : ")
        automate = creerAutomate(file_name)
        automates[automate.name] = automate

    elif get == 'b':
        erreur = False
        file_name = input("\nQuel est le nom du fichier de variantes : ")
        while 'variantes' not in file_name:
            print("\nil ne s'agit pas d'un fichier de variantes")
            file_name = input("Quel est le nom du fichier de variantes : ")
        solution = traiterLesEntrees(file_name)
        solutions[solution.no] = solution
        if solution.no not in automates:
            input("Aucun automate n'existe pour cette solution!\nConfirmer la reception")
        else:
            solutions[solution.no].reponse = trouverMotDePasse(
                solutions[solution.no].variantes, solution.no)

    elif get == 'c':
        erreur = False
        afficherLesMotsDePasse()
        input()

    else:
        erreur = True

print("Merci!")
