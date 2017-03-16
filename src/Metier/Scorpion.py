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
        Fonction generatrice d'un scorpion avec des paramètres aléatoires.

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
    :rtype: float[10]
    """
    return[
            uniform(LIMITE_ANGLE_BASSE, LIMITE_ANGLE_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE/10),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE/10),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE),
            uniform(LIMITE_MASSE_VOL_BASSE, LIMITE_MASSE_VOL_HAUTE),
            uniform(LIMITE_MODULE_YOUNG_BASSE, LIMITE_MODULE_YOUNG_HAUTE),
            uniform(LIMITE_POISSON_BASSE, LIMITE_POISSON_HAUTE)
    ]


def generate_scorpion_null():
    """
        Fonction generatrice d'un scorpion avec des paramètres tous initialises a 0.0

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
    :rtype: float[10]
    """
    return[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def obtenir_angle(scorpion):
    """
        Fonction qui renvoie l'angle d'un scorpion en rad

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: Angle de tir du scorpion
    :rtype: float
    """
    return scorpion[0]


def obtenir_longueur_bras(scorpion):
    """
        Fonction qui renvoie la longueur du bras d'un scorpion en m

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: Longueur du bras
    :rtype: float
    """
    return scorpion[1]


def obtenir_longueur_base_bras(scorpion):
    """
        Fonction qui renvoie la longueur de la base du bras d'un scorpion en m

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: longueur base du bras
    :rtype: float
    """
    return scorpion[2]


def obtenir_hauteur_base_bras(scorpion):
    """
        Fonction qui renvoie la hauteur de la base du bras d'un scorpion en m

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: hauteur base du bras
    :rtype: float
    """
    return scorpion[3]


def obtenir_longueur_corde(scorpion):
    """
        Fonction qui renvoie la longueur de la corde d'un scorpion en m

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: longueur corde du bras
    :rtype: float
    """
    return scorpion[4]


def obtenir_longueur_fleche(scorpion):
    """"
        Fonction qui renvoie la longueur de la fleche d'un scorpion en m

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: longueur fleche
    :rtype: float
    """
    return scorpion[5]


def obtenir_rayon_fleche(scorpion):
    """
            Fonction qui renvoie le rayon de la fleche d'un scorpion en m

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: rayon de la fleche
    :rtype: float
    """
    return scorpion[6]


def obtenir_masse_volumique_materiau(scorpion):
    """
        Fonction qui renvoie la masse volumique du materiau de la fleche d'un scorpion en kg / m3

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: masse volumique
    :rtype: float
    """
    return scorpion[7]


def obtenir_module_young_materiau(scorpion):
    """
        Fonction qui renvoie le module d'Young du materiau du projectile d'un scorpion en GPa

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: module d'Young
    :rtype: float
    """
    return scorpion[8]


def obtenir_coeff_poisson_materiau(scorpion):
    """
        Fonction qui renvoie la coefficient de poisson du materiau du projectile d'un scorpion en m

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: coefficient de poisson
    :rtype: float
    """
    return scorpion[9]


def scorpion_identique(scorpion1, scorpion2):
    """
        Fonction qui determine si deux scorpions sont identiques. On compare
        chaque element d'un scorpion. Renvoie 1 s'ils sont identiques, 0 sinon.

    :param scorpion1: liste contenant les paramètres du scorpion
    :type scorpion1: float[10]
    :param scorpion2: liste contenant les paramètres du scorpion
    :type scorpion2: float[10]
    :return: identique?
    :rtype: int
    """
    note = 0
    for i in range(len(scorpion1)):
        if scorpion1[i] == scorpion2[i]:
            note += 1
    if note == 10:
        return 1
    else:
        return 0


def calculer_ressort_scorpion(scorpion):

    """
        Fonction qui renvoie la valeur du ressort du scorpion en N / m

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: ressort
    :rtype: float
    """
    return calculer_ressort(
        obtenir_module_young_materiau(scorpion),
        obtenir_coeff_poisson_materiau(scorpion))


def calculer_longueur_vide_scorpion(scorpion):
    """
        Fonction qui renvoie la longueur à vide en m du scorpion.

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: longueur à vide
    :rtype: float

    .. seealso:: :func:`src.Tools.calculer_longueur_vide`
    """
    return calculer_longueur_vide(
        obtenir_longueur_bras(scorpion),
        obtenir_longueur_corde(scorpion)
    )


def calculer_longueur_deplacement_scorpion(scorpion):
    """
        Fonction qui renvoie la longueur de deplacement en m d'un scorpion.

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: longueur de deplacement
    :rtype: float

    .. seealso:: :func:`src.Tools.calculer_longueur_deplacement`
    """
    return calculer_longueur_deplacement(
        obtenir_longueur_fleche(scorpion),
        obtenir_longueur_bras(scorpion),
        obtenir_longueur_corde(scorpion)
    )


def calculer_masse_projectile_scorpion(scorpion):
    """
        Fonction qui renvoie la masse du projectile en kg d'un scorpion.

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: masse du projectile
    :rtype: float

    .. seealso:: :func:`src.Tools.calculer_masse_projectile`
    """
    return calculer_masse_projectile(
        obtenir_masse_volumique_materiau(scorpion),
        obtenir_rayon_fleche(scorpion),
        obtenir_longueur_fleche(scorpion)
    )


def calculer_vitesse_scorpion(scorpion):
    """
        Fonction qui renvoie la vitesse du projectile en m / s d'un scorpion.

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: vitesse d'un projectile
    :rtype: float

    .. seealso:: :func:`src.Tools.calculer_vitesse`
    """
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
    """
        Fonction qui renvoie la portee en m d'un scorpion.

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: portee scorpion
    :rtype: float

    .. seealso:: :func:`src.Tools.calculer_portee`
    """
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
    """
         Fonction qui renvoie l'energie cinetique en Joule d'un scorpion.

     :param scorpion: liste contenant les paramètres du scorpion
     :type scorpion: float[10]
     :return: energie cinetique
     :rtype: float

     .. seealso:: :func:`src.Tools.calculer_energie_cinetique_joule`
     """
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
    """
             Fonction qui renvoie l'energie cinetique en gramme de TNT d'un scorpion.

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: energie cinetique
    :rtype: float

    .. seealso:: :func:`src.Tools.calculer_energie_cinetique_tnt`
    """
    return calculer_energie_cinetique_tnt(calculer_energie_cinetique_joule_scorpion(scorpion))


def calculer_fleche_bras_max_scorpion(scorpion):
    """
        Fonction qui renvoie la valeur du bras maximum en m d'un scorpion.

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]
    :return: bras maximum
    :rtype: float

    .. seealso:: :func:`src.Tools.calculer_fleche_bras_max`
    """
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
    """
        Fonction qui affiche les caractéristiques d'un scorpion

    :param scorpion: liste contenant les paramètres du scorpion
    :type scorpion: float[10]

    """
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
    print("Vitesse du projectile :" + str(calculer_vitesse_scorpion(scorpion))+"en m / s")
    print("Portee du scorpion : "+str(calculer_portee_scorpion(scorpion))+" en m")
