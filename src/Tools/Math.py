from random import uniform

from src.Tools.Constante import DEUX


def moyenne(tableau):
    """
        Fonction qui calcule la moyenne des valeurs contenues dans un tableau

        :rtype: float
    """
    return sum(tableau, 0.0) / len(tableau)


def variance(tableau):
    """
        Fonction qui la variance moyenne des valeurs d'un tableau

        :rtype: float
    """
    m = moyenne(tableau)
    return moyenne([(x - m) ** DEUX for x in tableau])


def generation_longueur_aleatoire(bas, haut):
    """
        Fonction qui renvoie une longueur en m comprise entre une limite basse et une limite haute

        :rtype: float
    """
    return uniform(bas, haut)


def generation_angle_aleatoire(angle_min, angle_max):
    """
        Fonction qui renvoie une angle en m comprise entre une limite basse et une limite haute

        :rtype: float
    """
    return uniform(angle_min, angle_max)
