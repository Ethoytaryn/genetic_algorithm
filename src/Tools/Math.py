from src.Tools.Constante import DEUX


def moyenne(tableau):
    """
        Fonction qui calcule la moyenne des valeurs contenues dans un tableau.
        resultat = somme(element) / nombre_element

    :param tableau: tableau de valeurs
    :type tableau: [float]
    :return: moyenne du tableau de valeurs
    :rtype: float
    """
    return sum(tableau, 0.0) / len(tableau)


def variance(tableau):
    """
        Fonction qui calcule la variance des valeurs contenues dans un tableau
        resultat = moyenne([element - moyenne])

    :param tableau: tableau de valeurs
    :type tableau: [float]
    :return: variance du tableau de valeurs
    :rtype: float

    .. seealso:: :func:`src.Tools.moyenne`
    """
    m = moyenne(tableau)
    return moyenne([(x - m) ** DEUX for x in tableau])


