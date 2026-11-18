<!-- source: examples/notebooks/ap3_reader/ap3_reader.ipynb -->

# Lecture des fichiers *rates* d'Apollo3 : le `Reader`

La lecture des fichiers *rates* d'Apollo3 (réseau) est possible dans *valjean*, ainsi que les différents autres formats HDF5.

Deux modes de lecture sont possibles :

- lecture de tout le fichier HDF5 et stockage des résultats dans un `Browser`, récupération des résultats sous forme de `Dataset` grâce au `Browser` -\> utilisation du `Reader`
- lecture d'un résultat ou de plusieurs résultats donnés à partir du HDF5 pour une utilisation directe sous forme de `Dataset` -\> `Picker`

La seconde méthode est bien plus rapide car elle ne nécessite pas de charger l'intégralité du fichier et bénéficie des accès de lecture du HDF5.

Cet exemple se concentre sur la première méthode.

## Le `Reader` : résumé

``` python
from valjean.eponine.apollo3.hdf5_reader import Reader
```

Lecture d'un fichier *rates* typique : cas Mosteller, avec isotopes particularisés.

``` python
ap3r = Reader("full_rates.hdf")
```

Transformation en `Browser`

``` python
ap3b = ap3r.to_browser()
```

``` python
print(ap3b)
```

39 = nombre de résultats total dans le fichier.

Il est possible de faire les deux précédentes étapes en une seule :

``` python
from valjean.eponine.apollo3.hdf5_reader import hdf_to_browser
htb = hdf_to_browser("full_rates.hdf")
```

## Inspection du fichier

On peut inspecter davantage le fichier grâce au `Browser` et connaître notamment les valeurs possibles des clefs du `Browser`.

``` python
print(f'isotopes: {list(ap3b.available_values("isotope"))}')
print(f'resultats: {list(ap3b.available_values("result_name"))}')
print(f'zones: {list(ap3b.available_values("zone"))}')
print(f'outputs: {list(ap3b.available_values("output"))}')
```

Toutes les combinaisons ne sont pas possibles.

Pour sélectionner un résultat :

- si on ne sélectionne qu'un seul résultat : méthode `select_by` → dictionnaire correspondant au résultat demandé
- si on en sélectionne plusieurs en vue d'une sélection plus raffinée ensuite : `filter_by` → sous-`Browser` dont la liste de résultats a été réduite à ceux correspondant à la sélection demandée

Le résultat, sous forme de `Dataset`, se trouve sous la clef `'results'`.

``` python
sb_totout = ap3b.filter_by(zone='totaloutput')
print(sb_totout)
print(f'resultats: {list(sb_totout.available_values("result_name"))}')
print(f'outputs: {list(sb_totout.available_values("output"))}')
```

``` python
keffs = sb_totout.filter_by(result_name="keff")
print(len(keffs))
```

``` python
keff = sb_totout.select_by(result_name="keff")
print(keff)
```

``` python
sb_q = ap3b.filter_by(zone='q')
print(sb_q)
```

``` python
print(f'isotopes: {list(sb_q.available_values("isotope"))}')
print(f'resultats: {list(sb_q.available_values("result_name"))}')
print(f'outputs: {list(sb_q.available_values("output"))}')
```

``` python
sb_xe135 = sb_q.filter_by(isotope='Xe135')
print(f'resultats pour Xe135: {list(sb_xe135.available_values("result_name"))}')
```

``` python
sb_u238 = sb_q.filter_by(isotope='U238')
print(f'resultats pour U238: {list(sb_u238.available_values("result_name"))}')
```

## Sélection des résultats

La liste des résultats est disponible dans `content` dans le `Browser` ou directement grâce à la méthode `select_by` si la sélection est réduite à un résultat unique.

Les résultats sont sotckés sous la clef `'results'` sous forme de `Dataset`.

La plupart des résultats sont donnés par groupes d'énergie. Les intervalles (`bins` dans le `Dataset`) correspondent à l'index des groupes.

Certaines quantités ont différents axes :

- $k_{eff}$ et $k_{inf}$ : grandeurs scalaires, pas d'axes
- diffusion : le nombre d'anisotropies sur lequel le calcul est fait est pris en compte, s'il est différent de 1 les axes seront (anisotropies, groupes)
- flux surfacique : les axes sont (groupes, surfaces), surfaces contenant l'index des surfaces
- courant : les axes sont (groupes, surfaces, direction), surfaces contenant l'index des surfaces et direction (*incoming* et *leaving*)

``` python
xe135_abs = sb_q.select_by(isotope='Xe135', result_name='absorption')
print(list(xe135_abs.keys()))
xe135_abs = xe135_abs['results']
print(xe135_abs.shape)  # 26 groupes
print(xe135_abs.what)
xe135_abs.name = '$^{135}$Xe'
```

``` python
macro_diff = sb_q.select_by(isotope='macro', result_name='diffusion')
print(macro_diff['results'].what)
print(macro_diff['results'].shape)
print(list(macro_diff['results'].bins.keys()))
```

``` python
surf_flux = sb_totout.select_by(result_name='surfflux')
print(surf_flux['results'].what)
print(surf_flux['results'].shape)
print(list(surf_flux['results'].bins.keys()))
```

``` python
current = sb_totout.select_by(result_name='current')['results']
print(current.what)
print(current.shape)
print(current.bins)
```

## Comparaison de résultats

Les tests disponibles dans *valjean* peuvent tout à fait être appliqués aux résultats issus du `Reader` ou du `Picker`.

Ici `TestApproxEqual` : les résultats sont des `float` sans erreur associée (mise à `nan` par défaut).

### Import du test et des représentations (voir les autres notebooks)

``` python
from valjean.gavroche.test import TestApproxEqual
from valjean.javert.representation import FullRepresenter
from valjean.javert.rst import RstFormatter
from valjean.javert.mpl import MplPlot
from valjean.javert.verbosity import Verbosity

frepr = FullRepresenter()
rstformat = RstFormatter()
```

### Comparaison des aborptions pour différents isotopes

``` python
sm149_abs = sb_q.select_by(isotope='Sm149', result_name='absorption')['results']
sm149_abs.name = '$^{149}$Sm'
i135_abs = sb_q.select_by(isotope='I135', result_name='absorption')['results']
i135_abs.name = '$^{135}$I'
```

``` python
taeq_res = TestApproxEqual(xe135_abs, sm149_abs, i135_abs, name='TestApproxEqual',
                           description='Test le TestApproxEqual sur les absorptions', rtol=1e-2).evaluate()
print(bool(taeq_res))  # expected: False
```

Ajout d'une fonction pour passer en échelle logarithmique l'axe des ordonnées vu les variations du spectre.

``` python
from valjean.javert import plot_repr as pltr
def log_post(templates, tres):
    pltr.post_treatment(templates, tres)
    for templ in templates:
        templ.subplots[0].attributes.logy = True
    return templates
```

``` python
logaeqrepr = FullRepresenter(post=log_post)(taeq_res, verbosity=Verbosity.FULL_DETAILS)
aeqrst = rstformat.template(logaeqrepr[1])
print(aeqrst)
```

``` python
mpl = MplPlot(logaeqrepr[0]).draw()
```

### Comparaison de la diffusion pour les différentes valeurs d'anisotropie

La méthode `squeeze` permet de supprimer les dimensions triviales d'un `Dataset` (on ne comparera que des `Datasets` à une dimension ici).

``` python
macro_diff_aniso = [macro_diff['results'][:1, :].squeeze()]
macro_diff_aniso[-1].name = 'anisotropie = 0'
macro_diff_aniso[-1].what = 'diffusion (macro)'
print(macro_diff_aniso[-1])
```

``` python
# anisotropie d'ordre 1
macro_diff_aniso.append(macro_diff['results'][1:2, :].squeeze())
macro_diff_aniso[-1].name = 'anisotropie = 1'
macro_diff_aniso[-1].what = 'diffusion (macro)'
# anisotropie d'ordre 2
macro_diff_aniso.append(macro_diff['results'][2:3, :].squeeze())
macro_diff_aniso[-1].name = 'anisotropie = 2'
macro_diff_aniso[-1].what = 'diffusion (macro)'
# anisotropie d'ordre 3
macro_diff_aniso.append(macro_diff['results'][3:, :].squeeze())
macro_diff_aniso[-1].name = 'anisotropie = 3'
macro_diff_aniso[-1].what = 'diffusion (macro)'
```

``` python
taeq_res = TestApproxEqual(*macro_diff_aniso, name='TestApproxEqual',
                           description=("Test le TestApproxEqual sur la diffusion macroscopique aux différents "
                                        "ordres d'anisotropie"),
                           rtol=1e-2).evaluate()
print(bool(taeq_res))  # expected: False
```

``` python
aeqrepr = frepr(taeq_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
aeqrst = rstformat.template(aeqrepr[1])
print(aeqrst)
```

``` python
mpl = MplPlot(aeqrepr[0]).draw()
```

### Comparaison des courants entrants et sortants

Il s'agit d'une comparaison d'arrays en 2 dimensions, mais cela ne change pas les tests.

Pour une question de lisibilité du graphique on se restreint à 20 surfaces.

``` python
current_in = current[:, :20, :1].squeeze()
current_out = current[:, :20, 1:].squeeze()
```

``` python
caeq_res = TestApproxEqual(
    current_in, current_out, name='TestApproxEqual',
    description=("Test le TestApproxEqual sur la diffusion macroscopique aux différents "
                 "ordres d'anisotropie"),
    rtol=1e-2).evaluate()
print(bool(caeq_res))  # expected: False
```

``` python
caeqrepr = frepr(caeq_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
caeqrst = rstformat.template(caeqrepr[1])
# print(caeqrst)
```

``` python
mpl = MplPlot(caeqrepr[0]).draw()
```

``` python
ratio = current_out / current_in
```

``` python
import matplotlib.pyplot as plt
import numpy as np

fig, splts = plt.subplots()
bbins = np.broadcast_arrays(ratio.bins['groups'].reshape([26, 1]),
                            ratio.bins['surfaces'].reshape([20]))
h2d = splts.hist2d(
    bbins[0].flatten(), bbins[1].flatten(),
    bins=[np.append(ratio.bins['groups']-0.5, [ratio.bins['groups'][-1]+0.5]),
          np.append(ratio.bins['surfaces']-0.5, [ratio.bins['surfaces'][-1]+0.5])],
    weights=ratio.value.flatten())
cbar = fig.colorbar(h2d[3], ax=splts)
splts.set_xlabel('groups')
splts.set_ylabel('surfaces')
```
