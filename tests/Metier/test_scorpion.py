from src.Metier.Parametre_simulation import \
    LIMITE_ANGLE_BASSE,\
    LIMITE_ANGLE_HAUTE, \
    LIMITE_MASSE_VOL_BASSE,\
    LIMITE_MASSE_VOL_HAUTE, \
    LIMITE_MODULE_YOUNG_BASSE, \
    LIMITE_MODULE_YOUNG_HAUTE, \
    LIMITE_POISSON_BASSE,\
    LIMITE_POISSON_HAUTE,\
    LIMITE_LONGUEUR_BASSE,\
    LIMITE_LONGUEUR_HAUTE
from src.Metier.Scorpion import \
    generate_scorpion, \
    obtenir_angle,\
    obtenir_longueur_bras,\
    obtenir_longueur_base_bras, \
    obtenir_longueur_fleche, \
    obtenir_module_young_materiau,\
    obtenir_masse_volumique_materiau,\
    obtenir_coeff_poisson_materiau,\
    obtenir_hauteur_base_bras,\
    obtenir_longueur_corde,\
    obtenir_rayon_fleche, \
    scorpion_identique


class TestScorpion:

    scorpion = generate_scorpion()

    def test_nombre_parametre_scorpion(self):
        assert len(self.scorpion) == 10
        for nombre in self.scorpion:
            assert type(nombre) == float

    def test_fonction_obtenir_parametre_scorpion(self):
        assert self.scorpion[0] == obtenir_angle(self.scorpion)
        assert self.scorpion[1] == obtenir_longueur_bras(self.scorpion)
        assert self.scorpion[2] == obtenir_longueur_base_bras(self.scorpion)
        assert self.scorpion[3] == obtenir_hauteur_base_bras(self.scorpion)
        assert self.scorpion[4] == obtenir_longueur_corde(self.scorpion)
        assert self.scorpion[5] == obtenir_longueur_fleche(self.scorpion)
        assert self.scorpion[6] == obtenir_rayon_fleche(self.scorpion)
        assert self.scorpion[7] == obtenir_masse_volumique_materiau(self.scorpion)
        assert self.scorpion[8] == obtenir_module_young_materiau(self.scorpion)
        assert self.scorpion[9] == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_limite_parametre_scorpion(self):
        assert LIMITE_ANGLE_BASSE <= obtenir_angle(self.scorpion) <= LIMITE_ANGLE_HAUTE
        assert LIMITE_LONGUEUR_BASSE <= obtenir_longueur_bras(self.scorpion) <= LIMITE_LONGUEUR_HAUTE
        assert LIMITE_LONGUEUR_BASSE <= obtenir_longueur_base_bras(self.scorpion) <= LIMITE_LONGUEUR_HAUTE
        assert LIMITE_LONGUEUR_BASSE <= obtenir_hauteur_base_bras(self.scorpion) <= LIMITE_LONGUEUR_HAUTE
        assert LIMITE_LONGUEUR_BASSE <= obtenir_longueur_corde(self.scorpion) <= LIMITE_LONGUEUR_HAUTE
        assert LIMITE_LONGUEUR_BASSE <= obtenir_longueur_fleche(self.scorpion) <= LIMITE_LONGUEUR_HAUTE
        assert LIMITE_LONGUEUR_BASSE <= obtenir_rayon_fleche(self.scorpion) <= LIMITE_LONGUEUR_HAUTE
        assert LIMITE_MASSE_VOL_BASSE <= obtenir_masse_volumique_materiau(self.scorpion) <= LIMITE_MASSE_VOL_HAUTE
        assert LIMITE_MODULE_YOUNG_BASSE <= obtenir_module_young_materiau(self.scorpion) <= LIMITE_MODULE_YOUNG_HAUTE
        assert LIMITE_POISSON_BASSE <= obtenir_coeff_poisson_materiau(self.scorpion) <= LIMITE_POISSON_HAUTE

    def test_scorpions_identique(self):
        scorpion2 = TestScorpion.generate_scorpion_null()
        assert scorpion_identique(self.scorpion, self.scorpion) == 1
        assert scorpion_identique(scorpion2, self.scorpion) == 0

    def test_generate_scorpion_null(self):
        scorpion_null = TestScorpion.generate_scorpion_null()
        scorpion_null2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        assert len(scorpion_null) == 10
        assert len(scorpion_null2) == 10
        assert scorpion_identique(scorpion_null, scorpion_null2) == 1

    @staticmethod
    def generate_scorpion_null():
        """
           Fonction generatrice d'un individu null. Tous c'est paramatres sont à -1

           :return: liste contenant les paramètres du scorpion
           :rtype:
        """
        return [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
