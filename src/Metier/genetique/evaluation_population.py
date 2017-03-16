from math import exp, sqrt, pi

from src.Metier.Parametre_simulation import \
    DESIRED_SCOPE
from src.Metier.Scorpion import \
    calculer_longueur_vide_scorpion,\
    calculer_longueur_deplacement_scorpion, \
    calculer_fleche_bras_max_scorpion,\
    calculer_portee_scorpion, \
    calculer_energie_cinetique_tnt_scorpion
from src.Tools.Math import \
    moyenne, \
    variance


def evaluation_population(population):
    """
        Fonction qui evalue une population de scorpion et renvoie un liste d'info scorpion de la forme
        [scorpion, energie, portee, note]

    :param population: tableau de scorpion
    :type population: scorpion[n]
    :return: liste d'info scorpion
    :rtype: info_scorpion[n]

    .. seealso:: :func:`src.Metier.genetique.calculer_energie_cinetique_tnt_scorpion`
    .. seealso:: :func:`src.Metier.genetique.calculer_portee_scorpion`
    .. seealso:: :func:`src.Metier.genetique.calculer_energie_cinetique_tnt_max`
    .. seealso:: :func:`src.Metier.genetique.evaluation_individu`
    """
    liste_info_scorpion = []
    for scorpion in population:
        energie = calculer_energie_cinetique_tnt_scorpion(scorpion)
        portee = calculer_portee_scorpion(scorpion)
        info_scorpion = [scorpion, energie, portee, 0]
        liste_info_scorpion.append(info_scorpion)

    energie_cinetique_max_tnt = calculer_energie_cinetique_tnt_max(liste_info_scorpion)
    for info_scorpion in liste_info_scorpion:
        info_scorpion[3] = evaluation_individu(info_scorpion, energie_cinetique_max_tnt)

    return liste_info_scorpion


def evaluation_individu(info_scorpion, energie_cinetique_max_tnt):
    """
        Fonction d"évaluation d'un scorpion qui renvoie un tableau info scorpion de la forme
        [scorpion, energie, portee, note]

    :param info_scorpion: tableau d'info d'un scorpion avec un note de zero
    :type info_scorpion: [scorpion, energie, portee, 0]
    :param energie_cinetique_max_tnt: energie cinetique maximum de la generation
    :type energie_cinetique_max_tnt: float
    :return: tableau d'info d'un scorpion complete
    :rtype: [scorpion, energie, portee, note]

    .. seealso:: :func:`src.Metier.genetique.calculer_fitness`
    """
    return calculer_fitness(info_scorpion, energie_cinetique_max_tnt)


def calculer_energie_cinetique_tnt_max(liste_info_scorpion):
    """
        Fonction qui calcul l'energie cinetique max d'une population

    :param liste_info_scorpion: liste d'info d'un scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: energie cinetique max en tnt de la generation
    :rtype: float
    """
    return max([liste_info_scorpion[1] for liste_info_scorpion in liste_info_scorpion])


def calculer_fitness(info_scorpion, energie_tnt_max):
    """
        Fonction qui calcule le score d'un scorpion en fonction de la portee et de l'energie de celui, de la portee
        voulue et de l'energie maximum de la population.

        On determine les notes de notre scorpion par rapport a sa porte et son energie. On utilise une loi normale qui
        détermine logiquement la densité de probabilité. Le score final de notre scorpion est l'addition des deux notes.
         Si le scorpion ne remplie pas les critères minimums pour pouvoir tirer, sa note sera de 10^-99

    :param info_scorpion: liste d'info d'un scorpion avec note a zero
    :type info_scorpion: [scorpion, energie, portee, 0]
    :param energie_tnt_max: energie cinetique maximum de la generation en gramme de tnt
    :type energie_tnt_max: float
    :return: liste d'info d'un scorpion avec note actualisee
    :rtype: [scorpion, energie, portee, note]
    """
    scorpion = info_scorpion[0]
    if calculer_longueur_vide_scorpion(scorpion) == -1:
        return pow(10, -99)
    else:
        if calculer_longueur_deplacement_scorpion(scorpion) == -1:
            return pow(10, -99)
        else:
            if calculer_longueur_deplacement_scorpion(scorpion) > calculer_fleche_bras_max_scorpion(scorpion):
                return pow(10, -99)
            else:
                return exp(-(pow((info_scorpion[2]-DESIRED_SCOPE), 2) / (2*DESIRED_SCOPE))) \
                       / sqrt(2*pi*DESIRED_SCOPE) + \
                       (exp(-pow((info_scorpion[1]-energie_tnt_max), 2) / (2*energie_tnt_max))
                        / sqrt(2*pi*energie_tnt_max))


def calculer_note_moyenne_generation(liste_info_scorpion):
    """
        fonction qui calcul la valeur moyenne de la note d'une generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: moyenne des notes de la generation
    :rtype: float

    .. seealso:: :func:`src.Tools.moyenne`
    """
    return moyenne([couple[3] for couple in liste_info_scorpion])


def determiner_note_min(liste_info_scorpion):
    """
        fonction qui determine la note minimum d'une generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: note minimum de la generation
    :rtype: float

    """
    return min([couple[3] for couple in liste_info_scorpion])


def determiner_note_max(liste_info_scorpion):
    """
        fonction qui determine la note maximum d'une generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: note maximum de la generation
    :rtype: float

    """
    return max([couple[3] for couple in liste_info_scorpion])


def selection_meilleur_scorpion(liste_info_scorpion):
    """
        Fonction qui selectionne le meilleur scorpion d'une generation par rapport à sa note

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: meilleur scorpion
    :rtype: float[10]

    """
    if len(liste_info_scorpion) == 0:
        return -1
    else:
        note_max = max([couple[3] for couple in liste_info_scorpion])
        for couple in liste_info_scorpion:
            if couple[3] == note_max:
                return couple[0]


def calcule_variance_notes_generation(liste_info_scorpion):
    """
        fonction qui calcul la variance des note d'une generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: variance des notes de la generation
    :rtype: float

    .. seealso:: :func:`src.Tools.variance`
    """
    return variance([couple[3] for couple in liste_info_scorpion])


def calculer_portee_moyenne_generation(liste_info_scorpion):
    """
        fonction qui calcul la portee moyenne d'une generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: portee moyenne de la generation
    :rtype: float

    .. seealso:: :func:`src.Tools.moyenne`
    """
    return moyenne([liste_info_scorpion[2] for liste_info_scorpion in liste_info_scorpion])


def determiner_portee_min(liste_info_scorpion):
    """
        fonction qui determine la portee minimum de la generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: portee minimum de la generation
    :rtype: float

    """
    return min([couple[2] for couple in liste_info_scorpion])


def determiner_portee_max(liste_info_scorpion):
    """
        fonction qui determine la portee maximum de la generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: portee maximum de la generation
    :rtype: float

    """
    return max([couple[2] for couple in liste_info_scorpion])


def calculer_energie_moyenne_generation(liste_info_scorpion):
    """
        fonction qui calcul l'energie moyenne de la generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: energie cinetique moyenne de la generation
    :rtype: float

    """
    return moyenne([liste_info_scorpion[1] for liste_info_scorpion in liste_info_scorpion])


def determiner_energie_min(liste_info_scorpion):
    """
        fonction qui determine l'energie minimum de la generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: energie cinetique minimum de la generation
    :rtype: float

    """
    return min([couple[1] for couple in liste_info_scorpion])


def determiner_energie_max(liste_info_scorpion):
    """
        fonction qui determine l'energie maximum de la generation

    :param liste_info_scorpion: liste d'info scorpion
    :type liste_info_scorpion: info_scorpion[n]
    :return: energie cinetique maximum de la generation
    :rtype: float

    """
    return max([couple[1] for couple in liste_info_scorpion])
