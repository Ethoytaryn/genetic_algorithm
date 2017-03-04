from random import random, randrange, randint

from src.Metier.Scorpion import generate_scorpion
from src.Tools.Math import generation_angle_aleatoire, generation_longueur_aleatoire, variance, moyenne
from src.Tools.Physique import calculer_fitness, calculer_energie_cinetique_max_generation, calculer_portee

from src.Metier.Parametre_simulation import CHANCE_TO_MUTATE, POPULATION_COUNT


def muter_angle_tir(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de l'angle en rad

        :rtype:
    """
    scorpion[0] = generation_angle_aleatoire()
    return scorpion


def muter_longueur_bras(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[1] = generation_longueur_aleatoire()
    return scorpion


def muter_longueur_base_bras(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[2] = generation_longueur_aleatoire()
    return scorpion


def muter_hauteur_bras(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[3] = generation_longueur_aleatoire()
    return scorpion


def muter_longueur_corde(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[4] = generation_longueur_aleatoire()
    return scorpion


def muter_longueur_fleche(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[5] = generation_longueur_aleatoire()
    return scorpion


def muter_rayon_fleche(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[6] = generation_longueur_aleatoire()
    return scorpion


def muter_masse_volumique(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[7] = generation_longueur_aleatoire()
    return scorpion


def muter_module_Young(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[8] = generation_longueur_aleatoire()
    return scorpion


def muter_coefficient_poisson(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    scorpion[9] = generation_longueur_aleatoire()
    return scorpion


def scorpion_different(scorpion1, scorpion2):
    note = 0
    for i in range(len(scorpion1)):
        if scorpion1[i] == scorpion2[i]:
            note += 1
    if note == 10:
        return 0
    else:
        return 1


def generer_enfants(scorpion1, scorpion2):
    enfant1 = [scorpion1[0],
               scorpion1[1],
               scorpion1[2],
               scorpion1[3],
               scorpion1[4],
               scorpion2[5],
               scorpion2[6],
               scorpion2[7],
               scorpion2[8],
               scorpion2[9]
               ]
    enfant2 = [scorpion1[0],
               scorpion2[1],
               scorpion1[2],
               scorpion2[3],
               scorpion1[4],
               scorpion2[5],
               scorpion1[6],
               scorpion2[7],
               scorpion1[8],
               scorpion2[9]
               ]
    return enfant1, enfant2

def generer_population(nbre):
    """
            Fonction generatrice de N individus de type genetic_algorithm
    """
    return [generate_scorpion() for _ in range(nbre)]


def evaluation_individu(scorpion, energie_cinetique_max_tnt, variance_portee):
    """
            Fonction d"évaluation d'un scorpion

            On évalue chaque individu individuellement.

            :rtype: float
    """
    return calculer_fitness(scorpion, energie_cinetique_max_tnt, variance_portee)


def calculer_note_moyenne(notes):
    """
        Calcul la valeur moyenne de la note de la génération.
    """
    return moyenne(notes)


def calculer_portee_moyenne(tableau_portee):
    return moyenne(tableau_portee)


def calculer_energie_max(population):
    """
        determine la valeur maximal de l'énergie pour la génération.
    """
    return calculer_energie_cinetique_max_generation(population)


def mutation_individu(scorpion):
    if random() < CHANCE_TO_MUTATE:
        gene = randrange(0, 9, 1)
        if gene == 0:
            scorpion = muter_angle(scorpion)
        elif gene in [1, 2, 3, 4, 5, 6]:
            scorpion = muter_longueur(scorpion, gene)
    return scorpion


def selection_parents_tournoi(couples_scorpion_note):

    population_parent = []

    while len(population_parent) < POPULATION_COUNT:
        challenger1 = randrange(0, POPULATION_COUNT-1, 1)
        continuer = 1
        while continuer:
            challenger2 = randrange(0, POPULATION_COUNT-1, 1)
            if challenger2 != challenger1:
                continuer = 0

        winner = duel(couples_scorpion_note[challenger1], couples_scorpion_note[challenger2])
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


def generer_generation_suivante(population_parent):

    population_enfant = []

    while len(population_enfant) < POPULATION_COUNT:
        parent1 = randrange(0, POPULATION_COUNT-1,1)
        continuer = 1
        while continuer:
            parent2 = randrange(0, POPULATION_COUNT - 1, 1)
            if parent2 != parent1 & parent_different(population_parent[parent1], population_parent[parent2]):
                continuer = 0
        enfant1, enfant2 = generer_enfants(population_parent[parent1],population_parent[parent2])
        enfant1 = mutation_individu(enfant1)
        enfant2 = mutation_individu(enfant2)
        population_enfant.append(enfant1)
        population_enfant.append(enfant2)
    return population_enfant


def parent_different(scorpion1, scorpion2):
    return scorpion_different(scorpion1,scorpion2)


def calculer_variance(tableau_note):
    return variance(tableau_note)


def calculer_variance_portee(population):
    portees_population = []
    for scorpion in population:
        portee = calculer_portee(scorpion)
        portees_population.append(portee)

    return variance(portees_population)


