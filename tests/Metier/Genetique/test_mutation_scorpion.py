from src.Metier.genetique.mutation_scorpion import \
    muter_angle_tir, \
    muter_longueur_bras, \
    muter_longueur_base_bras, \
    muter_hauteur_base_bras,\
    muter_longueur_fleche,\
    muter_longueur_corde,\
    muter_rayon_fleche,\
    muter_coefficient_poisson,\
    muter_masse_volumique,\
    muter_module_young, \
    mutation_individu
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
    obtenir_rayon_fleche
import copy


class TestMutationScorpion:

    scorpion = generate_scorpion()

    def test_muter_angle_tir(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_angle_tir(self.scorpion)
        assert obtenir_angle(scorpion_origin) != obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_longueur_bras(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_longueur_bras(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) != obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_longueur_base_bras(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_longueur_base_bras(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) != obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_hauteur_base_bras(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_hauteur_base_bras(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) != obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_longueur_corde(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_longueur_corde(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) != obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_longueur_fleche(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_longueur_fleche(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) != obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_rayon_fleche(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_rayon_fleche(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) != obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_module_young(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_module_young(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) != obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_masse_volumique(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_masse_volumique(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) != obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) == obtenir_coeff_poisson_materiau(self.scorpion)

    def test_muter_coefficient_poisson(self):
        scorpion_origin = copy.copy(self.scorpion)
        muter_coefficient_poisson(self.scorpion)
        assert obtenir_angle(scorpion_origin) == obtenir_angle(self.scorpion)
        assert obtenir_longueur_bras(scorpion_origin) == obtenir_longueur_bras(self.scorpion)
        assert obtenir_longueur_base_bras(scorpion_origin) == obtenir_longueur_base_bras(self.scorpion)
        assert obtenir_hauteur_base_bras(scorpion_origin) == obtenir_hauteur_base_bras(self.scorpion)
        assert obtenir_longueur_corde(scorpion_origin) == obtenir_longueur_corde(self.scorpion)
        assert obtenir_longueur_fleche(scorpion_origin) == obtenir_longueur_fleche(self.scorpion)
        assert obtenir_rayon_fleche(scorpion_origin) == obtenir_rayon_fleche(self.scorpion)
        assert obtenir_module_young_materiau(scorpion_origin) == obtenir_module_young_materiau(self.scorpion)
        assert obtenir_masse_volumique_materiau(scorpion_origin) == obtenir_masse_volumique_materiau(self.scorpion)
        assert obtenir_coeff_poisson_materiau(scorpion_origin) != obtenir_coeff_poisson_materiau(self.scorpion)

    def test_mutation_individu(self):
        scorpion_origin = copy.copy(self.scorpion)
        mutation_individu(self.scorpion)
