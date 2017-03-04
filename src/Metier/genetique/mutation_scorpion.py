from src.Metier.Parametre_simulation import \
    CHANCE_TO_MUTATE,\
    LIMITE_ANGLE_BASSE,\
    LIMITE_ANGLE_HAUTE,\
    LIMITE_LONGUEUR_BASSE,\
    LIMITE_LONGUEUR_HAUTE, \
    LIMITE_MASSE_VOL_BASSE,\
    LIMITE_MASSE_VOL_HAUTE, \
    LIMITE_MODULE_YOUNG_BASSE, \
    LIMITE_MODULE_YOUNG_HAUTE, \
    LIMITE_POISSON_BASSE,\
    LIMITE_POISSON_HAUTE
from random import\
    random, \
    randrange, \
    uniform

from src.Metier.Scorpion import \
    obtenir_angle, \
    obtenir_longueur_bras, \
    obtenir_longueur_base_bras


def muter_angle_tir(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de l'angle en rad

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_ANGLE_BASSE, LIMITE_ANGLE_HAUTE)
        if new_value != obtenir_angle(scorpion):
            print(new_value)
            scorpion[0] = new_value
            continuer = 0
    return scorpion


def muter_longueur_bras(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_bras(scorpion):
            print(new_value)
            scorpion[1] = new_value
            continuer = 0
    return scorpion


def muter_longueur_base_bras(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            print(new_value)
            scorpion[2] = new_value
            continuer = 0
    return scorpion


def muter_hauteur_base_bras(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            print(new_value)
            scorpion[3] = new_value
            continuer = 0
    return scorpion


def muter_longueur_corde(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            print(new_value)
            scorpion[4] = new_value
            continuer = 0
    return scorpion


def muter_longueur_fleche(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            print(new_value)
            scorpion[5] = new_value
            continuer = 0
    return scorpion


def muter_rayon_fleche(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la longueur du bras en m

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            print(new_value)
            scorpion[6] = new_value
            continuer = 0
    return scorpion


def muter_masse_volumique(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur de la masse volumique en kg / m3

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_MASSE_VOL_BASSE, LIMITE_MASSE_VOL_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            print(new_value)
            scorpion[7] = new_value
            continuer = 0
    return scorpion


def muter_module_young(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur du module d'Young en GPa
        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_MODULE_YOUNG_BASSE, LIMITE_MODULE_YOUNG_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            print(new_value)
            scorpion[8] = new_value
            continuer = 0
    return scorpion


def muter_coefficient_poisson(scorpion):
    """
        Fonction qui simule une mutation en regenerant la valeur du coefficient de poisson en

        :rtype:
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_POISSON_BASSE, LIMITE_POISSON_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            print(new_value)
            scorpion[9] = new_value
            continuer = 0
    return scorpion


def mutation_individu(scorpion):
    """
        Fonction qui peut entraîner une mutation (dependant de la constante CHANCE_TO_MUTATE) sur un gene aléatoire

        :rtype:
    """
    if random() < CHANCE_TO_MUTATE:
        gene = randrange(0, 9, 1)
        if gene == 0:
            scorpion = muter_angle_tir(scorpion)
        elif gene == 1:
            scorpion = muter_longueur_bras(scorpion)
        elif gene == 2:
            scorpion = muter_longueur_base_bras(scorpion)
        elif gene == 3:
            scorpion = muter_hauteur_base_bras(scorpion)
        elif gene == 4:
            scorpion = muter_longueur_corde(scorpion)
        elif gene == 5:
            scorpion = muter_longueur_fleche(scorpion)
        elif gene == 6:
            scorpion = muter_rayon_fleche(scorpion)
        elif gene == 7:
            scorpion = muter_masse_volumique(scorpion)
        elif gene == 8:
            scorpion = muter_module_young(scorpion)
        elif gene == 9:
            scorpion = muter_coefficient_poisson(scorpion)
    return scorpion
