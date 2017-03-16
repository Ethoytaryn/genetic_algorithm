from math import pi
from src.Tools.Constante import ZERO
# ##################################################################
# PARAMETRE DE LA SIMULATION
# ##################################################################

# Portée du scorpion que l'on souhaite
DESIRED_SCOPE = 350

# Probabilite de mutation
CHANCE_TO_MUTATE = 0.05

# Probabilite d'hybridation
CHANCE_TO_HYBRID = 0.98

# Population
POPULATION_COUNT =8000

# Nombre de génération maximum
GENERATION_COUNT = 200


LIMITE_LONGUEUR_BASSE = 0.01
LIMITE_LONGUEUR_HAUTE = 50

LIMITE_ANGLE_BASSE = ZERO
LIMITE_ANGLE_HAUTE = pi / 2

LIMITE_MASSE_VOL_BASSE = 20
LIMITE_MASSE_VOL_HAUTE = 7000

LIMITE_MODULE_YOUNG_BASSE = ZERO
LIMITE_MODULE_YOUNG_HAUTE = 2000

LIMITE_POISSON_BASSE = ZERO
LIMITE_POISSON_HAUTE = 0.5
