<!-- source: examples/notebooks/ap3_reader/ap3_picker.ipynb -->

# Lecture des fichiers *rates* d'Apollo3 grâce au `Picker`

La lecture des fichiers *rates* d'Apollo3 (réseau) est possible dans *valjean*, ainsi que les différents autres formats HDF5.

Deux modes de lecture sont possibles :

- lecture de tout le fichier HDF5 et stockage des résultats dans un `Browser`, récupération des résultats sous forme de `Dataset` grâce au `Browser` -\> utilisation du `Reader`
- lecture d'un résultat ou de plusieurs résultats donnés à partir du HDF5 pour une utilisation directe sous forme de `Dataset` -\> `Picker`

La seconde méthode est bien plus rapide car elle ne nécessite pas de charger l'intégralité du fichier et bénéficie des accès de lecture du HDF5. Cet exemple se concentre sur cette seconde méthode.

## Le `Picker` : résumé

À utiliser notamment si vous connaissez les métadonnées du résultat qui vous intéresse : `'zone'`, `'output'`, `'result_name'`, etc.

``` python
from valjean.eponine.apollo3.hdf5_picker import Picker
```

``` python
ap3p = Picker("Mosteller.hdf")
```

La méthode à utiliser pour récupérer les résultats est `pick_standard_value` :

``` python
keff = ap3p.pick_standard_value(output='output_1', zone='totaloutput', result_name='KEFF')
```

**Attention : les strings correspondant aux différents arguments (`'output'`, `'result_name'`, etc) sont celles stockées dans le fichier, en capitales pour les résultats la plupart du temps.**

Les résultats correspondants à des taux microscopiques (par isotopes) sont souvent en minuscules avec la première lettre en majuscules.

## Inspection du fichier HDF5

Il est tout de même possible d'inspecter le fichier (mais cela peut prendre un peu de temps).

``` python
print(ap3p.zones(output='output_0'))
print(ap3p.zones(output='output_2'))
```

Illustration pour l'output `'output_0'`.

``` python
print(f"isotopes dans la zone 3: {ap3p.isotopes(output='output_0', zone='3')}")
print(f"isotopes dans la zone 1: {ap3p.isotopes(output='output_0', zone='1')}")
```

Recherche des résultats macroscopiques (pas d'isotope de mentionné) :

``` python
print(f"résultats dans la zone 1: {ap3p.results(output='output_0', zone='1')}")
print(f"résultats pour totaloutput: {ap3p.results(output='output_0', zone='totaloutput')}")
```

Recherche des résultats macroscopiques et microscopiques (isotope requis) :

``` python
print(f'resultats sans isotopes: {ap3p.results(output="output_0", zone="3")}')
print(f'resultats pour B10: {ap3p.results(output="output_0", zone="3", isotope="B10")}')
```

## Sélection des résultats

Récupération d'un résultat sous forme de `Dataset` : utilisation de la méthode `pick_standard_value` pour les fichiers *rates* standards

### Exemple sur les $k_{eff}$

``` python
keff_o0 = ap3p.pick_standard_value(output='output_0', zone='totaloutput', result_name='KEFF')
print(keff_o0)
```

``` python
keff_o1 = ap3p.pick_standard_value(output='output_1', zone='totaloutput', result_name='KEFF')
print(keff_o1)
```

``` python
print(f"Difference between keffs (output_0, output1) = "
      f"{(1/keff_o0.value - 1/keff_o1.value)*1e5:.0f} pcm")
```

### Exemple sur les flux (arrays)

``` python
flux = ap3p.pick_standard_value(output='output_0', zone='1', result_name='FLUX')
print(flux)
print(flux.value)
flux.name = 'output 0'
```

``` python
absB10 = ap3p.pick_standard_value(output='output_0', zone='3', result_name='Absorption', isotope='B10')
print(absB10)
print(absB10.value)
```

## Comparaison de résultats

Les tests disponibles dans *valjean* peuvent tout à fait être appliqués aux résultats issus du `Reader` ou du `Picker`.

Ici `TestApproxEqual` : les résultats sont des `float` sans erreur associée (mise à `nan` par défaut).

``` python
flux_1 = ap3p.pick_standard_value(output='output_1', zone='1', result_name='FLUX')
flux_1.name = 'output 1'
```

``` python
flux_2 = ap3p.pick_standard_value(output='output_2', zone='1', result_name='FLUX')
flux_2.name = 'output 2'
```

Import du test et des représentations (voir les autres notebooks)

``` python
from valjean.gavroche.test import TestApproxEqual
from valjean.javert.representation import FullRepresenter
from valjean.javert.rst import RstFormatter
from valjean.javert.mpl import MplPlot
from valjean.javert.verbosity import Verbosity

frepr = FullRepresenter()
rstformat = RstFormatter()
```

``` python
taeq_res = TestApproxEqual(flux, flux_1, flux_2, name='TestApproxEqual',
                           description='Test le TestApproxEqual sur les flux', rtol=1e-2).evaluate()
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
