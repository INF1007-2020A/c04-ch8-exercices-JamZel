PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import json
from recettes import *
from os import path

# TODO: Définissez vos fonction ici
def difference(file_1, file_2):
    with open(f"./Files_needed/{file_1}", 'r', encoding='utf-8') as first_file,\
         open(f"./Files_needed/{file_2}", 'r', encoding='utf-8') as second_file:
        for row in first_file:
            for ligne in second_file:
                if row != ligne:
                    return print("Il y a une différence entre les deux fichiers au niveau de ces deux lignes:\n\n"
                                 f"Ligne du fichier {file_1}:\n"
                                 f"{row}\n"
                                 f"Ligne du fichier {file_2}:\n"
                                 f"{ligne}")
                break



def its_a_triple(file):
    with open(f"./Files_needed/{file}", 'r', encoding='utf-8') as reading_file,\
         open("./Files_needed/triple_space.txt", "w", encoding='utf-8') as writing_file:

        for row in reading_file:
            for char in row:
                if char != ' ':
                    writing_file.write(char)
                else:
                    writing_file.write('   ')


def grades():
    with open("./Files_needed/notes.txt", 'r', encoding='utf-8') as grade,\
         open("./Files_needed/notes_lettre.txt", 'w', encoding='utf_8') as letter:

        for row in grade:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] < int(row) <= value[1]:
                    letter.write(f"{row.strip()} {key}\n")
                    break
                else:
                    continue


def recette():
    if path.exists("./Files_needed/recettes.json"):
        with open("./Files_needed/recettes.json", 'r') as file:
            recipe = json.load(file)
    else:
        recipe = {}

    while True:
        user_input = input("Veuillez selectionner une option:\n"
                           "1) Ajouter une recette\n"
                           "2) Consulter les recettes\n"
                           "3) Supprimer une recette\n"
                           "4) Quitter\n")

        if user_input == "1":
            recipe = add_recipes(recipe)
            json.dump(recipe, open("./Files_needed/recettes.json", 'w'))

        if user_input == "2":
            print(recipe)

        if user_input == "3":
            while True:
                supr = input("Entrer le nom de la recette:\n")
                if supr in recipe:
                    del recipe[supr]
                    print(f"La recette {supr} a été supprimée")
                    json.dump(recipe, open("./Files_needed/recettes.json", 'w'))
                    break
                else:
                    print(f"La recette {supr} n'existe pas, veuillez consulter les recettes disponibles")

        if user_input == "4":
            print("Bye")
            break


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    difference('exemple.txt', 'comparaison.txt')
    its_a_triple('exemple.txt')
    grades()
    recette()
    pass
