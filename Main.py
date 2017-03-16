import time

import matplotlib.pyplot as plt

from src.Metier.Parametre_simulation import \
    POPULATION_COUNT,\
    GENERATION_COUNT, \
    CHANCE_TO_HYBRID, \
    CHANCE_TO_MUTATE
from src.Metier.Scorpion import \
    afficher_scorpion
from src.Metier.genetique.evaluation_population import \
    evaluation_population, \
    calculer_note_moyenne_generation, \
    selection_meilleur_scorpion, \
    calcule_variance_notes_generation,\
    calculer_portee_moyenne_generation,\
    calculer_energie_moyenne_generation,\
    determiner_note_min,\
    determiner_note_max,\
    determiner_portee_min, \
    determiner_portee_max,\
    determiner_energie_min,\
    determiner_energie_max
from src.Metier.genetique.population_generator import \
    generer_population, \
    generer_generation_suivante


def main():

    print("caracteristique de la run : ")
    print("Nombre de generation : " + str(GENERATION_COUNT))
    print("Nombre d'individu par genration : " + str(POPULATION_COUNT))
    print("Coefficient d'hybridation : " + str(CHANCE_TO_HYBRID))
    print("Coefficient de mutation : " + str(CHANCE_TO_MUTATE))

    population = generer_population(POPULATION_COUNT)
    notes_moyenne_par_generation = []
    notes_min_par_generation = []
    notes_max_par_generation = []
    variances_notes_par_generation = []
    portees_moyenne_par_generation = []
    portees_min_par_generation = []
    portees_max_par_generation = []
    energies_moyenne_par_generation = []
    energies_min_par_generation = []
    energies_max_par_generation = []
    info_scorpion_energie_portee_note = []

    start_time = time.time()
    start_time_struct = time.gmtime(start_time)
    print("Debut de la simulation : " + time.strftime("%H:%M:%S", start_time_struct))
    for i in range(GENERATION_COUNT):
        instant_time = time.time()
        elapse_time = instant_time - start_time
        elapse_time_struct = time.gmtime(elapse_time)
        print("\rProgression : " + str(round(((i + 1) / GENERATION_COUNT * 100), 3)) +
              "%, Numero Generation traitée : " + str(i) + "/" + str(GENERATION_COUNT) +
              " , temps ecoule : " + time.strftime("%H:%M:%S", elapse_time_struct), end='')
        # Evaluation de chaque individu de notre generation
        info_scorpion_energie_portee_note = evaluation_population(population)

        # Calcul de la note moyenne
        notes_moyenne_par_generation.append(
            calculer_note_moyenne_generation(info_scorpion_energie_portee_note))

        # Determination de la note minimum et maximum
        notes_min_par_generation.append(
            determiner_note_min(info_scorpion_energie_portee_note))
        notes_max_par_generation.append(
            determiner_note_max(info_scorpion_energie_portee_note))

        # Calcul de la variance des note de la generation
        variances_notes_par_generation.append(
            calcule_variance_notes_generation(info_scorpion_energie_portee_note))

        # Calcul de portee moyenne de la generation
        portees_moyenne_par_generation.append(
            calculer_portee_moyenne_generation(info_scorpion_energie_portee_note))

        # Determination de la portee minimum et maximum
        portees_min_par_generation.append(
            determiner_portee_min(info_scorpion_energie_portee_note)
        )
        portees_max_par_generation.append(
            determiner_portee_max(info_scorpion_energie_portee_note)
        )

        # Calcul de l'energie moyenne par generation
        energies_moyenne_par_generation.append(
            calculer_energie_moyenne_generation(info_scorpion_energie_portee_note)
        )

        # Determination de l'energie minimum et maximum
        energies_min_par_generation.append(
            determiner_energie_min(info_scorpion_energie_portee_note)
        )
        energies_max_par_generation.append(
            determiner_energie_max(info_scorpion_energie_portee_note)
        )

        # Generation de la population suivante
        population = generer_generation_suivante(
            info_scorpion_energie_portee_note, CHANCE_TO_HYBRID, CHANCE_TO_MUTATE)

    afficher_scorpion(selection_meilleur_scorpion(info_scorpion_energie_portee_note))

    # GEneration des graphes d'évolution
    x = range(0, GENERATION_COUNT, 1)
    plt.figure(1)
    plt.xlabel('nombre de generation')
    plt.subplot(221)
    plt.title("Fitness en fonction du nombre de generation")
    plt.ylabel('fitness')
    plt.plot(x, notes_moyenne_par_generation, label="moyenne")
    #plt.plot(x, notes_min_par_generation, label="min")
    #plt.plot(x, notes_max_par_generation, label="max")
    plt.subplot(222)
    plt.title("Variance dela finesse en fonction du nombre de génération")
    plt.ylabel("variance")
    plt.plot(x, variances_notes_par_generation)
    plt.subplot(223)
    plt.title("Portee en fonction du nombre de generation")
    plt.ylabel("Portee en metre")
    plt.plot(x, portees_moyenne_par_generation)
    #plt.plot(x, portees_min_par_generation, label="min")
    #plt.plot(x, portees_max_par_generation, label="max")
    plt.subplot(224)
    plt.title("Energie en fonction du nombre de génération")
    plt.ylabel("Energie en gramme de TNT")
    plt.plot(x, energies_moyenne_par_generation)
    #plt.plot(x, energies_min_par_generation, label="min")
    #plt.plot(x, energies_max_par_generation, label="max")
    plt.show()


if __name__ == "__main__":
    main()
