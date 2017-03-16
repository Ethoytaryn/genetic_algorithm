from random import\
    random, \
    randrange, \
    uniform

from src.Metier.Parametre_simulation import \
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
from src.Metier.Scorpion import \
    obtenir_angle, \
    obtenir_longueur_bras, \
    obtenir_longueur_base_bras, obtenir_longueur_corde, obtenir_longueur_fleche, obtenir_rayon_fleche, \
    obtenir_masse_volumique_materiau, obtenir_module_young_materiau, obtenir_coeff_poisson_materiau


def muter_angle_tir(scorpion):
    """
        Fonction qui simule un mutation de l'angle de tir d'un scorpion en regenerant la valeur de l'angle

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_angle`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_ANGLE_BASSE, LIMITE_ANGLE_HAUTE)
        if new_value != obtenir_angle(scorpion):
            scorpion[0] = new_value
            continuer = 0
    return scorpion


def muter_longueur_bras(scorpion):
    """
        Fonction qui simule un mutation de la longueur de bras d'un scorpion en regenerant la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_longueur_bras`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_bras(scorpion):
            scorpion[1] = new_value
            continuer = 0
    return scorpion


def muter_longueur_base_bras(scorpion):
    """
        Fonction qui simule un mutation de la longueur de la base bras d'un scorpion en regenerant
        la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_longueur_base_bras`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            scorpion[2] = new_value
            continuer = 0
    return scorpion


def muter_hauteur_base_bras(scorpion):
    """
        Fonction qui simule un mutation de la hauteur de la base bras d'un scorpion en regenerant
        la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_hauteur_base_bras`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_base_bras(scorpion):
            scorpion[3] = new_value
            continuer = 0
    return scorpion


def muter_longueur_corde(scorpion):
    """
        Fonction qui simule un mutation de la longueur de la corde d'un scorpion en regenerant la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_longueur_corde`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_corde(scorpion):
            scorpion[4] = new_value
            continuer = 0
    return scorpion


def muter_longueur_fleche(scorpion):
    """
        Fonction qui simule un mutation de la longueur de la fleche d'un scorpion en regenerant
        la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_longueur_fleche`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_longueur_fleche(scorpion):
            scorpion[5] = new_value
            continuer = 0
    return scorpion


def muter_rayon_fleche(scorpion):
    """
        Fonction qui simule un mutation du rayon de la fleche d'un scorpion en regenerant la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_rayon_fleche`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_LONGUEUR_BASSE, LIMITE_LONGUEUR_HAUTE)
        if new_value != obtenir_rayon_fleche(scorpion):
            scorpion[6] = new_value
            continuer = 0
    return scorpion


def muter_masse_volumique(scorpion):
    """
        Fonction qui simule un mutation de la masse volumique du projectile
        d'un scorpion en regenerant la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_masse_volumique_materiau`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_MASSE_VOL_BASSE, LIMITE_MASSE_VOL_HAUTE)
        if new_value != obtenir_masse_volumique_materiau(scorpion):
            scorpion[7] = new_value
            continuer = 0
    return scorpion


def muter_module_young(scorpion):
    """
        Fonction qui simule une mutation du module d'young du materiau de projectile
         d'un scorpion en regenerant la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_module_young_materiau`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_MODULE_YOUNG_BASSE, LIMITE_MODULE_YOUNG_HAUTE)
        if new_value != obtenir_module_young_materiau(scorpion):
            scorpion[8] = new_value
            continuer = 0
    return scorpion


def muter_coefficient_poisson(scorpion):
    """
        Fonction qui simule une mutation du coefficient de poison du materiau du projectile
         d'un scorpion en regenerant la valeur dans le tableau

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.obtenir_coeff_poisson_materiau`
    """
    continuer = 1
    while continuer:
        new_value = uniform(LIMITE_POISSON_BASSE, LIMITE_POISSON_HAUTE)
        if new_value != obtenir_coeff_poisson_materiau(scorpion):
            scorpion[9] = new_value
            continuer = 0
    return scorpion


def mutation_individu(scorpion, chance_to_mutate):
    """
        Fonction qui simule une mutation aleatoire d'un gene d'un scorpion

    :param scorpion: scorpion avant mutation
    :type scorpion: float[10]
    :param chance_to_mutate: probabilite de mutation
    :type chance_to_mutate: float
    :return: scorpion après mutation
    :rtype: float[10]

    .. seealso:: :func:`src.metier.muter_angle_tir
    .. seealso:: :func:`src.metier.muter_longueur_bras`
    .. seealso:: :func:`src.metier.muter_longueur_base_bras`
    .. seealso:: :func:`src.metier.muter_hauteur_base_bras`
    .. seealso:: :func:`src.metier.muter_longueur_corde`
    .. seealso:: :func:`src.metier.muter_longueur_fleche`
    .. seealso:: :func:`src.metier.muter_rayon_fleche`
    .. seealso:: :func:`src.metier.muter_masse_volumique`
    .. seealso:: :func:`src.metier.muter_module_young`
    .. seealso:: :func:`src.metier.muter_coefficient_poisson`
    `
    """
    if random() < chance_to_mutate:
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
