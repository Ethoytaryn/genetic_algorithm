from src.Metier.Scorpion import generate_scorpion, scorpion_identique
from src.Metier.genetique.evaluation_population import evaluation_population
from src.Metier.genetique.population_generator import \
    generer_population, \
    generation_enfant_croise, \
    generation_enfant, \
    generer_generation_suivante


class TestMutationScorpion:

    def test_generate_population(self):
        scorpions = generer_population(1000)
        assert len(scorpions) == 1000
        for scorpion in scorpions:
            assert len(scorpion) == 10

    def test_generation_enfant_croise_hybride(self):
        pere = generate_scorpion()
        mere = generate_scorpion()
        enfant = generation_enfant_croise(pere, mere, 1)
        assert len(enfant) == 10
        assert enfant[0] == pere[0]
        assert enfant[1] == mere[1]
        assert enfant[2] == pere[2]
        assert enfant[3] == mere[3]
        assert enfant[4] == pere[4]
        assert enfant[5] == mere[5]
        assert enfant[6] == pere[6]
        assert enfant[7] == mere[7]
        assert enfant[8] == pere[8]
        assert enfant[9] == mere[9]

    def test_generation_enfant_hybride(self):
        pere = generate_scorpion()
        mere = generate_scorpion()
        enfant = generation_enfant(pere, mere, 1)
        assert len(enfant) == 10
        assert enfant[0] == pere[0]
        assert enfant[1] == pere[1]
        assert enfant[2] == pere[2]
        assert enfant[3] == pere[3]
        assert enfant[4] == pere[4]
        assert enfant[5] == mere[5]
        assert enfant[6] == mere[6]
        assert enfant[7] == mere[7]
        assert enfant[8] == mere[8]
        assert enfant[9] == mere[9]

    def test_generation_enfant_croise_non_hybride(self):
        pere = generate_scorpion()
        mere = generate_scorpion()
        enfant = generation_enfant_croise(pere, mere, 0)
        assert len(enfant) == 10
        assert scorpion_identique(enfant, pere) | scorpion_identique(enfant, mere)

    def test_generation_enfant_non_hybride(self):
        pere = generate_scorpion()
        mere = generate_scorpion()
        enfant = generation_enfant(pere, mere, 0)
        assert len(enfant) == 10
        assert scorpion_identique(enfant, pere) | scorpion_identique(enfant, mere)
