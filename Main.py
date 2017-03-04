import matplotlib.pyplot as plt

from src.Metier.Genetique import \
    generer_population,\
    calculer_energie_max,\
    evaluation_individu, \
    calculer_note_moyenne, \
    selection_parents_tournoi,\
    generer_generation_suivante,\
    calculer_variance,\
    calculer_portee_moyenne, \
    calculer_variance_portee
from src.Metier.Parametre_simulation import POPULATION_COUNT, GENERATION_COUNT

"""
"""
def main():

    population = generer_population(POPULATION_COUNT)
    notes_moyenne_par_generation = []
    portees_moyenne_par_generation = []
    energies_moyenne_par_generation = []
    variances_notes_par_generation = []
    variances_portee_par_generation = []

    for i in range(GENERATION_COUNT):
        print("Progression : " + str((i + 1) / GENERATION_COUNT * 100) + "%")

        energie_max_generation = calculer_energie_max(population)

        variance_portee = calculer_variance_portee(population)
        variances_portee_par_generation.append(variance_portee)

        couples_scorpion_note = []
        notes_individu_meme_generation = []
        portees_individu_meme_generation = []
        energies_individu_meme_generation = []

        for scorpion in population:
            note_individu, portee, energie = evaluation_individu(scorpion, energie_max_generation, variance_portee)
            couple = [scorpion, note_individu]
            couples_scorpion_note.append(couple)
            notes_individu_meme_generation.append(note_individu)
            portees_individu_meme_generation.append(portee)
            energies_individu_meme_generation.append(energie)

        variance = calculer_variance(notes_individu_meme_generation)
        variances_notes_par_generation.append(variance)

        moyenne = calculer_note_moyenne(notes_individu_meme_generation)
        notes_moyenne_par_generation.append(moyenne)

        portee_moyenne = calculer_portee_moyenne(portees_individu_meme_generation)
        portees_moyenne_par_generation.append(portee_moyenne)

        energie_moyenne = calculer_portee_moyenne(energies_individu_meme_generation)
        energies_moyenne_par_generation.append(energie_moyenne)

        population_parent = selection_parents_tournoi(couples_scorpion_note)
        population = generer_generation_suivante(population_parent)

    x = range(0, GENERATION_COUNT, 1)
    plt.subplots_adjust(0.5)
    plt.xlabel('nombre de generation')
    plt.subplot(321)
    plt.title("Fitness en fonction du nombre de generation")
    plt.ylabel('fitness')
    plt.plot(x, notes_moyenne_par_generation)
    plt.subplot(322)
    plt.title("Variance dela finesse en fonction du nombre de génération")
    plt.ylabel("variance")
    plt.plot(x, variances_notes_par_generation)
    plt.subplot(323)
    plt.title("Portee en fonction du nombre de generation")
    plt.ylabel("Portee en metre")
    plt.plot(x, portees_moyenne_par_generation)
    plt.subplot(324)
    plt.title("Variance de la Portee en fonction du nombre de generation")
    plt.ylabel("Variance")
    plt.plot(x, variances_portee_par_generation)
    plt.subplot(325)
    plt.title("Energie en fonction du nombre de génération")
    plt.ylabel("Energie en gramme de TNT")
    plt.plot(x, energies_moyenne_par_generation)

    plt.show()


if __name__ == "__main__":
    main()
