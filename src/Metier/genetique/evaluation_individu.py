from src.Tools.Physique import calculer_fitness


def evaluation_individu(scorpion, energie_cinetique_max_tnt, variance_portee):
    """
            Fonction d"évaluation d'un scorpion

            On évalue chaque individu individuellement.

            :rtype: float
    """
    return calculer_fitness(scorpion, energie_cinetique_max_tnt, variance_portee)
