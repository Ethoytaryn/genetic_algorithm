from math import pow, sqrt, pi, sin

from src.Tools.Constante import GRAVITATION_CONSTANTE


def calculer_ressort(module_young, coefficient_poisson):
    """
        Fonction qui calcul le ressort en N / m

        :param module_young
        :param coefficient_poisson
        :type module_young: float
        :type coefficient_poisson: float
        :return: Ressort
        :rtype: float

        .. warning:: Si le coefficient de poisson vaut 0.5, la fonction
        renvoie 999999999.99
    """
    if coefficient_poisson == 0.5:
        return 999999999.99
    else:
        return 1 / 3 * module_young / (1 - 2 * coefficient_poisson)


def calculer_longueur_vide(longueur_bras, longueur_corde):
    """
        Fonction qui la longueur à vide du genetic_algorithm en m

        :rtype: float
    """
    try:
        return sqrt(pow(longueur_bras, 2)/4 - (pow(longueur_corde, 2)))
    except ValueError:
        return -1


def calculer_longueur_deplacement(longueur_fleche, longueur_bras, longueur_corde):
    """
        Fonction qui calcul la longueur de deplacement en m.

        Cette fonction calcul la longueur de déplacement du scorpion. Si
        la longueur de la fleche > longueur a vide alors on renvoie 0.

        :rtype: float
    """
    longueur_vide = calculer_longueur_vide(longueur_bras, longueur_corde)
    if longueur_fleche < longueur_vide:
        return 0.0
    else:
        if calculer_longueur_vide(longueur_bras, longueur_corde) == -1:
            return 0
        else:
            return longueur_fleche - calculer_longueur_vide(longueur_bras, longueur_corde)


def calculer_masse_projectile(masse_volumique, rayon_fleche, longueur_fleche):
    """
        Fonction qui calcul la masse 'mf' du projectile en kg

        :rtype: float
    """
    return masse_volumique * pi * pow(rayon_fleche, 2) * longueur_fleche


def calculer_vitesse(
        module_young,
        coefficient_poisson,
        longueur_fleche,
        longueur_bras,
        longueur_corde,
        masse_volumique,
        rayon_fleche):
    """
        Fonction qui calcul la vitesse 'v' du projectile en m / s

        Formule : v = sqrt( K * ld² / mf)
        :rtype: float
    """
    try:
        vitesse = sqrt(
            calculer_ressort(module_young, coefficient_poisson) *
            pow(calculer_longueur_deplacement(longueur_fleche, longueur_bras, longueur_corde), 2) /
            calculer_masse_projectile(masse_volumique, rayon_fleche, longueur_fleche))
    except ValueError:
        return 0

    return vitesse


def calculer_portee(
        angle_tir,
        module_young,
        coefficient_poisson,
        longueur_fleche,
        longueur_bras,
        longueur_corde,
        masse_volumique,
        rayon_fleche):
    """
         Fonction qui calcul la portee 'p' du scorpion en m

         :rtype: float
     """
    return sqrt(
        pow(calculer_vitesse(module_young,
                             coefficient_poisson,
                             longueur_fleche,
                             longueur_bras,
                             longueur_corde,
                             masse_volumique,
                             rayon_fleche), 2) * sin(2 * angle_tir) / GRAVITATION_CONSTANTE)


def calculer_energie_cinetique_joule(masse_volumique, rayon_fleche, longueur_fleche, module_young,
                                     coefficient_poisson, longueur_bras, longueur_corde):
    """
         Fonction qui calcul l'energie cinetique en joule du projectile en Joule

         :rtype: float
     """
    return calculer_masse_projectile(masse_volumique, rayon_fleche, longueur_fleche) * \
           pow(calculer_vitesse(
               module_young,
               coefficient_poisson,
               longueur_fleche,
               longueur_bras,
               longueur_corde,
               masse_volumique,
               rayon_fleche), 2) / 2


def calculer_energie_cinetique_tnt(energie_cinetique):
    """
         Fonction qui convertie l'energie cinetique en joule du projectile en gramme de tnt

         :rtype: float
     """
    return energie_cinetique / 4184


def calculer_moment_quadratique(longueur_base, hauteur_base_bras):
    """
         Fonction qui calcule le moment quadratique en m^4

         :rtype: float
     """
    return longueur_base * pow(hauteur_base_bras, 3) / 12


def calculer_force_traction(module_young, coefficient_poisson, longueur_fleche,
                            longueur_bras, longueur_corde):
    """
        Fonction qui calcule la force de traction en N

        :rtype: float
    """
    return calculer_ressort(module_young, coefficient_poisson) * \
           calculer_longueur_deplacement(longueur_fleche, longueur_bras, longueur_corde)


def calculer_fleche_bras_max(module_young, coefficient_poisson, longueur_fleche,
                             longueur_bras, longueur_corde, longueur_base, hauteur_base_bras):
    """
        Fonction qui calcule la fleche de bras max en m

        :rtype: float
    """
    return calculer_force_traction(module_young, coefficient_poisson, longueur_fleche,
                                   longueur_bras, longueur_corde) * \
           pow(longueur_bras, 3) / (48 * module_young *
                                    calculer_moment_quadratique(longueur_base, hauteur_base_bras)
                                    )
