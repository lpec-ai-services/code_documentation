<!-- source: examples/notebooks/replica/replica_example.ipynb -->

# Benchmark REPLICA : exemples de parsing

## Principe du parsing des sorties Tripoli-4 standard

Le parsing est effectué en deux temps :

- un premier parcours rapide du fichier répérant un certain nombre de balises (nombre de bacthes requis, temps d'initialisation, de simulation, `NORMAL COMPLETION`, etc) $\rightarrow$ module `scan.py`. Ce parcours permet également de repérer les résultats dans la sortie, débutant par `RESULTS ARE GIVEN` et terminant le plus souvent par `'simulation time:'`.

- le réel parsing des résultats, piloté par le module `parse.py` qui appelle la grammaire (utilisant `pyparsing`) et transformant le résultat en objets python standards (listes, dictionnaires, tableaux numpy).

## Exemple de parsing, jeu de données `fast_neutron.t4`

### Présentation du jeu de données

[Le jeu de données](fast_neutron.t4) est issu du benchmark REPLICA du programme SINBAD, dont la géométrie Tripoli-4 est représentée ci-dessous. Il s'agit ici de la simulation des neutrons rapides.

<img src="replica_full.png" width="400">

2 types de réponses sont attendus :

- réactions dans des détecteurs
- flux surfacique

Dans le cas des neutrons rapides on dispose de 3 détecteurs : $^{103}\mathrm{Rh}$ (`RH103_IRDF85`), $^{115}\mathrm{In}$ (`IN115_IRDF85`) et $^{32}\mathrm{S}$ (`S32_IRDF85`).

On fait ces mesures à différents emplacements. Le résultat final est constitué de :

- 10 réactions sur le $^{103}\mathrm{Rh}$ (10 frontières de volume différentes)
- 3 réactions sur le $^{115}\mathrm{In}$
- 3 réactions sur le $^{32}\mathrm{S}$
- 2 flux surfaciques

Les emplacements des mesures sont représentés ci-dessous.

<img src="replica_detectors.png" width="400">

### Étape 1 : scan puis parsing du résultat

On charge le module `Parser`. Le jeu de données est scanné automatiquement, tous les résultats de batches sont stockés dans la variable `scan_res`. On peut ensuite parser ceux qui nous intéressent.

Par défaut le résultat parsé sera le dernier batch, mais on pourrait en parser un autre.

Dernier batch $\rightarrow$ -1

#### Scan du jeu de données

``` python
from valjean.eponine.tripoli4.parse import Parser
```

``` python
t4vv_replica_fast = 'fast_neutron.res'
t4p = Parser(t4vv_replica_fast)
```

Parmi les membres de `t4p` il y a le résultat du scan. Certains paramètres accessibles à partir de ce résultat sont montrés ici :

- parallèle ou mono-processeur (booléen)
- les temps

``` python
t4p.scan_res.normalend
```

``` python
t4p.scan_res.para
```

``` python
type(t4p.scan_res)
```

``` python
t4p.scan_res.times
```

#### Parsing du jeu de données

Le jeu de données peut être parser soit par numéro du batch quand on le connaît, grâce à la méthode `parse_from_number`, soit par son index dans la liste des batches scannés grâce à la méthode `parse_from_index`.

Le plus souvent c'est le dernier batch qui nous intéresse, le défaut de `parse_from_index` est donc `-1`.

Ces méthodes renvoient un `ParseResult` qui contient le batch parsé ainsi que les variables globales du jeu de données récupérées lors du scan (objet `res`).

Le `ParseResult` peut alors être transformé en `Browser` pour faciliter l'accès aux différents résultats grâce à la méthode `to_browser`.

``` python
t4pres = t4p.parse_from_index()
```

``` python
len(t4pres.res), type(t4pres.res), list(t4pres.res.keys())
```

``` python
print('run_data:', t4pres.res['run_data'])
print('batch_data:', t4pres.res['batch_data'])
```

Le résultat stocké dans `ParseResult` est un dictionnaire.

- `'batch_data'` correspond aux données spécifiques du batch (temps de simulation cumulé à la fin de celui-ci, numéro d'édition, intensité de la source, etc.)
- `'run_data'` correspond aux données globales du jeu de données (temps d'initialisation, les nombres d'erreurs et de warnings, le nom du jeu de données, etc.
- `'list_responses'` est la liste des résultats (liste de dictionnaires)

``` python
print(type(t4pres.res['list_responses']))
print(type(t4pres.res['list_responses'][-1]))
```

Les différents résultats sont stockés dans la liste dans l'ordre où ils apparaissent dans la sortie de TRIPOLI4, sous forme de dictionnaires.

Exemple court :

``` python
print(t4pres.res['list_responses'][0])
```

Pour manipuler plus aisément les résultats un `Browser` est disponible :

``` python
t4b = t4pres.to_browser()
```

``` python
print(t4b)
```

Il permet notamment de faire la sélection des résultats à partir des métadonnées du cas considéré. Leur nom est donné dans le `print` du `Browser`.

Les résultats de Tripoli-4 apparaissent sous la forme d'une liste de réponses (ou d'une liste de scores) dans le listing de sortie. Le `Browser` permet de les sélectionner de manière plus efficace.

Les résultats sont encapsulés dans un `Dataset`.

### Étape 2 : sélection des données grâce au `Browser`

On différencie dans chaque "réponse" les données, soit les résultats du calcul effectué, et les métadonnées qui permettent de l'identifier. Chaque réponse est un dictionnaire dont la clef `'results'` correspond aux données. Le `Browser` est construit à partir de cela.

Le `Browser` contient notamment :

- la liste des résultats et de leurs métadonnées (`content`)
- un index sur ces résultats (`index`), basé sur les métadonnées
- les variables globales du batch (`globals`)

À noter : il est possible d'utiliser une autre clef que `'results'` pour les données, à condition de le spécifier à la créaction du `Browser` grâce à l'argument `data_key`.

#### Explorer le `Browser`

2 niveaux d'impression sont également disponibles pour le `Browser`.

Méthodes d'aide pour découvrir le `Browser` :

- `keys`: pour obtenir toutes les clefs de l'index, soit le nom / identifiant des métadonnées du listing concerné
- `available_values`: pour obtenir les valeurs correspondant à ces métadonnées

Dans ces deux cas il s'agit de *générateurs*. Pour afficher correctement les résultats il faut les encapsuler dans une liste par exemple.

``` python
print('{!s}'.format(t4b))  # équivalent à print(t4rb)
```

``` python
print('{!r}'.format(t4b))
```

``` python
list(t4b.keys())
```

``` python
print('values for score_name:', list(t4b.available_values('score_name')))
print('values for response_function:', list(t4b.available_values('response_function')))
print('values for scoring_zone_id:', list(t4b.available_values('scoring_zone_id')))
print('values for particle:', list(t4b.available_values('particle')))
print('values for reaction_on_nucleus:', list(t4b.available_values('reaction_on_nucleus')))
```

#### Sélection des réponses / résultats grâce au `Browser`

Il est possible de sélectionner les réponses à partir des métadonnées. La méthode à choisir dépend de l'objet dont on a besoin en sortie.

- `filter_by` pour récupérer un sous-`Browser`
- `select_by` pour récupérer la réponse si elle est unique

La sélection se fait

- par mot-clef/valeur, soit métadonnée/valeur de cette métadonnée (*keyword arguments* correspondant aux clefs disponibles)
- `include=tuple(key)` pour sélectionner toutes les réponses contenant cette métadonnée sans distinction de la valeur
- `exclude=tuple(key)` pour exclure les réponses contenant une métadonnée

`include` et `exclude` ne fonctionnent que sur le nom de la métadonnée, pas sur sa valeur.

Ces 3 possibilités sont bien sûr combinables.

``` python
b_flux = t4b.filter_by(response_function='FLUX')
print(b_flux)
```

Le nombre de réponses dans le `Browser` n'est maintenant plus que de 2 au lieu de 18, il ne reste plus que celles correspondant à un flux. Récupérer les réponses peut se faire directement ou avec l'autre méthode.

Le sous-`Browser` remet à zéro les index (en crée un nouveau en réalité).

À noter : les variables globales du `Browser` sont transmises au sous-`Browser`.

``` python
b_flux.globals == t4b.globals
```

``` python
b_excl_compo = t4b.filter_by(exclude=('composition',))  # attention à bien utiliser un tuple
print(b_excl_compo)
```

Les réponses ont été « aplaties » (ou *flattened*). Dans le jeu de données d'origine 3 réponses sont demandées sur une liste de scoring zones à chaque fois.

    SCORE
    	4
    	NAME reaction_Rh103_l10surf
    	reaction_Rh103
    	SURF DECOUPAGE DEC_INTEGRAL FRONTIER LIST 10
    		11 20	12 21	12 22	12 23	12 24	
    		12 25	12 26	14 27	14 28	16 29
    	NAME reaction_In115_l3surf
    	reaction_In115
    	SURF DECOUPAGE DEC_INTEGRAL FRONTIER LIST 3
    		14 27	14 28	16 29
    	NAME reaction_S32_l3surf
    	reaction_S32
    	SURF DECOUPAGE DEC_INTEGRAL FRONTIER LIST 3
    		14 27	14 28	16 29
    	NAME flux_l2surf
    	flux
    	SURF DECOUPAGE DEC_SPECTRE FRONTIER LIST 2
    		14 27	16 29
    FIN_SCORE

Pour récupérer une réponse donnée dans le cas présent il faut au moins deux critères, dont `scoring_zone_id`.

``` python
b_reacIn_16_29 = t4b.filter_by(score_name='reaction_In115_l3surf', scoring_zone_id=(16, 29))
print(b_reacIn_16_29)
```

Sélection d'une réponse donnée : `select_by`

``` python
reacIn_16_29 = t4b.select_by(score_name='reaction_In115_l3surf', scoring_zone_id=(16, 29))
print(type(reacIn_16_29))
print(reacIn_16_29)
```

``` python
flux_14_27 = t4b.select_by(response_function='FLUX', scoring_zone_id=(14, 27))
print(type(flux_14_27))
print(list(flux_14_27['results'].keys()))
```

Une fois le résultat voulu sélectionné on peut accéder aux données elles-mêmes.

Dans le cas de `flux_14_27` (flux surfacique entre les surfaces 14 et 27) il existe 6 types de données :

- les nombres de batches utilisés et mis de côté pour le calcul du flux
- le spectre utilisant tout le découpage en énergie (score demandé) (`score`)
- l'intégrale du spectre sur le découpage en énergie (`score_integrated`)
- le spectre score/lethargy, soit renormalisé à la largeur du bin, sur tout le découpage en énergie (`score/lethargy`)
- les unités

Tous ces résultats sont encapsulés dans un `Dataset`, à l'exception des unités qui sont dans un dictionnaire.

### Étape 3 : utilisation d'un `Dataset`

Le `Dataset` permet de comparer les données à d'autres grâce aux tests ou de les représenter par exemple.

Le `Dataset` permet de stocker les données et de faire des opérations dessus (ajout de datasets, sélection de dimension, multiplication par un dataset ou une constante, etc.). Les tests statistiques proposés par `valjean` attendent également des `Dataset`. Leur argument `name` est mis par défaut à celui du fichier parsé. L'argument `what` est utilisé pour donner à un nom au type de données qu'ils contiennent. Il sera utilisé en axe des ordonnées d'un histogramme 1D par exemple. Ces deux arguments sont modifiables à tout moment.

``` python
fds_flux_14_27 = flux_14_27['results']['score']
print(fds_flux_14_27)
fds_flux_14_27.name = 'flux(14, 27)'
fds_flux_14_27.what = 'Flux'
```

Les spectres (comme les maillages) sont par défault en 7 dimensions, dont les noms sont stockés dans les bins. Le dictionnaire de bins est un `OrderedDict` qui respecte l'ordre des dimensions de l'array Numpy.

Petit commentaire sur les noms de ces bins :

- `'u'`, `'v'`, `'w'` correspondent aux 3 variables d'espace (surtout pour les maillages), ce qui peut donc être par exemple $(x, y, z)$, $(r, \theta, z)$ ou $(r, \theta, \phi)$
- `'e'` l'énergie, `'t'` le temps
- `'mu'` et `'phi'` la direction de la particule

Des unités sont données par défaut (celle de Tripoli par défaut si non précisé, `unknown` pour les variables d'espace).

``` python
print(flux_14_27['results']['units'])
```

La plupart du temps beaucoup de ces dimensions ne sont pas précisées dans Tripoli-4, n'ont donc pas de découpage (ou de bins) et sont ainsi à 1 dans la shape. Pour les réduire, pour l'affichage ou l'utilisation, il est possible de *squeezer* le `Dataset`. Cette suppression des dimensions non utilisées en conseillée pour les tests.

Dans le cas de `flux_14_27` seule la dimension correspondant à l'énergie est pertinente, le *squeeze* permet de ne conserver qu'elle.

``` python
ds_flux_14_27 = fds_flux_14_27.squeeze()
print(ds_flux_14_27)
```

Le `Dataset` correspondant au résultat intégré du spectre donne quant à lui :

``` python
ds_flux_14_27_int = flux_14_27['results']['score_integrated']
print(ds_flux_14_27_int)
ds_flux_14_27_int.name='flux_14_27'
ds_flux_14_27_int.what='Flux'
print(ds_flux_14_27_int.squeeze())
```

Le *squeeze* supprime les bins dans deux conditions :

- il n'y a pas de bins
- il n'y a qu'un bin, donc la dimension est triviale

**Remarque** : pour une dimension donnée, si on a N valeurs, les bins sont

- soit donnés par leurs limites, il y a donc N+1 valeurs de bins,
- soit donnés par leurs centres, il y a donc N valeurs

Pour construire un `Dataset` on doit cependant connaître les clefs disponibles sous `results`.

Dans le cas des taux de réaction on a :

``` python
print(list(reacIn_16_29['results'].keys()))
```

Dans ce cas précis, comme le découpage ne comprend qu'un seul bin, le `Dataset` issu de `'integrated'` et celui issu de `'spectrum'` devraient être les mêmes.

``` python
ds_reacIn_16_29_spec = reacIn_16_29['results']['score']
ds_reacIn_16_29_spec.name='spectrum'
ds_reacIn_16_29_spec.what='Flux'
print(ds_reacIn_16_29_spec)
print(ds_reacIn_16_29_spec.value)
ds_reacIn_16_29_int = reacIn_16_29['results']['score_integrated']
ds_reacIn_16_29_int.name='integrated'
ds_reacIn_16_29_int.what='Flux'
print(ds_reacIn_16_29_int)
print(ds_reacIn_16_29_int.value)
```

### Étape 4 : faire un test et le représenter, exemple du test de Student

Pour avoir une description du test de Student, voir la documentation de *valjean*.

``` python
from valjean.gavroche.stat_tests.student import TestStudent
```

La représentation d'un test peut se faire sous forme de tableau ou de graphique.

``` python
# includes et initialisations pour les tableaux
from valjean.javert.representation import TableRepresenter
from valjean.javert.rst import RstFormatter

tabrepr = TableRepresenter()
rstformat = RstFormatter()
```

``` python
# include et initialisation pour les graphiques
from valjean.javert.representation import PlotRepresenter
from valjean.javert.mpl import MplPlot

plotrepr = PlotRepresenter()
```

#### Comparaison de l'intégrale du spectre et du spectre dans le cas de la réaction sur In115 entre les surfaces 16 et 29

``` python
stud_reacIn = TestStudent(ds_reacIn_16_29_spec, ds_reacIn_16_29_int, name='spectrum vs intregral',
                          description="Comparaison du spectre sur 1 bin à l'intégrale").evaluate()
print(type(stud_reacIn))
print(bool(stud_reacIn))
```

``` python
montab = tabrepr(stud_reacIn)  # il s'agit d'une liste de TableTemplate
monrst = rstformat.template(montab[0])
print(monrst)
```

``` python
monplot = plotrepr(stud_reacIn)
print(monplot)
```

Les graphiques ne sont pas disponibles pour les quantités sans réels bins.

#### Comparaison des flux entre les surfaces 14 et 27 et les surfaces 16 et 29

Le découpage en énergie de ces deux flux étant les mêmes leur comparaison est possible.

``` python
# construction du Dataset pour le flux entre les surfaces 16 et 29
flux_16_29 = t4b.select_by(response_function='FLUX', scoring_zone_id=(16, 29))
ds_flux_16_29 = flux_16_29['results']['score'].squeeze()
ds_flux_16_29.name='flux(16, 29)'
ds_flux_16_29.what='Flux'
```

``` python
tstud_flux = TestStudent(ds_flux_14_27, ds_flux_16_29, name="flux_14_17_vs_16_29",
                         description="Comparison of the flux between surfaces 14 and 27 and surfaces 16 and 29")
stud_flux = tstud_flux.evaluate()
print(bool(stud_flux))
```

``` python
montab = tabrepr(stud_flux)  # encore une liste
monrst = rstformat.template(montab[0])
print(monrst)
```

``` python
monplot = plotrepr(stud_flux)
mpl = MplPlot(monplot[0]).draw()
```

Dans le cas d'un spectre un test de Student est effectué par bin. Dans le cas présent les spectres ne sont manifestement pas en accord, ce qui est attendu. Cependant, dans le cas d'une comparaison avec des données réellement comparables on peut s'attendre à un certain nombre de bins pour lesquels la comparaison échoue mais pas tous. Ce nombre dépend du nombre de bins.

Pour évaluer cela un autre test statistique est possible, le test de Holm-Bonferroni (voir la documentation pour plus de précisions).
