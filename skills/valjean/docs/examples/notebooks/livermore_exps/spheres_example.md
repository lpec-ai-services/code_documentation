<!-- source: examples/notebooks/livermore_exps/spheres_example.ipynb -->

# Sphères de Livermore

## Description rapide de l'expérience

Les expériences dites "Sphères de Livermore" ont été réalisées fin des années 60 - début des années 70 au Lawrence Livermore Laboratory (États-Unis).

Une sphère creuse est placée au centre d'un bunker. En son centre on a une source de neutrons à 14 MeV (faisceau de $^2\mathrm{H}^+$ sur une cible d'tritium, réaction $^3\mathrm{H}(d, n)^4\mathrm{He}$). Des détecteurs sont positionnés autour de la sphère après collimation.

On observe le spectre en temps des neutrons qui arrivent dans les détecteurs (réponse type `REACTION` dans Tripoli-4).

Pour une sphère donnée on exécute deux fois la simulation :

- avec la sphère étudiée (matériau = fer, béryllium, azote, eau, etc)
- avec la même sphère dont le matériau étudié a été remplacé par de l'**air**

Cette seconde sphère nous permet de normaliser les résultats et de pouvoir nous comparer aux données expérimentales notamment grâce à un graphique. Il y a donc deux sorties Tripoli-4 à lire et des opérations à faire sur les spectres.

Dans le cas présent la sphère considérée est celle d'azote liquide, d'une épaisseur de 3.1 mfp (libre parcours moyen), avec un spectre à 30°.

<img src="N_3.1mfp.png" width="600">

## Parsing des résultats Tripoli-4 et récupération du spectre

### Parser les résultats

``` python
from valjean.eponine.tripoli4.parse import Parser
jdd_sphere = 'prob103_nitrogen3.1_fine_timeShifted_sphere_PARA.d.res'
jdd_air = 'prob103_nitrogen3.1_fine_timeShifted_air_PARA.d.res'
```

Le module permettant de lire, parser et récupérer les résultats de Tripoli-4 sous un format plus facilement exploitable est `Parser`.

On ne regardera ici que le résultat du dernier batch. Le parsing est effectivement fait par la méthode `parse_from_index`. L'index par défaut est `-1`, ce qui correspond au dernier batch.

Pour manipuler plus aisément les réponses de Tripoli-4 et en particulier les sélectionner on utilise un objet `Browser`.

``` python
sphere_b = Parser(jdd_sphere).parse_from_index(name='sphere').to_browser()
air_b = Parser(jdd_air).parse_from_index(name='air').to_browser()
```

### Sélection du résultat

À chaque réponse dans ce jeu de données a été associé un `SCORE NAME` unique (et explicite). C'est le moyen le plus aisé de récupérer les réponses nécessaires.

Dans le cas de la sphère (ici d'azote liquide), on récupère `score_name='neutron_response_30deg'`, soit le spectre neutron à 30 degrés (des spectres photons sont aussi disponibles). Il s'agira du numérateur (variable `nsphere`). Dans le cas de l'air, seule l'intégrale du spectre est nécessaire pour la normalisation, donc au dénominateur (variable `dair`). La sélection de la réponse se fait sur `score_name='neutron_response_integral_30deg'`.

``` python
nsphere = sphere_b.select_by(score_name='neutron_response_30deg')
dair = air_b.select_by(score_name='neutron_response_integral_30deg')
```

### Transformation des données en `Dataset`

Pour pouvoir manipuler les données plus aisément mais aussi pour faciliter leur manipulation, elles sont transformées en `Dataset`.

Le but de `Dataset` est d'être commun à tous les types de données (Tripoli-4, données expérimentales, PATMOS, MCNP, etc). Chaque dataset contient au moins 2 membres : `value` et `error`. Il s'agit de l'incertitude absolue (et non pas relative comme dans les résultats standard Tripoli-4). Trois autres membres sont optionnels : `bins`, `name` et `what`.

Les données sont stockées sous forme de `Dataset` accessible dans le `Browser` sous la clef `'results'`.

Pour info :

``` python
test_ds = nsphere['results']['score']
print(type(test_ds))
print(test_ds)
```

``` python
print(test_ds.squeeze().shape)
```

Pour les manipuler plus simplement, les `Dataset` sont *squeezés* : nous récupérons des spectres en temps, les 6 autres dimensions sont donc à 1 et non utiles ici (et triviales).

``` python
nsphereds = nsphere['results']['score'].squeeze()
nsphereds.name="azote (num)"
```

``` python
dairds = dair['results']['score'].squeeze()
dairds.name='air (denom)'
print(dairds)
```

### Normalisation du spectre

Le résultat correspondant à l'intégrale du spectre n'est en réalité ici pas un score générique, mais un réel spectre. Cette différence est due aux intervalles extrêmes :

- entre t=0 et le début des résultats expérientaux, à t=138 ns pour le premier
- entre t=410 ns et t=10 s pour le dernier, soit entre la fin des résultats expérimentaux et la valeur maximale du temps dans Tripoli-4

Pour être plus juste, notamment au niveau du calcul des incertitudes associées, le choix a été fait de faire un spectre de 3 intervalles où seul celui du milieu nous intéresse dans le cas présent.

L'incertitude sur la norme est négligée par la suite (elle est dominée par celle sur chaque intervalle).

``` python
import numpy as np
norm = dairds.value[1]
print("type(norm) = {0}, shape(norm) = {1}".format(type(norm), norm.shape))
```

En réalité deux normalisations du spectre sont à effectuer, celle par l'intégrale de l'air et celle par la largeur des bins, appelée ici `TIME_BIN_WIDTH`, valant 2 ns.

``` python
TIME_BIN_WIDTH = 2
t4ds = nsphereds / norm / TIME_BIN_WIDTH
```

Remarque : il n'aurait pas été possible d'utiliser un `Dataset` issu de `dairds` pour la normalisation.

``` python
print(dairds)
test_dairds = dairds.copy()[1:-1]
print(test_dairds)
```

``` python
test_ds = nsphereds / test_dairds / TIME_BIN_WIDTH
```

Ces deux datasets n'ont bien pas les shapes or les calculs sur les `Dataset` ne peuvent être effectués que s'ils ont la même *shape* et, dans le cas où des bins ont été fournis, si leurs bins sont équivalents.

``` python
'shape(t4ds) = {0}, shape(test_dairds) = {1}'.format(t4ds.shape, test_dairds.shape)
```

### Réarrangement des intervalles

Les temps sont par défaut en *s* dans Tripoli-4 alors que les données que nous avons à disposition sont données par intervalles de temps en *ns*, on convertit donc les intervalles de Tripoli-4 en *ns*.

Par ailleurs, les intervalles en temps dans le jeu de données ont été décalés de 100 ns pour que la description de la source (gaussienne) soit correcte et complètement prise en compte dans le temps de la simulation (jeu de données tourné avec Tripoli-4, version 10.2, ce bug a été corrigé pour la version 11, mais c'est une jolie illustration des calculs possibles sur les `Dataset`).

``` python
print('Bins en s et avant décalage:\n',t4ds.bins['t'] )
t4ds.bins['t'] = t4ds.bins['t'] * 1e9 - 100
print('Bins en ns et après décalage:\n', t4ds.bins['t'])
```

De plus, le dataset actuel, `t4ds`, contient toujours les bins extrêmes, il faut donc les enlever.

Le *slicing* a été codé dans `Dataset` : il est effectué en même temps sur les valeurs, sur les erreurs et sur les intervalles.

``` python
print('bins en temps (avant slicing):')
print(t4ds.bins['t'])
print("shape(t4ds) = {0}, bins(nom = {1}, shape = {2})"
      .format(t4ds.shape, list(t4ds.bins.keys()), t4ds.bins['t'].shape))
t4ds = t4ds[1:-1]
print('bins en temps (après slicing):')
print(t4ds.bins['t'])
print("shape(t4ds) = {0}, bins(nom = {1}, shape = {2})"
      .format(t4ds.shape, list(t4ds.bins.keys()), t4ds.bins['t'].shape))
```

Enfin, les données issues de la simulation sont données par intervalle (avec les extémités des intervalles) alors que les données expérimentales sont données au centre de l'intervalle. Ces dernières sont également des `int` et non des `float` comme les temps issus de Tripoli-4. L'étape finale est donc de supprimer la première (ou dernière) valeur dans les *bins* et de toutes les décaler d'1 ns (largeur d'intervalle toujours de 2 ns) et de les transformer en `int`.

``` python
t4ds.bins['t'] = np.rint(t4ds.bins['t'][1:] - 1)
print(t4ds.bins['t'])
```

Le `Dataset` est maintenant prêt pour la comparaison aux données. On met simplement à jour son nom et la variable qu'il représente (ordonnée) pour le représenter explicitement.

``` python
t4ds.name = 'T4'
t4ds.what = 'Neutron count rate'
```

## Résultats expérimentaux

Les résultats expérimentaux sont fournis dans un fichier ASCII, sous forme de tableaux de valeurs. Il faut donc les parser et les transformer en `Dataset`.

Cette étape est actuellement faite dans une petite classe externe : [LivermoreExps](livermore_exps.py)

``` python
from livermore_exps import LivermoreExps

exps = LivermoreExps('s10a11.res.mesure')
```

Toutes les données expérimentales sont ainsi disponibles, il suffit de les charger une seule fois pour toutes les analyses des sphères de Livermore. Ici on ne considèrera qu'un seul cas : `('NITROGEN', '3.1', '30')`.

``` python
exp_key = ('NITROGEN', '3.1', '30')
exp_data = exps.res[exp_key]
type(exp_data)
```

``` python
print(exp_data)
```

Les objets dans le dictionnaire de résultat (`exps.res`) sont des `Dataset`.

## Comparaison entre données et expérience

Pour les graphiques on utilise le rapport des spectres simulé et expérimental. La classe `Dataset` fournit les outils pour faire ce type de calculs.

``` python
print(np.array_equal(t4ds.bins['t'], exp_data.bins['t']))
```

Malgré le fait que les bins nous apparaissaient complètement équivalents, ils ne l'étaient pas : cela vient probablement de la conversion de strings (depuis les fichiers ASCII) en float alors que les nombres n'étaient pas écrits de la même manière (`int` pour les données expérimentales, `float` en notation exponentielle à 6 chiffres après la virgule pour Tripoli-4 ayant subis quelques calculs en plus).

``` python
ratio = t4ds / exp_data
```

## Comparaisons numériques

Il est possible de comparer les deux `Dataset` numériquement grâce aux fonctions disponibles dans `gavroche.test.py` qui agissent sur les datasets.

``` python
from valjean.gavroche.test import TestApproxEqual
test_equality = TestApproxEqual(t4ds, exp_data, name='light criteria on approx eq', rtol=0.1, atol=1e-2)
print(bool(test_equality.evaluate()))
```

Lors de la VV ce test est davantage fait sur l'intégrale du spectre.

``` python
integ = sphere_b.select_by(score_name='neutron_response_integral_30deg')
intnumds = integ['results']['score'].squeeze()
intnumds.name='integ'
integds = intnumds / norm / TIME_BIN_WIDTH
integds = integds[1:-1]
print(integds)
```

Petite vérification de routine rapide :

``` python
np.allclose(np.sum(t4ds.value), integds.value)
```

On supprime les bins ici pour simplifier la comparaison (il s'agit d'une intégrale).

``` python
from collections import OrderedDict
integds.bins = OrderedDict()
print(integds)
```

Intégrale des données, en supposant les intervalles indépendants :

``` python
from valjean.eponine.dataset import Dataset
```

``` python
quad_err = np.sqrt(np.sum(exp_data.error ** 2))
integ_data = Dataset(np.sum(exp_data.value), quad_err)
print(integ_data)
```

``` python
equ_integ = TestApproxEqual(integds, integ_data, name='approx eq integrales', rtol=0.03, atol=1e-4)
print(bool(equ_integ))
```

## Graphiques par défaut dans valjean

La majorité des tests peut être représentée sous forme de graphique.

``` python
from valjean.javert.representation import FullRepresenter
from valjean.javert.rst import RstFormatter
from valjean.javert.mpl import MplPlot
from valjean.javert.verbosity import Verbosity

frepr = FullRepresenter()
rstformat = RstFormatter()
```

``` python
teq_res = test_equality.evaluate()
eqrepr = frepr(teq_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
eqrst = rstformat.template(eqrepr[1])
print(eqrst)
mpl = MplPlot(eqrepr[0]).draw()
```

Avec un test de Holm-Bonferroni puisqu'il s'agit d'un spectre :

``` python
from valjean.gavroche.stat_tests.student import TestStudent
from valjean.gavroche.stat_tests.bonferroni import TestHolmBonferroni
```

``` python
sphere_b.globals
studt = TestStudent(t4ds, exp_data, name='Student test', ndf=sphere_b.globals['edition_batch_number'])
hb_res = TestHolmBonferroni(test=studt, name='Holm-Bonferroni test', description='').evaluate()
```

``` python
hbrepr = frepr(hb_res, verbosity=Verbosity.INTERMEDIATE)  # il s'agit d'une liste de templates
hbrst = rstformat.template(hbrepr[1])
print(hbrst)
mpl = MplPlot(hbrepr[0]).draw()
```

D'autres niveaux de verbosité sont disponibles. Il est également possible de changer un peu la représentation graphique des tests en utilisant une échelle logarithmique pour les données et la simulation par exemple.

``` python
from valjean.javert import plot_repr as pltr
def log_post(templates, tres):
    pltr.post_treatment(templates, tres)
    for templ in templates:
        templ.subplots[0].attributes.logy = True
    return templates
```

``` python
hbrepr = FullRepresenter(post=log_post)(hb_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
print(len(hbrepr[1:]))
hbrst = '\n'.join([str(rstformat.template(hbrepr[1])), str(rstformat.template(hbrepr[2]))])
print(hbrst)
mpl = MplPlot(hbrepr[0]).draw()
```

L'impression des résultats des `TestStudent` dans le cas `FULL_DETAILS` donne le tableau de Student en `INTERMEDIATE`, soit les bins où le test à échouer.

**Remarque** : le test de Holm-Bonferroni n'est pas très adapté ici, comme nous comparons les données à la simulation, nous n'avons pas de nombre de degrés de liberté similaire pour les deux échantillons.

## Graphiques de comparaison entre les données expérimentales et Tripoli-4

L'analyse des données peut également être faite en dehors de **valjean** en fonction de ses nécessités.

Comme pour la lecture des résultats expérimentaux, une petite classe a été dérivée pour facilier et personnaliser les graphiques de comparaison.

La bibliothèque utilisée est `matplotlib`.

Dans notre cas, on souhaite aisément :

- ajouter une nouvelle courbe, avec ses erreurs
- visualiser le rapport entre les différentes courbes
- pouvoir personnaliser facilement la couleur et l'aspect des courbes (aisé grâce à `matplotlib`, les arguments sont juste transmis ici)

Cette petite classe, [CompPlot](comp_plots.py), est aussi disponible dans le notebook.

Le nom de « l'analyse » correspond à la clef pour les données expérimentales. Cela permet de générer par exemple le titre.

``` python
import matplotlib.pyplot as plt
from comp_plots import CompPlot

cplot = CompPlot(exp_key)
cplot.add_errorbar_plot(exp_data.bins['t'], exp_data.value, exp_data.error,
                        fmt='o', c='black', ms=2, ecolor='black', label='Experiment')
cplot.add_errorbar_plot(t4ds.bins['t'], t4ds.value, t4ds.error,
                        label='T4', drawstyle='steps-mid', fmt='-', c='orange')

cplot.add_errorbar_ratio(ratio.bins['t'], ratio.value, 0,
                         drawstyle='steps-mid', fmt='-', c='green')
cplot.splt[1].fill_between(
    ratio.bins['t'],
    np.ones(ratio.bins['t'].size) - exp_data.error/exp_data.value,
    np.ones(ratio.bins['t'].size) + exp_data.error/exp_data.value,
    facecolor='lightgrey', step='mid')
cplot.customize_plot()
plt.show()
```
