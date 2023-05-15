#Dépendances
import csv


def importCsv():
    """
    Fonction de traitement du fichier resultatVF.csv et transformation en liste
    :return: table:list
    """
    table = []
    with open('../../resources/resultatVF.csv') as csvfile:
        lecture_fichier_csv = csv.reader(csvfile,delimiter=',')
        for ligne in lecture_fichier_csv:
            table.append(ligne)
    return table


table = importCsv() #Création d'une variable globale qui sera utilisée pour toutes les autres fonctions


def moyenneDevoirs(notes: dict) -> dict:
    """
    Fonction qui à partir des notes de l'entrée 'notes' retourne un dictionnaire avec les moyennes des 5 DS
    :return: dict:dict
    """
    dict = {"DS1": 0, "DS2": 0,"DS3": 0,"DS4": 0,"DS5": 0} #On créer le dictionnaire qui contient les moyennes des DS
    for i in range(1, len(notes)):      # On fait le total des notes de tout les DS
        dict["DS1"] += int(notes[i][2])
        dict["DS2"] += int(notes[i][3])
        dict["DS3"] += int(notes[i][4])
        dict["DS4"] += int(notes[i][5])
        dict["DS5"] += int(notes[i][6])
    dict["DS1"] = round(dict["DS1"] / len(notes), 2) #Puis on calcul les moyennes respectives en arrondisant à 2 chiffres après la virgule
    dict["DS2"] = round(dict["DS2"] / len(notes), 2)
    dict["DS3"] = round(dict["DS3"] / len(notes), 2)
    dict["DS4"] = round(dict["DS4"] / len(notes), 2)
    dict["DS5"] = round(dict["DS5"] / len(notes), 2)
    return dict


def moyenneEleves(notes: dict) -> list:
    """
    Fonction qui à partir des notes de l'entrée 'notes' retourne une liste de dictionnaire comprenant le Nom & Prénom de l'élève ainsi que sa moyenne général
    :return: moyenneEleves:dict
    """
    moyenneeleves = []
    for i in range(1, len(notes)): #Pour chaque élève on créer un dictionnaire avec Nom,Prénom et Moyenne qui correspond
        temp_dict = {}
        temp_dict["Nom"] = notes[i][0]
        temp_dict["Prénom"] = notes[i][1]
        temp_dict["Moyenne"] = (int(notes[i][2]) + int(notes[i][3]) + int(notes[i][4]) + int(notes[i][5]) + int(notes[i][6])) / 5
        moyenneEleves.append(temp_dict)
    return moyenneEleves


def annexeNotesByMoyennes(l: list) -> list:
    """
    Fonction qui permet à partir des moyennes des élèves de la fonction moyenneEleves de récupérer uniquement les notes sous forme de liste
    :return: new_l:list
    """
    new_l = []
    for i in range(len(l)): #Pour chaque élève on ne conserve que la moyenne en chiffre
        new_l.append(l[i]["Moyenne"])
    return new_l


def annexeTriDecroissant(l: list) -> list:
    """
    Fonction qui permet à partir de la liste des notes des élèves de la fonction annexeNotesByMoyennes de trier les notes par ordre décroissant
    (modèle de tri par sélection)
    :return: l:list
    """
    n = len(l)
    for i in range(0, n - 1):
        indexminimum = i
        for j in range(i + 1, n):
            if l[j] > l[indexminimum]:
                indexminimum = j
        if indexminimum != i:
            l[i], l[indexminimum] = l[indexminimum], l[i]
    return l


def moyennesDecroissant(notes: dict) -> list:
    """
    Fonction qui permet à partir des notes de l'entrée 'notes' et des moyennes des élèves d'établir un classement de la plus grosse à la plus faible moyenne sous forme de liste
    :return: moyennesDecroissant:list
    """
    moyennes = moyenneEleves(notes) #On récupère les moyennes des élèves
    moyennes_notes = annexeNotesByMoyennes(moyennes) #On récupère uniquement les notes
    moyennes_notes_triees = annexeTriDecroissant(moyennes_notes) #On les tri dans l'ordre décroissant
    moyennesDecroissant = []
    for i in range(len(moyennes_notes_triees)): #On ré-attribue les moyennes triés aux élèves
        for j in range(len(moyennes_notes)):
            if moyennes[j]["Moyenne"] == moyennes_notes_triees[i]:
                moyennesDecroissant.append([moyennes[j]["Nom"],moyennes_notes_triees[i]])
    return moyennesDecroissant