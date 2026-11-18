<!-- source: examples/notebooks/godiva_keff/godiva_keff.ipynb -->

# Godiva : analyse de $k_\mathrm{eff}$

Le jeu de données utilisé est : [heu-met-fast-001-godiva](heu-met-fast-001-godiva.t4).

Les résultats à analyser sont les $k_\mathrm{eff}$ calculés par Tripoli-4.

## Parsing du jeu de données et exploration des résultats

``` python
from valjean.eponine.tripoli4.parse import Parser

# scan du jeu de données
t4p = Parser('heu-met-fast-001-godiva.res')
# parsing du dernier batch (par défaut, index=-1)
t4res = t4p.parse_from_index()
# clefs disponibles dans le dictionnaire de résultats
list(t4res.res.keys())
```

Pour manipuler plus aisément les réponses de Tripoli-4 et en particulier les sélectionner on utilise un objet `Browser`.

``` python
t4b = t4res.to_browser()
print(t4b)
```

Accès aux paramètres globaux du résultat :

``` python
from pprint import pprint
pprint(t4b.globals)
```

Le contenu (soit les réponses) est caractérisé par des mots-clefs - valeurs :

``` python
for k in list(t4b.keys()):
    print("{0} -> {1}".format(k, list(t4b.available_values(k))))
```

La sélection de la réponse se fait grâce aux mots-clefs - valeurs ci-dessus par les méthodes

- `filter_by` → sous-`Browser` correspondant à la sélection
- `select_by` → réponse unique correspondant à la sélection (exception s'il n'y a pas de correspondance ou si plusieurs réponses correspondent)

## Sélection des $k_\mathrm{eff}$

Deux types de résultats de $k_\mathrm{eff}$ sont disponibles :

- les $k_\mathrm{eff}$ qui apparaissent comme les réponses standard dans le listing de sortie de Tripoli-4, qui comportent normalement trois évaluations : `KSTEP`, `KCOLL` et `KTRACK` ainsi que leurs corrélations et le résultat de leur combinaison, appelés ici $k_\mathrm{eff}$ "génériques"
- les $k_\mathrm{eff}$ apparaissant le plus souvent en toute fin de listing, donc le *discard* est calculé automatiquement, de manière à en donner la meilleure estimation, appelés ici $k_\mathrm{eff}$ "automatiques"

### $k_\mathrm{eff}$ "génériques"

``` python
keffs = t4b.filter_by(response_function='KEFFS')
print(len(keffs))
```

Il y a 7 $k_\mathrm{eff}$ disponibles comme attendu (les 3 valeurs, les 3 combinaisons deux à deux et les corrélations associées et la combinaison des trois. Pour en connaître la liste précise et pouvoir les isoler le plus simple est d'utiliser la clef `'keff_estimator'` :

``` python
pprint(list(keffs.available_values('keff_estimator')))
```

La sélection des $k_\mathrm{eff}$ avec les clefs `'response_function'` et `'keff_estimator'` donnant un unique résultat il est possible d'utiliser `select_by` pour le récupérer directement.

``` python
kstep = t4b.select_by(response_function='KEFFS', keff_estimator='KSTEP')
print(list(kstep['results'].keys()))
ds_kstep = kstep['results']['keff']
ds_kstep.name='kstep'  # name is '' by default
print(ds_kstep)
```

``` python
kstep_kcoll = t4b.select_by(response_function='KEFFS', keff_estimator='KSTEP-KCOLL')
print(list(kstep_kcoll['results'].keys()))
print(kstep_kcoll['results']['keff'])
```

Pour obtenir la corrélation :

``` python
print(kstep_kcoll['results']['correlation_keff'])
```

Remarque : elle n'a pas d'erreur.

### $k_\mathrm{eff}$ "automatiques"

``` python
keffs = t4b.filter_by(response_type='keff_auto')
print(len(keffs))
pprint(list(keffs.available_values('keff_estimator')))
```

Dans ce cas il y a un autre estimateur en plus : `'MACRO_KCOLL'`. À noter également la présence du nombre de batches *discarded* puisqu'il est calculé par Tripoli-4.

## Exemples de comparaison de $k_\mathrm{eff}$

Différents tests sont disponibles dans *valjean*. Par exemple :

- `TestEqual` qui vérifie que les datasets sont égaux (ce test est plutôt prévu pour des valeurs entières comme les nombres de batches)
- `TestApproxEqual` qui vérifie que les datasets sont approximativement égaux (pertinent pour les `float` pour lesquels on n'a pas d'erreur associée, les corrélations de $k_\mathrm{eff}$ par exemple)
- `TestStudent` dans le cas où l'on veut prendre en compte les erreurs sur les valeurs

Pour tous ces tests il faut définir une référence, qui sera le premier dataset donné au test.

L'exemple ci-dessous présente la comparaison des $k_\mathrm{eff}$ obtenus grâce à la modélisation simplifiée utilisée ci-dessus à celle du modèle en couches décrit dans [heu-met-fast-001-shell_model](heu-met-fast-001-shell_model.t4).

On utilisera les $k_\mathrm{eff}$ "génériques" en comparant tous les estimateurs un à un.

``` python
sb = t4b.filter_by(response_function='KEFFS')
print('estimators values:', list(sb.available_values('keff_estimator')))
```

Tous les $k_\mathrm{eff}$ sont récupérés et stockés dans une liste. L'estimateur sera utilisé comme `'name'` pour chaque `Dataset`.

``` python
dsets = []
for keff in sb.content:
    dsets.append(keff['results']['keff'])
    dsets[-1].name=keff['keff_estimator']
# print(dsets)
```

Pour rendre le résultat plus lisible un seul `Dataset` va être construit, contenant tous les $k_\mathrm{eff}$ pour une modélisation donnée. Les bins correspondent alors aux noms des estimateurs, actuellement stockés dans la variable `'name'` des `Dataset`.

``` python
from collections import OrderedDict
import numpy as np
from valjean.eponine.dataset import Dataset
```

``` python
dset_simple = Dataset(value=np.array([k.value for k in dsets]),
                      error=np.array([k.error for k in dsets]),
                      bins=OrderedDict([('estimator', np.array([k.name for k in dsets]))]),
                      name='Simple model', what='keff')
```

``` python
print(dset_simple)
```

Un `Dataset` similaire est construit pour la modélisation en couche.

``` python
t4p_shell = Parser('heu-met-fast-001-shell_model.res')
t4b_shell = t4p_shell.parse_from_index().to_browser()
```

``` python
sb_shell = t4b_shell.filter_by(response_function='KEFFS')
ldsets_shell = []
for keff in sb_shell.content:
    ldsets_shell.append(keff['results']['keff'])
    ldsets_shell[-1].name=keff['keff_estimator']
```

``` python
dset_shell = Dataset(value=np.array([k.value for k in ldsets_shell]),
                     error=np.array([k.error for k in ldsets_shell]),
                     bins=OrderedDict([('estimator', np.array([k.name for k in ldsets_shell]))]),
                     name='Shell model', what='keff')
```

On importe les tests et la possibilité d'en faire des représentations

``` python
from valjean.gavroche.stat_tests.student import TestStudent
from valjean.javert.representation import FullRepresenter
from valjean.javert.rst import RstFormatter
from valjean.javert.mpl import MplPlot
from valjean.javert.verbosity import Verbosity

frepr = FullRepresenter()
rstformat = RstFormatter()
```

La comparaison sera faite grâce à un `TestStudent` pour prendre en compte les erreurs statistiques de Tripoli-4.

``` python
tstud_res = TestStudent(dset_simple, dset_shell, name='TestStudent',
                        description='Test le TestStudent sur les keff').evaluate()
print(bool(tstud_res))
```

``` python
stud_temp = frepr(tstud_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
stud_rst = rstformat.template(stud_temp[1])
print(stud_rst)
```

``` python
mpl = MplPlot(stud_temp[0]).draw()
```
