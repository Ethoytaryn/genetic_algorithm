#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import uniform

from src.Metier.Parametre_simulation import \
    LIMITE_ANGLE_BASSE,\
    LIMITE_ANGLE_HAUTE, \
    LIMITE_MASSE_VOL_BASSE,\
    LIMITE_MASSE_VOL_HAUTE, \
    LIMITE_MODULE_YOUNG_BASSE, \
    LIMITE_MODULE_YOUNG_HAUTE, \
    LIMITE_POISSON_BASSE,\
    LIMITE_POISSON_HAUTE,\
    LIMITE_LONGUEUR_BASSE,\
    LIMITE_LONGUEUR_HAUTE


def generate_scorpion():
    """
        Fonction generatrice d'un individu genetic_algorithm avec des paramètres aléatoires.

        Partie scorpion :
            - angle [0;Pi/2] en rad
            - longueur bras [0.001;1000] en m
            - longueur de la base du bras [0.001; 100] en m
            - hauteur de section du bras [0.001;100] en m
            - longueur de corde [0.001;2000] en m
        Projectile :
            - longueur de la fleche [0.001;15000] en m
            - rayon de la fleche [0.001,100] en m
            - masse volumique de la fleche
            - module d'Young
            - coefficient de poisson

        :return: liste contenant les paramètres du scorpion
        :rtype:
    """
    return[
            uniform(LIMITE_ANGLE_BASSE, LIMITE_ANGLE_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_MASSE_VOL_BASSE, LIMITE_MASSE_VOL_HAUTE),
            uniform(LIMITE_MODULE_YOUNG_BASSE, LIMITE_MODULE_YOUNG_HAUTE),
            uniform(LIMITE_POISSON_BASSE, LIMITE_POISSON_HAUTE)
    ]


def obtenir_angle(scorpion):
    """
        Fonction qui renvoie l'angle du genetic_algorithm en rad

        :rtype: float
    """
    return scorpion[0]


def obtenir_longueur_bras(scorpion):
    """
        Fonction qui renvoie la longueur du bras du genetic_algorithm en m

        :rtype: float
    """
    return scorpion[1]


def obtenir_longueur_base_bras(scorpion):
    """
        Fonction qui renvoie la longueur de la base du bras du genetic_algorithm en m

        :rtype: float
    """
    return scorpion[2]


def obtenir_hauteur_base_bras(scorpion):
    """
        Fonction qui renvoie la hauteur du bras du genetic_algorithm en m

        :rtype: float
    """
    return scorpion[3]


def obtenir_longueur_corde(scorpion):
    """
        Fonction qui renvoie la longueur de la corde du genetic_algorithm en m

        :rtype: float
    """
    return scorpion[4]


def obtenir_longueur_fleche(scorpion):
    """
        Fonction qui renvoie la longueur de la fleche en m

        :rtype: float
    """
    return scorpion[5]


def obtenir_rayon_fleche(scorpion):
    """
        Fonction qui renvoie le rayon de la fleche en m

        :rtype: float
    """
    return scorpion[6]


def obtenir_masse_volumique_materiau(scorpion):
    """
        Fonction qui renvoie la masse volumique du materiau utilisé en kg / m^3

        :rtype: float
    """
    return scorpion[7]


def obtenir_module_young_materiau(scorpion):
    """
        Fonction qui renvoie le module d'Young du materiau utilisé en GPa

        :rtype: float
    """
    return scorpion[8]


def obtenir_coeff_poisson_materiau(scorpion):
    """
        Fonction qui renvoie le coefficient de poisson du materiau utilisé

        :rtype: float
    """
    return scorpion[9]


def scorpion_different(scorpion1, scorpion2):
    note = 0
    for i in range(len(scorpion1)):
        if scorpion1[i] == scorpion2[i]:
            note += 1
    if note == 10:
        return 0
    else:
        return 1