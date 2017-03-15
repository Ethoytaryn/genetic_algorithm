from src.Tools.Physique import \
    calculer_ressort, \
    calculer_longueur_vide,\
    calculer_longueur_deplacement, \
    calculer_masse_projectile, \
    calculer_vitesse
from math import sqrt


class TestPhysique:

    def test_calculer_ressort_infini(self):
        module_young = 10.0
        coefficient_poisson = .5
        ressort = calculer_ressort(module_young, coefficient_poisson)
        assert ressort == 999999999.99
        assert type(ressort) == float

    def test_calculer_ressort_standart(self):
        module_young = 10
        coefficient_poisson = 0.1
        ressort = calculer_ressort(module_young, coefficient_poisson)
        result = 100.0 / 24.0
        assert round(ressort, 5) == round(result, 5)
        assert type(ressort) == float

    def test_calculer_longueur_vide_corde_sup_bras(self):
        longueur_bras = 10.0
        longueur_corde = 50.0
        assert calculer_longueur_vide(longueur_bras,longueur_corde) == -1

    def test_calculer_longueur_vide(self):
        longueur_bras = 10.0
        longueur_corde = 4.0
        result = calculer_longueur_vide(longueur_bras, longueur_corde)
        assert round(result, 5) == round(sqrt(9), 5)
        assert type(result) == float

    def test_calculer_longeur_deplacement_vide_sup_fleche(self):
        longueur_bras = 10.0
        longueur_corde = 4.0
        longueur_fleche = 1
        result = calculer_longueur_deplacement(longueur_fleche,longueur_bras,longueur_corde)
        assert result == 0.0
        assert type(result) == float

    def test_calculer_longeur_deplacement(self):
        longueur_bras = 10.0
        longueur_corde = 4.0
        longueur_fleche = sqrt(96)
        result = calculer_longueur_deplacement(longueur_fleche, longueur_bras, longueur_corde)
        assert type(result) == float

    def test_calculer_masse_projectile(self):
        masse_volumique = 10.0
        rayon_fleche = 1.0
        longueur_fleche = 10.0
        result = calculer_masse_projectile(masse_volumique, rayon_fleche, longueur_fleche)
        assert round(result, 5) == 314.15927

    def test_calculer_vitesse_projectile(self):
        module_young = 10.0
        coefficient_poisson = 0.4
        longueur_bras = 10.0
        longueur_corde = 4.0
        longueur_fleche = 1.0
        masse_volumique = 10.0
        rayon_fleche = 10.0
        masse = calculer_masse_projectile(masse_volumique,rayon_fleche,longueur_fleche)
        ressort = calculer_ressort(module_young,coefficient_poisson)
        ld = calculer_longueur_deplacement(longueur_fleche,longueur_bras,longueur_corde)
        vitesse = sqrt(ressort * pow(ld, 2) / masse)
        result = calculer_vitesse(module_young, coefficient_poisson,
                                  longueur_fleche, longueur_bras, longueur_corde, masse_volumique, rayon_fleche)
        assert vitesse == result
        assert type(result) == float
