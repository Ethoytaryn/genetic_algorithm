# Genetic Algorithm 

### Paramètre de la simulation

<p> Dans le fichier « src.Metier.Parametre_simulation.py », vous pourrez trouver toutes les constantes qui paramètre la simulation :
<ul>
<li>DESIRED_SCOPE,  type : float : portée que le scorpion doit atteindre en mètre</li>
<li>CHANCE_TO_MUTATE, type : float : chance de muter entre 0 et 1</li>
<li>CHANCE_TO_HYBRIDE, type : float : chance d’hybridation d’un enfant</li>
<li>POPULATION_COUNT, type: integer : nombre de scorpion par génération</li>
<li>GENERATION_COUNT, type : integer : nombre de génération</li>
<li>LIMITE_<parametre>_<limite>*, type : float : limite haute ou basse de l’intervalle de valeur possible lors de la génération aléatoire du <parametre></li>
</ul>
</p>

### Run une simulation

<p>Pour lancer la simulation, il faut ouvrir une console depuis le dossier genetic_algorithm puis lancer la commande :</p>

<pre><code>pip install matplotlib</code></pre>

<p> Une fois la librairie installée, on peut lancer le script :<p>
	
<pre><code>Python Main.py</code></pre>

###Affichage console et graphe

Pendant l’exécution du script, les paramètres de la simulation, la progression, le nombre de génération traitée et le temps écoulé seront affichés dans la console.
Une fois le script terminé, les caractéristiques du meilleur scorpion seront affichés dans la console et une fenêtre avec les graphes : fitness, variance, énergie, portée en fonction de la génération s’ouvrira.
