from src.Metier.Parametre_simulation import DESIRED_SCOPE
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
            Fonction d"évaluation d'un scorpion

            On évalue chaque individu individuellement.

            :rtype: float
    """
    return calculer_fitness(info_scorpion, energie_cinetique_max_tnt)


def calculer_energie_cinetique_tnt_max(liste_couple):
    return max([liste_info_scorpion[1] for liste_info_scorpion in liste_couple])


def calculer_fitness(info_scorpion, energie_max_tnt):
    """
        Fonction qui calcule le score d'un scorpion

        On calcul le score en fonction de la portée du scorpion par rapport
        à la portée souhaitée et de l'énergie en fonction du maximum d'energie jamais atteinte.

        :rtype: float
    """
    scorpion = info_scorpion[0]
    if calculer_longueur_vide_scorpion(scorpion) == -1:
        return 0.0001
    else:
        if calculer_longueur_deplacement_scorpion(scorpion) == -1:
            return 0.0001
        else:
            if calculer_longueur_deplacement_scorpion(scorpion) > calculer_fleche_bras_max_scorpion(scorpion):
                return 0.0001
            else:
                fitness = abs(1/(DESIRED_SCOPE - info_scorpion[2]))*1000 + \
                              (info_scorpion[1]/energie_max_tnt)*0
                #(exp(-pow((info_scorpion[2]-DESIRED_SCOPE), 2) / (2*DESIRED_SCOPE)) / sqrt(2*pi*DESIRED_SCOPE))*100
                return fitness


def calculer_note_moyenne_generation(couple_scorpion_note):
    return moyenne([couple[3] for couple in couple_scorpion_note])


def selection_meilleur_scorpion(couple_scorpion_note):
    if len(couple_scorpion_note) == 0:
        return -1
    else:
        note_max = max([couple[3] for couple in couple_scorpion_note])
        for couple in couple_scorpion_note:
            if couple[3] == note_max:
                return couple[0]


def calcule_variance_notes_generation(couples_scorpion_note):
    return variance([couple[3] for couple in couples_scorpion_note])


def calculer_portee_moyenne_generation(info_scorpion_energie_portee_note):
    return moyenne([liste_info_scorpion[2] for liste_info_scorpion in info_scorpion_energie_portee_note])


def calculer_energie_moyenne_generation(info_scorpion_energie_portee_note):
    return moyenne([liste_info_scorpion[1] for liste_info_scorpion in info_scorpion_energie_portee_note])
