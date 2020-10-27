#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def exo1(fichier_1, fichier_2):
    with open(fichier_1, "r", encoding="utf-8") as f_1, open(fichier_2, "r", encoding="utf-8") as f_2:
        x = f_1.readlines()
        y = f_2.readlines()
        for i in x:
            for j in y:
                if i != j:
                    print(f"diff {i} {j}")
                    break
                else:
                    print("papa")

def exo2(ancien_fichier):
    with open(ancien_fichier, encoding="utf-8") as origin, open("espace.txt", "w", encoding="utf-8") as copy:
        contenu = origin.read()
        for i in contenu:
            if i == " ":
                copy.write("   ")
            else:
                copy.write(i)

def exo3(le_fichier):
    with open(le_fichier, encoding="utf-8") as notes, open("note_lettre.txt", "w", encoding="utf-8") as ABCD:
        for ligne in notes:
            note = int(ligne)
            for i in PERCENTAGE_TO_LETTER:
                if note in range(PERCENTAGE_TO_LETTER[i][0], PERCENTAGE_TO_LETTER[i][1]):
                    ABCD.write(f"Note:{notes.readline().strip()}, Pourcentage en lettre: {i}\n")


exo3("notes.txt")

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #exo1("exemple.txt", "le1.txt")
    #exo2("exemple.txt")
    pass