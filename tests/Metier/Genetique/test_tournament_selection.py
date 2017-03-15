from src.Metier.Parametre_simulation import POPULATION_COUNT
from src.Metier.Scorpion import generate_scorpion, scorpion_identique
from src.Metier.genetique.tournament_selection import duel


class TestTournamentSelection:

    scorpion1 = generate_scorpion()
    scorpion2 = generate_scorpion()

    def test_duel_scorpion1_meilleur(self):
        liste_info_scorpion1 = [self.scorpion1, 0, 0, 1]
        liste_info_scorpion2 = [self.scorpion2, 0, 0, 0]

        scorpion_gagnant = duel(liste_info_scorpion1, liste_info_scorpion2)
        assert len(scorpion_gagnant) == 10
        assert scorpion_identique(scorpion_gagnant, self.scorpion1)

    def test_duel_scorpion2_meilleur(self):
        liste_info_scorpion1 = [self.scorpion1, 0, 0, 0]
        liste_info_scorpion2 = [self.scorpion2, 0, 0, 1]

        scorpion_gagnant = duel(liste_info_scorpion1, liste_info_scorpion2)
        assert len(scorpion_gagnant) == 10
        assert scorpion_identique(scorpion_gagnant, self.scorpion2)

    def test_selection_parents_tournoi(self):
        info_scorpion_energie_portee_note = []

        for i in range(POPULATION_COUNT):
            scorpion = generate_scorpion()
            energie = 0
            portee = 0
            note = 1
            liste_info_scorpion = [scorpion, energie, portee, note]
            info_scorpion_energie_portee_note.append(liste_info_scorpion)

        for liste in info_scorpion_energie_portee_note:
            assert len(liste) == 4
        assert len(info_scorpion_energie_portee_note) == POPULATION_COUNT

