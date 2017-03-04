from math import pi
from src.Tools.Constante import ZERO
# ##################################################################
# PARAMETRE DE LA SIMULATION
# ##################################################################

# Portée du scorpion que l'on souhaite
DESIRED_SCOPE = 350

# Probabilite de mutation
CHANCE_TO_MUTATE = 0.01

# Probabilite d'hybridation
CHANCE_TO_HYBRID = 0.95

# Population
POPULATION_COUNT = 200

# Nombre de génération maximum
GENERATION_COUNT = 1000


LIMITE_LONGUEUR_BASSE = 0.01
LIMITE_LONGUEUR_HAUTE = 15000

LIMITE_ANGLE_BASSE = ZERO
LIMITE_ANGLE_HAUTE = pi / 2

LIMITE_MASSE_VOL_BASSE = 20
LIMITE_MASSE_VOL_HAUTE = 15000

LIMITE_MODULE_YOUNG_BASSE = ZERO
LIMITE_MODULE_YOUNG_HAUTE = 2000

LIMITE_POISSON_BASSE = ZERO
LIMITE_POISSON_HAUTE = 0.999999
