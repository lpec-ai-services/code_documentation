<!-- source: examples/notebooks/dataset_representation/meshes_with_scatter_plots.ipynb -->

# Représentation de scores sur maillages

Par défaut la représentation des scores sur maillages dans valjean se fait centrée sur la maille. Si le score Tripoli4 a été tourné avec l'option `MESH_INFO` les coordonnées du centre de la maille sont en plus disponibles. Il est alors possible de faire un graphique davantage à l'échelle, même si les axes des mailles ne correspondent pas aux axes par défaut.

Différents exemples sont présentés pour illustrer ces représentations. Elles sont faites grâce à *matplotlib*, hors *valjean*.

## Les imports par défaut

``` python
import numpy as np
import matplotlib.pyplot as plt
from valjean.eponine.tripoli4.parse import Parser
from valjean.eponine.dataset import Dataset
```

## Quelques fonctions

Certaines fonctionnalités ont été encapulées dans des fonctions pour plus de simplicité. Ce sont des exemples.

### Sélection des intervalles

Cette fonction permet de sélectionner les intervalles que l'on veut représenter et permet de *squeezer* le `Dataset` et les coordonnées en même temps (suppresion des dimensions triviales). La sélection se fait sur un dictionnaire dont les clefs correspondent au nom des coordonnées à réduire et dont les valeurs correspondent aux indices des intervalles à sélectionner. Deux cas sont possibles :

- seul le deuxième intervalle est gardé sur l'axe `'u'` : `{'u': 1}`
- les intervalles d'indices 3 à 8 sont gardés sur l'axe `'v'` (qui en a au moins 9) : `{'v': (3, 9)}`

Dans le dernier cas les indices sont donnés à une `slice` ([slice doc](https://docs.python.org/3/library/functions.html#slice)) dans la fonction.

``` python
def select_space_bins(dset, coords, selection):
    """Select slice to be represented and squeeze dataset and coordinates accordingly.
    
    The slice can be done on one value or on a range of values if a tuple is given.
    
    :param Dataset dset: dataset
    :param np.ndarray coords: coordinates (structured array which names are the axis names)
    :param dict selection: selection to be applied, keys correspond to the axis names
    :rtype: Dataset, np.ndarray
    :returns: sliced and squeezed dataset and coordinates
    """
    islices = tuple(slice(None) for _ in range(dset.ndim))
    oslices = list(islices)
    for key, val in selection.items():
        icoord = list(dset.bins.keys()).index(key)
        if isinstance(val, int):
            oslices[icoord] = slice(val, val+1)
        elif isinstance(val, (list, tuple)):
            oslices[icoord] = slice(val[0], val[1])
    oslices = tuple(oslices)
    return dset[oslices].squeeze(), coords[oslices[:3]].squeeze()
```

### Représentation des mailles individuelles

Le choix fait ici est de donner à la maille sa forme "réelle". Pour cela le marqueur utilisé est défini comme un chemin entre les différents vertex donnés ([marker doc](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers) et [marker examples](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_star_poly.html)).

Dans les cas présentés ici le maillage est supposé régulier (une petite vérification est faite, cela suppose en général une précision dégradée sur l'estimation de la distance entre deux points consécutifs, ce qui apparaît dans l'argument `decimals` demandé par la fonction). Le chemin proposé est calculé à partir des 4 premiers points (2 sur chacune des 2 dimensions utilisées). Un parallélogramme est ainsi défini. Le sens de parcours des sommets est le sens direct pour s'assurer d'avoir un quadrilatère convexe.

Les dimensions fournies sont celles qui sont gardées.

``` python
def vertices(coords, decimals, dims=('u', 'v')):
    """Compute the vertices of the elementary cell from regular coordinates.
    
    :param np.ndarray coords: coordinates (structured array which names are axis names)
    :param int decimals: number of decimals to consider to identify unique coordinates values
    :param list, tuple dims: dimension names of the corrdinated considered
    :rtype: list(tuple(float))
    :returns: verticies of the path matching the cell (4 points here)
    """
    uu = np.unique(np.diff(coords[dims[0]]).round(decimals))
    uv = np.unique(np.diff(coords[dims[1]]).round(decimals))
    if len(uu) != len(uv):
        print("Not a rectangle or parallelogram, returning arbitrary triangle")
        print(f'u: {uu}, v: {uv}')
        return [[-1, -1], [1, -1], [1, 1], [-1, -1]]
    if len(uu) > 2:
        print('Not a parallelogram, returning arbitrary triangle')
        print(uu, np.ediff1d(coords[dims[0]]).round(decimals))
        return [[-1, -1], [1, -1], [1, 1], [-1, -1]]
    f4pts = coords[:2, :2]
    meanu = np.mean([np.min(f4pts[dims[0]]), np.max(f4pts[dims[0]])])
    meanv = np.mean([np.min(f4pts[dims[1]]), np.max(f4pts[dims[1]])])
    # vertices: points rotated in direct order
    return [(f4pts[dims[0]][0, 0]-meanu, f4pts[dims[1]][0, 0]-meanv),
            (f4pts[dims[0]][1, 0]-meanu, f4pts[dims[1]][1, 0]-meanv),
            (f4pts[dims[0]][1, 1]-meanu, f4pts[dims[1]][1, 1]-meanv),
            (f4pts[dims[0]][0, 1]-meanu, f4pts[dims[1]][0, 1]-meanv)]
```

## Cas d'une maille cartésienne alignée sur les axes

Lecture du jeu de données

``` python
t4p_bd = Parser("box_dyn.res")
t4b_bd = t4p_bd.parse_from_index().to_browser()
```

Sélection du score (mesh)

``` python
neut_flux = t4b_bd.select_by(score_name="neutron_flux_mesh_score")
print(neut_flux['results']['score_eintegrated'].shape)
nfm = neut_flux['results']['score_eintegrated'].squeeze()
print(nfm)
```

Sélection / accès aux coordonnées associées

``` python
nfc = neut_flux['results']['coordinates']
print(nfc.shape, nfc.dtype.names)
```

Les représentations proposées ici sont en 2 dimensions. Pour représenter complètement le score neuf graphiques sont nécessaires : 3 pour chaque couple de coordonnées. Pour simplifier seul un graphique pour chaque couple de données sera présenté.

``` python
nfm_u0, nfc_u0 = select_space_bins(nfm, nfc, {'u': 0})
nfm_v0, nfc_v0 = select_space_bins(nfm, nfc, {'v': 0})
nfm_w0, nfc_w0 = select_space_bins(nfm, nfc, {'w': 0})
```

``` python
print(nfm_u0)
print(nfc_u0.shape, nfc.dtype.names)
print('coordonnées restantes pour u=0')
print(nfc_u0)
print('coordonnées restantes pour w=0')
print(nfc_w0)
```

Calcul des sommets (vertex) du parallélogramme représentant la maille (ici un rectangle en fait).

``` python
nfv_u0 = vertices(nfc_u0, 3, ['v', 'w'])
nfv_v0 = vertices(nfc_v0, 3, ['u', 'w'])
nfv_w0 = vertices(nfc_w0, 3, ['u', 'v'])
print(nfv_u0)
```

Représentation graphique grâce à *matplotlib*.

Le graphique est représenté 3 fois :

- marqueur correspondant au chemin défini plus haut en grisé transparent pour pouvoir ajuster sa taille (argument `s`), la transparence permettant de mieux visualiser les recouvrements
- marqueur correspondant au chemin défini plus haut avec le contenu attendu (argument `c`=couleur contenant la valeur du `Dataset`)
- marqueur + rouge pour visualiser le centre de la maille

``` python
fig, axs = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'aspect': "equal"}, constrained_layout=True)
axs[0].scatter(nfc_u0['v'].flatten(), nfc_u0['w'].flatten(),
                  c="gray", s=30000, marker=nfv_u0, alpha=0.3)
im0 = axs[0].scatter(nfc_u0['v'].flatten(), nfc_u0['w'].flatten(),
                  c=nfm_u0.value.flatten(), s=28000, marker=nfv_u0)
axs[0].scatter(nfc_u0['v'].flatten(), nfc_u0['w'].flatten(), c="red", marker="+")
axs[0].set(xlabel='v', ylabel='w')
cbar0 = fig.colorbar(im0, ax=axs[0], label='neutron flux')
axs[1].scatter(nfc_v0['u'].flatten(), nfc_v0['w'].flatten(),
                  c="gray", s=30000, marker=nfv_v0, alpha=0.2)
im1 = axs[1].scatter(nfc_v0['u'].flatten(), nfc_v0['w'].flatten(),
                  c=nfm_v0.value.flatten(), s=27000, marker=nfv_v0, alpha=0.9)
axs[1].scatter(nfc_v0['u'].flatten(), nfc_v0['w'].flatten(), c="red", marker="+")
axs[1].set(xlabel='u', ylabel='v')
cbar1 = fig.colorbar(im1, ax=axs[1], label='neutron flux')
axs[2].scatter(nfc_w0['u'].flatten(), nfc_w0['v'].flatten(),
               c="gray", s=24000, marker=nfv_w0, alpha=0.2,)
im2 = axs[2].scatter(nfc_w0['u'].flatten(), nfc_w0['v'].flatten(),
                  c=nfm_w0.value.flatten(), s=20000, marker=nfv_w0)
axs[2].scatter(nfc_w0['u'].flatten(), nfc_w0['v'].flatten(), c="red", marker="+")
axs[2].set(xlabel='u', ylabel='v')
cbar2 = fig.colorbar(im2, ax=axs[2], label='neutron flux')
```

Un des arguments les plus imporants ici est : `subplot_kw={'aspect': "equal"}` sans lui les axes sont optimisés et ne sont plus à l'échelle. L'effet sera plus flagrant plus loin, sur des mailles non rectangulaires.

``` python
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].scatter(nfc_u0['v'].flatten(), nfc_u0['w'].flatten(),
                  c="gray", s=22000, marker=nfv_u0, alpha=0.2)
im0 = axs[0].scatter(nfc_u0['v'].flatten(), nfc_u0['w'].flatten(),
                  c=nfm_u0.value.flatten(), s=20000, marker=nfv_u0)
axs[0].scatter(nfc_u0['v'].flatten(), nfc_u0['w'].flatten(), c="red", marker="+")
axs[0].set(xlabel='v', ylabel='w')
cbar0 = fig.colorbar(im0, ax=axs[0], label='neutron flux')
im1 = axs[1].scatter(nfc_v0['u'].flatten(), nfc_v0['w'].flatten(),
                  c=nfm_v0.value.flatten(), s=21000, marker=nfv_v0, alpha=0.9)
axs[1].scatter(nfc_v0['u'].flatten(), nfc_v0['w'].flatten(), c="red", marker="+")
axs[1].set(xlabel='u', ylabel='v')
cbar1 = fig.colorbar(im1, ax=axs[1], label='neutron flux')
axs[2].scatter(nfc_w0['u'].flatten(), nfc_w0['v'].flatten(),
               c="gray", s=11000, marker=nfv_w0, alpha=0.2,)
im2 = axs[2].scatter(nfc_w0['u'].flatten(), nfc_w0['v'].flatten(),
                  c=nfm_w0.value.flatten(), s=10000, marker=nfv_w0)
axs[2].scatter(nfc_w0['u'].flatten(), nfc_w0['v'].flatten(), c="red", marker="+")
axs[2].set(xlabel='u', ylabel='v')
cbar2 = fig.colorbar(im2, ax=axs[2], label='neutron flux')
```

## Cas d'une maille cartésienne dont les axes ont été tournés

Lecture du jeu de données

``` python
t4p_em = Parser("extended_mesh_cartesian_info.res")
t4b_em = t4p_em.parse_from_index().to_browser()
```

Sélection du score

``` python
phot_flux_m8 = t4b_em.select_by(score_name="mesh8_reg")
pfm8 = phot_flux_m8['results']['score_eintegrated']
cm8 = phot_flux_m8['results']['coordinates']
```

``` python
print(pfm8.shape, cm8.shape)
```

La représentation sera également faite dans le premier intervalle.

``` python
pfm8u0, cm8u0 = select_space_bins(pfm8, cm8, {'u': 0})
pfm8v0, cm8v0 = select_space_bins(pfm8, cm8, {'v': 0})
pfm8w0, cm8w0 = select_space_bins(pfm8, cm8, {'w': 0})
print(pfm8u0.shape, cm8u0.shape)
```

Calcul des sommets des parallélogrammes

``` python
verts_u0 = vertices(cm8u0, 3, ['v', 'w'])
verts_v0 = vertices(cm8v0, 3, ['u', 'w'])
verts_w0 = vertices(cm8w0, 3, ['u', 'v'])
print(verts_u0)
print(verts_v0)
print(verts_w0)
```

Représentation **sans** `aspect='equal'`

``` python
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].scatter(cm8u0['v'].flatten(), cm8u0['w'].flatten(),
                  c=pfm8u0.value.flatten(), s=35000, marker=verts_u0)
axs[0].scatter(cm8u0['v'].flatten(), cm8u0['w'].flatten(), c="red", marker="+")
axs[0].set(xlabel='v', ylabel='w')
axs[1].scatter(cm8v0['u'].flatten(), cm8v0['w'].flatten(),
                  c=pfm8v0.value.flatten(), s=18000, marker=verts_v0)
axs[1].scatter(cm8v0['u'].flatten(), cm8v0['w'].flatten(), c="red", marker="+")
axs[1].set(xlabel='u', ylabel='w')
axs[2].scatter(cm8w0['u'].flatten(), cm8w0['v'].flatten(),
                  c=pfm8w0.value.flatten(), s=30000, marker=verts_w0)
axs[2].scatter(cm8w0['u'].flatten(), cm8w0['v'].flatten(), c="red", marker="+")
axs[2].set(xlabel='u', ylabel='v')
```

Les parallélogrammes se chevauchent, cela ne correspond pas à ce que l'on attend -\> `aspect='equal'`...

``` python
fig, axs = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'aspect': "equal"})
axs[0].scatter(cm8u0['v'].flatten(), cm8u0['w'].flatten(),
                  c="gray", alpha=0.2, s=40000, marker=verts_u0)
axs[0].scatter(cm8u0['v'].flatten(), cm8u0['w'].flatten(),
                  c=pfm8u0.value.flatten(), s=30000, marker=verts_u0)
axs[0].scatter(cm8u0['v'].flatten(), cm8u0['w'].flatten(), c="red", marker="+")
axs[0].set(xlabel='v', ylabel='w')
axs[1].scatter(cm8v0['u'].flatten(), cm8v0['w'].flatten(),
                  c="gray", alpha=0.2, s=13000, marker=verts_v0)
axs[1].scatter(cm8v0['u'].flatten(), cm8v0['w'].flatten(),
                  c=pfm8v0.value.flatten(), s=10000, marker=verts_v0)
axs[1].scatter(cm8v0['u'].flatten(), cm8v0['w'].flatten(), c="red", marker="+")
axs[1].set(xlabel='u', ylabel='w')
axs[2].scatter(cm8w0['u'].flatten(), cm8w0['v'].flatten(),
                  c="gray", alpha=0.2, s=31000, marker=verts_w0)
axs[2].scatter(cm8w0['u'].flatten(), cm8w0['v'].flatten(),
                  c=pfm8w0.value.flatten(), s=25000, marker=verts_w0)
axs[2].scatter(cm8w0['u'].flatten(), cm8w0['v'].flatten(), c="red", marker="+")
axs[2].set(xlabel='u', ylabel='v')
```
