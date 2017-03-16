import copy
from random import random, randrange

from src.Metier.Scorpion import generate_scorpion, scorpion_identique
from src.Metier.genetique.mutation_scorpion import mutation_individu
from src.Metier.genetique.tournament_selection import selection_parents_tournoi


def generer_population(n):
    """
        Fonction qui genere un tableau de n scorpion.

    :param n: nombre de scorpion
    :type n: int
    :return: tableau de scorpion
    :rtype: scorpion[n]

    .. seealso:: :func:`src.Tools.generate_scorpion`
    """
    return [generate_scorpion() for _ in range(n)]


def generer_generation_suivante(info_scorpion_energie_portee_note, chance_to_hybrid, chance_to_mutate):
    """
        Fonction qui genere la generation suivante de scorpion. A partir d'une liste de longueur n d'info scorpion de la
        forme [scorpion, energie, portee, note]. On va sélectionner n parent grâce à un algorithme de selection par tournoi
        à 1 étage. Puis on formera des couples qui genereront 2 enfants avec une chance d'hybridation. Chaque enfant aura ensuite
        une chance de muter.

    :param info_scorpion_energie_portee_note: tableau d'info
    :type info_scorpion_energie_portee_note: liste[scorpion, energie, portee, note]
    :param chance_to_hybrid: coefficient d'hybridation
    :type chance_to_hybrid: float
    :param chance_to_mutate: coefficient de mutation
    :return: tableau de scorpion
    :rtype: scorpion[n]

    .. seealso:: :func:`src.Tools.selection_parents_tournoi`
    .. seealso:: :func:`src.Tools.scorpion_identique`
    .. seealso:: :func:`src.Tools.generer_enfants`
    .. seealso:: :func:`src.Tools.mutation_individu`
    """
    population_parent = selection_parents_tournoi(info_scorpion_energie_portee_note)
    population_enfant = []
    population_count = len(population_parent)
    while len(population_enfant) < population_count:

        id_parent1 = randrange(0, population_count-1, 1)
        id_parent2 = 0

        continuer = 1
        while continuer:
            id_parent2 = randrange(0, population_count - 1, 1)
            if id_parent2 != id_parent1:
                identique = scorpion_identique(population_parent[id_parent1], population_parent[id_parent2])
                if identique == 0:
                    continuer = 0

        enfant1, enfant2 = generer_enfants(
            population_parent[id_parent1], population_parent[id_parent2], chance_to_hybrid)
        enfant1 = mutation_individu(enfant1, chance_to_mutate)
        enfant2 = mutation_individu(enfant2, chance_to_mutate)
        population_enfant.append(enfant1)
        population_enfant.append(enfant2)

    return population_enfant


def generer_enfants(pere, mere, coeff_hybrid):
    """
        Fonction générant les enfants de deux scorpions avec un taux d'hybridation.

    :param pere: scorpion 'pere'
    :type pere: float[10]
    :param mere: scorpion 'mere'
    :type mere: float[10]
    :param coeff_hybrid: coefficient d'hybridation
    :type coeff_hybrid: float
    :return: 2 scorpions enfant
    :rtype: float[10], float[10]

    .. seealso:: :func:`src.Tools.generation_enfant_croise`
    .. seealso:: :func:`src.Tools.generation_enfant`
    """
    return generation_enfant_croise(pere, mere, coeff_hybrid), generation_enfant(pere, mere, coeff_hybrid)


def generation_enfant_croise(pere, mere, coeff_hybrid):
    """
        Fonction générant un enfants de type croisé à partir de deux scorpions avec un taux d'hybridation. Un enfant de
        type croisé est un enfant dont un gene sur deux provient d'un parent.
        Si il n'y a pas d'hybridation, on renvoie le pere ou la mere de facon aleatoire.

    :param pere: scorpion 'pere'
    :type pere: float[10]
    :param mere: scorpion 'mere'
    :type mere: float[10]
    :param coeff_hybrid: coefficient d'hybridation
    :type coeff_hybrid: float
    :return: scorpion enfant
    :rtype: float[10]
    """
    if random() < coeff_hybrid:
        enfant = [pere[0],
                  mere[1],
                  pere[2],
                  mere[3],
                  pere[4],
                  mere[5],
                  pere[6],
                  mere[7],
                  pere[8],
                  mere[9]
                  ]
    else:
        choix = randrange(0, 1, 1)
        if choix == 0:
            enfant = copy.copy(pere)
        else:
            enfant = copy.copy(mere)
    return enfant


def generation_enfant(pere, mere, coeff_hybrid):
    """
        Fonction générant un enfants à partir de deux scorpions avec un taux d'hybridation. L'enfant aura la premiere
        moitié de ses gène herite du pere et l'autre moitie herite de la mere.
        Si il n'y a pas d'hybridation, on renvoie le pere ou la mere de facon aleatoire.

    :param pere: scorpion 'pere'
    :type pere: float[10]
    :param mere: scorpion 'mere'
    :type mere: float[10]
    :param coeff_hybrid: coefficient d'hybridation
    :type coeff_hybrid: float
    :return: scorpion enfant
    :rtype: float[10]
    """
    if random() < coeff_hybrid:
        enfant = [pere[0],
                  pere[1],
                  pere[2],
                  pere[3],
                  pere[4],
                  mere[5],
                  mere[6],
                  mere[7],
                  mere[8],
                  mere[9]
                  ]
    else:
        choix = randrange(0, 1, 1)
        if choix == 0:
            enfant = copy.copy(pere)
        else:
            enfant = copy.copy(mere)
    return enfant
