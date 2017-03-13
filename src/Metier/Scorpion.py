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
from src.Tools.Physique import calculer_ressort, calculer_longueur_vide, calculer_longueur_deplacement, \
    calculer_masse_projectile,\
    calculer_vitesse, calculer_portee,\
    calculer_energie_cinetique_joule, \
    calculer_fleche_bras_max,\
    calculer_energie_cinetique_tnt


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


def scorpion_identique(scorpion1, scorpion2):
    note = 0
    for i in range(len(scorpion1)):
        if scorpion1[i] == scorpion2[i]:
            note += 1
    if note == 10:
        return 1
    else:
        return 0


def calculer_ressort_scorpion(scorpion):
    return calculer_ressort(
        obtenir_module_young_materiau(scorpion),
        obtenir_coeff_poisson_materiau(scorpion))


def calculer_longueur_vide_scorpion(scorpion):
    return calculer_longueur_vide(
        obtenir_longueur_bras(scorpion),
        obtenir_longueur_corde(scorpion)
    )


def calculer_longueur_deplacement_scorpion(scorpion):
    return calculer_longueur_deplacement(
        obtenir_longueur_fleche(scorpion),
        obtenir_longueur_bras(scorpion),
        obtenir_longueur_corde(scorpion)
    )


def calculer_masse_projectile_scorpion(scorpion):
    return calculer_masse_projectile(
        obtenir_masse_volumique_materiau(scorpion),
        obtenir_rayon_fleche(scorpion),
        obtenir_longueur_fleche(scorpion)
    )


def calculer_vitesse_scorpion(scorpion):
    return calculer_vitesse(
        obtenir_module_young_materiau(scorpion),
        obtenir_coeff_poisson_materiau(scorpion),
        obtenir_longueur_fleche(scorpion),
        obtenir_longueur_bras(scorpion),
        obtenir_longueur_corde(scorpion),
        obtenir_masse_volumique_materiau(scorpion),
        obtenir_rayon_fleche(scorpion)
    )


def calculer_portee_scorpion(scorpion):
    return calculer_portee(
        obtenir_angle(scorpion),
        obtenir_module_young_materiau(scorpion),
        obtenir_coeff_poisson_materiau(scorpion),
        obtenir_longueur_fleche(scorpion),
        obtenir_longueur_bras(scorpion),
        obtenir_longueur_corde(scorpion),
        obtenir_masse_volumique_materiau(scorpion),
        obtenir_rayon_fleche(scorpion)
    )


def calculer_energie_cinetique_joule_scorpion(scorpion):
    return calculer_energie_cinetique_joule(
        obtenir_masse_volumique_materiau(scorpion),
        obtenir_rayon_fleche(scorpion),
        obtenir_longueur_fleche(scorpion),
        obtenir_module_young_materiau(scorpion),
        obtenir_coeff_poisson_materiau(scorpion),
        obtenir_longueur_bras(scorpion),
        obtenir_longueur_corde(scorpion)
    )


def calculer_energie_cinetique_tnt_scorpion(scorpion):
    return calculer_energie_cinetique_tnt(calculer_energie_cinetique_joule_scorpion(scorpion))


def calculer_fleche_bras_max_scorpion(scorpion):
    return calculer_fleche_bras_max(
        obtenir_module_young_materiau(scorpion),
        obtenir_coeff_poisson_materiau(scorpion),
        obtenir_longueur_fleche(scorpion),
        obtenir_longueur_bras(scorpion),
        obtenir_longueur_corde(scorpion),
        obtenir_longueur_base_bras(scorpion),
        obtenir_hauteur_base_bras(scorpion)
    )


def afficher_scorpion(scorpion):
    print("caracteristique du scorpion :")
    print("Angle de tir : " + str(obtenir_angle(scorpion)) + " rad")
    print("Longueur du bras :" + str(obtenir_longueur_bras(scorpion)) + " m")
    print("Largeur de la base du bras : " + str(obtenir_longueur_base_bras(scorpion)) + " m")
    print("Hauteur de la base du bras : " + str(obtenir_hauteur_base_bras(scorpion)) + " m")
    print("Longueur de la corde : " + str(obtenir_longueur_corde(scorpion)) + " m")
    print("Longueur de la fleche : " + str(obtenir_longueur_fleche(scorpion)) + " m")
    print("Rayon de la fleche" + str(obtenir_rayon_fleche(scorpion)) + " m")
    print("Masse volumique : " + str(obtenir_masse_volumique_materiau(scorpion)) + " kg / m3")
    print("Module d'Young : " + str(obtenir_module_young_materiau(scorpion)) + " GPa")
    print("Coefficient de poisson : " + str(obtenir_coeff_poisson_materiau(scorpion)))
    print("Masse du projectile : " + str(calculer_masse_projectile_scorpion(scorpion))+" kg")
    print("Ressort " + str(calculer_ressort_scorpion(scorpion)) + " en N / m")
    print("Vitesse du projectile :" + str(calculer_vitesse_scorpion(scorpion))+"en m / s")
    print("Portee du scorpion : "+str(calculer_portee_scorpion(scorpion))+" en m")

