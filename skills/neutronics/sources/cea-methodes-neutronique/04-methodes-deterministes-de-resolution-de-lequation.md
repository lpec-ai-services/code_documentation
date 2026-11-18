# Méthodes déterministes de résolution de l’équation de Boltzmann en situation stationnaire
<!-- source PDF pages 19-46 -->

<!-- page 61 (PDF 19) -->
# Méthodes déterministes de résolution de l’équation de Boltzmann en situation stationnaire

breuses méthodes, développées dans le cadre de la théorie
du transport des neutrons. L’examen de l’ensemble de ces
méthodes fait apparaître différentes stratégies de calcul relevées
par J. J. Duderstadt et W. R. Martin [2] et synthétisées
dans le tableau 10 suivant le degré de complexité du problème
de transport à résoudre :
• Modèles simples analytiques ayant pour finalité l’analyse
d’un aspect particulier du comportement de la population
de neutrons. Par exemple, la théorie du ralentissement permet
de comprendre l’allure du spectre en énergie des neutrons
, ainsi que les particularités du comportement des
neutrons pénétrant dans une résonance ;
B. Davison et J. B. Skypes [1], dans leur ouvrage pionnier
Neutron Transport Theory, paru en 1957, précisent que si les
problèmes soulevés par la théorie du transport des particules
neutres ont été identifiés et en partie résolus avant même la
découverte du neutron, par des astrophysiciens comme
K. Schwarzschild et E. A. Milne, puis plus tard par
S. Chandrasekhar qui étudiait les transferts radiatifs, par un
effet boomerang, les méthodes développées par la suite
autour du transport des neutrons ont bénéficié au traitement
des transferts radiatifs. La variété des situations à étudier en
physique des réacteurs (multiplicité des formes, des matériaux
, des dimensions, les hétérogénéités, les situations stationnaires
et non stationnaires…) est à la source des nom-
Les méthodes de la neutronique
Tableau 10
Types de problèmes de transport des neutrons et stratégies de calcul
A : résolution analytique possible N : résolution numérique
Géométries
Unidimensionnelle
Bidimensionnelle
Tridimensionnelle
Nature du problème
infinie
semi-infinie
finie
x-y et r-z
générale
Énergie
Monocinétique
A
A
A
N
N
N
Multigroupe
A
A, N
N
N
N
N
Continue
A
A, N
N
N
N
N
Direction
Isotrope
A
A
A
N
N
N
Anisotrope
A
A
N
N
N
N
Milieu
Vide
A
A
A
A
A
A
Purement absorbant
A
A
A
A
A
A
Homogène
A
A
A
N
N
N
Hétérogène
N
A
N
N
N
N
Sources
Localisée : point, fil, plane
A
A
A
N
N
N
Fonction de Green
A
A
A
N
N
N
Pulsée ou oscillante
A
A
A
N
N
N
Sans ou avec conditions aux limites
-
A
N
N
N
N
Quelconque
N
N
N
N
N
N
Dépendance en temps
Stationnaire à source fixe
A
A
A
N
N
N
Stationnaire critique
A
A
A
N
N
N
Source pulsée ou oscillante
A
A
A
N
N
N

<!-- page 62 (PDF 20) -->
• approximations qui «altèrent» la forme d’origine de l’équation
du transport. L’équation de la diffusion en est un
exemple ;
• méthodes numériques déterministes – méthode SN,
méthode des caractéristiques, par exemple – ou stochastiques
comme la méthode de Monte-Carlo permettant de
traiter des configurations complexes.
L’approche déterministe* choisie pour résoudre sur ordinateur
l’équation de Boltzmann en régime stationnaire repose
sur une discrétisation de l’espace des phases.Plusieurs types
de discrétisations existent pour une même variable et des
modélisations peuvent être conjointement introduites. Toutes
ces options possibles de discrétisation et de modélisation
associées débouchent sur la mise au point d’autant de
méthodes numériques de résolution de l’équation de
Boltzmann, chacune présentant des avantages et des inconvénients
.
Cette section décrit en premier lieu et de manière succincte,
le passage de l’équation du transport continue à une forme
discrétisée de cette même équation. Ce sont ensuite les
grands principes de quelques-unes des méthodes numériques
déterministes emblématiques de la neutronique, qui
sont successivement présentés.

## La discrétisation de l’espace des phases

La connaissance du flux angulaire = ()□, E, □
→), défini dans la
section précédente, permet d’accéder à d’autres grandeurs
d’intérêt à évaluer.Parmi celles-ci, le flux scalaire ? ()□, /) joue
un rôle fondamental, car c’est à partir de celui-ci que sont calculés
les différents taux de réaction dont la connaissance est
indispensable pour calculer un réacteur nucléaire.
La résolution déterministe de l’équation de Boltzmann stationnaire
a recours à la discrétisation de toutes les variables de
l’espace des phases, à savoir l’espace )□, l’énergie E et la
direction □
→.L’usage est de discrétiser d’abord la variable énergie
et, ensuite, les variables de direction et d’espace.
Le domaine en énergie des neutrons allant de 0 à 20 MeV
est découpé en intervalles conventionnellement appelés
« groupes d’énergie* » ou de manière encore plus concise
groupes* (voir supra, p. 33). Par exemple, le code neutronique
APOLLO résout l’équation du transport à 172 groupes
ou à 281 groupes ou encore à 12 000 groupes selon la spécificité
de la configuration physique étudiée et des modélisations
adoptées pour représenter la variation importante des
sections efficaces neutroniques dans les résonances. Dans
la suite un groupe quelconque du domaine en énergie sera
noté T.
La discrétisation angulaire (variable □
→) comporte généralement
de l’ordre de 100 à 1 000 directions dans le but d’obtenir
une bonne description du flux angulaire. On note □
→
< la nème
direction de la discrétisation angulaire.
Dans un réacteur nucléaire, la taille du système est de l’ordre
du mètre, et la taille des hétérogénéités locales (l’épaisseur
de la gaine du combustible, la longueur caractéristique du gradient
de flux dans le crayon, etc.) est de l’ordre du millimètre.
Il faut, par conséquent, découper l’espace (variable )□) en 103
mailles par dimension, ce qui donne 109 mailles spatiales. On
note 4 une maille quelconque du domaine spatial.
L’application d’une telle discrétisation à l’équation du transport
conduit à remplacer les dérivées par des différences finies,
par exemple, et les intégrales par des sommes discrètes ou
formules de quadrature. Au flux angulaire = ()□, E, □
→) se substituent
les formes discrétisées =4
T(□
→
<), =T
4–1/2(□
→
<) et
=T
4+1/2(□
→
<) qui représentent le flux angulaire des neutrons
dans le groupe d’énergie T, au milieu de l’intervalle 4 et aux
bornes notées (4 – 1/2) et (4 + 1/2) de cet intervalle et dans la
direction □
→
<. En raison du caractère linéaire de l’équation du
transport, la discrétisation du flux angulaire conduit à l’obtention
d’un système d’équations linéaires dont les =4
T(□
→
<),
=T
4–1/2(□
→
<) et =T
4+1/2(□
→
<) sont les inconnues à déterminer.Pour
pouvoir effectivement résoudre ce système, il convient de disposer
d’autant d’équations que d’inconnues ; à cette fin, on y
adjoint, d’une part, des conditions aux limites (les valeurs du
flux angulaires aux frontières du cœur du réacteur, par
exemple), et, d’autre part, des relations modélisant la variation
spatiale du flux entre le milieu des intervalles en espace
et leurs extrémités respectives. Permettant une écriture compacte
, le formalisme matriciel est souvent utilisé pour écrire
le système d’équations à résoudre.
En reprenant pour les différentes discrétisations les ordres de
grandeur les plus élevés qui ont été mentionnés plus haut,
on aboutit à 109 × 103 × 104 = 1016 volumes élémentaires de
l’espace des phases. Par conséquent, on est amené à
résoudre, à chaque pas de temps, des systèmes linéaires à
1017 degrés de liberté !
Historiquement, on comprend pourquoi les modèles analytiques
ou semi-analytiques ont initialement dominé la physique
des réacteurs nucléaires, permettant ainsi de réduire drastiquement
ce nombre de degrés de liberté, tout en étant efficace
. Progressivement, certains de ces modèles ont été associés
à des techniques numériques de plus en plus
sophistiquées que la disponibilité de calculateurs électroniques
, puis d’ordinateurs, a fait émerger.
La figure 21, ci-après, indique quelques-unes des principales
méthodes de résolution de l’équation du transport utilisées en
neutronique :

<!-- page 63 (PDF 21) -->
Il a été indiqué plus haut que la résolution de l’équation du
transport par des méthodes numériques fait intervenir des formules
de quadrature en remplacement des intégrales continues
. Il s’agit d’une approximation numérique entachée d’une
certaine erreur qui dépend de la finesse de la discrétisation des
domaines respectifs de variation des variables concernées.
En considérant, à titre d’illustration, une quadrature trapézoïdale
, en désignant par u la dimension du problème traité (par
exemple, les trois dimensions de l’espace) et par < le nombre
total de nœuds de la discrétisation, on montre que l’erreur
commise est proportionnelle à :
Cette expression représente le taux de convergence de la
quadrature choisie en fonction de la finesse de la discrétisation
. On constate donc que l’obtention d’une convergence cible
(valeur imposée de l’erreur) est d’autant plus coûteuse en
temps de calcul que la dimension u du problème à résoudre
est élevée.
Le nombre minimal d’inconnues associées au calcul de cœur d’un réacteur nucléaire de puissance
La discrétisation imposée par la résolution numérique de l’équation
de Boltzmann conduit aux ordres de grandeurs minimaux
suivants pour un REP de 900 MWe :
• Nombre d’assemblages : 150 de 4 m de hauteur ;
• nombre de crayons/cellules (combustible, gaine, zone modératrice
) par assemblage : 17 x 17 = 289 ;
• nombre total de cellules : 150 x 289 = 43 350 ;
• nombre de régions concentriques dans la zone combustible
: 3 ;
• nombre de régions par cellule : 3 + 2 = 5
• nombre de régions axiales : 40. La longueur d’un crayon est
de 4 m, le gradient axial du flux étant a priori plus petit que son
gradient radial, nous avons pris une hauteur de région de
10 cm ;
• nombre de régions par cellule : 5 x 40 = 200 ;
• nombre de cellule dans tout le cœur : 8.6 106 ;
• nombre de groupes d’énergie : 100 ;
• nombre total de valeurs du flux scalaire (inconnues) sur tout
le cœur : 8,6 106 x 100 = 8,6 108.
Si le flux scalaire est construit à partir du flux angulaire (cas de
la méthode SN par exemple) ce dernier doit être également calculé
. Environ 250 directions angulaires doivent donc encore
être définies conduisant à un nombre d’inconnues – valeurs
recherchées du flux angulaire – de l’ordre de :
8,6 108 x 250 ~ 2 1011
La résolution du système d’équations linéaires correspondant
doit se faire par des itérations sur la source de fission, sur les
groupes d’énergie thermique et fait appel à des techniques d’accélération
.
Les besoins en mémoire ordinateur associés à une telle résolution
sont estimés à quelques Gigaoctets.
Fig. 21. Classification des différentes méthodes numériques de résolution de l’équation du transport des neutrons (voir aussi Y. AZMY,
International School in Nuclear Engineering, Saclay, 2010).
Stochastiques
Déterministes : discrétisation
Espace
Angle / espace
Formalisme
de la diffusion
Probabilité de
collision 1D, 2D
Caractéristiques
1D, 2D, 3D
Différences finies
1D, 2D, 3D
Nodal 1D, 2D, 3D
Éléments finis
1D, 2D, 3D
Forme intégro-différentielle
PN, SPN
SN
Espace
Énergie : multigroupe
un à quelques milliers
Monte-Carlo
Forme intégrale
Énergie et transfert
angle / énergie
continus
3D
Énergie et transfert
angle / énergie
multigroupes
3D
Forme intégrale
Angle
Méthodes numériques de résolution de l’équation du transport

<!-- page 64 (PDF 22) -->
Libre parcours moyen et discrétisations en espace et en énergie
Le libre parcours moyen d’un neutron dans la matière est la distance
moyenne qu’il parcourt avant d’interagir. Celle-ci dépend
de la densité de noyaux-cibles N()□), et de la section efficace
microscopique d’interaction σ (/):
Le libre parcours moyen est l’inverse de la section efficace
macroscopique totale et dépend donc, en un point donné, de
l’énergie du neutron. On peut définir autant de libres parcours
moyens que de types d’interactions : dans la définition précédente
, on substitue alors à la section efficace microscopique
(resp. macroscopique) totale, la section efficace microscopique
(resp. macroscopique) partielle considérée.
Quelques ordres de grandeur : dans le dioxyde d’uranium UO2
enrichi à 5 %, pour des neutrons lents de quelques centièmes
d’eV, le libre parcours moyen de fission est de l’ordre du cm (le
diamètre d’un crayon combustible), et le libre parcours moyen
de capture est d’une vingtaine de cm (la dimension transversale
d’un assemblage). Cependant, la section efficace des premières
résonances de capture de l’uranium 238 avoisine les
10 000 barns, ce qui correspond à un libre parcours moyen
d’une cinquantaine de micromètres !
Pour faire un calcul neutronique correct, la discrétisation spatiale
du système neutronique à étudier doit être de l’ordre de grandeur
du libre parcours moyen.
À titre de comparaison, la convergence de la méthode stochastique
Monte-Carlo est contrôlée par une erreur statistique
variant comme 1/√–< où < représente cette fois-ci le nombre
d’histoires de neutrons simulées dans le système physique
étudié. Cette expression montre que le comportement de l’erreur
statistique est indépendante de la dimension u du problème
considéré.
La comparaison du comportement de la convergence des
deux approches déterministe et stochastique explique pourquoi
la méthode de Monte-Carlo devient attractive, lorsqu’augmente
la dimension du problème à résoudre.

## La discrétisation en énergie

La résolution de l’équation du transport est rendue particulièrement
complexe par la variation en énergie de certaines données
, comme les sections efficaces neutroniques des noyaux
présents dans un réacteur.
On rappelle que la section efficace microscopique d’un noyau
caractérise la probabilité qu’a un neutron d’interagir avec ce
noyau. Cette probabilité peut devenir très grande, lorsque
l’énergie du neutron incident est telle que l’énergie conférée au
noyau composé est proche de l’énergie de l’un de ses niveaux
d’excitation. Cela se traduit par une brusque remontée de la
section efficace d’interaction entre le neutron et le noyau, au
voisinage de ces énergies. Pour ces énergies, le noyau présente
des résonances ; il est dit «résonnant*» (voir fig. 22).
L’équation du transport peut être résolue, soit de façon ponctuelle
(équation de Boltzmann ponctuelle), soit de façon multigroupe
. Dans la première approche, la variation « exacte » en
énergie des données est traitée et la répartition ponctuelle des
neutrons en fonction de l’énergie est calculée. Dans la
seconde approche, le domaine en énergie est discrétisé en
un certain nombre de groupes d’énergie, et seule une répartition
moyenne des neutrons à l’intérieur de chaque groupe
est évaluée. Conventionnellement, ici, le premier groupe est
-6 10
-5 10
-4 10
-3 10
-2 10
-1 10
0 10
1 10
2 10
3 10
4 10
5 10
6 10
7 10
8 10
1 000
10 000
Section efficace (barn)
Section efficace totale
Énergie (eV)
Uranium 238 – JEFF-3.1.2 -300 K
Fig. 22. Section efficace microscopique totale de l’uranium 238.
celui avec l’énergie maximale, et le dernier celui avec l’énergie
minimale, car les neutrons issus de la fission naissent
majoritairement à haute énergie (~ 2 MeV) et se ralentissent
jusqu’aux énergies thermiques (< ~ 1eV).On adopte, en général
, un découpage ayant en nombre « raisonnable » de
groupes, c’est-à-dire de l’ordre de quelques centaines à
quelques milliers. Ce nombre de groupes est à comparer au
nombre de points utilisés pour représenter la variation ponctuelle
en énergie des sections efficaces dans les calculs
Monte-Carlo de référence (plusieurs dizaines, voire plusieurs
centaines de milliers de points).
On appelle flux angulaire multigroupe 'T()□, □
→) l’intégrale
du flux angulaire ponctuel ' ()□, /, □
→) dans le groupe, c’està
-dire :
De même, on appelle flux scalaire multigroupe 'T()□) l’intégrale
du flux scalaire ponctuel ' ()□, /) dans le groupe, c’està
-dire :

<!-- page 65 (PDF 23) -->
Pour obtenir les équations donnant les flux multigroupes, on
intègre l’équation de Boltzmann sur chacun des groupes. Ces
équations sont appelées « équations multigroupes ».
À titre d’exemple, dans le cas d’un problème stationnaire avec
source externe, on obtient les équations multigroupes suivantes
pour le flux angulaire :
(1)
Ces équations ne contiendraient pas d’approximation si on définissait
les sections efficaces multigroupes σC
T et les sections
efficaces multigroupes de transfert* σP,C(T□→T, □
→□→□
→)
comme des moyennes pondérées par le flux angulaire ponctuel
en énergie ψ ()□, E, □
→), ce qui impliquerait une dépendance
en espace et en angle de ces sections efficaces multigroupes
. En pratique, pour s’affranchir de la dépendance
angulaire, ces sections efficaces sont pondérées par le flux
scalaire ? ()□, E), ce qui conduit à des sections efficaces multigroupes
ne dépendant que de l’espace. Par exemple, la section
efficace multigroupe totale est définie par :
(2)
Malgré cette simplification, l’obtention des données nucléaires
multigroupes reste un des problèmes les plus délicats de la
neutronique, qui requiert encore aujourd’hui des modélisations
complexes connues sous le terme de « formalisme d’autoprotection
* ». À titre d’illustration, nous décrivons dans le paragraphe
suivant le formalisme d’autoprotection utilisé dans le
code APOLLO2.

### Le formalisme d’autoprotection Définition des sections efficaces multigroupes

Les données de l’équation multigroupe sont les sections efficaces
multigroupes. Ces sections sont définies de façon que,
pour chaque groupe T, le taux de réaction multigroupe (produit
de la section efficace multigroupe par le flux scalaire multigroupe
, solution de l’équation multigroupe de Boltzmann) soit
égal à la valeur intégrée sur le groupe T du taux de réaction
ponctuel (produit de la section efficace ponctuelle par le flux
scalaire solution de l’équation ponctuelle de Boltzmann). On
cherche donc à conserver, dans chaque groupe T, le nombre
de réactions observées entre un neutron et un noyau, par
unité de temps et de volume.
Par commodité, les équations de ce paragraphe sont écrites
en fonction de la variable « léthargie* » et non en fonction de
la variable « énergie ».
La section efficace multigroupe dans le groupe T, pour la réaction
nucléaire de type q induite par un neutron, σ
T
q, est donc
obtenue en écrivant la préservation des taux de réaction :
(3)
Dans l’équation (3), ?()□,) représente le flux scalaire au point
)□ et à la léthargie u, ?T()□) le flux scalaire multigroupe au point
)□, dans le groupe T.
Les taux de réaction sont des grandeurs qui dépendent de
l’espace, par l’intermédiaire du flux (sauf dans le cas d’un
milieu homogène infini). Il en est donc de même pour les sections
efficaces multigroupes σ
T
q()□).
En toute rigueur, il n’est donc pas possible de définir une fois
pour toutes les sections efficaces multigroupes des noyaux et
de créer des bibliothèques de sections efficaces multigroupes
indépendantes de la géométrie.
L’équation (3) montre toute la complexité de l’obtention de ces
sections.
• Les taux de réaction ponctuels à préserver (membre de
droite de l’équation (3)) sont inconnus puisque le flux ponctuel
? ()□, ) est inconnu ;
• Le flux multigroupe ?T ()□) est solution de l’équation multigroupe
de Boltzmann dont on cherche à calculer les données
(sections efficaces multigroupes σ
T
q ()□)) ;
• Les sections efficaces ponctuelles σ() peuvent avoir un
comportement résonnant en fonction de la léthargie.
Il est naturel d’essayer de simplifier l’équation (3) en utilisant,
à la place du flux réel inconnu ? ()□, ), un spectre de pondération
connu (représentatif du réacteur à traiter) qui soit indépendant
de l’espace : ?l(). C’est ce qui est fait lors de la
création des bibliothèques de données multigroupes (voir infra,
p. 33-35).
Nous pouvons donc distinguer deux méthodes d’obtention des
sections efficaces multigroupe :
• Celles utilisant le flux réel ? ()□, ),
- Les sections efficaces multigroupes sont appelées « sections
efficaces multigroupes autoprotégées* ».
- Elles sont données par l’équation (3).
- Elles dépendent de l’espace et ne pourront être obtenues
que lorsque le flux réel sera connu.
• Celles utilisant un spectre de pondération connu ?l () :
- Les sections efficaces multigroupes sont appelées sections
efficaces multigroupes « à dilution infinie ». La terminologie
utilisée sera expliquée par la suite ;

<!-- page 66 (PDF 24) -->
- elles sont notées %
T
q,∞et sont données par l’équation (4) ;
- elles sont indépendantes de l’espace et peuvent être calculées
une fois pour toutes, en amont du calcul de transport,
lors de la création des bibliothèques multigroupes.
(4)
Il faut s’interroger sur la pertinence des sections efficaces multigroupe
« à dilution infinie ». En dehors de leur domaine de
résonances, les noyaux ont des sections efficaces qui varient
lentement et de façon régulière avec la léthargie. Dans ce cas,
l’influence du spectre de pondération utilisé pour « moyenner
» leurs sections efficaces est faible et la pondération simplifiée
décrite par l’équation (4) est pertinente.
Pour les noyaux résonnants, dans le domaine des résonances
, cette simplification est généralement inacceptable
(maillage multigroupe grossier).En effet, les sections efficaces
peuvent varier plusieurs fois et de plusieurs décades, à l’intérieur
d’un groupe du maillage multigroupe (fig. 23). Les sections
efficaces multigroupe autoprotégées devront donc être
calculées par l’équation (3) dans la géométrie spécifique du
cas à traiter.

### Le phénomène physique d’autoprotection

Le phénomène physique d’autoprotection peut être décrit de
la façon suivante. Dans un milieu donné, le flux neutronique
se creuse, en fonction de l’énergie, de façon d’autant plus
accentuée que la section efficace macroscopique de ce milieu
est grande. Les taux de réaction ont donc des variations, en
fonction de l’énergie, beaucoup plus lentes que les sections
efficaces et que le flux. C’est cette compensation des effets
au niveau du calcul des taux de réaction qui est désignée par
le terme d’« autoprotection ».
Le calcul des sections efficaces multigroupes, lorsqu’il est
effectué en utilisant le flux réel qui se creuse au niveau des
résonances, prend en compte le phénomène d’autoprotection
et conduit donc à des sections efficaces multigroupes autoprotégées
.
Le phénomène d’autoprotection a un aspect énergétique et
un aspect spatial. En effet, il intervient aux énergies des résonances
* des nucléides et dans les matériaux contenant des
nucléides résonnants.
Pour illustrer l’aspect spatial de l’autoprotection, prenons
l’exemple d’un neutron de 6,67 eV (donc, à l’énergie de la première
résonance de l’U 238). Ce neutron possède, dans le
dioxyde d’uranium, un libre parcours moyen de 80 µm seulement
, ce qui signifie qu’il ne pourra pénétrer profondément à
l’intérieur du crayon combustible d’un réacteur à neutrons thermiques
. La périphérie des crayons sera donc irradiée différemment
du centre. Les calculs de neutronique doivent pouvoir
décrire ce phénomène, ce qui imposera un maillage très
fin en périphérie de crayon, si l’on a recours à un calcul maillé.
L’aspect énergétique du phénomène d’autoprotection est
schématisé sur la figure 23.
Pour l’uranium 238, dans le cas de la résonance à 6,67 eV, la
section efficace de capture varie d’environ quatre décades, le
flux d’un peu moins de trois décades en sens inverse, alors
que le taux de réaction ne varie que d’environ une décade.
-3
-2
-1
Fig. 23. Le phénomène d’autoprotection.
Unités arbitraires
Section efficace de capture
Taux de capture
Flux
Le creusement du flux dépend
du problème traité (nombre
de noyaux, géométrie…)
Énergie (eV)
Uranium 238 – Résonance à 6,67 eV
Enjeux de la modélisation du phénomène
d’autoprotection
La prise en compte du phénomène d’autoprotection dans le
cadre d’un code de transport multigroupe est indispensable.
Prenons l’exemple du calcul d’une cellule contenant un crayon
combustible composé d’uranium 238 et d’uranium 235, avec
un maillage en énergie d’une centaine de groupes. Si le calcul
est effectué en utilisant les sections efficaces multigroupes à
dilution infinie de l’uranium 238, au lieu de ses sections efficaces
multigroupes autoprotégées, le taux d’absorption de
l’uranium 238 dans son domaine de résonances est surestimé
d’un facteur 2 et la valeur du coefficient de multiplication effectif
, qui caractérise le bilan de la réaction en chaîne s’établissant
dans un système nucléaire, est sous-estimée de 25 %.
Les ordres de grandeur des quantités calculées sont perdus.
Le phénomène d’autoprotection doit donc être modélisé dans
les codes de transport multigroupes avant tout calcul de flux.
Pour ces codes, cette modélisation peut donc être vue comme
la dernière étape du traitement des sections efficaces.
Dans les réacteurs à neutrons thermiques, les résonances les
plus importantes à traiter sont les résonances d’absorption des
noyaux lourds. Mais pour les réacteurs à neutrons rapides ou
pour des calculs spécifiques (calculs de réflecteurs, par
exemple), il faut aussi prendre en compte les résonances de
diffusion des noyaux plus légers, comme le sodium ou le fer.

<!-- page 67 (PDF 25) -->
### Principes de la modélisation du phénomène d’autoprotection

Comme le montre l’équation (3), le calcul des sections efficaces
multigroupe autoprotégées d’un noyau résonnant passe
par l’estimation du flux réel ? ()□, ) qui dépend des variables
d’espace et d’énergie. Or, le domaine en énergie pour lequel
les noyaux présentent des résonances est essentiellement le
domaine du ralentissement (de quelques centaines de keV à
quelques eV).Le flux utilisé pour calculer les sections efficaces
multigroupes autoprotégées est donc obtenu en résolvant une
équation de ralentissement. La répartition spatiale du flux est
calculée par le biais d’une discrétisation des milieux contenant
le noyau résonnant en différentes régions d’autoprotection
notées α. On fait l’hypothèse que, dans chaque région d’autoprotection
α, le flux est ponctuel en léthargie et constant en
espace. Il est noté φα() et est utilisé pour le calcul des sections
efficaces multigroupes autoprotégées dans la région α.
Cette modélisation permet d’associer à un noyau résonnant
un jeu de sections efficaces multigroupes spécifique à chaque
région d’autoprotection α. Pour une réaction de type q, ces
sections efficaces sont données, dans chaque groupe en
énergie T, par l’équation (5) :
(5)
où φg
α est le flux multigroupe dans le groupe T et la région α.
Il existe deux familles de méthodes permettant de réaliser le
calcul des sections efficaces multigroupes autoprotégées pour
les noyaux résonnants.
Méthodes procédant par équivalence
avec un milieu homogène infini
On peut dériver de l’équation du ralentissement une équation
appelée « équation de structure fine ». Cette équation est établie
en milieu homogène infini dans l’encadré ci-après (p. 68).
Pour les méthodes procédant par équivalence avec un milieu
homogène infini, on choisit d’utiliser pour φα() (dans l’équation
(5)), le facteur de structure fine solution de l’équation de
structure fine dans la région d’autoprotection α.Le calcul d’autoprotection
s’effectue alors en deux étapes :
• Comme les taux de réaction ponctuels associés à ce facteur
de structure fine ne peuvent être calculés directement dans
le cadre de la modélisation du phénomène d’autoprotection
(description fine des transferts en énergie « perdue » dans
un calcul multigroupe), le calcul d’autoprotection les évalue
en effectuant une équivalence avec un milieu homogène
infini pour lequel ces taux de réaction sont connus grâce à
des tabulations effectuées en amont du code de transport, à
l’étape de création des bibliothèques (voir encadré ci-après,
p. 68) ;
• une fois les taux de réactions ponctuels obtenus, le calcul
d’autoprotection effectue une deuxième équivalence appelée
« équivalence multigroupe » qui calcule les sections efficaces
multigroupes qui préservent ces taux de réaction.
La partie délicate de ce calcul est l’obtention des taux de réaction
à préserver. Cette partie nécessite, en effet, une modélisation
physique de l’opérateur de ralentissement résonnant.
La partie « équivalence multigroupe » se ramène, quant à elle,
à la résolution d’un système non linéaire.
Les méthodes de ce type, dédiées initialement aux réacteurs
à neutrons thermiques, sont mises en œuvre dans plusieurs
codes de transport multigroupe, par exemple APOLLO, WIMS,
HELIOS, CASMO, LANCER02, DRAGON (voir tableau des
codes de neutronique, p. 138-139).
Méthodes de type « sous-groupes »
Les méthodes de type « sous-groupes » étaient dédiées, à
l’origine, aux réacteurs à neutrons rapides.
Elles reposent sur l’hypothèse fondamentale que les sections
efficaces résonnantes et les densités de collision
(sources de ralentissement) ne sont pas corrélées. Cette
hypothèse est vérifiée dans le domaine non résolu des
noyaux (domaine prépondérant, dans le cas des réacteurs
à neutrons rapides) ou dans tout le domaine en énergie,
pourvu que le maillage multigroupe soit suffisamment fin.
Ces méthodes sont des méthodes de référence dans leur
domaine d’application. Elles sont présentes dans le code
ECCO* et dans le code APOLLO*.
Ces méthodes, qui ne demandent aucune modélisation de
l’opérateur de ralentissement résonnant, permettent d’obtenir
les sections efficaces multigroupes autoprotégées par une
résolution directe de l’équation du ralentissement dans chaque
région d’autoprotection α. Ces sections efficaces sont alors
données par l’équation (6).
(6)
Les méthodes de type « sous-groupes » peuvent aussi être
« étendues », de façon à élargir leur domaine d’application
aux réacteurs à neutrons thermiques, dans le cadre d’un
découpage multigroupe grossier. C’est ce qui est fait dans le
code WIMS ou le code DRAGON. Les méthodes qui en résultent
ne peuvent alors plus être considérées comme des
méthodes de référence.

<!-- page 68 (PDF 26) -->
### Traitement des mélanges de noyaux résonnants

Un point particulièrement délicat de la modélisation du phénomène
d’autoprotection est le traitement des mélanges de
noyaux résonnants.Ce traitement est souvent effectué par des
méthodes simplifiées, parmi lesquelles :
Du fait du caractère résonnant des sections efficaces, le flux a
aussi un caractère résonnant. On a coutume de factoriser le flux
scalaire ? en un flux macroscopique Υ qui est le flux régnant hors
des résonances et qui a donc une variation très lente en fonction
de la léthargie, et un facteur de structure fine φ qui caractérise
le comportement résonnant du flux dans la résonance. Ce
facteur est sans dimension. L’équation permettant de le calculer
s’appelle l’« équation de structure fine ».Elle est obtenue en factorisant
le flux scalaire dans l’équation du ralentissement.
Pour un milieu homogène infini contenant un noyau résonnant
dont les données sont indicées par 0 et des noyaux modérateurs
dont les données sont indicées par 1, l’équation du ralentissement
s’écrit :
• (0 : nombre de noyaux résonnants par unité de volume,
• σ0() : section efficace microscopique totale du noyau résonnant
à la léthargie u,
• 61() : section efficace macroscopique totale des noyaux
modérateurs à la léthargie ,
• )0?() : opérateur microscopique de ralentissement sur le
noyau résonnant,
• R1?(): opérateur macroscopique de ralentissement sur les
noyaux modérateurs.
Cette équation de bilan traduit le fait qu’il y a autant de neutrons
qui disparaissent par chocs que de neutrons qui apparaissent
par ralentissement à une léthargie  donnée.
Le flux macroscopique et le facteur de structure fine sont respectivement
donnés par :
L’opérateur microscopique de ralentissement sur le noyau résonnant
s’exprime par :
où ε0 est le gain maximum en léthargie sur le noyau résonnant
(de l’ordre de — pour un noyau lourd,  étant le rapport de la
masse du noyau à celle du neutron).
En substituant le flux réel par le produit du facteur de structure
fine et du flux macroscopique dans l’équation du ralentissement
et en faisant l’approximation r0(φΥ)() ≈Υ()r0φ(u), approximation
justifiée par le fait que le domaine d’intégration de l’opérateur
r0 est très petit et que le flux macroscopique Υ() varie
très peu en fonction de la léthargie, on obtient :
Le paramètre σb, quotient de la section efficace macroscopique
totale des noyaux modérateurs par le nombre de noyaux résonnants
par unité de volume :
caractérise la dilution du noyau résonnant dans les noyaux
modérateurs. Il est appelé « section de dilution ». On obtient
donc l’équation dite « de structure fine » :
Quand le nombre de noyaux résonnants est nul, la section de
dilution devient infinie. Il n’y a alors plus de phénomène d’autoprotection
, puisqu’il n’y a plus de résonances. C’est ce qui
explique la terminologie « sections efficaces multigroupes à dilution
infinie » pour les sections efficaces multigroupes calculées
sans prendre en compte le phénomène d’autoprotection (voir
l’équation (4)).
Dans le cas d’un milieu homogène infini contenant un seul noyau
résonnant, l’équation de structure fine est résolue, pour une
série de températures et de dilutions, par des codes disposant
des données nucléaires ponctuelles. Ces calculs sont généralement
faits par les systèmes de traitement à l’étape de création
des bibliothèques multigroupes.
Les résultats sont conservés sous forme de tabulations, en fonction
de la température et de la dilution, des différents taux de
réaction (absorption, diffusion et production) du noyau résonnant
sur un maillage multigroupe donné. Ces taux sont appelés
« taux effectifs » et font partie des données de base des
méthodes d’autoprotection procédant par équivalence avec un
milieu homogène infini.
Factorisation du flux - Notion de structure fine
• Les méthodes itératives : chaque noyau résonnant est calculé
séparément, les autres noyaux résonnants étant considérés
comme des noyaux modérateurs avec des sections efficaces
constantes par groupe.Ces calculs peuvent être itérés.


<!-- page 69 (PDF 27) -->
• Les méthodes de type « Williams » : les taux de réaction du
noyau dans le mélange sont calculés à partir des taux de
réaction du noyau seul (quand on remplace les autres
noyaux résonnants par leurs sections potentielles) et d’un
facteur correctif (caractérisant le mélange résonnant) évalué
grâce à un calcul multigroupe fin.
Ces méthodes simplifiées ne prennent pas correctement en
compte le creusement du flux qui est dû à l’ensemble des
résonances de tous les noyaux présents. Une difficulté apparaît
donc lorsque les noyaux formant le mélange résonnant
présentent des recouvrements de résonances. Ce problème
est illustré dans la figure 24 où sont tracées les sections efficaces
des noyaux résonnants présents dans un combustible
mixte composé d’oxyde d’uranium et de plutonium (MOX)
dans le domaine en énergie allant de 19 eV à 23 eV.
L’idée de base du traitement développé dans le code
APOLLO2 est de considérer le mélange résonnant comme
une entité résonnante unique dont la section efficace est celle
du mélange. Cette section est représentée en cercles noirs
dans la figure 24.
Le traitement des mélanges résonnants est présenté dans le
cadre de la méthode procédant par équivalence avec un
milieu homogène infini, méthode appelée « Livolant-
Jeanpierre », du nom de ses deux concepteurs qui l’ont élaborée
dans le code APOLLO1, à la fin des années 60.
On ne s’intéresse ici qu’au calcul des taux de réaction à préserver
lors du calcul des sections efficaces multigroupes autoprotégées
car, comme cela a déjà été mentionné, c’est cette
partie qui nécessite une modélisation physique. Ces taux sont
issus de la résolution de l’équation de structure fine dans
chaque région d’autoprotection. Cette équation est écrite en
1E-4
1E-3
0,01
0,1
U 238
PU 240
PU 239
U 235
PU 238
PU 241
PU 242
Fig. 24. Combustible MOX : Recouvrements de résonances
et section efficace microscopique du mélange.
Sections (barn)
Mélange
Énergie (eV)
Section efficace microscopique du mélange
dans un MOX (19 eV à 23 eV)
utilisant la méthode des probabilités de collision (voir p. 00)
pour traiter la variable spatiale.
Pour établir cette équation dans une géométrie donnée, il faut
faire l’hypothèse que le flux macroscopique est spatialement
plat, hypothèse qui, jusqu’à présent, n’a pas été mise en
défaut.
Pour un mélange de M noyaux résonnants, l’équation de structure
fine s’écrit de la façon suivante :
(7)
• φα () : facteur de structure fine dans la région α
• r0Iβ φβ () : opérateur de ralentissement du composant I
du mélange résonnant dans la région β
• 0I2 : proportion, dans le mélange résonnant, du composant
I dans la région β
Dans cette équation, la matrice C, dérivée de la matrice des
probabilités de collision, traduit le couplage spatial entre les
différentes régions d’autoprotection et le vecteur S, les sources
dues aux noyaux non résonnants.
Modélisation de l’opérateur de ralentissement résonnant
Dans le cadre d’un calcul multigroupe sur un maillage grossier,
on a perdu toute information fine sur les transferts en énergie.
On ne peut donc plus traiter de façon exacte le couplage en
énergie dû aux opérateurs de ralentissement résonnant. Par
conséquent, on simplifie l’équation (7) en introduisant une
modélisation de ces opérateurs. Plusieurs modèles de ralentissement
existent, soit « physiques », c’est-à-dire liés à une
forme ou à une distribution des résonances, soit « mathématiques
», c’est-à-dire généraux. On peut citer les modèles :
• NR : « Narrow Resonance », qui traite une résonance étroite
isolée dans un groupe ;
• WR : « Wide Resonance », qui traite une résonance large
isolée dans un groupe ;
• ST : qui traite une distribution STatistique de résonances
étroites dans un groupe ;
• TR : « Toute Résonance », qui traite n’importe quelle distribution
de résonances.
Dans le cas du traitement des mélanges, on a utilisé le modèle
TR qui approche l’opérateur r0m par :
(8)
Dans cette expression, πI (T□, T) est la probabilité moyenne
pour le neutron d’être diffusé par le noyau résonnant I du

<!-- page 70 (PDF 28) -->
groupe T□ dans le groupe T et □σs0Iφ□T□ est le taux moyen de
diffusion du noyau résonnant I dans le groupe T□.
La modélisation « TR » a une propriété fondamentale qui est
utilisée dans la suite : plus le maillage multigroupe est fin, plus
la modélisation « TR » écrite sur ce maillage est précise.
La modélisation « TR » des opérateurs de ralentissement
lourd permet de résoudre de façon approchée l’équation (7) et
donc d’en déduire dans chaque région d’autoprotection α, un
flux approché noté φα
TR (). Grâce à des formules de quadrature
spécifiques déduites des tables de probabilité de chaque
noyau du mélange résonnant, des taux de réaction approchés
sont calculés dans le groupe T, pour chaque composant I du
mélange et chaque région d’autoprotection α. Ils s’écrivent
pour la réaction  :
(9)
Équivalence avec un milieu homogène infini
Les taux obtenus par l’équation (9) sont entachés de l’erreur
de modélisation sur les opérateurs de ralentissement résonnant
. Pour s’affranchir de cette erreur, on procède, pour
chaque groupe résonnant T, chaque région d’autoprotection
α et chaque composant I du mélange à une équivalence
avec un milieu homogène infini contenant le mélange de
noyaux résonnants à une certaine dilution à définir.
Pour expliciter cette équivalence, on écrit l’équation de structure
fine pour le mélange en milieu homogène infini, en modélisant
les opérateurs de ralentissement par le modèle TR précédemment
décrit dans l’équation (8) :
(10)
Cette équation permet d’obtenir une expression analytique du
facteur de structure fine, qui est paramétrée par la dilution σb.
Le principe de l’équivalence est le suivant :
• Pour chaque groupe résonnant T, chaque région d’autoprotection
α et chaque composant I du mélange, on cherche un
milieu homogène infini caractérisé par sa dilution (dite « équivalente
»), de façon que le taux d’absorption calculé avec le
modèle TR soit le même pour le composant I dans le milieu
homogène infini et dans la région d’autoprotection α.
• Suivant que le mélange résonnant est constitué d’un seul
noyau ou de plusieurs noyaux, le traitement est différent.
- Dans le cas particulier où le mélange résonnant est composé
d’un seul noyau, on interpole, pour la dilution équivalente
obtenue, les tabulations de taux effectifs « exacts » du
noyau calculés en milieu homogène infini (voir encadré
«Factorisation du flux – Notion de structure fine»).
- Dans le cas d’un milieu homogène infini contenant un
mélange de noyaux résonnants, l’équation de structure fine
ne peut plus être résolue une fois pour toutes en amont du
calcul de transport, puisque les proportions des différents
noyaux du mélange sont inconnues. Il faut donc simuler, lors
du calcul d’autoprotection, la résolution « exacte » de l’équation
de structure fine en milieu homogène infini.Cela est réalisé
en approchant les opérateurs de ralentissement résonnants
par leurs approximations TR effectuées sur un maillage
multigroupe extrêmement fin comprenant plus d’une dizaine
de milliers de groupes. Cette modélisation est alors quasi
exacte, comme expliqué ci-dessus.
• On en déduit, enfin, les taux « corrigés » dans chaque
groupe résonnant T et chaque région d’autoprotection α.
Cette équivalence est résumée dans la figure 25 ci-dessous.
Fig. 25. Équivalence entre taux de réaction homogènes
et hétérogènes pour un mélange de noyaux résonnants.
Lors du calcul pour un noyau seul, les formules de quadrature
peuvent être établies une fois pour toutes et stockées dans les
bibliothèques multigroupes, alors que pour un mélange de
noyaux résonnants, comme les proportions relatives ne sont
pas connues, elles doivent être calculées « au vol ».

### Modélisation d’un mélange d’isotopes résonnants : exemple de validation sur un calcul d’assemblage de réacteur à eau bouillante.

L’exemple présenté ici est tiré de l’étude du benchmark international
ATRIUM-10 MOX. Il s’agit du calcul d’un assemblage
de réacteur à eau bouillante. Les grandeurs physiques calculées
sont le facteur de multiplication effectif des neutrons, C□LL,
et les taux de réaction d’absorption pour différents nucléides
résonnants : uranium 238, plutonium 239, plutonium 240 et
plutonium 241. La démarche de validation repose sur la comparaison
des résultats issus de trois types de calcul :
Formules
de quadrature
Tabulation pré-établie
ou calcul direct
Équivalence

<!-- page 71 (PDF 29) -->
• Un calcul de référence avec le code de transport Monte-
Carlo TRIPOLI-4® (cent millions d’histoires de neutrons ont
été simulées) ;
• un calcul APOLLO2, noté ITER, qui utilise la méthode itérative
de calcul des sections efficaces multigroupes autoprotégées
;
• un calcul APOLLO2, noté MEL, qui utilise la méthode de traitement
des mélanges résonnants.
Les deux calculs APOLLO2 ont utilisé un maillage en énergie
à 172 groupes, et le calcul d’autoprotection a été réalisé entre
13,71 eV et 203,995 eV, domaine correspondant aux groupes
64 à 82.
L’assemblage ATRIUM 10 est un assemblage 10 x 10 contenant
:
• Des crayons « MOX » dont le combustible est de l’oxyde
mixte PUO2/UO2 avec six types d’enrichissements différents
en plutonium (cellules MOX1 à MOX6) ;
• des crayons absorbants composés d’oxyde d’uranium et de
gadolinium (cellules UOXG).
Les crayons « MOX » sont sur base d’uranium appauvri (enrichissement
massique de 0,2 % en uranium 235). Les crayons
absorbants sont sur base d’uranium enrichi (enrichissement
massique de 3,95 % en uranium 235). L’assemblage traité est
sans croix de contrôle insérée.
La figure 26 représente la géométrie d’un huitième d’assemblage
ATRIUM 10.
La comparaison des coefficients de multiplication effectifs
entre les deux calculs APOLLO2 et le calcul TRIPOLI-4® est
donnée dans le tableau 11.
Fig. 26. Géométrie d’un huitième d’assemblage ATRIUM 10.
MOX1 : 2,69 %
MOX2 : 3,86 %
MOX3 : 5,20 %
MOX4 : 6,71 %
MOX5 : 7,55 %
MOX6 : 10,57 %
UOXG : 1,50 %
Boîtier
152,5 mm
Boîtier
Eau diphasique
Eau monophasique
Eau monophasique
Tableau 11
Coefficients de multiplication effectifs TRIPOLI-4®
et APOLLO2 pour un assemblage ATRIUM-10 MOX
C□LL
σ TRIPOLI-4® Écart en pcm*
TRIPOLI-4®
1,14016
11 pcm
Calcul ITER
1,13637
-379 ± 33
Calcul MEL
1,13795
-221 ± 33
Bien qu’aucun des résultats des deux calculs APOLLO2 ne soit
dans les barres d’erreur à trois écarts types de TRIPOLI-4®, on
note que l’utilisation du modèle de traitement direct des
mélanges résonnants permet d’avoir une amélioration significative
du résultat du calcul, de l’ordre de 160 pcm. Cette
conclusion est confirmée par la comparaison détaillée, groupe
par groupe et noyau par noyau, des calculs déterministes et
stochastiques.
À titre d’illustration, la figure 27 représente l’absorption résonnante
dans les crayons de type « MOX6 » dont la teneur en
plutonium est la plus forte et qui sont donc les plus sensibles
au phénomène de recouvrement de résonances (voir fig. 28).
Le graphe inférieur représente les taux de référence (exprimés
en pcm) calculés par TRIPOLI-4®. Le graphe supérieur
représente les écarts relatifs exprimés en % entre les calculs
APOLLO2 et le calcul TRIPOLI-4®. Avec la méthode MEL,
dans les crayons de type « MOX6 », l’absorption résonnante
intégrée entre les groupes 64 et 82 est calculée de façon très
précise, puisque l’écart relatif est de 0,16 %, alors qu’il était
de 4,27 % avec la méthode itérative. De plus, les écarts relatifs
dans tous les groupes sont réduits de 16,4 % à 2,3 %, ce
qui est un excellent résultat.Les améliorations les plus visibles
sont apportées dans les groupes 69, 73 et 82 où l’on observe
T4
-10
-5
ITER
MEL
Fig. 27. Absorption résonnante dans les crayons « MOX6 » :
comparaison des modèles d’autoprotection dans le cas de
recouvrement de résonances, par rapport à la référence Monte-Carlo
TRIPOLI4® (notée T4). On note l’apport du modèle de traitement
des mélanges.
Écart en %
Absorption (pcm)
Groupe
< 16,4 %
< 2,3 %
U 238
Pu 239
Pu 240
Pu 239
Pu 240
Pu 239
Pu 241

<!-- page 72 (PDF 30) -->
respectivement des recouvrements de résonances entre l’uranium
238, le plutonium 239 et le plutonium 240, le plutonium
239 et le plutonium 240, le plutonium 239 et le plutonium 241.
Ces recouvrements sont visibles dans la figure 28.

### Perspectives

La modélisation du phénomène d’autoprotection est une des
modélisations les plus délicates d’un code de transport déterministes
multigroupe, mais elle a atteint désormais une certaine
maturité.
U 238
Pu 239
Pu 240
Pu 241
Pu 242
U 235
Pu 238
0,01
0,1
14,5
15,5
0,01
0,1
0,01
0,1
10 000
Fig. 28. Recouvrements de résonances dans les crayons « MOX6 ».
Sections (barn)
Sections (barn)
Sections (barn)
Énergie (eV)
Énergie (eV)
Énergie (eV)
Groupe 69
Groupe 73
Groupe 82
Les méthodes procédant par équivalence avec un milieu homogène
infini ont été sophistiquées à l’extrême pour prendre en
compte des géométries complexes, des profils de température
dans le combustible, des recouvrements de résonance…
Les méthodes de type « sous-groupes » qui, par nature, sont
beaucoup plus simples et plus précises, puisqu’elles ne
requièrent aucune modélisation de l’opérateur de ralentissement
, ne sont adaptées qu’au domaine non résolu ou aux
maillages multigroupe fins. La puissance informatique étant
sans cesse croissante, l’avenir est certainement dans l’utilisation
de ces méthodes. Le prix à payer est l’utilisation d’un
maillage énergétique suffisamment fin, mais le calcul d’autoprotection
peut être réalisé sur un maillage différent de celui
du calcul de flux.

## La discrétisation en angle pour un groupe d’énergie donné

La discrétisation liée à la variable direction □
→de l’espace des
phases est appelée « discrétisation en angle ». Elle tire parti
de l’isotropie des matériaux traversés, déjà signalée.
Il y a deux méthodes principalement utilisées pour traiter la
variable angulaire : l’une est une méthode de collocation,
connue sous le nom de méthode des ordonnées discrètes ou
de méthode SN ; l’autre est une méthode de développement
du flux angulaire sur la base des harmoniques sphériques,
connue sous le nom de méthode PN ou méthode des harmoniques
sphériques.

### La méthode SN

La méthode SN consiste à choisir un ensemble de directions
discrètes dans 4π stéradians : {□
→
<; < = 1, N} et à écrire l’équation
du transport pour ces directions. Si l’on considère l’équation
du transport stationnaire à source, pour un seul groupe T,
on peut écrire :
(11)
Pour évaluer l’intégrale sur les angles, on utilise une formule
de quadrature du type :
(12)
En ayant ainsi choisi les N directions □
→
< et les N poids w<, on
peut écrire N fois l’équation (11) pour < =1,…N, et avoir un
système d’équations, couplées par les sources, à résoudre
pour les inconnues
. Ce sont des équations

<!-- page 73 (PDF 31) -->
Gian Carlo Wick est un physicien théoricien
italien auquel on doit des contributions
majeures en théorie quantique des champs.
Dans ses travaux il a été conduit, pour la
résoudre, à approximer une équation intégrodifférentielle
par un système d’équations différentielles
, en remplaçant le terme intégral par
une formule de quadrature [1] :
Formule de quadrature de Wick permettant
d’approximer l’intégrale d’une fonction arbitraire
f (µ) définie dans l’intervalle [-1, +1].
Plusieurs voies existent pour en déterminer les
constantes aj et μj.G. C.Wick propose, comme
meilleur choix, la quadrature de Gauss* qui rend exacte l’équation
ci-dessus pour tout polynôme en μ de degré inférieur à 2n-1.
Subrahmanyan Chandrasekhar est un astrophysicien et un
mathématicien américain, d’origine indienne, co-lauréat du Prix
Nobel de physique de 1983.Pour traiter des problèmes de transfert
radiatif, S.Chandrasekhar reprend le schéma proposé par G.
C. Wick, le développe significativement pour en faire une large
utilisation [2].
La méthode initialement introduite par G. C. Wick se popularise
alors sous le nom de « Wick-Chandrasekhar discrete ordinate
method ». La démonstration mathématique de sa convergence
n’interviendra qu’en 1958. Elle est due au mathématicien P. M.
Anselone [3].
À partir des années 50, au Los Alamos Scientific Laboratory de
l’Université de Californie, elle est appliquée au transport des neutrons
par B. G. Carslon, C. E. Lee et K. D. Lathrop [4]. Elle est
alors souvent appelée « méthode SN » (S pour « Angular
Segmentation », « N » pour l’ordre de la quadrature angulaire).
Les premiers codes de calcul traitant le transport des neutrons
par
des
méthodes
déterministes
font
leur
apparition.
P. M. Anselone reprend son étude de la convergence de la
méthode aux ordonnées discrètes, cette fois-ci, dans le cadre
de la résolution numérique de l’équation du transport des neutrons
, dans un document publié par Oak Ridge National
Laboratory [5]. K. D. Lathrop en étudie les effets de raies, sorte
de « talon d’Achille » de la méthode dans des configurations
lacunaires, par exemple. Plusieurs lignées historiques de codes
SN à une, deux et trois dimensions d’espace sortent des laboratoires
nationaux américains, d’ANISN à TORT en passant par
TWOTRAN et TWODANT, codes qui par la suite seront largement
utilisés dans la communauté nucléaire mondiale via leur
distribution par RSICC* et l’OCDE/AEN*, tant pour les calculs
de neutronique / criticité que pour ceux de radioprotection.
Le CEA développe, au cours des années 80, les codes SN BIS-
TRO [6] incorporé par la suite dans le code de réseau APOLLO2
et SN1D dédié aux études de radioprotection. Un développement
original a été d’introduire dans le code SN1D [7] des sections
efficaces représentées par des tables de probabilités,
permettant ainsi d’améliorer significativement le calcul de propagation
des neutrons en fonction de leur énergie [8] dans des
configurations à forte atténuation du flux des neutrons.
□Quelques références historiques
[1] G. C. WICK, “Über ebene Diffusionsproblem”, Zs. f. Phys., 121,
702, 1943.
[2] S. CHANDRASEKHAR, Radiative Transfer, Oxford, Clarendon Press,
1950 ; réédition : New York, Dover, 1960.
[3] P. M. ANSELONE, “Convergence of the Wick-Chandrasekhar
Approximation Technique in Radiative Transfer” Astrophys. J., 128,
124; 130, 881, 1958.
[4] K. D. LATHROP, “The Early Days of the SN method”, SLAC-PUB
5829, December 1992 ; B. G. Carlson, “A solution of the transport
equation by SN approximations”, LA- 1599, Los Alamos Scientific
Laboratory,
1953,
revised
version,
LA
1891,
1955 ;
B. G. CARLSON, C. E. LEE, “Mechanical Quadrature and Transport
Equations”, LAMS-2573, Physics, TID-4500, June 1961.
[5] P. M. ANSELONE, A. G. GIBBS, “Convergence of the Discrete
Ordinates Method for the Transport Equation”, ORNL-4984, UC-32,
Mathematics and Computers, July 1974.
[6] G. PALMIOTTI, J.M. RIEUNIER, C. GHO, M. SALATORES, “BISTRO
Optimized Two Dimensional SN Transport Code”, Nucl. Sc. Eng. 104,
26, 1990.
[7] G. DEJONGHE, L. LUNEVILLE, SN1D :“Code de protection nucléaire
à une dimension”, Rapport interne CEA, 1983.
[8] L. LUNEVILLE, Méthode multibande aux ordonnées discrètes.
Formalisme et résultats, Note CEA-N-2832, 1998.
Aux sources de la méthode aux ordonnées discrètes ou méthode SN
Gian Carlo Wick
1909-1992
Subrahmanyan Chandrasekhar
1910-1995

<!-- page 74 (PDF 32) -->
différentielles en espace, auxquelles il faut encore appliquer
une discrétisation spatiale.
Il existe une infinité de choix possibles pour les directions et les
poids. Par exemple, en géométrie plane unidimensionnelle,
l’angle se réduisant à la seule variable μ = cosθ (avec θ l’angle
entre la direction de propagation et l’axe de référence), il est
usuel de choisir les {μ<, w<} correspondant à une quadrature
de Gauss*.
La méthode SN est très largement utilisée malgré sa faiblesse
intrinsèque qu’est l’« effet de raies » : en présence d’une
source de neutrons très localisée dans un milieu peu diffusif,
certaines des directions choisies peuvent complètement
« manquer » une vue directe de la source et, par conséquent,
conduire à des flux presque nuls non physiques. On pallie ce
défaut par un raffinement du maillage angulaire.

### La méthode PN

La méthode PN consiste à utiliser un développement de la
dépendance angulaire du flux en harmoniques sphériques
(à une dimension celles-ci deviennent les polynômes
de Legendre, d’où le nom de la méthode) selon l’expression :
(13)
Puisque les harmoniques sphériques forment un ensemble
orthonormé et complet, on sait que l’équation (13) est toujours
vraie, même si, dans la pratique, on est obligé de tronquer le
développement après les premiers termes. Pour obtenir des
équations pour les inconnues
, il faut prendre les
moments de l’équation du transport par rapport aux harmoniques
sphériques. Il s’ensuit un système d’équations couplées
, différentielles en espace.
Les coefficients des équations PN sont assez compliqués à
exprimer analytiquement (sauf dans le cas à une dimension).
De surcroît, les équations obtenues par projection de l’équation
du transport sur les harmoniques sphériques sont fortement
couplées et donc nécessitent des algorithmes de résolution
spécifiques. En revanche, la méthode PN ne présente
pas de problèmes notoires comme l’effet de raies de la
méthode SN.
Les difficultés de mise en œuvre de la méthode PN à trois
dimensions expliquent pourquoi peu de codes industriels choisissent
cette approche.

### La méthode du transport simplifié SPN

Dans les années 60, pour diminuer la grande complexité des
équations PN pour les problèmes multidimensionnels et rendre
possible leur résolution, E.M. Gelbard [3] a proposé une nouvelle
approximation baptisée « PN simplifiée » ou SPN. Le principe
de la méthode est de construire un opérateur généralisant
l’opérateur de diffusion et prenant en compte la majorité des
effets de transport.L’idée de Gelbard était de supposer que localement
la solution du transport était équivalente à la solution
d’une équation en géométrie plane et donc pouvait se résoudre
par une méthode PN 1D. Ceci permet de réduire le nombre
d’harmoniques à prendre en compte qui croît alors en N au lieu
de N2. Dans la méthode proposée, le passage des équations
locales aux équations 3D était obtenu par une méthode empirique
et formelle. Après une phase de sommeil d’une trentaine
d’années due au manque de puissance des ordinateurs pour
résoudre ces équations, et également au manque de justification
théorique, un regain d’intérêt s’est produit dans les années
1990 lorsque Pomraning [4] et Larsen, Morel and McGhee [5]
ont présenté indépendamment des analyses asymptotiques qui
justifiaient la méthode empirique de Gelbard.
Les équations SPN peuvent également être obtenues par un
principe variationnel. Ce principe fut tout d’abord proposé par
Pomraning pour le milieu infini et le choc anisotrope en théorie
monocinétique et fut étendu ensuite par Brantley et Larsen
[6], dans le cadre des équations SP3, à un milieu fini avec
prise en compte de conditions aux limites, choc isotrope et
description multigroupe de la variable énergie.
On présente ici l’analyse faite par Pomraning qui part de la
constatation suivante : si l’équation du transport est localement
en géométrie plane, alors la solution SPN est aussi solution
de l’équation du transport. Cette hypothèse se justifie, par
exemple, pour un calcul homogène quand on se trouve loin
des interfaces entre les différents milieux.
On considère un système de coordonnées local (4□, □, C□).
La direction □
→peut alors s’écrire :
où μ est le cosinus de l’angle polaire et φ est l’angle azimutal.
On fait l’hypothèse que, dans ce système, la solution a une
faible dépendance suivant la direction azimutale (hypothèse
de symétrie plane) et qu’elle a également une faible dépendance
en h et en i. En introduisant un facteur  quantifiant
cette faible variation, et en passant à la limite ( →0), on
obtient une équation du type transport 1D dans le système
local.Cependant dans ce système local, la direction □
→dépend
de l’espace (puisque ce système varie en espace), ce qui n’est
pas le cas dans l’équation du transport. Il faut donc faire l’hypothèse
supplémentaire que le système local (4□, □, C□) varie
lentement en espace (variation quantifiée par le coefficient ).
Avec cette hypothèse, le terme de fuite s’écrit :
On obtient ainsi un problème local en géométrie plane qui peut
être résolu exactement par la méthode PN. Si l’on décompose

<!-- page 75 (PDF 33) -->
la solution =1D(,)du problème local en géométrie plane sur
la base des polynômes de Legendre, on peut écrire :
On tronque ce développement à un ordre N choisi impair. Les
coefficients du développement (harmoniques) vérifient le système
couplé suivant :
pour 1 ≤< ≤(.
On rappelle que :
Le problème est d’obtenir l’approximation de = à partir de =1
1D.
On procède de la façon suivante (par analogie avec le flux scalaire
et le courant dans l’équation de la diffusion) :
• pour les < pairs, on peut écrire en prenant en compte la faible
dépendance de = selon h et i :
• pour les < impairs, on définit un vecteur =→
< à partir de l’harmonique
1D qui vérifie :
Cela permet d’écrire les équations suivantes dans le système
global avec une erreur en 0().Faire tendre  vers zéro ramène
à une équation 1D dans le système global.
On obtient ainsi un système d’équations aux dérivées partielles
. Les équations paires sont scalaires, les équations
impaires sont vectorielles. Pour être fermé, on doit adjoindre
à ce système un ensemble de conditions aux limites (par
exemple flux pairs nuls sur les bords ou trace normale des flux
impairs nulle sur les bords en cas de symétrie). À l’ordre 1, on
retrouve les équations de la diffusion. L’harmonique 0 correspond
au flux scalaire et l’harmonique 1 au courant.
Dans le cas de la géométrie plane ou pour un milieu infini
homogène la méthode converge (quand < tend vers l’infini)
vers la solution exacte du transport. Par contre, dans le cas
général, elle converge vers une solution différente (mais
proche) de la solution exacte du transport. Jusqu’à présent,
aucune estimation a priori d’erreur n’a été obtenue pour mesurer
l’écart entre la solution SPN et la solution exacte.
Cette approximation est disponible pour le solveur MINOS
pour les calculs statique et cinétique avec choc anisotrope [7].
La résolution se fait par élimination des harmoniques paires
et résolution par éléments finis mixtes duaux. Elle est également
disponible pour le solveur MINARET. On utilise dans ce
cas une forme diagonalisée des équations précédentes [8], la
résolution s’effectuant par élimination des harmoniques paires
et discrétisation par éléments finis de Galerkin discontinus.

### L’approximation de la diffusion

L’approximation de la diffusion permet de simplifier sous certaines
hypothèses l’opérateur de transport de l’équation de
Boltzmann, conduisant à une équation simple satisfaite par le
flux scalaire.
La voie classique pour dériver l’équation de la diffusion de
l’équation de Boltzmann passe par un développement de la
dépendance angulaire du flux dans un groupe en énergie T,
=T()□, □
→) sur la base des harmoniques sphériques.
L’approximation consiste à tronquer le développement aux
deux premiers termes, en supposant que les sources sont isotropes
dans le système du laboratoire :
(14)
('T()□) et
représentent les deux premiers moments du
flux angulaire).

<!-- page 76 (PDF 34) -->
L’équation (14) a une interprétation physique correspondant à
l’hypothèse d’une dépendance faible (au plus linéaire) du flux
en fonction de la direction □
→. Si l’on introduit cette approximation
dans l’équation de Boltzmann, on obtient, après diverses
manipulations, l’équation suivante à laquelle satisfait le flux
scalaire ?T()□) :
(15)
Les termes sont définis comme suit :
• –
: courant de neutrons qui est proportionnel
au gradient du flux ; c’est la loi de Fick :
(16)
Dg ()□) : coefficient de diffusion donné par l’expression :
(17)
: section efficace de transport dans le groupe T
définie par :
: cosinus de l’angle moyen de diffusion dans le
groupe T. Si les chocs sont isotropes dans le système du
laboratoire,
vaut 0 et la section efficace de transport
est simplement la section efficace totale.
Σ
T()□) : section efficace macroscopique de diffusion dans
le groupe T.
• Σ
T()□) : section de disparition du groupe T définie par :
• q
T ()□) : terme source.
Une deuxième manière d’aboutir à l’équation de la diffusion,
en partant d’une forme intégrale de l’équation de
Boltzmann, consiste à supposer que les sources et les chocs
sont isotropes dans le système du laboratoire, et que le flux
scalaire ?T()□) et la section macroscopique totale sont faiblement
dépendant de l’espace. On développe alors le flux scalaire
?T()□) en série deTaylor en espace en l’arrêtant au premier
ordre :
(18)
Après quelques transformations, on retrouve l’équation de la
diffusion (15), mais avec un coefficient de diffusion égal à :
La troisième manière d’arriver à l’équation de la diffusion
repose sur l’hypothèse que les absorptions du système sont
très faibles et que les gradients de flux le sont aussi.On réécrit
l’équation de Boltzmann en insérant un paramètre ε (ε << 1) qui
mesure la « petitesse » des absorptions. Une analyse asymptotique
de cette équation montre qu’au premier ordre, le flux
scalaire doit satisfaire à l’équation de la diffusion (15). La particularité
de cette dérivation est que les hypothèses ne sont
plus faites sur la forme du flux (dépendance faible en espace
ou en angle) que l’on ne connaît pas a priori, mais (du moins
en partie) sur les coefficients de l’équation elle-même (la section
efficace macroscopique d’absorption est faible devant la
section efficace macroscopique totale).
Quels avantages présente l’équation de la diffusion, par rapport
à l’équation du transport ?
En premier lieu, on est passé d’un espace des phases à 6
dimensions ()□, E, □
→) à un espace des phases à 4 dimensions
()□, /). Selon l’estimation que l’on avait donnée auparavant,
cela peut réduire d’un facteur cent à mille le nombre de degrés
de liberté d’une résolution numérique.
Par ailleurs, l’équation de la diffusion, que l’on rencontre dans
plusieurs domaines de la physique (conduction de la chaleur,
migration d’espèces chimiques dans un milieu, etc.) est une
équation différentielle aux dérivées partielles parmi les plus
simples et les plus étudiées des mathématiciens et des numériciens
. Par conséquent, elle bénéficie de méthodes numériques
de résolution très performantes et continuellement
améliorées par les meilleurs spécialistes.
On peut, enfin, souligner que la diffusion est une approximation
« robuste », dans le sens où même lorsque l’on s’éloigne
de son domaine de validité, les résultats, à défaut d’être précis
, sont qualitativement acceptables.
En pratique, la diffusion est applicable aux grands systèmes
(la dimension d’un système étant mesurée en nombre de
libres parcours moyens) presque homogènes, à l’image des
réacteurs de puissance avec assemblages combustibles
homogénéisés. Les industriels calculent souvent leurs réacteurs
en théorie de la diffusion à quelques groupes d’énergie,
avec des résultats satisfaisants, en utilisant comme coefficients
de l’équation des grandeurs obtenues au moyen de calculs
de transport précis. Ce point est détaillé infra, p. 193-213.

## La discrétisation en espace pour un groupe d’énergie donné

Nous présentons dans ce chapitre trois types de méthodes de
discrétisation spatiale : les méthodes des différences finies,
les méthodes nodales, les méthodes des éléments finis.
On peut aussi citer la méthode des probabilités de première
collision, fondée sur la forme intégrale de l’équation du trans-

<!-- page 77 (PDF 35) -->
port, qui a été pendant de nombreuses années la méthode de
prédilection des codes d’assemblage, dans le but de déterminer
les sections efficaces multigroupes autoprotégées pour
les calculs de cœurs de réacteurs. Cette méthode, qui souffre
de l’approximation du choc isotrope dans le système du laboratoire
, est aujourd’hui souvent remplacée par la méthode des
caractéristiques, plus souple et plus précise. Néanmoins, elle
a encore une place dans les calculs d’autoprotection, où le
traitement en énergie est primordial. Une comparaison entre
ces deux méthodes est présentée dans l’encadré p. 84.
La méthode des différences finies est très simple d’implémentation
en géométrie cartésienne, cylindrique ou sphérique.
Pour plus d’efficacité, on peut avoir recours avec succès à des
méthodes nodales (ou volumes finis) d’ordre supérieur. Les
méthodes des différences finies et les méthodes nodales sont
souvent utilisées dans la communauté des neutroniciens pour
résoudre l’équation de la diffusion.
Les méthodes des éléments finis ont été développées, à l’origine
, par les mécaniciens et sont fondées sur le principe du
calcul du minimum d’énergie. Elles peuvent être appliquées
soit à la résolution de l’équation de la diffusion, soit à celle de
l’équation du transport.
Les méthodes de discrétisation en espace pour un groupe
d’énergie donné sont exposées ici dans le cadre de l’équation
de la diffusion à source. On suppose que la discrétisation en
énergie (multigroupe) est déjà réalisée et on se place dans un
groupe T.Pour simplifier les notations, on omet volontairement
dans la suite l’indice sur le groupe.
L’équation de la diffusion à source dans un groupe donné
s’écrit :
(19)
où ' ()□) représente le flux scalaire (indépendant de la variable
angulaire), Σr ()□) la section de disparition du groupe et q ()□) le
terme source.
Dans la suite, et par un souci de simplification, on ne fera pas
intervenir les conditions aux limites au bord du domaine de
calcul. L’introduction de ces conditions aux limites modifie partiellement
les équations discrètes, mais ne remet pas en
cause leur fondement.

### Les méthodes des différences finies

Une façon simple de résoudre l’équation de la diffusion des
neutrons sur un maillage spatial est d’évaluer cette équation
aux points du maillage en remplaçant les dérivées partielles
par des différences finies.
Pour simplifier, mettons-nous dans le cadre d’une géométrie
1D, ℛ= [h0, hN+1], sur laquelle on se donne un maillage spatial
: h0 < h1 < … < h4–1 < h4 < h4+1 < … < hN+1
En supposant le flux de neutrons suffisamment régulier, et en
utilisant la formule de Taylor :
il est possible de remplacer l’opérateur différentiel de l’équation
de la diffusion par un opérateur aux différences finies :
où Di
+ (resp. Di
–) est la valeur du coefficient de diffusion dans
l’intervalle [h4–1, h4] (resp. [h4, h4+1]).
En écrivant l’équation de la diffusion aux points du maillage,
et après avoir remplacé l’opérateur différentiel par l’opérateur
aux différences précédent, on se ramène à résoudre un système
matriciel dont les inconnues sont les valeurs du flux aux
points du maillage :
Comme on l’a précédemment mentionné, on ne spécifiera pas
ici le traitement des conditions aux limites.
Il est à noter que la matrice A est symétrique, définie positive
et à diagonale dominante.De surcroît, elle est tri-diagonale (le
flux en un point n’étant relié qu’à ses voisins proches). Les
méthodes de résolution de systèmes linéaires, qu’elles soient
directes ou itératives, sont donc bien adaptées à ce système.
On peut remarquer que si on utilise la formule de Taylor en faisant
apparaître les points milieux
des intervalles [h4, h4+1],
on obtient un système matriciel de même nature que celui
obtenu précédemment, mais où les inconnues sont, dans ce
cas, les points milieux du maillage. On parlera dans le premier
cas de différences finies aux « points » des mailles, et dans
le deuxième cas de différences finies aux « centres » des
mailles.
La méthode des différences finies se généralise aisément aux
géométries 3D cartésiennes et les propriétés de la matrice globale
sont conservées. C’est pourquoi cette méthode a été
employée dès le début de la conception des cœurs de réacteur
à pas carré (type REP, par exemple).En effet, les méthodes itératives
de résolution du système sont performantes et ne nécessitent
que peu de place mémoire, ce qui était compatible avec
les toutes premières générations d’ordinateur.
Par contre, la méthode des différences finies se généralise
plus difficilement à des géométries à pas hexagonal (par
exemple, aux réacteurs RNR).

<!-- page 78 (PDF 36) -->
Cette méthode converge en O (h2 ) où h est le pas maximum
du maillage spatial. Il est donc nécessaire d’augmenter largement
le nombre de points de discrétisation, si l’on veut s’approcher
de la solution exacte. Cela est encore plus vrai dans
le cas de calculs de cœurs de réacteurs, homogénéisés au
niveau de l’assemblage.
La difficulté de généralisation de la méthode des différences
finies aux géométries hexagonales et la lente convergence
spatiale ont amené les ingénieurs à développer de nouvelles
méthodes d’approximation spatiale, en particulier les
méthodes nodales.

### Les méthodes nodales

Les méthodes nodales sont fondées sur une résolution semianalytique
de l’équation de la diffusion.
Pour illustrer la méthode, supposons une géométrie ℛcartésienne
2D, et considérons une maille [h4, h4+1] × [ i4, i4+1] où
les sections efficaces sont constantes en espace.
Intégrons l’équation de la diffusion (19) selon la direction h sur
l’intervalle [h4, h4+1], puis selon la direction i sur l’intervalle
[ i4, i4+1], et notons :
On obtient les équations différentielles selon h et i :
(20a)
Λ (h) et Λ4 (i) sont appelés les « fuites transverses » suivant
h et i.
Enfin, l’intégration de l’équation de la diffusion sur [h4, h4+1]
× [ i, i+1] donne l’équation de bilan :
(20b)
avec
et
Pour établir cette équation, on remarque que :
Les méthodes nodales consistent à résoudre les équations
différentielles selon les directions h et i, en prenant en compte
l’équation de bilan. Cette résolution peut être faite de façon
analytique ou en supposant une approximation polynomiale
des inconnues.
Dans le cas de l’approximation polynomiale, on introduit une
approximation des fuites transverses, soit plate, soit quadratique
. La résolution du système d’équations (20a) et (20b) s’effectue
alors pas à pas, de la manière suivante :
• L’intégration de l’équation différentielle selon i, en supposant
Λi (i) connu, donne une expression analytique de φi (i)
qui, une fois dérivée selon i, donnera une valeur de
• De même, l’intégration de l’équation différentielle selon h, en
supposant Λj (h) connu, donne une expression analytique
de φj (h) qui, une fois dérivée selon h, donnera une valeur
de
• L’équation de bilan permet, enfin, de calculer les valeurs du
flux intégré dans les mailles ?□.
Les inconnues introduites dans cette formulation sont les fuites
transverses à l’interface des mailles, et le flux dans les mailles.
Cette formulation s’apparente à la formulation mixte en approximation
éléments finis, décrite ci-après (p. 79 et suiv.), et des
analogies, voire des équivalences, sont démontrables dans
certains cas.
Ces méthodes ont été généralisées aux géométries hexagonales
.
Elles souffrent cependant de leur absence de fondements
mathématiques, ce qui rend difficile l’introduction de la notion
d’opérateur adjoint (contrairement aux méthodes aux « éléments
finis » décrites dans le paragraphe suivant) utilisée lors
de calculs de perturbation sur lesquels se fondent les études
de sensibilité à des variations de paramètres, comme les paramètres
géométriques ou les données nucléaires.

<!-- page 79 (PDF 37) -->
### Les méthodes des « éléments finis »

Grâce à la méthode de Rayleigh-Ritz il est possible de réécrire
l’équation de diffusion des neutrons présentée dans le paragraphe
précédent :
(21)
sous une forme variationnelle équivalente. On suppose ici les
sections efficaces constantes en espace.

### La formulation primale et son approximation spatiale

La formulation variationnelle primale du problème, la plus
immédiate à écrire, est :
Trouver ? ∈V (ℛ) tel que
où V est l’espace de Sobolev des fonctions qui sont L2 intégrables
sur le domaine spatial ℛ, ainsi que leurs dérivées.
Là encore, on fait abstraction des conditions aux limites.
Pour simplifier, on se restreint à la géométrie 1D et à son
maillage spatial {h4, 4 = 0 à N + 1} dont les points sont supposés
également répartis dans l’intervalle [h0, hN+1] ; h sera alors
la distance entre deux points contigus.
Pour la méthode des éléments finis d’ordre C, on introduit
le sous espace discret Vh de V défini par :
où □k est l’espace des polynômes de degré C. On note (w□)
une base de Vh.
La formulation discrète du problème est :
Trouver ?h ∈Vh tel que :
Il est ensuite relativement aisé de transformer ce problème en
un système matriciel A∅= Q où les inconnues sont les coordonnées
du flux ?h dans la base (w□).
La formulation discrète se généralise évidemment à trois dimensions
, avec un découpage du domaine ℛen polygones réguliers
(parallélépipèdes rectangles, prismes, pyramides…) à bords
droits ou courbes. Par exemple, en 2D sur un maillage cartésien
, les bases de polynômes sont illustrées dans la figure 29.
On peut montrer que, dans le cas d’un domaine ℛsuffisamment
régulier, et sous conditions sur les sections efficaces, la
Fig. 29. Base de polynômes de degré 2 en 2D.
x
x
x
y
y
z
z
z
y
solution du problème discret est bien une approximation du
problème continu initial, et que l’erreur est en 0(hC+1).
Remarque
• Il est possible de démontrer l’équivalence des approximations
de type « différences finies » aux sommets des mailles
et « éléments finis » d’ordre 1, à condition d’intégrer numériquement
(intégration de Gauss-Lobatto) les intégrales qui
interviennent dans la formulation discrète ;
• il a également été démontré qu’en utilisant une intégration de
Gauss, il est possible d’obtenir une erreur en 0(hC+2) ; c’est
ce qu’on appelle le phénomène de « super convergence ».
L’approximation du flux, telle qu’elle est proposée ici, donne
une solution continue sur le domaine ℛ. En revanche, le courant
(i.e. la dérivée du flux) n’est pas continu. Cette continuité
du flux peut produire parfois des contraintes sur le découpage
du domaine, en particulier à l’interface cœur-réflecteur où le
flux thermique subit une remontée brusque de son niveau
avant de s’annuler hors cœur. Ce phénomène est également
visible à l’interface de deux assemblages de natures différentes
(UOX et MOX, par exemple).Une bonne approximation
de la réalité doit donc nécessiter un découpage fin du cœur au
niveau de ces interfaces, pour « suivre au mieux » les
brusques variations du flux.
Une alternative est de « relâcher » la contrainte de continuité
du flux ; cela est possible en utilisant une formulation mixte du
problème.

### La formulation mixte du problème

En revenant à la formulation continue du problème donné par
l’équation (21), on introduit l’inconnue auxiliaire p□ qui représente
le courant :
La formulation variationnelle mixte du problème ainsi écrit est :
Trouver

<!-- page 80 (PDF 38) -->
où V est l’espace de Sobolev des fonctions L2 intégrables
(ainsi que leurs dérivées) et f est l’espace de Sobolev des
fonctions vectorielles L2 intégrables et à divergence L2 intégrable
.
La formulation discrète de ce problème est obtenue en se plaçant
dans des espaces discrets de V et W.On ne donnera pas
ici les conditions que doivent vérifier ces espaces, mais on
illustrera simplement cette discrétisation dans le cas d’un
maillage 2D cartésien. Dans ce cas particulier, les éléments
finis utilisés sont représentés dans la figure 30.
Remarque
• La contrainte de continuité du flux a été relâchée, tout en
conservant la continuité du courant dans la direction normale
à l’interface ;
• il est possible de démontrer l’équivalence des approximations
de type « différences finies » aux centres des mailles et
« éléments finis » mixtes d’ordre 1, à condition d’intégrer
numériquement (intégration de Gauss-Lobatto) les intégrales
qui interviennent dans la formulation discrète.
Fig. 31. Couplage des inconnues courant en géométrie cartésienne
2D.
Fig. 32. Représentation schématique des flux calculés
à une interface UOX/MOX.
Flux réel
Flux calculé avec une formulation primale
Flux calculé avec une formulation mixte
MOX
UOX
La résolution du problème discret s’effectue sur l’inconnue
« courant » après élimination de l’inconnue « flux » qui est
interne à la maille. Dans le cas de maillages réguliers, cartésiens
, voire hexagonaux, cette résolution peut être itérative,
comme montré dans la figure 31. De surcroît, cette méthode
se prête à une vectorisation efficace des calculs.
Du fait du relâchement de la contrainte de continuité du flux,
il est possible de rajouter des contraintes physiques de
« saut » du flux aux interfaces. L’utilisation des ADF* (facteurs
de discontinuité*), en particulier à l’interface d’assemblages
UOX et MOX, permet alors de modéliser la discontinuité
du flux.
La figure 32 schématise un flux réel (issu d’un calcul de transport
fin effectué par un code de réseau), un flux calculé par
une méthode aux éléments finis d’ordre 2 en formulation primale
, qui est continu à l’interface mais qui ne respecte pas la
valeur moyenne du flux réel et un flux calculé par une méthode
aux éléments finis d’ordre 2 en formulation mixte, qui est discontinu
à l’interface, mais qui respecte mieux la valeur
moyenne du flux réel.

## La discrétisation en angle et en espace pour un groupe d’énergie donné

Pour le calcul du flux angulaire dans un groupe donné, les discrétisations
en angle et en espace interviennent simultanément.
Dans ce cadre, nous allons présenter la méthode des éléments
finis et la méthode des caractéristiques. On suppose pour simplifier
, que les sections efficaces sont constantes en espace.
La méthode des éléments finis est particulièrement adaptée
aux géométries non structurées.
Fig. 30. Éléments finis mixtes Raviart-Thomas d’ordre 1, 2 et 3 en
géométrie cartésienne (• : inconnue flux, •→: inconnue courant).

<!-- page 81 (PDF 39) -->
La méthode des caractéristiques, qui exploite le comportement
hyperbolique de l’équation du transport, est beaucoup
utilisée pour les calculs d’assemblage, où l’on veut traiter des
géométries non structurées (les crayons dans un réseau, les
tubes guides, etc.), sans pour autant passer par un maillage,
ce qui demanderait un grand nombre de mailles pour respecter
les volumes fissiles (on sait qu’au premier ordre, une erreur
de 1 % dans le volume du crayon peut induire une erreur de
l’ordre de 1 000 pcm sur le C□LL).

### La méthode des éléments finis

On considère à présent l’équation de transport à source dans
un groupe donné :
(22)
où  ()□, □
→) regroupe les termes source de l’équation.
On peut écrire deux formulations variationnelles du problème
de transport à source, l’une du second ordre se rapprochant
de la formulation variationnelle obtenue pour l’équation de la
diffusion, l’autre du premier ordre issue de l’équation (22).

### La formulation paire de l’équation de transport

On suppose dans ce paragraphe que l’équation de transport
est déjà discrétisée en angle via la méthode SN.Les équations
sont donc écrites pour une suite discrète de valeurs de □
→.
Nous avons décrit précédemment les méthodes aux « éléments
finis » de résolution d’une équation du second ordre,
l’équation de la diffusion.
Une façon simple de se ramener à ce type d’équation est de
définir les inconnues suivantes :
dénommées respectivement « flux pair » et « flux impair ».
En écrivant l’équation de transport pour les directions □
→et –□
→
et en sommant (resp. soustrayant) ces deux équations, on
peut écrire le système d’équations, appelé « formulation pairimpair
» :
La deuxième équation du système permet d’éliminer le flux
impair et de se ramener à la « formulation paire » du système
:
Cette équation est du second ordre, et les méthodes primales
aux « éléments finis » permettent de calculer une approximation
du flux pair.
La résolution itérative sur les directions est généralement
accélérée par une méthode dite d’« accélération synthétique
» qui permet de calculer une estimation d’erreur entre
deux itérations par résolution d’une équation de la diffusion.
Cette formulation paire de l’équation du transport rend naturelle
l’équation de la diffusion synthétique associée.
Remarque
Il est possible de définir également une formulation mixte de
l’équation de transport en conservant le flux impair comme
inconnue, inconnue scalaire dans ce cas, alors qu’elle est vectorielle
(le courant) dans le cas de la diffusion. Cette dernière
formulation n’apporte pas d’amélioration quant à la résolution.

### La méthode des éléments finis discontinus

Des méthodes aux « éléments finis » ont été également développées
pour les équations aux dérivées partielles du premier
ordre, comme l’équation du transport. L’une de ces méthodes
est fondée sur des « éléments finis » discontinus aux interfaces
des mailles. Associée à l’approximation SN, cette
méthode a l’avantage de pouvoir bénéficier d’une résolution
maille par maille qui ne nécessite pas la construction, et donc
la résolution, du système global sur toutes les inconnues.
La formulation variationnelle du problème (2) s’écrit :
Trouver = ∈V (ℛ) tel que :
où V est l’espace de Sobolev des fonctions L2 intégrables ainsi
que leurs gradients.
L’absence de continuité du flux impose le choix de la discrétisation
. La méthode des « éléments finis » discontinus consiste
à écrire le flux sur chaque maille K comme un polynôme, sans
imposer la continuité du flux aux interfaces entre deux mailles
adjacentes.
La formulation discrète s’écrit sur la maille K :
Γ□ représente une quelconque face « éclairée » de la maille
(voir fig.33), n□□ est la normale à Γ□, w est une fonction de base,
c’est-à-dire un polynôme dont le degré dépend de l’ordre d’approximation
demandé.Le flux sur les faces des mailles n’étant
pas défini, l’intégrale de surface fait intervenir le saut de discontinuité
du flux sur les faces éclairées : =□
+ est le flux amont

<!-- page 82 (PDF 40) -->
(choix « upwind ») supposé connu, et =e
– est le flux inconnu
de la maille K restreint à la face Γe.
Ces équations sont résolues successivement sur chaque
maille selon un front de propagation propre à chaque direction
□
→.
À titre d’illustration, supposons le domaine ℛmaillé en triangles
. La direction □
→est une direction fixée par la méthode
SN. On suppose une approximation linéaire du flux (l est un
polynôme de degré au plus 1). Sur ABC (fig. 33), le flux =
s’écrit :
Il s’agit de calculer les trois flux =
–, =b
–, =c
–. La résolution a
déjà été faite sur les deux triangles dont les côtés sont en pointillés
. Les flux amont sont les flux évalués aux points bleus et
rouges. Pour calculer les flux aux sommets du triangle ABC,
on résout donc un système de trois équations à trois inconnues.
Remarque
• Il est possible d’écrire une formulation variationnelle de
l’équation de transport dans un espace où le flux est continu.
Il a cependant été démontré que la résolution souffre de problèmes
d’oscillations.
• Il est possible de paralléliser la méthode de résolution, car
les calculs sont locaux à la maille et les directions peuvent
être traitées indépendamment les unes des autres moyenant
une méthode itérative ;
• la méthode d’ordre C converge en O (ℎC+1/2) vers la solution
exacte ; on rappelle que les méthodes aux éléments finis
décrites précédemment convergent en O (ℎC+1).
Comme pour la résolution de la forme paire de l’équation, l’itération
sur les directions angulaires est accélérée en résolvant
un problème de diffusion. Pour assurer la cohérence de l’approximation
des deux problèmes, transport et diffusion, une
méthode aux « éléments finis » discontinus est utilisée pour
le problème de la diffusion.
La forme variationnelle du problème de diffusion associé :
Comme les flux ne sont pas définis sur les faces, les intégrales
de surface font intervenir les opérateurs [] et {} qui sont, respectivement
, le saut et la moyenne :
La première intégrale de surface est un terme de stabilisation
avec un paramètre de pénalisation α. La troisième intégrale
est un terme de symétrisation de la matrice.
Le paramètre α est estimé en fonction des propriétés physiques
des mailles, de part et d’autre de l’interface.

### La méthode des caractéristiques

En mathématiques, la méthode des caractéristiques est une
technique résolvant des équations aux dérivées partielles du
premier ordre qui, en reformulant le problème dans un système
de coordonnées curvilignes, identifie des courbes que
l’on appelle « courbes caractéristiques » ou tout simplement
« caractéristiques », le long desquelles l’équation aux dérivées
partielles dégénère en une équation différentielle ordinaire
.
Sa discrétisation en fait une technique numérique particulièrement
bien adaptée à la résolution des équations aux dérivées
partielles de type transport ([3], [4], [5], [6]). Elle est, en effet,
actuellement l’une des plus employées pour les calculs industriels
, car elle permet d’obtenir un bon rapport entre précision
et temps de calcul, tout en facilitant la description précise de
géométries complexes arbitraires (grâce à un maillage non
structuré) et en assurant une solution rigoureuse (en prenant
en compte des conditions aux limites très générales et un
ordre d’anisotropie de choc quelconque). Cette méthode est
disponible dans les codes APOLLO2 et APOLLO3 du CEA [7].
Elle a fait l’objet, au CEA, de nombreux travaux récents ([8],
[9], [10]) sur lesquels s’appuie cette description. La méthode
des caractéristiques est couramment utilisée dans le cadre du
schéma multi-niveau APOLLO2-A mis en œuvre par AREVA,
en partenariat avec le CEA pour le calcul industriel de réacteurs
à eau sous pression et à eau bouillante [11].
Fig. 33.Visualisation de la résolution sur le triangle ABC pour une
direction □
→donnée. Les faces « éclairées » sont les faces AC et AB.
=
–
=
+
=c
–
=c
+
=b
–
=b
+
A
B
C
□
→

<!-- page 83 (PDF 41) -->
La méthode des caractéristiques est exposée en deux dimensions
, en se plaçant à l’intérieur d’un groupe d’énergie T dont
l’index est omis afin de simplifier les notations.Dans ce groupe,
l’équation intégro-différentielle multigroupe de Boltzmann
s’écrit :
(23)
où q (r□, □
→) regroupe les termes de source de l’équation.

### Discrétisation en espace et en angle

La méthode des caractéristiques repose sur une discrétisation
spatiale en régions homogènes et une discrétisation
angulaire en ordonnées discrètes (fig. 34).
Variable spatiale : le domaine géométrique D, sur lequel
l’équation (23) est résolue, est décomposé en un ensemble de
I régions homogènes D4 constituant un maillage non structuré.
On suppose que les sections efficaces et les termes sources
sont spatialement constants par région :
(24)
Variable angulaire : on rappelle que la formulation aux ordonnées
discrètes (SN) consiste à choisir un ensemble fini de
directions discrètes et de poids associés :
Les inconnues du problème deviennent les valeurs que le flux
angulaire prend en ces directions discrètes. De surcroît, l’intégration
angulaire d’une fonction L(□
→) arbitraire se fait en
employant la formule de quadrature :
Fig. 34. Méthode des caractéristiques : discrétisation en espace
et en angle.
S
□
→
k
□
→
⊥
P⊥k
Ak
Ii
k
¨
Di
P□
P□□
(25)
Pour chaque direction angulaire □
→, un ensemble de lignes
caractéristiques interceptant les frontières des régions discrétisées
du domaine fournit un ensemble discret de points entre
lesquels l’approximation de régions homogènes (24) peut être
faite.
Soit □
→la direction de la droite caractéristique C, □
→
⊥sa direction
perpendiculaire. Tous les points de la droite caractéristique
C peuvent s’écrire sous la forme : )□ = P⊥k□
→
⊥+ P□
→où P⊥k
caractérise la trajectoire C et où s, qui représente l’abscisse
curviligne le long d’une courbe caractéristique, varie.Pour simplifier
, on note )□0k = s⊥k□
→
⊥.
La forme caractéristique de l’équation de transport sur la droite
caractéristique C est la suivante :
(26)
Dans le cas des neutrons, les courbes caractéristiques sont
des lignes droites colinéaires à □
→.

### Intégration le long d’une caractéristique

Équation de transmission
Par intégration sur une région de calcul Di le long de la droite
caractéristique k, la solution analytique de l’équation caractéristique
(26) en un point quelconque )□0k + P□
→s’obtient en fonction
de la solution analytique au point d’entrée )□0k + s□□
→par
l’équation suivante :
(27)
où le parcours optique τ (s1) est défini de la manière suivante :
(28)
D’après l’hypothèse (24) stipulant que les sections efficaces et
le terme source q sont spatialement constants dans la région
de calcul D4, l’équation (27) devient :
(29)
En choisissant comme point courant le point de sortie
()□0C + s□□□
→) de la région D4, on peut donc écrire :
(30)

<!-- page 84 (PDF 42) -->
où I4
k = s□□ – s□
L’équation (30) est appelée « équation de transmission».
Équation de bilan
Pour obtenir une information moyenne sur l’ensemble de la ligne
caractéristique, il suffit de « moyenner » l’équation (29) sur le
parcours optique en faisant varier s entre s□ et s□□ pour obtenir:
(31)
Cette équation, appelée « équation de bilan», permet d’obtenir
des valeurs de flux « moyennées » le long d’une trajectoire
, tout en garantissant de manière exacte la conservation
du nombre de neutrons dans le système.

### Intégration transverse

Pour traiter la coordonnée transverse s⊥, nous devons définir,
pour chaque direction □
→un maillage dans la direction transverse
. Une fois ce maillage défini (mailles Ak sur la figure 34),
nous traçons l’ensemble des trajectoires C de direction □
→passant
par le centre des mailles transverses. L’ensemble des trajectoires
ainsi obtenues est appelé « traçage ».
Il est important de noter que le traçage ne contient que des
données géométriques : angle de propagation, liste des
régions traversées et longueurs d’intersections correspondantes
. Cette étape n’est réalisée qu’une fois et contient toutes
les informations géométriques nécessaires au solveur.
Les équations précédentes (30) et (31) permettent d’obtenir
les variations du flux angulaire le long d’une ligne caractéristique
de direction □
→. Pour obtenir le flux angulaire moyen sur
l’ensemble des régions, il faut prendre en compte la variable
transverse s⊥le long de □
→
⊥, direction perpendiculaire à □
→.
Sur la région discrétisée Di de volume Vi, le flux angulaire
moyen ψ© 4 s’exprime comme :
L’approximation de cette intégrale se fait à l’aide d’une formule
de quadrature obtenue en considérant un ensemble de trajectoires
parallèles recouvrant la région considérée. Le volume
D4 (fig. 34) est balayé par un ensemble de lignes C qui définissent
un tuyau d’aire transverse AC, de longueur Ii
k, de flux
moyen sur la ligne ψ© 4
k La valeur moyenne ψ© 4 sur la région D4
peut donc être approchée par la formule suivante :
(32)
La sommation est faite sur les lignes caractéristiques C qui
sont parallèles à □
→et qui interceptent la région D4.

### Conditions aux limites

Il existe deux types de conditions aux limites fréquemment
appliquées lors du calcul d’un assemblage de réacteur, selon
que l’on considère la frontière du domaine comme ouverte ou
fermée. Une frontière est considérée comme ouverte, lorsque
des neutrons peuvent s’échapper du domaine par au moins
une des zones délimitant la frontière. On parlera dès lors de
« trajectoires ouvertes » (simples ou composées), lorsque la
La méthode des probabilités de collision et la méthode des caractéristiques
Par contre, l’équivalence entre les méthodes des probabilités de
collision et des caractéristiques n’est pas exacte en géométrie
2D xy. Ici, la méthode des probabilités de collision utilise des
fonctions spéciales, les fonctions de Bickley-Naylor, qui intègrent
exactement la dépendance sur l’angle polaire, tandis qu’avec la
méthode des caractéristiques, cette dépendance est résolue par
intégration numérique sur cet angle.Néanmoins, la méthode des
probabilités de collision ne s’applique qu’à des problèmes avec
choc isotrope et a donc besoin d’une correction du transport qui
introduit une approximation difficilement contrôlable. En outre,
elle conduit à un système algébrique qui nécessite l’inversion
directe, et donc coûteuse, d’une matrice par groupe d’énergie.
Tous ces inconvénients font que la méthode des probabilités de
collision est employée seulement pour des problèmes avec relativement
peu de régions et, souvent, avec des approximations
dégradées (approximation multicellule*). La méthode des
caractéristiques reste donc le candidat idoine pour des grands
calculs ou pour des calculs où l’anisotropie de la collision est
importante.
La méthode des probabilités de collision résout, dans chaque
groupe d’énergie, l’équation intégrale en variable spatiale pour
le flux scalaire. Cette méthode utilise l’approximation de flux plat
par région. Elle fournit une matrice qui relie les sources aux flux
scalaires par région, et dont les éléments peuvent s’interpréter
comme des probabilités de collision. Comme pour la méthode
des caractéristiques, le calcul de cette matrice utilise un traçage
de trajectoires parallèles pour un ensemble fini de directions
angulaires, et l’on montre que, pour la même partition en régions
et les mêmes trajectoires, les méthodes des probabilités de collision
et des caractéristiques donnent le même résultat pour des
géométries 3D. On conclut que :
• La méthode des caractéristiques peut se voir comme une résolution
itérative de la méthode des probabilités de collision ;
• l’idée courante selon laquelle la méthode des probabilités de
collision ne fait pas d’hypothèse sur les flux angulaires est
fausse.

<!-- page 85 (PDF 43) -->
Fig. 35. Méthode des caractéristiques : trajectoires ouverte et cyclique.
Trajectoire cyclique (b)
Trajectoire ouverte (a)
Conditions aux limites
Réflexion spéculaire
Réflexion spéculaire
Conditions aux limites
[11] K.S SMITH, J.D. RHODES, “CASMO-4 Characteristics methods for
two dimensional PWR and BWR core simulations”, Trans Am. Nucl.
Soc., vol. 83, pp. 294-296, 2000.
[12] R. SANCHEZ, L. LI MAO, S. SANTANDREA: “Treatment of boundary
conditions in trajectory-based deterministic transport methods”,
Nuclear Science and Engineering, vol. 140, pp. 23-50, 2002.
[13] R. SANCHEZ, I. ZMIJAREVIC, M. COSTE-DELCLAUX, E. MASIELLO,
S. SANTANDREA, E. MARTINOLLI, L. VILLATTE, N. SCHWARTZ, N. GULER,
“APOLLO2 year 2010”, Nuclear Engineering and Technology, vol. 42,
n°5, pp. 474-499, October 2010.
[14] F. FÉVOTTE, Techniques de traçage pour la méthode des caractéristiques
appliquées à la résolution de l’équation de transport des neutrons
en domaines multidimensionnels, rapport CEA-R-6212, février
2009.
[15] G. GRASSI, Conception de nouveaux schémas multigrilles appliquées
à la méthode des caractéristiques pour la résolution de l’équation
de transport des neutrons, rapport CEA-R-6211, février 2009.
[16] S. SANTANDREA, J.-C. JABOULAY, P. BELLIER, F. FÉVOTTE, H. GOLFIER,
“Improvements and validation of the linear surface characteristics
scheme”, Annals of Nuclear Energy, vol. 36, pp. 46-59, 2010.
[17] E. MARTINOLLI et al., “APOLLO2-A – AREVA’s new generation lattice
physics code: methodology and validation”, Proc Int Conf on
Advances in Reactor Physics to Power the Nuclear Renaissance
(PHYSOR 2010), Pittsburgh, PA, USA, May, 9-14, 2010.
□Bibliographie
Formalisme d’autoprotection
LIVOLANT (M.), JEANPIERRE (F. ), Autoprotection des résonances dans
les réacteurs nucléaires, Rapport CEA-R-4533-1974.
GRANDOTTO-BIETTOLI (M.), AUTOSECOL, Un calcul automatique de
l’autoprotection des résonances des isotopes lourds, Note CEA-N-
1961, 1977.
WILLIAMS (M.L.), “Correction of Multigroup Cross-Sections for Resolved
Resonance Interference in Mixed Absorbers”, Nuclear Science and
Engineering, 83, pp. 37-49, 1983.
RIMPAULT (G.), GRIMSTONE (M.J.), “Validation of New Subgroup
Algorithms
for
Resonance
Self-Shielding
in
Heterogeneous
Structures”, Proc. Int.Top. Meet. on Advances in Nuclear Engineering
Computation and Radiation Shielding, Santa Fe, New Mexico, USA,
April 9-13, 1989.
REUSS (P.), Théorie de l’absorption résonnante des neutrons, Note
CEA-N-2679-1991.
SANCHEZ (R.), Module d’autoprotection du code APOLLO2, Note CEA
N- 2765-1994.
BOULAND (O.), Amélioration du calcul de l’autoprotection des résonances
résolues par un traitement quasi-exact du ralentissement des
neutrons, Thèse de doctorat, Université Paris XI, Orsay, 1994.
HÉBERT (A.), “The Ribon Extended Self-Shielding Model”, Nuclear
Science and Engineering, vol. 151, pp. 1-24, 2005.
COSTE-DELCLAUX (M.), Modélisation du phénomène d’autoprotection
dans le code de transport multigroupe APOLLO2, Rapport CEA
R- 6114, 2006.
frontière est ouverte et de « trajectoires cycliques », lorsque
la frontière est fermée (fig. 35). Un traitement approfondi de
ces conditions aux limites est disponible dans la référence [7].
□Références
[1] B. DAVISON, J. B. SKYPES, Neutron Transport Theory, Oxford,
Clarendon Press, 1957.
[2] J. J. DUDERSTADT, W. R. MARTIN, Transport Theory, New York, John
Wiley & Sons, USA, 1979.
[3] E.M. GELBARD, Simplified Spherical Harmonics Equations and their
Use in Shielding Problems, WAPD-T-1182 (Rev.1), Bettis Atomic
Power Laboratory, February 1961.
[4] G.C.POMRANING, “Asymptotic and variational derivations of the simplified
PN Equations”, Ann. Nucl. Energy, 20(9), pp. 623-637, 1993.
[5] E.W. LARSEN, J.M. MCGHEE, J.E. MOREL, “Asymptotic Derivation of
the Simplified PN Equations”, Proceedings of Topical. Meeting,
Mathematical Methods and Supercomputers in Nuclear Applications,
M&C+ SNA 93, Karlsruhe, Germany, April 19-23, 1993.
[6] P.S. BRANTLEY, E.W. LARSEN, “A variational derivation of the simplified
P3 approximation”, Proceedings of ANS Meeting on Mathematical
Models and Supercomputing for Nuclear Applications, Saratoga
Springs, New York, 1997.
[7] A.M. BAUDRON and J.J. LAUTARD, “MINOS: A Simplified PN Solver
for Core Calculation”, Nuclear Science and Engineering, 155(2),
pp. 250-263, February, 2007.
[8] A.M. BAUDRON and J.J. LAUTARD, “Simplified PN Transport Core
Calculations in the APOLLO3 System”, International Conference on
Mathematics and Computational Methods Applied to Nuclear Science
and Engineering, M&C 2011, Rio de Janeiro, RJ, Brazil, May 8-12,
2011.
[9] M. J. HALSALL, “CACTUS : a Characteristics solutions to the neutron
transport equations in complicated geometries”, AEEWR-1291, Atomic
Energy Establishment, UK, 1980.
[10] S. G. HONG, N. Z. CHO, “CRX : a code for rectangular and hexagonal
lattices based on the method of characteristics”, Annals of Nuclear
Energy, vol. 25, pp. 547-565, 1998.

<!-- page 86 (PDF 44) -->
HFAIEDH (N.), Nouvelle Méthodologie de Calcul de l’Absorption Résonnante
.Thèse de doctorat, Université Louis Pasteur Strasbourg I, 2006.
Méthode des éléments finis
LESAINT (P.) and RAVIART (P. A.), “On a Finite Element Method for
Solving the Neutron Transport Equation”, in Mathematical Aspects of
Finite Elements in Partial Differential Equations, p. 89, C. A. De Boor,
Ed., Academic Press, New York, 1974.
LAUTARD (J.J.), “New Finite Element Representation for 3D Reactor
Calculations”, ANS/ENS Meeting, Munich,Germany, April 1981.
L
a méthode des caractéristiques est présentée, pour la
première fois, par Georg Friedrich Bernhard Riemann,
en 1859, dans un article intitulé « Ueber die Fortpflanzung
ebener Luftwellen von endlicher Schwingungsweite » (« Sur la
propagation d’ondes planes d’amplitude finie dans l’air ») [1].Une
présentation en est faite par deux auteurs, H. M. Paynter et I. J.
Busch-Vishniac, dans la référence [2]. Cette méthode numérique
présente un caractère générique pour traiter des problèmes
linéaires ou non linéaires de propagation dans des milieux tant
solides que liquides ou gazeux.
Dans le domaine d’études relevant de la résolution de l’équation
du transport des neutrons, cette méthode a été introduite, pour
la première fois, en 1972, par le britannique J. R. Askew dans
son article « A characteristics formulation of the neutron transport
equation in complicated geometries » [3]. L’un des intérêts
de la méthode des caractéristiques est justement de permettre
une plus grande flexibilité dans la discrétisation spatiale (“flexibilité
géométrique”) devant être faite du système physique étudié.
Elle est particulièrement adaptée pour les maillages géométriques
dits « non structurés ». Elle est aussi intéressante pour
traiter le transport des neutrons dans des configurations physiques
où le phénomène de « streaming* » est important,
comme, par exemple, dans des géométries présentant des vides
ou une forte atténuation du flux neutronique.
L’implémentation de la méthode des caractéristiques dans les
codes de calcul de neutronique s’étend progressivement, ainsi
que le montre les revues critiques qui en sont faites, en 1980,
dans la référence [4] relative à M. J. Halsall, puis en 1981, dans
la référence [5] par R. E. Alcouffe et E. W. Larsen du Los
Alamos National Laboratory, aux États-Unis.
R. Sanchez est à l’origine de l’introduction de cette méthode
dans les codes de neutronique du CEA [6-7].Elle est aujourd’hui
couramment appliquée à la résolution de problèmes à deux
dimensions. Elle constitue l’une des méthodes de calcul de
réseau offertes aux ingénieurs neutroniciens par le code
APOLLO développé au CEA.
Aux sources de la méthode des caractéristiques
Georg Friedrich Bernhard
Riemann (1826-1866)
est un mathématicien allemand
ayant apporté une contribution
majeure à l’analyse
et à la géométrie différentielle.
L’étape suivante est sa généralisation à trois dimensions d’espace
.
□Références
[1] Abhandlungen der Gesellshaft der Wissenshaften zu Göttingen,
Mathematisch- physikalishe Klasse 8, pp. 43 -65 (1858-59).
[2] J. ACOUST, “Remarks on Riemann’s method of characteristics”,
Soc. Am. 84 (3), September 1988, pp. 813-821.
[3] Rapport technique AEEW-M 1108, Atomic Energy Establishment,
Winfrith United Kingdom, 1972.
[4] M.J.HALSALL, “CACTUS, a Characteristics Solution to the Neutron
Transport Equations in Complicated Geometries”, AEEW-R 1291,
Atomic Energy Establishment, Winfrith, Dorchester, Dorset, United
Kingdom, April 1980.
[5] A review of characteristic methods used to solve the linear transport
equation, LAUR-136, ANS/ENS Joint Topical Meeting,
Mathematical Methods in Nuclear Engineering, April 26-29, 1981,
Munich, FRG.
[6] R. SANCHEZ, A. CHETAINE, “A Synthetic Acceleration for a Two-
Dimensional Characteristic Method in Unstructured Meshes”,
Nuclear Science and Engineering, 136, pp. 122–139, 2000.
[7] R. SANCHEZ, L. MAO, S. SANTANDREA, “Treatment of Boundary
Conditions in Trajectory-Based Deterministic Transport Methods”,
Nuclear Science and Engineering, 140, pp. 23–50, 2002.
KAVENOKY (A.) and LAUTARD (J. J.), “State of the Art in using Finite
Element Methods for Neutron Diffusion Calculations”, ANS Topical
Meeting on Advances in Reactor Computations, Salt-Lake-City,
USA,1983.
LAUTARD (J.J.) and MOREAU (F.), “A Fast 3D Parallel Diffusion Solver
Based on a Mixed Dual Finite Element Approximation”, Int. Conf. on
Mathematical Methods and Supercomputing in Nuclear Applications,
Karlsruhe, Germany, 1993.
ERN (A.), GUERMOND (J.-L.), Theory and Practice of Finite Elements,
Springer, New York, 2004.

<!-- page 87 (PDF 45) -->
BERNADI (C.), MADAY (Y.), RAPETTI (F.), Discrétisation variationnelle de
problèmes aux limites elliptiques, Springer, New York, 2004.
BAUDRON (A.M.), LAUTARD (J.J.), “MINOS: A Simplified Pn Solver for
Core Calculation”, Nuclear Science and Engineering, vol. 155, number
2, pp. 250-263, February 2007.
GUÉRIN (P.), BAUDRON (A.M.), LAUTARD (J.J.), “Domain Decomposition
Methods for Core Calculations Using the MINOS Solver”, Joint
International Topical Meeting on Mathematics & Computations and
Supercomputing in Nuclear Applications, M&C +SNA 2007, Monterey
April 15-19, 2007.
WANG (Y.), Adaptive Mesh Refinement Solution Techniques for the
Multi-group
SN
Transport
Equation
Using
a
Higher-Order
Discontinuous Finite Element Method, PhD Thesis, Texas A&M
University, 2009.
HÉBERT (A.), Applied Reactor Physics, Montréal, Presses Internationales
Polytechnique, 2009.
MOLLER (J.Y.), Résolution de l’équation du transport des neutrons dans
les cœurs de réacteurs nucléaires par la méthode (Galerkin) des éléments
finis discontinus courbes, thèse de l’université Henri Poincaré,
Nancy, 2011.
MOLLER (J.Y.) and LAUTARD (J.J.), “MINARET, A Deterministic Neutron
Transport Solver for Nuclear Core Calculations”, International
Conference on Mathematics and Computational Methods Applied to
Nuclear Science and Engineering (M&C 2011), Rio de Janeiro, RJ,
Brazil, May 8-12, 2011.
Mireille COSTE-DELCLAUX, Cheikh M. DIOP, Franck GABRIEL,
Jean-Jacques LAUTARD, Christine MAGNAUD,
Fausto MALVAGI, Sylvie NAURY et Anne NICOLAS
Département de modélisation des systèmes et structures

<!-- page 88 (PDF 46) -->

