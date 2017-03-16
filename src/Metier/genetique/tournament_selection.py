from random import choice, randint

from src.Metier.Scorpion import \
    scorpion_identique,\
    generate_scorpion_null
from src.Tools.Constante import \
    ZERO


def selection_parents_tournoi(info_scorpion_energie_portee_note):
    """
        Fonction selectionnant les parents à l'aide d'un algorithme de selection par tournoi.

    :param info_scorpion_energie_portee_note: liste d'info scorpion de longueur n
    :type info_scorpion_energie_portee_note: liste_info[scorpion, energie, portee, note]
    :return: scorpions parents
    :rtype: scorpion[n]

    .. seealso:: :func:`src.Metier.genetique.duel`
    """
    population_parent = []

    while len(population_parent) < len(info_scorpion_energie_portee_note):

        scorpion_note_1 = choice(info_scorpion_energie_portee_note)
        scorpion_note_2 = generate_scorpion_null()

        continuer = 1
        while continuer:
            scorpion_note_2 = choice(info_scorpion_energie_portee_note)
            if scorpion_identique(scorpion_note_1[0], scorpion_note_2[0]) == 0:
                continuer = 0

        winner = duel(scorpion_note_1, scorpion_note_2)
        population_parent.append(winner)

    return population_parent


def duel(couple_scorpion_note_1, couple_scorpion_note_2):
    """
        Fonction selectionnant un gagnant entre deux scorpions en fonction de la note du scorpion. Plus la note
         d'un scorpion est eleve, plus il a de chance d'etre selectionner.

    :param couple_scorpion_note_1: liste d'info scorpion de longueur n
    :type couple_scorpion_note_1: liste_info[scorpion, energie, portee, note]
    :param couple_scorpion_note_2: liste d'info scorpion de longueur n
    :type couple_scorpion_note_2: liste_info[scorpion, energie, portee, note]
    :return: scorpions
    :rtype: float[10]
    """
    somme = couple_scorpion_note_1[3] + couple_scorpion_note_2[3]
    if somme == ZERO:
        chance1 = 0.5
    else:
        chance1 = (couple_scorpion_note_1[3] / somme)*100
    n = randint(0, 100)
    if n < chance1:
        return couple_scorpion_note_1[0]
    else:
        return couple_scorpion_note_2[0]
