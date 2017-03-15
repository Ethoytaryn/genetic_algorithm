from random import choice, randint

from src.Metier.Scorpion import scorpion_identique


def selection_parents_tournoi(info_scorpion_energie_portee_note):

    population_parent = []

    while len(population_parent) < len(info_scorpion_energie_portee_note):

        scorpion_note_1 = choice(info_scorpion_energie_portee_note)
        continuer = 1
        while continuer:
            scorpion_note_2 = choice(info_scorpion_energie_portee_note)
            if scorpion_identique(scorpion_note_1[0], scorpion_note_2[0]) == 0:
                continuer = 0

        winner = duel(scorpion_note_1, scorpion_note_2)
        population_parent.append(winner)

    return population_parent


def duel(couple_scorpion_note_1, couple_scorpion_note_2):
    somme = couple_scorpion_note_1[3] + couple_scorpion_note_2[3]
    chance1 = (couple_scorpion_note_1[3] / somme)*100
    n = randint(0, 100)
    if n < chance1:
        return couple_scorpion_note_1[0]
    else:
        return couple_scorpion_note_2[0]






