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
    calculer_energie_moyenne_generation
from src.Metier.genetique.population_generator import \
    generer_population, \
    generer_generation_suivante


def main():

    population = generer_population(POPULATION_COUNT)
    notes_moyenne_par_generation = []
    variances_notes_par_generation = []
    portees_moyenne_par_generation = []
    energies_moyenne_par_generation = []
    info_scorpion_energie_portee_note = []

    for i in range(GENERATION_COUNT):
        print("Progression : " + str((i + 1) / GENERATION_COUNT * 100) + "%")
        info_scorpion_energie_portee_note = evaluation_population(population)
        variances_notes_par_generation.append(
            calcule_variance_notes_generation(info_scorpion_energie_portee_note))
        notes_moyenne_par_generation.append(
            calculer_note_moyenne_generation(info_scorpion_energie_portee_note))
        portees_moyenne_par_generation.append(
            calculer_portee_moyenne_generation(info_scorpion_energie_portee_note))
        energies_moyenne_par_generation.append(
            calculer_energie_moyenne_generation(info_scorpion_energie_portee_note)
        )
        population = generer_generation_suivante(
            info_scorpion_energie_portee_note, CHANCE_TO_HYBRID, CHANCE_TO_MUTATE)

    afficher_scorpion(selection_meilleur_scorpion(info_scorpion_energie_portee_note))

    x = range(0, GENERATION_COUNT, 1)
    plt.figure(1)
    plt.xlabel('nombre de generation')
    plt.subplot(221)
    plt.title("Fitness en fonction du nombre de generation")
    plt.ylabel('fitness')
    plt.plot(x, notes_moyenne_par_generation)
    plt.subplot(222)
    plt.title("Variance dela finesse en fonction du nombre de génération")
    plt.ylabel("variance")
    plt.plot(x, variances_notes_par_generation)
    plt.subplot(223)
    plt.title("Portee en fonction du nombre de generation")
    plt.ylabel("Portee en metre")
    plt.plot(x, portees_moyenne_par_generation)
    plt.subplot(224)
    plt.title("Energie en fonction du nombre de génération")
    plt.ylabel("Energie en gramme de TNT")
    plt.plot(x, energies_moyenne_par_generation)
    plt.show()


if __name__ == "__main__":
    main()
