from random import randint

from src.Metier.Parametre_simulation import POPULATION_COUNT
from src.Metier.genetique.mutation_scorpion import *


def selection_parents_tournoi(couples_scorpion_note):

    population_parent = []

    while len(population_parent) < POPULATION_COUNT:

        id_challenger1 = randrange(0, POPULATION_COUNT-1, 1)
        continuer = 1
        while continuer:
            id_challenger2 = randrange(0, POPULATION_COUNT-1, 1)
            if id_challenger1 != id_challenger2:
                continuer = 0

        winner = duel(couples_scorpion_note[id_challenger1], couples_scorpion_note[id_challenger2])
        population_parent.append(winner)

    return population_parent


def duel(couple_scorpion_note_1, couple_scorpion_note_2):
    somme = couple_scorpion_note_1[1] + couple_scorpion_note_2[1]

    chance1 = (couple_scorpion_note_1[1] / somme)*100
    n = randint(0, 100)
    if n < chance1:
        return couple_scorpion_note_1[0]
    else:
        return couple_scorpion_note_2[0]





