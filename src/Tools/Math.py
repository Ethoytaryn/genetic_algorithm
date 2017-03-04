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


