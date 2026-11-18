<!-- source: examples/notebooks/sensitivities/sensitivities_example.ipynb -->

# Parsing des sensibilités

Le jeu de données utilisé ici est [sensitivity_godiva](sensitivity_godiva.d).

Comme dans le cas précédent les résultats sont stockés dans la liste des réponses. Le `Browser` simplifie l'accès à des données grâce à la possibilité de sélection sur les métadonnées.

``` python
from valjean.eponine.tripoli4.parse import Parser

t4vv_sg = 'sensitivity_godiva.d.res.ceav5'
# scan du jeu de données
t4p = Parser(t4vv_sg)
# parsing du dernier batch
t4pres = t4p.parse_from_index()
# clefs disponibles dans le dictionnaire de résultats
list(t4pres.res.keys())
```

``` python
lresp = t4pres.res['list_responses']
len(lresp)
```

Le nombre peut être plus grand qu'attendu par la lecture du jeu de données car chaque résultat consistue une entrée dans le dictionnaire, soit chaque résultat dont la valeur d'une métadonnée varie.

``` python
for i, resp in enumerate(lresp):
    print('Response {0}: clefs = {1}'.format(i, sorted(resp.keys())))
```

On construit donc un `Browser` pour nous faciliter la tâche.

``` python
t4b = t4pres.to_browser()
print(t4b)
```

``` python
for k in list(t4b.keys()):
    print("{0} -> {1}".format(k, list(t4b.available_values(k))))
```

## Exemples de sélection

Pour la « démo », mais cela reflète probablement une future démarche de développement de test, on va récupérer des `Browser` et non les réponses directement. Cela permet notamment de sélectionner la bonne réponse pas à pas.

### Sélection 1 : réponses correspondant à l'U238

``` python
b_u238 = t4b.filter_by(sensitivity_nucleus='U238')
["{0} -> {1}".format(k, list(b_u238.available_values(k))) for k in list(b_u238.keys())]
```

### Sélection 2 : réponses correspondant à des sections efficaces

``` python
b_cs = t4b.filter_by(sensitivity_type='CROSS SECTION')
["{0} -> {1}".format(k, list(b_cs.available_values(k))) for k in list(b_cs.keys())]
```

### Sélection 3 : réponses correspondant au code de section efficace 52 ($n \rightarrow \gamma$ absorption)

``` python
b_s42 = t4b.filter_by(sensitivity_reaction='SECTION CODE 42')
```

``` python
b_s52 = t4b.filter_by(sensitivity_reaction='SECTION CODE 52')
["{0} -> {1}".format(k, list(b_s52.available_values(k))) for k in list(b_s52.keys())]
```

Dans ce cas on peut récupérer directement la réponse et l'utiliser grâce à la méthode `select_by`. Elle ne fonctionne que s'il n'y a qu'une seule réponse satisfaisant la sélection.

``` python
r_s52 = t4b.select_by(sensitivity_reaction='SECTION CODE 52')
list(r_s52.keys())
```

``` python
list(r_s52['results'].keys())
```

Dans ce cas quatre résultats sont disponibles et disponibles sous forme de `Dataset`.

#### Nombre de batches utilisés

``` python
print('nombre de batches utilisés :', r_s52['results']['used_batches'])
ubres_s52 = r_s52['results']['used_batches']
print(ubres_s52)
```

*Remarque* : il n'y a pas d'erreur sur le nombre de batches utilisés, le choix a été fait de l'initialiser à `np.nan`, ce qui ne bloque pas les tests. Il en est de même pour tous les résultats non affectés d'une erreur.

#### Spectre

``` python
dssres_s52 = r_s52['results']['score']
```

``` python
dssres_s52.ndim
```

``` python
dssres_s52.shape
```

``` python
dssres_s52.bins
```

Comme pour les spectres ou les maillages les bins des sensibilités sont stockés dans un `OrderedDict`, comme dans le cas d'un spectre habituel. Seules les coordonnées sont changées, précisées par les bins.

``` python
dssres_s52.what
```

Le `what` par défaut est `'sensitivity'`.

``` python
dssres_s52.name='section 52'
print(dssres_s52)
```

Comme dans l'exemple précédent, il est possible de réduire le spectre aux seuls bins utilisés.

``` python
print(dssres_s52.squeeze())
```

#### Résultat intégré

``` python
ires_s52 = r_s52['results']['integrated']
ires_s52.name='section 52'
ires_s52.what='sensitivity'
print(ires_s52)
```

Il est également possible ici de réduire les dimensions, ce qui reviendra à ne plus avoir de bins, vu qu'il n'y en a qu'un en énergie :

``` python
print(ires_s52.squeeze())
```

### Sélection 4 : première réponse (0) : les $k_\mathrm{eff}$

Deux types de résultats de $k_\mathrm{eff}$ sont disponibles :

- les $k_\mathrm{eff}$ qui apparaissent comme les réponses standard dans le listing de sortie de Tripoli-4, qui comportent normalement trois évaluations : `KSTEP`, `KCOLL` et `KTRACK` ainsi que leurs corrélations et le résultat de leur combinaison, appelés ici $k_\mathrm{eff}$ "génériques"
- les $k_\mathrm{eff}$ apparaissant le plus souvent en toute fin de listing, donc le *discard* est calculé automatiquement, de manière à en donner la meilleure estimation, appelés ici $k_\mathrm{eff}$ "automatiques"

#### $k_\mathrm{eff}$ "génériques"

``` python
keffs = t4b.filter_by(response_index=0)
print(keffs.content)
```

D'autres sélections sont également possibles, sans nécessité de connaître l'index de la réponse :

``` python
keffs = t4b.filter_by(response_function='KEFFS')
print(len(keffs))
print(keffs.content)
```

Il y a 7 $k_\mathrm{eff}$ disponibles comme attendu (les 3 valeurs, les 3 combinaisons deux à deux et les corrélations associées et la combinaison des trois. Il est également possible de construire des datasets à partir de chacun de ces $k_\mathrm{eff}$. Il faut cependant isoler les résultats un par un :

``` python
kstep = t4b.select_by(response_function='KEFFS', keff_estimator='KSTEP')
print(list(kstep['results'].keys()))
ds_kstep = kstep['results']['keff']
ds_kstep.name='kstep'
print(ds_kstep)
```

``` python
kstep_kcoll = t4b.select_by(response_function='KEFFS', keff_estimator='KSTEP-KCOLL')
print(list(kstep_kcoll['results'].keys()))
print(kstep_kcoll['results']['keff'])
```

Dans ce cas la corrélation est atteignable par :

``` python
print(kstep_kcoll['results']['correlation_keff'])
```

Remarque : elle n'a pas d'erreur.

#### $k_\mathrm{eff}$ "automatiques"

``` python
keffs = t4b.filter_by(response_type='keff_auto')
print(len(keffs))
print(keffs)
```

Dans ce cas il y a un autre estimateur en plus : MACRO KCOLL. À noter également la présence du nombre de batches *discarded* puisqu'il est calculé par Tripoli-4.

### Sélection 5 : boucle sur toutes les réponses

Il est toujours possible de faire une boucle sur toutes les réponses, dans l'ordre dans lequel elles apparaissent dans le jeu de données (par exemple pour les besoins de la non-régression).

#### Premier choix : boucle directe sur la liste

``` python
for resp in lresp:
    print("Response function: {0}, response type: {1}, r_index = {2}, s_index = {3}\n results keys: {4}"
          .format(resp['response_function'], resp['response_type'], resp['response_index'],
                  resp.get('sensitivity_index', None), list(resp['results'].keys())))
```

Dans ce cas les réponses sont déjà « aplaties »... mais le gros avantage est que les métadonnées sont accessibles pour chaque réponse (même les communes), il n'y a donc pas de perte d'information.

#### Deuxième choix : boucle grâce au `Browser` (boucle sur le `'response_index'`)

``` python
val_rindex = list(t4b.available_values('response_index'))
val_rindex
```

``` python
for ind in val_rindex:
    b_ind = t4b.filter_by(response_index=ind)
    print("Nombre de 'scores' par réponse =", b_ind)
    for resp in b_ind.content:
        print("Response function = {0}, sensitivity type = {1}, sensitivity index = {2}"
              .format(resp['response_function'], resp.get('sensitivity_type', None),
                      resp.get('sensitivity_index', None)))
```

Dans le cas présent on obtient tous les résultats formatés de la même manière dans le listing de sortie de Tripoli-4, les $k_\mathrm{eff}$ "automatiques" n'y sont donc pas. Ils peuvent cependant être également obtenus dans la boucle, à condition de boucler sur `'index'` au lieu de `'response_index'` :

``` python
val_index = list(t4b.available_values('index'))
print('index :', val_index)
for ind in val_index:
    b_ind = t4b.filter_by(index=ind)
    print("Nombre de 'scores' par réponse =", b_ind)
    for resp in b_ind.content:
        print("Response function = {0}, response type = {1}, sensitivity type = {2}, sensitivity index = {3}"
              .format(resp.get('response_function', None), resp['response_type'],
                      resp.get('sensitivity_type', None), resp.get('sensitivity_index', None)))
        if resp.get('response_function') is None:
            print(resp)
```

## Exemples de comparaison de $k_\mathrm{eff}$

On va faire différents tests pour comparer les valeurs de $k_\mathrm{eff}$ :

- `TestEqual` qui vérifie que les datasets sont égaux (ce test est plutôt prévu pour des valeurs entières comme les nombres de batches)
- `TestApproxEqual` qui vérifie que les datasets sont approximativement égaux (pertinent pour les `float` pour lesquels on n'a pas d'erreur associée, les corrélations de $k_\mathrm{eff}$ par exemple
- `TestStudent` dans le cas où l'on veut prendre en compte les erreurs sur les valeurs

Pour tous ces tests il faut définir une référence, qui sera en fait le premier dataset donné.

Pour les exemples ci-dessous on choisit les $k_\mathrm{eff}$ des réponses (`response_function='KEFFS'`). On prendra comme référence le `KSTEP` pour plus de facilités car c'est le premier résultat donné.

``` python
sb = t4b.filter_by(response_function='KEFFS')
print('estimators values:', list(sb.available_values('keff_estimator')))
dsets = []
for keff in sb.content:
    dsets.append(keff['results']['keff'])
    dsets[-1].name=keff['keff_estimator']
print(dsets)
```

On importe les tests et la possibilité d'en faire des représentations.

``` python
from valjean.gavroche.test import TestEqual, TestApproxEqual
from valjean.gavroche.stat_tests.student import TestStudent
from valjean.javert.representation import FullRepresenter
from valjean.javert.rst import RstFormatter
from valjean.javert.mpl import MplPlot
from valjean.javert.verbosity import Verbosity

frepr = FullRepresenter()
rstformat = RstFormatter()
```

``` python
teq_res = TestEqual(*dsets, name='TestEqual', description='Test le TestEqual sur les keff').evaluate()
print(bool(teq_res))  # expected: False
```

``` python
eqrepr = frepr(teq_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
print(eqrepr, len(eqrepr))
eqrst = rstformat.template(eqrepr[0])
print(eqrst)
```

``` python
tstud_res = TestStudent(*dsets, name='TestStudent', description='Test le TestStudent sur les keff').evaluate()
print(bool(tstud_res))
```

``` python
studrepr = frepr(tstud_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
print(len(studrepr), [type(t) for t in studrepr])
studrst = rstformat.template(studrepr[0])
print(studrst)
```

Il est possible d'avoir une représentation de ce test plus lisible en créant deux `Dataset` : l'un contenant tous ces résultats, l'autre, qui servira de référence, le KSTEP autant de fois que d'éléments dans le premier. Dans ce cas la représentation permettra également d'avoir une représentation graphique.

Pour les bins, le plus simple est de donner les noms des estimateurs, actuellement stocké comme `'name'`.

Cette forme permet également de comparer ces mêmes valeurs pour différentes versions de Tripoli-4 par exemple.

``` python
from collections import OrderedDict
import numpy as np
from valjean.eponine.dataset import Dataset
```

``` python
dset_test = Dataset(value=np.array([k.value for k in dsets]),
                    error=np.array([k.error for k in dsets]),
                    bins=OrderedDict([('estimator', np.array([k.name for k in dsets]))]),
                    name='Test', what='keff')
print(dset_test)
```

On fait maintenant le `Dataset` de référence.

    &#10;ATTENTION
&#10;    Pour pouvoir comparer des `Dataset` il faut qu'ils aient les mêmes bins. La référence (qui ne contient que KSTEP) doit donc avoir tous les estimateurs dans les bins (les valeurs étant bien sûr celles du KSTEP).

``` python
dset_ref = Dataset(value=np.array([ds_kstep.value for _ in dsets]),
                   error=np.array([ds_kstep.error for _ in dsets]),
                   bins=OrderedDict([('estimator', np.array([k.name for k in dsets]))]),
                   name='Ref (KSTEP)', what='keff')
print(dset_ref)
```

### Représentation avec le `TestStudent`

``` python
tstudRT_res = TestStudent(dset_ref, dset_test, name='TestStudent', description='Test le TestStudent sur les keff').evaluate()
print(bool(tstudRT_res))
```

``` python
studRTtemp = frepr(tstudRT_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
print(len(studRTtemp), [type(t) for t in studRTtemp])
studRTrst = rstformat.template(studRTtemp[1])
print(studRTrst)
mpl = MplPlot(studRTtemp[0]).draw()
```

### Représentation avec le `TestApproxEqual`

``` python
dscorr = []
for keff in sb.content:
    dscorr.append(keff['results']['correlation_keff'])
    dscorr[-1].name=keff['keff_estimator']
dscorr_test = Dataset(value=np.array([k.value for k in dscorr]),
                      error=np.array([k.error for k in dscorr]),
                      bins=OrderedDict([('estimator', np.array([k.name for k in dscorr]))]),
                      name='Test', what='correlation')
dscorr_kstep = kstep['results']['correlation_keff']
dscorr_kstep.name=kstep['keff_estimator']
dscorr_ref = Dataset(value=np.array([dscorr_kstep.value for _ in dscorr]),
                     error=np.array([dscorr_kstep.error for _ in dscorr]),
                     bins=OrderedDict([('estimator', np.array([k.name for k in dscorr]))]),
                     name='Ref (KSTEP)', what='correlation')
taeqRT_res = TestApproxEqual(
    dscorr_ref, dscorr_test, name='TestApproxEqual',
    description='Test le TestApproxEqual sur les correlations entre estimations de keff').evaluate()
print(bool(taeqRT_res))
aeqRTtemp = frepr(taeqRT_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
print(len(aeqRTtemp), [type(t) for t in aeqRTtemp])
aeqRTrst = rstformat.template(aeqRTtemp[1])
print(aeqRTrst)
mpl = MplPlot(aeqRTtemp[0]).draw()
```

### Représentation avec `TestEqual`

``` python
dsub = []
for keff in sb.content:
    dsub.append(keff['results']['used_batches'])
    dsub[-1].name=keff['keff_estimator']  #, what='used batches'))
dsub_test = Dataset(value=np.array([k.value for k in dsub]),
                    error=np.array([k.error for k in dsub]),
                    bins=OrderedDict([('estimator', np.array([k.name for k in dsub]))]),
                    name='Test', what='used batches')
dsub_kstep = kstep['results']['used_batches']
dsub_kstep.name=kstep['keff_estimator']  # , what='used batches')
dsub_ref = Dataset(value=np.array([dsub_kstep.value for _ in dsub]),
                   error=np.array([dsub_kstep.error for _ in dsub]),
                   bins=OrderedDict([('estimator', np.array([k.name for k in dsub]))]),
                   name='Ref (KSTEP)', what='used batches')
print(dsub)
teqRT_res = TestEqual(
    dsub_ref, dsub_test, name='TestEqual',
    description='Test le TestEqual sur les batches utilisés pour les estimations de keff').evaluate()
print(bool(teqRT_res))
eqRTtemp = frepr(teqRT_res, verbosity=Verbosity.FULL_DETAILS)  # il s'agit d'une liste de templates
print(len(eqRTtemp), [type(t) for t in eqRTtemp])
eqRTrst = rstformat.template(eqRTtemp[1])
print(eqRTrst)
mpl = MplPlot(eqRTtemp[0]).draw()
```

Si on veut comparer les résultats à d'autres obtenus à partir d'une autre version de Tripoli-4 par exemple, on peut faire un dataset unique et le mettre dans un test.
