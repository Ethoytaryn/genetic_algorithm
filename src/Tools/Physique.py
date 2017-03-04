from math import pow, sqrt, pi, sin

from Tools.Constante import GRAVITATION_CONSTANTE, DESIRED_SCOPE

from src.Metier.Scorpion import obtenir_module_young_materiau, obtenir_coeff_poisson_materiau, obtenir_longueur_bras, \
    obtenir_longueur_fleche, obtenir_longueur_corde, obtenir_masse_volumique_materiau, obtenir_rayon_fleche, \
    obtenir_angle, obtenir_longueur_base, obtenir_hauteur_base


def calculer_ressort(scorpion):
    """
        Fonction qui calcul le ressort en N / m

        :rtype: float
    """
    return obtenir_module_young_materiau(scorpion) / (3 * (1 - 2 * obtenir_coeff_poisson_materiau(scorpion)))


def calculer_longueur_vide(scorpion):
    """
        Fonction qui la longueur à vide du genetic_algorithm en m

        :rtype: float
    """
    res = pow(obtenir_longueur_bras(scorpion), 2) - (pow(obtenir_longueur_corde(scorpion), 2) / 4)
    if res < 0:
        return 1
    else:
        return sqrt(res)


def calculer_longueur_deplacement(scorpion):
    """
        Fonction qui calcul la longueur de deplacement en m.

        Cette fonction calcul la longueur de déplacement du scorpion. Si
        la longueur de la fleche > longueur a vide alors on renvoie 0.

        :rtype: float
    """
    ld  = obtenir_longueur_fleche(scorpion) - calculer_longueur_vide(scorpion)
    if ld < 0:
        return 0.01
    else:
        return ld

def calculer_masse_projectile(scorpion):
    """
        Fonction qui calcul la masse 'mf' du projectile en kg

        :rtype: float
    """
    return obtenir_masse_volumique_materiau(scorpion) * pi * pow(
        obtenir_rayon_fleche(scorpion), 2) * obtenir_longueur_fleche(scorpion)


def calculer_vitesse(scorpion):
    """
        Fonction qui calcul la vitesse 'v' du projectile en m / s

        Formule : v = sqrt( K * ld² / mf)
        :rtype: float
    """
    return sqrt(calculer_ressort(scorpion)*pow(calculer_longueur_deplacement(scorpion), 2) / calculer_masse_projectile(scorpion))


def calculer_portee(scorpion):
    """
         Fonction qui calcul la portee 'p' du scorpion en m

         :rtype: float
     """
    return sqrt(
        pow(calculer_vitesse(scorpion), 2) * sin(2 * obtenir_angle(scorpion)) / GRAVITATION_CONSTANTE)


def calculer_energie_cinetique_joule(scorpion):
    """
         Fonction qui calcul l'energie cinetique en joule du projectile en Joule

         :rtype: float
     """
    return calculer_masse_projectile(scorpion) * pow(calculer_vitesse(scorpion), 2) / 2


def calculer_energie_cinetique_tnt(scorpion):
    """
         Fonction qui convertie l'energie cinetique en joule du projectile en gramme de tnt

         :rtype: float
     """
    return calculer_energie_cinetique_joule(scorpion) / 4184


def calculer_moment_quadratique(scorpion):
    """
         Fonction qui calcule le moment quadratique en m^4

         :rtype: float
     """
    return obtenir_longueur_base(scorpion) * pow(obtenir_hauteur_base(scorpion), 3) / 12


def calculer_force_traction(scorpion):
    """
        Fonction qui calcule la force de traction en N

        :rtype: float
    """
    return calculer_ressort(scorpion) * calculer_longueur_deplacement(scorpion)


def calculer_fleche_bras_max(scorpion):
    """
        Fonction qui calcule la fleche de bras max en m

        :rtype: float
    """
    return calculer_force_traction(scorpion) * \
           pow(obtenir_longueur_bras(scorpion), 3) / (48 * obtenir_module_young_materiau(scorpion) *
                                                      calculer_moment_quadratique(scorpion)
                                                      )


def destruction_scorpion(scorpion):
    if calculer_longueur_deplacement(scorpion) > calculer_fleche_bras_max(scorpion):
        return 1
    else:
        return 0


def calculer_energie_cinetique_max_generation(population):
    energie_max = 0
    for scorpion in population:
        energie = calculer_energie_cinetique_tnt(scorpion)
        if energie > energie_max:
            energie_max = energie
    return energie_max


def calculer_fitness(scorpion, energie_max_tnt_generation, variance_portee):
    """
        Fonction qui calcule le score d'un scorpion

        On calcul le score en fonction de la portée du scorpion par rapport
        à la portée souhaitée et de l'énergie en fonction de l'énergie max de la génération.
        Il s'agit d'un note sur 2.

        :rtype: float
    """
    portee = calculer_portee(scorpion)
    energie = calculer_energie_cinetique_tnt(scorpion)
    destruction = destruction_scorpion(scorpion)
    fitness = (((DESIRED_SCOPE - portee) / DESIRED_SCOPE + energie / energie_max_tnt_generation)-1)*100
    print(fitness)
    if destruction:
        return -1000, portee, energie
    else:
        return fitness, portee, energie
