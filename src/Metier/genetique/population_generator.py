import copy
from random import random, randrange

from src.Metier.Scorpion import generate_scorpion, scorpion_identique
from src.Metier.genetique.mutation_scorpion import mutation_individu
from src.Metier.genetique.tournament_selection import selection_parents_tournoi


def generer_population(nbre):
    """
            Fonction generatrice de N individus de type genetic_algorithm


    """
    return [generate_scorpion() for _ in range(nbre)]


def generer_generation_suivante(info_scorpion_energie_portee_note, chance_to_hybrid, chance_to_mutate):

    population_parent = selection_parents_tournoi(info_scorpion_energie_portee_note)
    population_enfant = []
    population_count = len(population_parent)
    while len(population_enfant) < population_count:

        id_parent1 = randrange(0, population_count-1, 1)

        continuer = 1
        while continuer:
            id_parent2 = randrange(0, population_count - 1, 1)
            if id_parent2 != id_parent1:
                identique = scorpion_identique(population_parent[id_parent1], population_parent[id_parent2])
                if identique == 0:
                    continuer = 0

        enfant1, enfant2 = generer_enfants(
            population_parent[id_parent1], population_parent[id_parent2], chance_to_hybrid)
        enfant1 = mutation_individu(enfant1, chance_to_mutate)
        enfant2 = mutation_individu(enfant2, chance_to_mutate)
        population_enfant.append(enfant1)
        population_enfant.append(enfant2)

    return population_enfant


def generer_enfants(pere, mere, coeff_hybrid):
    """
        Fonction générant les enfants de deux scorpions avec un taux d'hybridation.

        Si l'hybridation n'a pas lieu, l'enfant est de manière aléatoire un clone du père ou de la mère
    """
    return generation_enfant_croise(pere, mere, coeff_hybrid), generation_enfant(pere, mere, coeff_hybrid)


def generation_enfant_croise(pere, mere, coeff_hybrid):
    if random() < coeff_hybrid:
        enfant = [pere[0],
                  mere[1],
                  pere[2],
                  mere[3],
                  pere[4],
                  mere[5],
                  pere[6],
                  mere[7],
                  pere[8],
                  mere[9]
                  ]
    else:
        choix = randrange(0, 1, 1)
        if choix == 0:
            enfant = copy.copy(pere)
        else:
            enfant = copy.copy(mere)
    return enfant


def generation_enfant(pere, mere, coeff_hybrid):
    if random() < coeff_hybrid:
        enfant = [pere[0],
                  pere[1],
                  pere[2],
                  pere[3],
                  pere[4],
                  mere[5],
                  mere[6],
                  mere[7],
                  mere[8],
                  mere[9]
                  ]
    else:
        choix = randrange(0, 1, 1)
        if choix == 0:
            enfant = copy.copy(pere)
        else:
            enfant = copy.copy(mere)
    return enfant
