#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def comparer_fichier(nomfichier1, nomfichier2):
    with open(nomfichier1, 'r', encoding='utf-8') as fichier1, open(nomfichier2, 'r', encoding='utf-8') as fichier2:
        contenu_fichier1 = fichier1.readlines()
        contenu_fichier2 = fichier2.readlines()

    for i in range(len(contenu_fichier1)):
        if contenu_fichier1[i] == contenu_fichier2[i]:
            return True
        else:
            return False

def recopier_fichier (nom_fichier, fichier_écrire):
    with open(nom_fichier, "r", encoding="utf-8") as fichier, open(nom_fichier, "w", encoding="utf-8") as écrire:
        for ligne in fichier:
            mot = ligne.split()
            ligne_espacées = "   ".join(mot)
            écrire.write(ligne_espacées)

def exercice3(nom_fichier, nouveau_fichier):
    with open(nom_fichier, 'r') as fichier, open(nouveau_fichier, 'w') as écrire:
        notes = fichier.readlines()
        for i in range(len(notes)):
            if notes[i]>=90:
                écrire.write(notes[i]+' '+'A')
            elif 80 <= notes[i] < 90:
                écrire.write(notes[i] + ' ' + 'B')
            elif 70 <= notes[i] < 80:
                écrire.write(notes[i] + ' ' + 'C')
            elif 60 <= notes[i]< 70:
                écrire.write(notes[i] + ' ' + 'D')
            else:
                écrire.write(notes[i] + ' ' + 'F')

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #print(comparer_fichier('./exemple.txt', './exemple.txt'))
    #recopier_fichier('./exemple.txt', './ exemple_copie')
    exercice3('./notes.txt')
    pass
