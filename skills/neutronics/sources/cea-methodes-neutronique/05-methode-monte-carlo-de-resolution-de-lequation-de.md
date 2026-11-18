# Méthode Monte-Carlo de résolution de l’équation de Boltzmann
<!-- source PDF pages 47-64 -->

<!-- page 89 (PDF 47) -->
# Méthode Monte-Carlo de résolution de l’équation de Boltzmann

L’approche probabiliste de type Monte-Carlo permet de
simuler la « réalité » à l’échelle microscopique pour remonter
aux grandeurs physiques macroscopiques : les neutrons sont
suivis individuellement et les événements considérés sont les
interactions auxquelles ils donnent lieu avec les différents
noyaux des atomes qui constituent le milieu traversé : diffusions
, capture, fission, réactions (n, 2n), etc.Cette suite d’événements
est désignée par le terme d’« histoire ». C’est en
simulant suffisamment d’histoires de neutrons que l’on peut
quantifier les grandeurs physiques macroscopiques d’intérêt.
La population de neutrons dans le cœur d’un REP en fonctionnement
normal produits par seconde est de quelque 1019.
La technologie actuelle ne permet pas encore de suivre autant
de particules. Avec un échantillon représentatif d’un milliard
(109) d’histoires, l’on détermine ainsi le facteur de multiplication
effectif d’un cœur de REP avec une précision statistique
de quelques pcm, et la puissance par assemblage à 1 % à un
écart-type.
La méthode de Monte-Carlo appliquée à la résolution de
l’équation du transport des neutrons est réputée « exacte »
car capable de reproduire « sans approximations » les phénomènes
d’interaction particule-matière (par opposition aux
modélisations des méthodes déterministes : par exemple, pas
d’approximation multigroupe) dans des systèmes physiques
de géométrie tridimensionnelle quelconque. La contrepartie
est cependant son « coût temporel » : la lenteur de la
convergence statistique de la simulation qui induit une
contrainte forte sur la taille des régions dans lesquelles les
résultats sont recherchés, même si, dans certaines situations,
il est possible d’obtenir une estimation du flux en un point de
l’espace.Pour cette même raison, dans le cadre des études de
neutronique, la résolution de l’équation de Boltzmann par la
méthode de Monte-Carlo se fait généralement en situation stationnaire
.
Les codes de transport des neutrons fondés sur la méthode
de Monte-Carlo simulent la propagation des neutrons à partir
des données nucléaires ponctuelles en énergie (sections
efficaces, transferts énergétiques et angulaires, spectres
d’émission de particules…) fournies dans les évaluations
internationales (voir supra, p. 21-38). C’est la raison pour
laquelle, on les qualifie souvent de codes de transport
Monte-Carlo à énergie continue et qu’ils ont acquis le statut
de code de transport de référence vis-à-vis des codes
de transport déterministes.

## Les principes généraux

L’application de la méthode de Monte-Carlo ([1], [2], [3]) pour
résoudre l’équation de Boltzmann s’appuie sur la forme intégrale
de celle-ci présentée supra, p. 55-57.
L’intérêt de cette forme intégrale est de faire apparaître les
opérateurs utilisés pour effectuer la simulation des histoires
des neutrons.
Avant d’exposer les principes généraux de l’application de la
méthode de Monte-Carlo à la résolution de l’équation du transport
, il est utile de rappeler la définition de deux grandeurs physiques
: la réponse d’un détecteur et la densité de collision.
La réponse d’un détecteur, notée ici R (), est l’expression
couramment utilisée pour spécifier une grandeur physique
d’intérêt (flux, un taux de réaction, par exemple) intégrée dans
une zone  circonscrite de l’espace des phases. Par définition
, R () s’écrit :
(1)
où ψ (-) est le flux angulaire des neutrons au point - de l’espace
des phases, défini par le triplet (), /, 
→), et sR (-) est la
fonction réponse ou sensibilité qui caractérise la grandeur
R () : sR (-) = 1 pour le calcul du flux et sR (-) = Σ (), /) pour
le calcul d’un taux de réaction macroscopique, par exemple.
La densité de collision des neutrons entrant en collision au
point P a pour expression :
(2)
où Σ (), /) = Σ (-) représente la section efficace neutronique
macroscopique totale au point ) et à l’énergie / du neutron.
Il est commode ici de réécrire l’expression donnant R () en
introduisant la densité de collision des neutrons entrant en collision
:
(3)
La forme intégrale de l’équation de Boltzmann (voir encadré
p. 57) peut être écrite avec la densité de collision ζ (-) sous
la forme compacte ci-après:
(4)
Les méthodes de la neutronique

<!-- page 90 (PDF 48) -->
où K (-→-) : est le noyau de l’opérateur intégral de transport
qui fait passer la particule du point - au point - de l’espace
des phases D couvert par le système physique étudié.
Cet opérateur intégral est le produit de deux opérateurs déplacement
et collision dont les noyaux sont notés respectivement
: T ()→), E, 
→) et C (), /→E, 
→→
→) :
• Le noyau de l’opérateur déplacement T ()→), E, 
→) :
(5)
avec : ) = ) + s
→.
En interprétant la section efficace macroscopique Σ (), /)
comme une densité de probabilité (probabilité d’interaction par
unité de longueur [en cm-1]) l’expression (5) s’interprète
comme le produit de la probabilité,
pour le neutron de ne pas avoir de collision sur le trajet de longueur
s par la probabilité Σ (), /) ds d’avoir une collision sur le
trajet élémentaire compris entre s et s + ds. Autrement dit,
s’interprète comme la
densité de probabilité pour le neutron de franchir la distance
s = |) – )| sans subir de collision et d’avoir une collision en ).
• Le noyau de l’opérateur collision : C (), /→E, 
→→
→)
(6)
où Σs (), /→/, 
→→
→) est la section efficace macroscopique
différentielle de diffusion des neutrons en énergie et en direction
.
• Q (-) représente les particules sources arrivant directement
en P sans avoir subi de collisions :
(7)
où DS désigne le domaine source dans l’espace des phases.

### La décomposition en série de Neumann

On montre que ζ (-) solution de l’équation intégrale (4) peut
être exprimée par un développement en série appelé
« décomposition en série de Neumann» :
(8)
dont chacun des termes ª< (-) a une interprétation physique
(voir fig. 36) :
ζ0 (-) = Q (-) est la contribution à ζ (-) des neutrons directement
issus de la source,
ζ1 (-) est la contribution à ζ (-) des neutrons ayant subi une
collision et une seule,
ζ2 (-) est la contribution à ζ (-) des neutrons ayant subi deux
collisions,
…
ζn (-) est la contribution à ζ (-) des neutrons ayant subi n collisions
et s’écrit :
(9)
pour < ≥1, les intégrations se faisant sur l’espace des phases.
On remarquera que le processus aléatoire de propagation des
neutrons est un processus discret de type markovien : l’état
de la particule à l’étape < est déterminé à partir de la connaissance
de son état à l’étape immédiatement antérieure (< – 1),
l’histoire d’une particule constituant une chaîne de Markov.
Cette décomposition ζ (-) de en série de Neumann, montre
donc que les histoires de toute longueur arrivant dans la zone
de résultat contribuent à la grandeur cherchée R ().
Elle conduit naturellement à la résolution de l’équation du
transport par la méthode de Monte-Carlo, c’est-à-dire en
simulant (sur ordinateur) la chaîne des événements constituant
l’histoire de chaque neutron source : diffusion, absorption
, multiplication, fuite hors du système physique étudié.
Fig. 36. Illustration de la décomposition en série de Neumann.
(n) : numéro d’ordre de la collision ou nombre de collisions subies
par un neutron issu de la région source, avant d’arriver dans la zone
résultat.
(1)
(2)
(n)
(3)
(0)
Zone de résultat
Région source

<!-- page 91 (PDF 49) -->
### La résolution de l’équation du transport par la méthode de Monte-Carlo

La résolution de l’équation du transport par la méthode de
Monte-Carlo consiste ainsi à :
a. Construire un processus statistique appelé « jeu » qui
reproduit, à partir d’une source, l’histoire des particules
émises représentée par un ensemble de trajectoires et de
collisions bornant chaque trajectoire (diffusion, absorption
…). On obtient alors une chaîne de sites d’événements
: P0, P1, P2, …, P<…
b. définir une variable aléatoire X () que l’on associe à la grandeur
cherchée R () : X () est appelée « estimateur » de
R ().Lorsque, au cours de son histoire, un neutron pénètre
dans la zone de résultat Z, on enregistre ce fait par l’attribution
d’une valeur ϖ à X ().Par exemple, en considérant l’expression
(3), si une interaction a lieu en un point P de Z,
alors on attribue à ϖ la valeur égale à :
.La quantité
ϖ est appelée « encaissement » ou « score ». Si, au
cours de son histoire, le neutron n’a pas pénétré la zone de
résultat, alors le score correspondant est ϖ = 0.
c. fixer des « règles du jeu », c’est-à-dire à définir les densités
de probabilité avec lesquelles les événements sont choisis.
Cela revient à choisir, pour les particules, leur parcours, la
nature de l’interaction subie, leur énergie et leur direction
après choc, dans le cas d’une diffusion. Cela est réalisé
aléatoirement et en conformité avec les caractéristiques
physiques de la source de particules et les lois physiques
qui régissent leurs interactions avec la matière. Les densités
de probabilité utilisées pour simuler l’histoire des particules
doivent être telles que E [X ()], espérance mathématique
de X (), satisfasse :
(10)
d. réaliser le jeu M fois de manière indépendante : on simule
M (I = 1, M) histoires de particules. Dans la pratique, on
simule N batchs (ou « lots » ou « cycles » ou « générations
») de M particules d’où résulte une estimation correspondante
X˜9() de R (), 9 = 1, N. La quantité X˜9() est
obtenue par la moyenne empirique :
(11)
où ϖI,9() est le score associé à l’histoire I du batch 9.
e. estimer la grandeur R () cherchée en appliquant la loi des
grands nombres (N doit être suffisamment grand). R () est
approchée par la moyenne empirique ­©N () des quantités
X˜9() :
(12)
Le théorème central limite stipule que les quantités X˜9() sont
distribuées selon une gaussienne et la variance
associée
à ­©N () est estimée sans biais par :
(13)
L’intervalle de confiance est défini par :
(14)
où  est un réel positif, c () étant calculé pour une densité de
probabilité gaussienne, compte tenu du théorème central limite.
Il est d’usage d’utiliser les valeurs suivantes de e et les valeurs
correspondantes de l’intervalle de confiance :
•  = ε­©N (), N() = 0,689 (68,9 % de confiance)
•  = 2ε­©N (), N() = 0,954 (95,4 % de confiance)
•  = 3ε­©N (), N() = 0,997 (99,7 % de confiance).
En particulier, dans le domaine de la sûreté-criticité, la valeur
calculée du facteur de multiplication effectif CLLest donnée a
minima à 3ε­©N ().
La figure 37, ci-dessous, schématise l’algorithme de la simulation
de l’histoire de particules (le jeu) se propageant dans la
matière.
Fig. 37. Algorithme général de principe de la simulation de l’histoire
d’une particule par la méthode de Monte-Carlo dans un milieu non
multiplicateur de neutrons.
Collision :
• Choix nucléide
• Choix interaction
Capture stérile
Fuite
Fin de l’histoire de la particule
Caractéristiques
après interaction :
• Choix direction
• Choix énergie
Frontière
Réflexion
Interface
de milieux
Parcours :
• Choix longueur
Émission :
• Choix position
• Choix énergie
• Choix direction

<!-- page 92 (PDF 50) -->
On peut effectuer deux types de simulations :
• Une simulation naturelle ou analogue qui utilise les lois
naturelles d’occurrence des phénomènes physiques auxquels
le neutron donne lieu ;
• une simulation non analogue, souvent nommée (maladroitement
) « simulation biaisée », qui utilise des lois non naturelles
d’occurrence des phénomènes physiques auxquels le
neutron donne lieu, offrant la possibilité d’obtenir un résultat
en un temps plus court que celui requis par la simulation analogue
, à variance égale (voir encadré, p. 102).

### Les lois de tirage des événements – construction du processus statistique

On a indiqué plus haut que la construction de l’histoire d’un
neutron s’effectue à l’aide d’un échantillonnage (voir encadré)
des événements successifs auxquels donne lieu ce neutron,
de sa naissance à sa disparition. Ce choix des événements
s’effectue à partir des lois de probabilité qui les régissent. Ces
densités de probabilité sont définies comme indiqué ci-après.
Le premier événement d’une histoire est la naissance d’un
neutron. Faire naître un neutron, c’est déterminer le point P0
de l’espace des phases appartenant à la zone source d’où on
le fait surgir. Ce point P0 est choisi à l’aide d’une densité de
probabilité L0 (P0) construite à partir de la distribution de la
source S0 (P0) normalisée sur son domaine de définition DS
dans l’espace des phases :
(15)
Dans la pratique la source se présente souvent comme un
produit de fonctions dépendant respectivement de l’espace,
de l’énergie et de la direction, voire du temps. Ces variables
sont donc successivement échantillonnées à l’aide des densités
de probabilité construites selon le principe énoncé cidessus
. Sont ainsi fixées les caractéristiques physiques initiales
du neutron requises pour amorcer sa propagation.
Le point P0 étant connu, on choisit le point suivant P1 de la
chaîne d’événements à l’aide de la densité de probabilité
L1 (P1) déduite du noyau de l’opérateur intégral de transport :
(16)
Et ainsi de suite : le point P4 de la chaîne d’événements est
choisi en connaissant le point P4–1 avec la densité de probabilité
L4 (P4) :
(17)
Dans la pratique, les densités L4 (P4) se présentent sous forme
factorisée, conformément aux expressions (5) et (6) : on effectue
le choix du parcours du neutron, puis le choix de l’interaction
et, s’il s’agit d’une diffusion ou d’une fission, celui des
caractéristiques du neutron réémis (direction et énergie).
L’expression (5) se prête directement à un échantillonnage
conduisant au choix du parcours du neutron entre deux collisions
successives.
Dans le cas d’une propagation dans un milieu homogène, la
loi du parcours (densité de probabilité) déduite de (5) prend la
forme simple suivante :
(18)
où s est la longueur du parcours. Cette longueur est échantillonnée
en inversant la fonction de répartition de la densité
(18) :
(19)
où ξ est un nombre aléatoire uniformément choisi entre 0 et 1
(voir encadrés, p. 93 et 94).
L’expression (6) relative au noyau de l’opérateur de collision
peut être explicitée de manière à faire apparaître les probabilités
des différents événements associés à une collision (voir
fig.37) : choix du nucléide, choix du type d’interaction, choix de
la direction et, éventuellement, de l’énergie du neutron après
diffusion, si l’interaction choisie est une diffusion. Considérant
un milieu constitué d’un mélange homogène de nucléides j,
le noyau de l’opérateur de collision s’écrit :
(20)
•σsj (/) : section efficace microscopique de diffusion totale à
l’énergie E relative au nucléide j.
•σj (/) : section efficace microscopique totale à l’énergie /
relative au nucléide j.
•σ4j (/) : section efficace microscopique de diffusion totale à
l’énergie / relative à la réaction nucléaire de type 4 (diffusion
élastique, diffusions inélastiques, [n, 2n], fission) sur le noyau
atomique j.
•Σ (), /) : section efficace macroscopique totale au point )
à l’énergie / relative au nucléide j.
•Σ (), /) = Σj Σj (), /) : section efficace macroscopique totale
du milieu de propagation des neutrons, mélange homogène
des nucléides j, au point ) à l’énergie /.
•ν4j : multiplicité des neutrons produits lors de l’interaction 4 sur
le nucléide j : réaction (n, 2n)… fission.
•L4 (E→E, 
→→
→) : densité de probabilité de renvoi en énergie
et en angle de la particule lors l’interaction de type 4 sur le
nucléide j.

<!-- page 93 (PDF 51) -->
L’intérêt de (20) est de faire apparaître les probabilités et densité
de probabilité suivantes, directement utilisées pour réaliser
la simulation Monte-Carlo :
•
: probabilité de choix du nucléide j.
•
: probabilité de non absorption (ou de survie) du neutron.
•
: probabilité de choix du type de diffusion.
• L4 (/→E, 
→→
→) : densité de probabilité de renvoi en énergie
et en angle de la particule lors de l’interaction de type 4 sur
le nucléide j.
Dans les trois premiers cas, on a affaire à des probabilités discrètes
.
Les encadrés ci-après décrivent respectivement le principe de
l’échantillonnage des événements et les générateurs de
nombres aléatoires utilisés.
On a donc :
d’où :
Par exemple, si Σ = 0,791 cm–1 et ξ = 0,8 alors s = 2,0347 cm.
Dans le cas de probabilités discrètes p4 associées à un
ensemble d’événements 4 possibles (par exemple, le type d’interaction
du neutron avec un nucléide donné), la sélection de
l’un d’entre eux s’effectue en identifiant l’intervalle de la fonction
de répartition dans lequel se trouve le nombre aléatoire ξ
uniformément échantillonné dans l’intervalle (0, 1). Par conséquent
, si 0 < ξ ≤p1 c’est l’événement 1 qui est choisi ; si
c’est l’événement 4 qui est choisi.
Par exemple, considérons les trois types d’événements induits
par un neutron, diffusion, capture stérile et fission dont les sections
efficaces macroscopiques respectives dans le milieu
considéré et à une énergie donnée sont :
• diffusion : Σs = 0,203 cm–1
• capture stérile : Σc = 0,381 cm–1
• fission : ΣL = 0,207 cm–1
Les probabilités associées à chacun de ces trois types de réactions
sont :
• diffusion : ps =
= 0,2566
• absorption : pc =
= 0,4817
• fission : pL =
= 0,2617
En adoptant l’ordre arbitraire suivant des interactions : diffusion
, absorption, fission :
• si la valeur échantillonnée de ξ a une valeur comprise entre
0 et ps = 0,2566, par exemple ξ = 0,11, alors c’est la diffusion
qui est sélectionnée ;
• si ξ a une valeur comprise entre ps = 0,2566 et ps + pc = 0,7383,
par exemple ξ = 0,71, c’est la capture stérile qui est choisie ;
• si, enfin, ξ prend une valeur comprise entre ps + pc = 0,7383
et ps + pc + pL = 1, par exemple ξ = 0,863, c’est la fission que
l’on simule.
ΣS
Σ
Σc
Σ
Σf
Σ
Échantillonnage d’une variable aléatoire
selon une loi de probabilité
Dans la pratique, comment choisir une valeur de la variable
aléatoire h conformément à sa densité de probabilité L(h) ?
On procède en deux étapes principales :
• Des générateurs de nombres aléatoires, uniformément répartis
sur l’intervalle (0, 1) de la droite réelle ont été mis au point
et rendus disponibles sur ordinateurs. Il s’agit, en réalité, de
nombres pseudo-aléatoires dont la qualité aléatoire depend
de la performance du générateur qui les produit. À l’aide d’un
générateur de nombres aléatoires approprié, un nombre
aléatoire ξ est donc choisi ;
• la densité de probabilité L(h) étant définie sur un segment
(, °) de la droite réelle, on établit la relation qui existe entre
le nombre ξ échantillonné sur l’intervalle (0, 1), selon une densité
de probabilité uniforme constante égale à l’unité et la
variable h distribuée sur l’intervalle (, °) selon la densité L(h).
Cette relation est obtenue en écrivant l’égalité des fonctions
de répartition :
Il existe une valeur de la variable h distribuée selon la densité
L(h) qui satisfait cette dernière égalité et qui s’obtient, en fonction
de ξ, en résolvant cette équation en h.
Prenons l’exemple du choix d’un parcours s d’un neutron se
déplaçant dans un milieu caractérisé par une section efficace
macroscopique Σ (en cm-1). La densité de probabilité associée
à ce parcours s est :

<!-- page 94 (PDF 52) -->
Un générateur de nombres aléatoires, ξ, est le moyen par lequel
il est possible d’échantillonner une variable aléatoire d’une densité
de probabilité donnée.Un générateur de nombres aléatoires
a pour fonction de choisir au hasard – ou presque – un nombre
réel dans l’intervalle (0, 1). Ainsi, les nombres délivrés par les
générateurs de nombres aléatoires sont qualifiés de pseudoaléatoires
, car ces générateurs ne sont pas (encore) en mesure
de reproduire parfaitement le hasard. La qualité d’un générateur
de nombres aléatoires est donc définie par sa capacité à reproduire
le hasard. Cette qualité est reflétée par une série de propriétés
dont la stochasticité et l’uniformité de la distribution des
nombres aléatoires produits, soumises à des tests appropriés
(tests de Marsaglia [1, 2, 3], tests de Knuth [4], tests de L’Écuyer
[5, 6, 7]...)
Il existe plusieurs sortes de générateurs de nombres aléatoires
disponibles sur ordinateurs :
• les générateurs congruentiels linéaires (Linear Congruential
Generator, LCG [8]), tels que le DRAND48 [9],
• les générateurs à registre à décalage à rétroaction tels que le
Generalised Feedback Shift Register (GFSR [10], [11], issu du
Multiplicative Lagged-Fibonacci Generator) ou le Mersenne
Twister (TGSFR) [12], [13],
• les générateurs à décalage (« shift register ») : SHR3 [14] (3-
shift random number generator)…
• le générateur « Blum Blum Shub » [15]…
Le code de transport MCNP-5 utilise un générateur de nombres
aléatoires congruentiel [16]. Le code de transport Monte-Carlo
TRIPOLI utilise les générateurs DRAND48 en mode de fonctionnement
mono-processeur, GFSR et Mersenne Twister en mode
de fonctionnement multiprocesseur ou parallèle.
Exemple du générateur congruentiel linéaire.
Le générateur congruentiel linéaire produit une suite de nombres
aléatoires ξ4 définie par la récurrence suivante :
X4+1 = (X4 + c) (mod I), 4 = 1, …, <,
•  : nombre entier positif choisi appelé le « multiplicateur »,
• c : nombre entier positif ou nul choisi appelé l’« incrément »,
• I : nombre entier positif appelé le « module »,
Le nombre aléatoire ξ4 à valeur réelle dans l’intervalle (0, 1), est
obtenu par la divison :
Ce processus itératif est amorcé par la donnée du premier terme
de la suite, X0 appelé la « graine » (seed, en anglais).
La suite (déterministe) ainsi définie de nombres aléatoires
(pseudo-aléatoires) possède une période à l’issue de laquelle
Générateurs de nombres aléatoires
la suite se reproduit à l’identique. La qualité d’un générateur de
nombres aléatoires s’apprécie aussi à la longueur de sa période
(celle-ci devant être suffisamment longue), à sa reproductibilité, à
sa portabilité, à sa rapidité.
À titre d’illustration, l’ordinateur IBM System/360 des années 70,
machine à 32 bits, proposait le générateur congruentiel de
nombres aléatoires suivant :
 = 75
c = 0
I = 231 – 1
X4+1 = 75X4 = 16807 X4
On montre que la période maximale de ce générateur est égale à
231 – 2, [17], [18].
Le tableau ci-dessous indique les périodes de générateurs de
nombres aléatoires utilisés dans les codes de calcul Monte-Carlo :
Générateur
de nombres
aléatoires
Période
Utilisation
DRAND48
Monoprocesseur
GFSR
2607 – 1
Multiprocesseurs
(simulations en parallèle)
Technique de parallélisation :
« Leap Frog »
MERSENNE
219937 – 1
Multiprocesseurs
TWISTER
(simulations en parallèle)
Technique de parallélisation :
utilisation d’un autre générateur
Le générateur Mersenne Twister tire son nom du mathématicien
français Marin Mersenne (1588-1648) ; un nombre premier de
Mersenne est un nombre premier pouvant se mettre sous la forme
2p – 1 où p est aussi un nombre entier premier.
Des recherches sont menées pour construire un générateur quantique
de nombres parfaitement aléatoires : Quantum Random
Number Generator, QRNG, [19].
Références
[1] G. MARSAGLIA, and A. ZAMAN, “A new Class of Random Number
Generators”, The Annals of Applied Mathematics, Vol. 1, no 3, 1991.
[2] G. MARSAGLIA, “Random numbers for C: The END?” electronic billboard
sci.crypt. random-numbers, January 20, 1999.
[3] G. MARSAGLIA, and W. W. TSANG, “The 64-bit universal RNG”,
Statistics & Probability Letters, vol. 66, no 2, 2004.
[4] D. E. KNUTH, The Art of Computer Programming, Massachusetts,
Addison-Wesley Reading, 1969.
[5] P. L’ECUYER, “Random number generation”, in W. Haerdle, J.E.
Gentle and Y. Mori, Handbook of Computational Statistics, Springer
Verlag, Chapter 2, pp. 35-70, 2004.
[6] L’ECUYER, R. SIMARD, “Test01: A C Library for Empirical Testing of
Random Number Generators“, ACM Transactions on Mathematical
Software, vol. 33, no 4, art. 22, August 2007.

<!-- page 95 (PDF 53) -->
### Le « poids » d’un neutron

Dans une simulation strictement naturelle (ou analogue) le
poids du neutron est égal à l’unité : un neutron représente un
neutron et on le comptabilise pour un lorsqu’il atteint la zone
de résultat.
Pour des raisons d’optimisation de temps de calcul, au lieu
de simuler explicitement l’éventualité de l’absorption d’une
particule, on préfère multiplier son poids valant l’unité au
départ de la simulation par sa probabilité de survie égale au
rapport de la section efficace de diffusion à la section efficace
totale,
, et ce à chaque collision.
Ce procédé justifie que le rapport
soit appelé « facteur
de capture implicite ».
Comme σsj (/) < σj (/), le poids l du neutron diminue au
fur et à mesure des collisions qu’il subit et tend vers zéro,
lorsque le nombre de collisions tend vers l’infini. En effet,
considérons, pour simplifier, le transport monocinétique dans
un milieu infini monoatomique. Dans ce cas, le poids du neutron
après < collisions s’écrit
.En faisant tendre
le nombre de collisions vers l’infini, on a :
Autrement dit, le neutron voit son « potentiel vital » et/ou
« potentiel d’information » décroître de collision en collision.
Pour un nombre de collisions suffisamment élevé, le neutron
n’apporte donc plus de contribution significative au résultat
cherché, et au regard du critère d’optimisation du temps de
calcul, on le fait disparaître par un procédé statistique adéquat
, appelé «roulette russe», lorsque son poids passe en
dessous d’un seuil fixé.
L’estimateur d’une réponse R () cherchée dépend donc du
poids du neutron.
L’application de cette technique de simulation fournit un premier
exemple d’une simulation qui n’est plus strictement naturelle
, puisque l’on ne simule pas explicitement la capture,
conduisant donc à réaliser une simulation non analogue.
Le tableau 12, page suivante, donne des ordres de grandeurs
de quelques-unes des caractéristiques de simulations relatives
au calcul du facteur de multiplication effectif des neutrons
[7] X. HUGOT, Y.K. LEE, “Verification Tool For Tripoli-4 Criticality Code
Validation”, Proceedings of ICNC’2007, St.Petersburg, p.453, 2007.
[8] D. H. LEHMER, “Mathematical methods in large scale computing
units”, in Proceedings of the Second Symposium on Large Scale
Digital Computing Machinery, Cambridge Harvard University Press,
pp. 141-146, 1951.
[9] DRAND48 Man, Page: http://manpagesfr.free.fr/man/man3/
drand48.3.html.
[10] T.G. LEWIS, W.H. PAYNE, “Generalized Feedback Shift Register
Pseudorandom Number”, Algorithm, Journal of the Association for
Computing Machinery, vol. 20, No 3, July 1973.
[11] S. ALURU, G.M. PRABHU, J. GUSTAFSON, “A random number generator
for parallel computers”, Parallel Computing 18, 1992.
[12] M. MATSUMOTO, T. NISHIMURA, “Mersenne Twister: A 623-dimensionally
equidistributed uniform pseudorandom number generator”,
ACM:Transactions on Modeling and Computer Simulations, Special
Issue on Uniform Random Number Generation, 1998.
[13] F. PANNETON, P. L’ECUYER, M. MATSUMOTO, “Improved Long-Period
Generators Based on Linear Recurrences Modulo 2”, ACM
Transactions on Mathematical Software, 32, pp. 1-16, 2006.
[14] G. MARSAGLIA, “Xorshift RNGs”, Journal of Statistical Software,
vol. 8, Issue 14, July 2003.
[15] L. BLUM, M. BLUM, and M. SHUB. “A Simple Unpredictable
Pseudo-Random Number Generator”, SIAM Journal on Computing,
vol. 15, pp. 364-383, May 1986.
[16] F. BROWN, Y. NAGAYA, The MCNP5 Random Number Generator,
LA-UR-02-3782, Los Alamos National Laboratory, American Nuclear
Society Winter Meeting, Washington DC, November 17-21, 2002.
[17] R.Y. RUBINSTEIN, Simulation and the Monte-Carlo Method, New
York, John Wiley & Sons, Coll. Wiley Series in Probability and
Mathematical Statistics, 1981, pp. 25-26.
[18] S.K. PARK, K. W. MILLER, “Random number generators: Good
ones are hard to find”, Communications of ACM, Computing
Practices, vol. 31, n° 10, October 1988.
[19] P. J. BUSTARD, D. MOFFATT, R. LAUSTEN, G. WU, I. A. WALMSLEY,
B. J. SUSSMAN, “Quantum random bit generation using stimulated
Raman scattering”, Optics Express, vol. 19, no. 25, pp. 25173-25180,
5 December 2011.

<!-- page 96 (PDF 54) -->
(résolution du problème à valeurs propres) dans une configuration
rencontrée dans les études de criticité du cycle du combustible
.
L’encadré ci-dessous montre qu’à une réponse donnée on
peut associer différentes formes mathématiques d’estimateur
dont le choix est dicté par leur « vitesse » de convergence vers
la valeur cherchée. Par exemple, dans un milieu peu dense
l’« estimateur corde » converge plus vite que l’« estimateur
collision ». Dans certaines situations, grâce à un « estimateur
ponctuel » (dénommé en anglais point kernel estimator), une
grandeur physique peut être calculée en un point de l’espace
des phases : c’est le cas des milieux vides ou très peu denses.
Tableau 12
Ordres de grandeurs relatifs à un benchmark de criticité
Ces simulations ont été effectuées sur un processeur Optéron à 1,8 GHz.
Nombre
Nombre total
Nombre
Nombre
Nombre
Précision
Temps
d’histoires
d’opérations
de tirages
de collisions
de tirages
statistique
de calcul
de particules
d’échantillonnage
par histoire
par histoire
par collision
4 106
20 pcm
900 s
tions efficaces (microscopiques ou macroscopiques) relatives
aux réactions considérées.
L’expression de l’estimateur collision montre qu’il n’est pas
défini pour un milieu vide, car alors, Σ = 0. Dans un tel milieu,
on aura recours à l’estimateur corde qui comptabilisera les longueurs
des traversées du volume V par les neutrons.
L’estimateur dit « ponctuel » est construit en considérant toute
collision comme une source secondaire de neutrons. Le terme
apparaissant dans l’expression de cet estimateur correspond
au flux sans choc au point de calcul engendré par une
source de neutron unitaire placée à une distance s.
L’estimateur « ponctuel » est adapté pour estimer des
réponses dans le vide ou dans des milieux de très faible densité
. A contrario, dans la matière, il soulève un problème de
singularité dû à son comportement en
, car un site de collision
peut se trouver très proche du point de calcul ou même
coïncider avec celui-ci [4], [5], [6].
Le facteur de multiplication effectif des neutrons peut aussi être
évalué avec différents estimateurs :
• lν : à chaque fission, on « encaisse » le nombre ν de neutrons
de fission produits.
•
: à chaque interaction sur un noyau fissile, le nombre
de neutrons de fission est comptabilisé.
• l9ΣL : à chaque parcours dans le milieu fissile
(de longueur ), on « encaisse » la valeur prise par cette
expression.
Estimateurs de grandeurs physiques
dans une simulation Monte-Carlo
Le tableau ci-dessous présente différents estimateurs du flux
et celui du courant de particules franchissant une surface
donnée :
Estimateurs volumiques du flux
Corde
l
Collision
Estimateur surfacique du flux
Estimateur (surfacique) du courant
l
Estimateur ponctuel du flux
l : poids du neutron avant collision.
 : parcours du neutron entre deux collisions.
Σ : section efficace macroscopique totale du milieu dans
lequel le neutron se propage à une énergie donnée /.
Σs : section efficace macroscopique de diffusion du milieu dans
lequel le neutron se propage à une énergie donnée /.
ΣL: section efficace macroscopique de fission du milieu dans
lequel le neutron se propage à une énergie donnée /.

→: est la direction de propagation du neutron.
< : normale à la surface considérée.
˜Σ : parcours optique entre le point de collision et le point de
calcul du flux :
où s est la distance entre le point de collision ) = ) – P
→et
le point de calcul ).
L’estimation volumique du flux est effectuée dans un volume V
donné de l’espace en « encaissant » (attribution du score) les
valeurs prises par les estimateurs correspondants, lors de
chaque événement se produisant dans le volume V. Les taux
de réaction sont obtenus en multipliant le score par les sec-

<!-- page 97 (PDF 55) -->
## Convergence statistique d’un calcul de transport par la méthode de Monte-Carlo

À un stade ou à un autre de leur réalisation, les études d’ingénierie
(calculs industriels de cœur, conception / optimisation
d’un réacteur, dimensionnement de protection, conception
d’un château de transport…) sont marquées par cette
exigence de calcul des grandeurs physiques d’intérêt avec la
meilleure précision possible obtenue en un temps le plus
réduit possible. Les codes de transport Monte-Carlo, dont le
caractère naturellement chronophage comparé aux méthodes
déterministes a été précédemment souligné, tentent de relever
ce défi par la mise en œuvre de diverses stratégies visant
à accélérer la convergence du calcul.

### Stratégies de simulation Monte-Carlo

Les deux exemples qui suivent permettent d’aborder la problématique
des stratégies de simulation Monte-Carlo en physique
des réacteurs nucléaires.

### Calcul de la distribution fine de puissance d’un cœur REP

Afin de pouvoir déterminer la distribution de puissance d’un
cœur de REP, l’utilisateur d’un code de transport Monte-Carlo
définit des «volumes d’encaissement» en espace et en énergie
dans chacun desquels le flux de neutrons et les taux de fission
seront calculés.
Pour un REP, le nombre de volumes spatiaux est égal à :
nombre de crayons x nombre de couronnes combustibles x
nombre de pas axiaux. L’obtention d’une cartographie fine de
la puissance dans le cœur d’un REP nécessite de l’ordre de :
40 000 x 4 x 30 = 4,8 106 volumes (d’encaissements). Si l’on
veut estimer un flux multigroupe dans une structure à 300
groupes en énergie on aboutit à un nombre d’encaissements
de 40 000 x 4 x 30 x 300 = 1,44 109. Dans une simulation
Monte-Carlo, chacun de ces volumes doit être visité par un
nombre suffisant de neutrons afin de satisfaire la précision statistique
requise sur chacune des grandeurs physiques calculées
.
Ces chiffres sont à multiplier par le nombre de types de grandeurs
physiques à calculer, flux et taux de réaction. Si l’on
envisage un calcul en évolution temporelle isotopique avec
prise en compte de 200 nucléides pour faire une évaluation
du bilan matière dans un cœur, on multiplie encore ce nombre
d’encaissements, par exemple par un facteur 50 si l’on considère
50 pas de taux de combustion entre 0 et 60 000 MWj/t.
On comprend ainsi, qu’un nombre considérable d’histoires de
neutron devront être simulées pour obtenir la valeur de chacune
des réponses demandées avec une erreur statistique
acceptable et que le calcul d’un si grand nombre de
«réponses» aura bien entendu une incidence significative sur
le temps de calcul.

### Calcul d’atténuation du flux de neutrons dans les structures d’un réacteur nucléaire

L’atténuation d’un flux de neutrons par des écrans de matière,
de l’ordre de plusieurs décades (jusqu’à 14 décades) est illustrée
par la figure 39.
Dans de telles situations, l’atteinte de la convergence statistique
dans des temps de simulation « raisonnable » est souvent
illusoire, d’où le recours à des méthodes d’accélération de
la simulation.

### Convergence et facteur de qualité d’une simulation Monte-Carlo

On montre que la variance, %2, associée à une réponse calculée
varie comme l’inverse du nombre < de particules simulées:
(21)
Fig. 38. Exemple de modélisation d’un cœur neuf REP pour le code
de transport Monte-Carlo TRIPOLI-4®, de la cellule au cœur complet
constitué de ses différents assemblages de 17x17 crayons
combustibles.
-1
Fig. 39. Atténuation du flux sur 14 décades au bord d’un réacteur
(d’après A. Baur, Protection contre les rayonnements, aspects
physiques et méthodes de calcul, CEA, 1985, p. 12).
Cœur
Enveloppe
Cuve
Protection primaire
Bâtiment réacteur
R (mètres)
Logarithme du flux (unités arbitraires)

<!-- page 98 (PDF 56) -->
Par conséquent, pour diminuer la variance d’un facteur 10, il
faut simuler un nombre 100 fois plus élevé de neutrons. Le
temps de calcul sera augmenté dans les mêmes proportions.
Cela confirme que la méthode de Monte-Carlo appliquée en
simulation naturelle* (ou jeu analogue*) présente l’inconvénient
déjà signalé de converger « lentement ».
Plusieurs stratégies s’offrent à l’utilisateur pour obtenir les
résultats cherchés en un temps plus réduit :
• effectuer des calculs parallèles sur un réseau de machines
ou, bien sûr, une machine massivement parallèle (sur le
calcul haute performance, voir infra, p. 149-161) ;
• effectuer des calculs en deux étapes : calcul de référence au
cours duquel on stocke les informations pertinentes relatives
aux histoires de particules simulées, puis exploitation de ces
informations par une fonctionnalité appropriée du code
Monte-Carlo qui permet de faire des études paramétriques
sous certaines conditions ;
• utiliser les ordinateurs les plus puissants disponibles ;
• mettre en œuvre des techniques d’accélération de la convergence
, encore appelées «techniques de réduction de la
variance».
Ces stratégies sont résumées dans le tableau 13, en y indiquant
des ordres de grandeurs de leur efficacité respective.
Elles ne s’excluent pas l’une l’autre.La figure 40 montre la progression
approximative du nombre d’histoires de neutron pouvant
être simulées pour réaliser une étude avec le développement
des ordinateurs, passant d’environ 5 000 dans les
années 60, au milliard, au début des années 2000 et aux centaines
de milliards en 2013.
Les trois premières stratégies améliorent la qualité « extrinsèque
» de la simulation permettant d’obtenir des résultats statistiquement
suffisamment convergés en un temps plus réduit.
En reprenant l’exemple précédent d’un REP, une évaluation
approximative du temps de calcul requis pour obtenir par
simulation Monte-Carlo un taux de fission dans les volumes
élémentaires d’un crayon combustible avec une précision statistique
de 1 % serait d’environ 100 ans en utilisant un ordinateur
monoprocesseur cadencé à 2 GHz. Cette durée tomberait
donc théoriquement à environ une année avec une
centaine de processeurs utilisés en parallèle et à quelques
jours avec 10 000 processeurs.
La quatrième stratégie vise à améliorer la qualité « intrinsèque
» d’une simulation Monte-Carlo. De manière générale
la qualité d’une simulation Monte-Carlo se mesure à l’aide
d’une grandeur appelée « figure of merit » (FOM), définie par
la relation :
(22)
où , est le temps de simulation et %2 la variance. La qualité de
la simulation est d’autant meilleure, et donc la figure de mérite
d’autant plus grande, qu’une petite valeur de %2 est atteinte en
une durée (,) courte.
On remarquera que la figure de mérite, reste inchangée si on
ne fait qu’augmenter le nombre de particules simulées puisque
le temps de calcul et la variance sont respectivement proportionnel
et inversement proportionnel au nombre de particules
simulées.
Tableau 13
Stratégies de réduction des temps de calcul et d’amélioration de la qualité d’une simulation Monte-Carlo
Stratégie
Gain possible
Commentaire
Calcul parallèle
2 à 10 000
Proportionnel au nombre de processeurs.
Stockage information
Exploitation de l’information relative aux histoires de particules simulées
une fois pour toutes pour faire des études paramétriques ou bien des calculs
en reprise. Contrepartie : volume de stockage.
Progrès des processeurs
Application de la loi de Moore : la puissance des processeurs augmente
d’un facteur 2, tous les deux ans.
Techniques d’accélération
1 à 1015
Efficacité sur plusieurs décades dans les problèmes à forte atténuation
de la convergence
des neutrons.
La mise au point de ce type de techniques pour les calculs de criticité
est plus délicat, mais d’actualité.
IB M
C R A Y
FU JITSU
C C R T
Fig. 40. Évolution temporelle du nombre d’histoires de particules
simulées en fonction de l’accroissement de la puissance
des ordinateurs.
Années
Nombre de particules

<!-- page 99 (PDF 57) -->
### Quelques spécificités de la convergence d’un calcul critique

Un calcul critique*, tel qu’il a été défini
supra, p. 56 (équation 3), vise à déterminer
le facteur de multiplication*
effectif CLL, grandeur physique globale
relative à l’ensemble du système fissile
étudié. Comme dans l’approche déterministe
, on met en œuvre la méthode
de l’itération de la puissance dont le
principe est illustré par la figure 41, à
la fois pour un calcul déterministe (à
gauche) et un calcul probabiliste Monte-
Carlo (à droite).
La simulation Monte-Carlo s’effectue en
simulant des batchs successifs, un
batch d’ordre (< + 1) utilisant comme
source de neutrons les neutrons de fission
issus du batch précédent d’ordre
(<). La source initiale étant arbitraire, au
fur et à mesure que le nombre de
batchs de neutrons simulés augmente,
le système évolue vers une situation
d’équilibre.
Le facteur de multiplication effectif des neutrons n’est pas la
seule valeur propre satisfaisant l’équation critique. La convergence
du processus itératif de résolution de cette équation fait
intervenir les autres valeurs propres et vecteurs propres solutions
de l’équation critique. Ainsi que le montrent les relations
(23) et (24), ces modes propres (ou harmoniques d’ordre
supérieur) « contaminent » le mode fondamental, cependant
d’une manière qui décroît avec le nombre d’itérations. À l’itération
(< + 1), en se limitant à l’impact de la deuxième harmonique
, on a, en effet :
(23)
(24)
où :
C1 : est la première valeur propre correspondant à la valeur
exacte du facteur de multiplication effectif CLL,
C2 : est la deuxième valeur propre,
1 : est le premier vecteur propre correspondant au mode fondamental
.
Les expressions (23) et (24) indiquent que la convergence
dépend d’abord du rapport
des deux premières valeurs
propres de l’état critique, appelé « rapport de dominance » :
Fig. 41. Calcul du facteur de multiplication effectif, CLL, par la méthode d’itération de la
puissance. Algorithmes déterministe à un groupe d’énergie (à gauche, source : J.J. Duderstadt,
L. J. Hamilton, Nuclear reactor Analysis, John Wikey & Sons, 1976, p. 219) et probabiliste Monte-
Carlo (à droite).
Sous sa forme intégro-différentielle (à gauche) l’équation aux valeurs propres résolue est de la
forme
avec
et
. Q(0) représente la distribution (arbitraire)
de la source initiale de neutrons permettant d’engager le processus de résolution itératif.
M? =
F?
CLL
CLL
Mφ(n+1) =
Q(n)
Q(n+1) = F?(n+1)
< εa et
< εb
k(n+1) = Q(n+1)())d3)
Q(n)())d3)
k(n+1) – k(n)
k(n)
k(n)
k(n+1)
M = –.grad? + Σ?
Q(0) et k(0)
F = vΣL ?
S(n+1) – S(n)
S(n+1)
Q(0)
Échantillonage de Q
Stationnarité
Q = Q(n+1)
Fin
Fin
« Scoring » de keff et σ 2
σ 2 < σ0
Calcul de la distribution
des neutrons source
de fission Q(n+1)
Batch (<+1)
Itérations
NON
NON
NON
OUI
OUI
OUI
plus C2 est proche de C1 plus la convergence est lente, et, par
conséquent, plus le nombre d’itérations nécessaires pour
atteindre la convergence est élevé, ce qui est, par exemple, le
cas des systèmes physiques de grandes dimensions comme
les réacteurs nucléaires de puissance.
On constate également, sur ces mêmes expressions, que le
facteur de multiplication effectif converge « plus vite » que le
flux de neutrons (ou que la distribution de source des neutrons
qui lui est proportionnelle).
La figure 42 représente une configuration de calcul connue
sous le nom de « Calcul du CLL du monde » constituée d’unités
fissiles sphériques, celle du centre étant la plus réactive.
La figure 43 montre l’évolution de son CLL en fonction du
nombre de batchs, pour différentes distributions initiales de la
source de neutrons. On constate que l’atteinte de la convergence
est plus ou moins « rapide » selon le cas. L’estimation
du CLL est faite en « moyennant » les valeurs de CLL qui sont
obtenues pour chacun des batchs simulés après l’atteinte de
l’équilibre de la population des neutrons. L’atteinte de l’équilibre
ou atteinte de la stationnarité est le stade d’évolution de
la population des neutrons caractérisé par le fait que ceux-ci
ont « perdu la mémoire » des conditions initiales du calcul,
c’est à dire des conditions de leur naissance.
C2
C1
−⟶

<!-- page 100 (PDF 58) -->
La figure 44 montre un exemple d’histogramme des valeurs
du CLL obtenues par la simulation Monte-Carlo.
Afin de vérifier que la distribution des valeurs du CLL obtenues
à chaque génération suit bien une loi normale, plusieurs tests
statistiques sont aujourd’hui proposés dans les codes de
transport Monte-Carlo, tels ceux de Kolmogorov ou de Cramer
von Mises [8].
Vouloir améliorer la qualité de la simulation, au sens qui lui a
été donné plus haut, conduit à envisager la problématique de
la convergence d’un calcul critique par la méthode de Monte-
Carlo, sous trois angles :
• Le diagnostic de la stationnarité de la population des neutrons
dans le système fissile étudié ;
• le calcul sans biais du facteur de multiplication des neutrons
(CLL) et de leur distribution ainsi que des variances respectives
associées ;
• l’accélération de la convergence.

### La recherche de critères pertinents diagnostiquant l’atteinte de la stationnarité

Dans la méthode de l’itération de la puissance, les neutrons
de fission produits au cours du batch (<) constituent les neutrons
source du batch (< + 1), ce qui induit une corrélation
statistique entre l’ensemble des batchs simulés. L’enjeu de
l’atteinte de la stationnarité de la population des neutrons est
l’estimation sans biais du facteur de multiplication des neutrons
(CLL) et du flux des neutrons. Cette estimation sans
biais sera garantie si les conditions d’application du théorème
central limite sont réalisées, c’est-à-dire si les batchs
de neutrons sont statistiquement indépendants. Mais comment
détecter cette stationnarité ?
Des auteurs [9], [10], [11] ont proposé un critère entropique
de diagnostic de l’équilibre de la population neutronique dérivé
de la formulation microscopique qu’a faite Boltzmann de l’entropie
. À cette fin, un maillage spatial est défini sur la géométrie
du système et l’entropie, S, du système fissile considéré
est déterminée par :
(25)
où p4 représente le nombre de particules source dans une
maille 4 divisé par le nombre total de particules et Y le nombre
total de mailles. Cette entropie est calculée à chaque batch.
Lorsqu’elle se stabilise, la stationnarité est atteinte comme
l’illustre la figure 45 (page suivante).
1,05
1,10
1,15
1,20
1,25
Fig. 43. Convergence du CLL en fonction du nombre de batchs
et pour différentes configurations de la source initiale (arbitraire)
des neutrons : source initiale placée dans la sphère centrale la plus
réactive, source initiale placée dans une sphère située en périphérie,
source initiale uniforme dans toutes les unités fissiles.
Source initiale dans la sphère fissile centrale
Source initiale placée uniformément dans toutes les sphères
Source initiale placée dans une sphère fissile en périphérie
Keff
Nombre de batchs
1,08
1,1
1,12
1,14
1,16
Fig. 44. Exemple d’histogramme du CLL obtenu par la simulation
Monte-Carlo du système critique schématisé sur la figure 42.
L’histogramme obtenu après un nombre suffisant de cycles simulés
a la forme gaussienne attendue. Les cycles précédant l’atteinte
de l’équilibre ne sont pas pris en compte.
keff
Nombre de valeurs du keff comprises dans un intervalle
Fig. 42. Problème n° 4 du « OECD/NEA source convergence
benchmark (Whiteside’s problem, “CLL of the world”) » [7].
80 cm
U metal
R = 8,71 cm
U metal
R = 10 cm
Air

<!-- page 101 (PDF 59) -->
L’intérêt de ce critère fondé sur l’entropie est qu’il a un sens
physique et qu’il permet d’explorer l’ensemble de l’espace des
phases. Néanmoins, ce critère se révèle insuffisant, lorsque
l’on a affaire à des systèmes faiblement couplés neutroniquement
[12], à l’exemple d’un REP dont le rapport de dominance
est proche de l’unité, en raison de ses dimensions : le centre
du cœur et sa périphérie sont faiblement couplés. L’analyse
de la variance permet d’identifier la nature de la difficulté à
faire converger un calcul critique Monte-Carlo.

### Le calcul de la variance du keff et du flux de neutrons

Dans la pratique, la stationnarité parfaite n’est jamais atteinte.
Cela est dû à la corrélation entre cycles imposée par la
méthode de l’itération de la puissance qui induit une propagation
des fluctuations statistiques d’un batch aux suivants. Les
formules (11), (12) et (13) appliquées au calcul des valeurs
moyennes du CLL et du flux de neutrons, ainsi qu’aux
variances associées, ne sont plus appropriées, et l’on montre
qu’elles doivent être remplacées par des expressions prenant
en compte les différents modes propres du système fissile étudié
, au risque sinon d’introduire des biais significatifs dans les
estimations faites [13], [14]. En particulier, cette corrélation
étant positive, ne pas en tenir compte conduit à sous-estimer
la variance.Ces effets statistiques sont particulièrement importants
pour les systèmes neutroniques de grande taille, tels que
les REP pour lesquels le rapport de dominance est proche
de l’unité.Dans la pratique, afin de réduire l’impact de ces biais
sur les résultats, on s’assure que l’on a :
(26)
et que le nombre N est suffisamment élevé (N > 1 000).
Une réduction « raisonnable » de ces fluctuations statistiques
requiert donc de simuler un nombre suffisamment élevé de
particules par batch et de batchs.
Ces problèmes ont été identifiés et analysés de longue date
[13], [14]. La puissance des ordinateurs actuels et à venir
ouvrant la perspective de véritables calculs de cœur de réacteur
de puissance les ont remis sur le devant de la scène, et
plusieurs auteurs les ont revisités proposant des approches
calculatoires diverses de ces effets statistiques [8, 9, 12, 15,
16, 17, 18, 19, 20]… certaines implémentées dans les codes
de transport Monte-Carlo. L’une d’entre elles consiste à réaliser
des « paquets » de calculs de criticité indépendants [21]
dont on moyenne ensuite les résultats, conformément aux
relations (11), (12) et (13).

## Accélération d’une simulation Monte-Carlo

La question posée ici est : comment pallier la lenteur naturelle
d’une simulation Monte-Carlo ? C’est au moyen de techniques
d’accélération de la convergence encore dénommées techniques
de réduction de la variance que l’on estime une grandeur
physique (flux, taux de réaction, etc.) avec une figure de
mérite satisfaisante.

### Cas des calculs critiques

En criticité, la technique actuellement la plus usitée consiste à
initier le calcul de transport Monte-Carlo par une distribution de
source de neutrons pré-calculée par un code déterministe.Elle
permet de réduire efficacement la durée de la phase transitoire.
Des travaux récents et en cours visent un objectif plus ambitieux
, celui d’accélérer la convergence de la simulation, une fois
la stationnarité atteinte [18], [19].Entre autres approches explorées
, la méthode deWielandt (ou « de déflation ») est appliquée
à la simulation Monte-Carlo du transport des neutrons, consistant
à ramener le problème à résoudre à un problème dont le
rapport de dominance est plus petit, ce qui, comme nous l’avons
vu précédemment, favorise la vitesse de convergence de la
méthode de l’itération de la puissance mise en œuvre.

### Les techniques de biaisage en propagation

Un type particulier de techniques d’accélération, dénommées
« techniques de biaisage », consistent à modifier artificiellement
les lois physiques régissant l’interaction particule-matière
(probabilité de subir une collision sur un noyau donné, probabilité
de provoquer une réaction donnée, probabilité de réémission
à une énergie et dans une direction données lors
d’une diffusion, etc.), de manière à favoriser les événements
qui contribuent de manière significative au résultat cherché,
tout en minimisant la dispersion statistique de leurs contributions
. En contrepartie, l’estimateur associé à la grandeur physique
considérée s’en trouve lui aussi modifié, comme le
montre le court développement mathématique présenté dans
1,12
1,14
1,16
1,18
1,20
1,22
1,24
1,26
0,6
0,5
0,4
0,3
0,2
0,1
Fig. 45. Détection de la stationnarité de la source de neutrons par
un calcul de l’entropie de Boltzmann. On observe une stabilisation
relative de l’entropie pour un nombre de batchs de l’ordre de 50
(courbe du bas). L’estimation du CLL est alors faite en « moyennant »
les estimations obtenues pour tous les batchs à partir du 50e [11].
Keff
Entropie
Nombre de batchs
Nombre de batchs
(nombre de neutrons simulés par batch)
(nombre de batchs)

<!-- page 102 (PDF 60) -->
l’encadré ci-contre. Relevant du même principe de base, différentes
techniques de biaisage sont mises en œuvre dans
un code de transport Monte-Carlo, parmi lesquelles :
• La technique dite de « splitting-roulette » qui gonfle ou diminue
artificiellement la population de neutrons suivant les
zones où ils se trouvent ;
• la technique dite de la « transformation exponentielle » dont
le principe est exposé ci-après.
Le principe de la « transformation exponentielle », repose sur un
changement de variable qui fait passer du flux naturel = (-) au
flux biaisé =*(-), par l’intermédiaire d’une fonction O(-) arbitraire :
(27)
où P est un point de l’espace des phases (), E, 
→).
La fonction I (-) a pour rôle de définir les domaines de l’espace
des phases qui sont importants vis-à-vis du résultat cherché.
C’est pourquoi I (-) est appelée « fonction d’importance ».
En introduisant ce changement de variable dans la forme intégro
-différentielle de l’équation du transport, on obtient une nouvelle
équation qui régit le flux biaisé =*(-) et dont la forme est
similaire à l’équation du transport qui régit le flux de neutrons
= (-). Elle en diffère par les lois modifiées d’interaction particule
-matière, en accord avec le tableau 14 (page suivante).
La quantité
est parfois appelée « paramètre de
biaisage » et le vecteur
est dénommé « direction
d’intérêt », c’est-à-dire la direction dans laquelle il convient
de diriger les neutrons pour maximiser la figure de mérite.
La figure 46 permet d’illustrer le mécanisme de fonctionnement
de la transformation exponentielle.
Principe des techniques de biaisage
Le problème à résoudre revient formellement à calculer l’espérance
mathématique d’une grandeur physique Y définie par :
où ­ est une variable aléatoire estimateur « naturel » de Y et
T(­) la densité de probabilité associée à la variable aléatoire
X définie sur un domaine D.
Désignons par T*(­) une densité de probabilité arbitraire associée
à la variable aléatoire X. On peut écrire l’espérance
mathématique de Y comme :
Cela montre qu’il est possible d’estimer sans biais la grandeur
Y en construisant une chaîne d’événements avec une
densité de probabilité T*(­), différente de la densité de probabilité
naturelle T(­) pourvu que l’on prenne comme nouvel estimateur
sans biais de la grandeur ³ non plus ­ mais
.
Dans le contexte de la simulation du transport des neutrons
par la méthode de Monte-Carlo et en pratique, cela revient, à
chaque événement concerné, à multiplier (on dit aussi « corriger
») le poids du neutron (voir supra, p. 95) par la valeur
prise par le rapport
. La densité T*(­) est souvent
appelée ici «densité de probabilité biaisée».
Les vocables « biaisage », « biaisé », dérivés du terme anglais
« biaising » portent à confusion, car l’estimation faite ici avec
la densité biaisée T*(­) est rigoureusement sans biais.
La capture implicite est une illustration particulière de ce
changement de densité de probabilité associée à l’occurrence
d’un événement.
Le problème revient donc à trouver la densité T*(­) conduisant
à la meilleure qualité possible de la simulation, au sens de
la deuxième expression de l’espérance de Y, améliorant donc
sensiblement la figure de mérite de la simulation Monte-Carlo.
On montre que si l’on prend pour T*(­) une forme construite
avec la solution du problème adjoint (pour cela il faut résoudre
l’équation du transport adjointe, voir supra, p.58) alors on aboutit
à une simulation idéale où la variance sur le résultat est nulle :
cette simulation idéale est appelée « jeu à variance nulle ».
Cependant, le problème adjoint est au moins aussi complexe
à résoudre que le problème direct. Autrement dit, ce résultat
théorique ne peut être transposé tel quel dans la pratique. Sa
résolution, dans le cadre d’hypothèses simplificatrices (milieu
infini, particules monocinétiques…), inspire cependant des
formes efficaces de la densité biaisée T*(­).
Fig. 46. Accélération d’un calcul de propagation de particules par
la méthode de Monte-Carlo illustrée dans le cas de la propagation
de neutrons (ou de gammas) dans un mur de protection. Sur cet
exemple, la fonction d’importance I(-) a été choisie de telle sorte
que les surfaces d’équi-importance soient planes, la direction
d’intérêt 
→
0 leur étant, par définition, en tout point perpendiculaire.
Source de particules
Région
des résultats
Surfaces d’équi-importance planes

→

→

<!-- page 103 (PDF 61) -->
En effet, à la densité naturelle du choix du parcours s, L(s) on
substitue la densité biaisée L*(s). D’après l’expression de
6* (-), on constate que :
• L*(s) allonge en moyenne les parcours s lorsque les particules
vont dans la direction d’intérêt 
→
0 (-) :

→
0 (-).
→(-) > 0 et 6*(-) < Σ (-)
• L*(s) raccourcit en moyenne les parcours des particules qui
vont en sens inverse de la direction d’intérêt 
→
0 (-) :
et 
→
0 (-).
→(-) > 0 et 6*(-) < Σ (-)
Conformément à ce qui a été dit plus haut, le poids de la particule
devra prendre en compte ce changement de loi du tirage
Tableau 14
Caractéristiques du biaisage, dans le cas de la transformation exponentielle
Simulation naturelle
Simulation biaisée
Section efficace
totale
Densité
de probabilité
du parcours
Noyau
de l’opérateur
collision
du parcours, en étant multiplié par le rapport de la densité
naturelle L (s) à la densité modifiée L*(s) :
Les figures 47 et 48 permettent de visualiser l’efficacité de l’application
de cette technique d’accélération de la convergence
dans le cas d’un transport stationnaire à source fixe. Des travaux
récents proposent de la mettre en œuvre dans des calculs
critiques.
Fig. 47. Simulation naturelle ou analogue des neutrons naissant
dans le cœur du réacteur : les points figurent l’emplacement des
collisions subies par les neutrons.Trop peu de neutrons atteignent
les structures externes du cœur (la cuve, en particulier) pour pouvoir
évaluer avec une précision statistique acceptable la fluence
neutronique à laquelle elles sont soumises. Cette simulation a été
réalisée avec le code de transport Monte-Carlo TRIPOLI.
Fig. 48. Simulation non analogue ou « biaisée » des neutrons
naissant dans le cœur du réacteur : la répartition des points figurant
les sites des collisions subies par les neutrons montrent l’efficacité
de la transformation exponentielle qui « pousse » les neutrons vers
les zones d’intérêt, ici l’enveloppe et la paroi interne de la cuve du
réacteur nucléaire pour lesquelles on cherche à estimer la fluence
neutronique reçue. Cette simulation a été réalisée avec le code de
transport Monte-Carlo TRIPOLI.

<!-- page 104 (PDF 62) -->
[7] G. E. WHITESIDES, “A Difficulty in Computing the k-effective of the
World,” Trans. Am. Nucl. Soc., 14, pp. 680, 1971.
[8]Y. RICHET, “Suppression du régime transitoire initial des simulations
Monte Carlo de criticité”, Thèse de Doctorat, École des Mines de Saint-
Étienne, décembre 2006.
[9] T.UEKI, F.B.BROWN, D.K.PARSONS, D.E.KORNREICH, “Autocorrelation
and Dominance Ratio in Monte Carlo Criticality Calculations”, Nuclear
Science and Engineering, 145, pp. 279-290, 2003.
[10] T. UEKI and F. B. BROWN, “Stationarity Modeling and Informatics-
Based Diagnostics in Monte Carlo Criticality Calculations”, Nuclear
Science and Engineering, 149, pp. 38-50, 2005.
[11] E. DUMONTEIL, A. LE PEILLET, Y.-K. LEE, O. PETIT, C. JOUANNE, et
A. MAZZOLO, “Source Convergence Diagnostics using Boltzmann
Entropy Criterion. Application to different OECD/NEA criticality benchmarks
with the 3-D Monte Carlo code Tripoli-4”, Physor, 2006.
[12] E. DUMONTEIL, T. COURAU, “Dominance Ratio Assessment and
Monte Carlo Criticality Simulations :Dealing with High Dominance Ratio
Systems”, Nuclear Technology, 112, pp. 120-131, November 2010.
[13] R. C. GAST and N. R. CANDALORE “Monte Carlo Eigenfunction
Strategies and Uncertainties”, Proceedings of the NEACRP Meeting
of a Monte Carlo Study Group, ANL-72-2 (NEA-CRP-L-118), pp. 162,
1974 ; E.M. GELBARD, R.E. PRAEL, “Monte Carlo work at Argonne
National Laboratory”, Proceedings of the NEACRP Meeting of a Monte
Carlo Study Group, ANL-72-2 (NEA-CRP-L-118), p. 202, 1974.
[14] J. BRISSENDEN and A. R. GARLICK, “Biases in the estimation of k-eff
and its Errors by Monte Carlo Methods”, Annals of Nuclear Energy,
13, 2, pp. 63-83, 1986.
[15] T. UEKI, T. MORI, and M. NAKAGAWA, “Error Estimations and their
Biases in Monte Carlo Calculations”, Nuclear Sciences and
Engineering, 125, p. 1, 1997.
[16] L. DEMARET, A. NOURI, L. CARRARO, and O. JACQUET, “Accurate
Determination of Confidence Intervals in Monte Carlo Eigenvalue
Calculations”, Proceedings of ICNC’99, p. 66, 1999.
[17] Y. DUFEK, Development of New Monte Carlo Methods in Reactor
Physics – Criticality, Non-Linear Steady State and Burnup Problems,
PhD, Stockholm, Sweden, June 2009.
[18] P. David GRIESHEIMER and R. Brian Nease, “Spectral Analysis of
Stochastic Noise in Fission Source Distributions from Monte Carlo
Eigenvalue Calculations”, Progress in Nuclear Science and
Technology, 2, pp. 706-715, 2011.
[19] S. CHRISTOFOROU, J.E. HOOGENBOOM, “A Zero-Variance-Based
Scheme for Monte Carlo Criticality Calculations”, Nuclear Science and
Engineering, 167, pp. 1, 91-104 (2011) ; S. CHRISTOFOROU, A Zero-
Variance-Based Scheme for Monte Carlo Criticality Simulations, PhD,
Technische Universtiteit Delft, October 2010.
[20] F. X. HUGOT,Y. K. LEE, F. MALVAGI, “Recent R&D around the Monte-
Carlo code TRIPOLI-4 for criticality calculation”, Proceedings of
International PHYSOR-2008, CD ROM, Interlaken, Switzerland,
September 14-19, 2008.
[21] N. PETROV, N. P. KOLEV, G. TODOROVA, F.X. HUGOT, T. VISONNEAU,
“TRIPOLI-4
Solutions
of
VVER-1000
Assembly
and
Core
Benchmarks”, Proceedings of International Conference M&C 2009,
Saratoga Springs, New York, May 3-7, 2009.
Dans le code de transport Monte-Carlo TRIPOLI, la fonction
d’importance est construite automatiquement selon une
approche adjointe et en utilisant un algorithme de plus court
chemin issu de la théorie des graphes, l’algorithme de
Dijkstra [22], [23]. Plusieurs autres techniques de réduction
de la variance, comme la roulette russe et le splitting (fractionnement
de neutrons en plusieurs autres neutrons) sont
conjointement utilisées dans une même simulation. Des travaux
sont en cours visant à améliorer la performance des fonctions
d’importances I (-) en utilisant, pour les construire, des
techniques à base de réseaux de neurones* [24].

## Perspectives

Dans le cadre de la physique des réacteurs nucléaires, la
méthode de Monte-Carlo appliquée au transport des neutrons
permet de traiter aussi bien des problèmes de physique du
cœur (calcul de CLL, distribution de puissance dans le cœur…)
que ceux de radioprotection (calcul à source fixe : détermination
de flux, d’échauffements, de débits de dose…) engendrés
par la propagation des neutrons sur des distances variables
pouvant aller jusqu’à plusieurs centaines de mètres (« effet de
ciel », par exemple). Selon les mêmes principes, elle simule
la propagation des rayonnements gammas produits dans une
installation nucléaire. Par ailleurs, elle autorise, avec les avantages
qui lui sont spécifiques (calcul à énergie continue et à
trois dimensions), une simulation toujours plus fine de la réalité
physique («Up-scattering résonnant [25]), des calculs de
perturbation de paramètres physiques et / ou de propagation
d’incertitudes [26, 27, 28, 29] ainsi que le traitement du transport
en milieu stochastique [30]. Enfin, la puissance toujours
croissante des ordinateurs [31] ouvre la voie au traitement
Monte-Carlo de la cinétique [32], et des couplages entre phénomènes
physiques tels que le transport Monte-Carlo et l’évolution
des nucléides (voir encadré, infra, p.136-137) ou encore
le transport Monte-Carlo et la thermohydraulique cœur [33].

### Références

[1] N. METROPOLIS, S. ULAM, “The Monte Carlo Method”, Journal of the
American Statistical Association, 247, 44, pp. 335-34, 1949.
[2] I. LUX, L. KOBLINGER, Monte Carlo Particle Transport Methods :
Neutron and Photon Calculations, CRC Press, 1991.
[3] J.C.NIMAL, J.RASTOIN, Méthodes de Monte-Carlo, Note CEA-N 533,
avril 1965.
[4] H.RIEF, A.DUBI, T.ELPRIN, “Track Length Estimation Applied to Point
Detectors”, Nuclear Science and Engineering, 87, pp. 59-71, 1984.
[5] F.H. CLARK, “Variance of Certain Flux Estimators Used in Monte
Carlo Calculations”, Nuclear Science and Engineering, 27, pp. 235-
239, 1967.
[6] N. AUTHIER, J.P. BOTH, J.C. NIMAL, “New Photon Biasing Schemes
for the ’One-More-Collided-Flux-Estimator’s Method”, Nuclear Science
and Engineering, 137, pp. 146-155, 2001.

<!-- page 105 (PDF 63) -->
L
a notion de hasard est ancienne, comme en témoignent
les dés ci-contre remontant à la haute Antiquité. L’invention
de la méthode de Monte-Carlo est attribuée au naturaliste
Georges-Louis Leclerc, Comte de Buffon, qui proposa
une méthode probabiliste originale – passée à la postérité sous
la désignation : « expérience de “l’aiguille de Buffon” » – permettant
d’obtenir une estimation de la valeur du nombre S, [1].
Dans son mémoire, Buffon expose la problématique de son travail
mathématique : « L’Analyse est le seul instrument dont on
se soit servi jusqu’à ce jour dans la science des probabilités,
pour déterminer et fixer les rapports du hasard ; la Géométrie
paroissoit peu propre à un ouvrage aussi délié ; cependant si
l’on y regarde de près, il sera facile de reconnoître que cet avantage
de l’Analyse sur la Géométrie, est tout-à-fait accidentel, et
que le hasard, selon qu’il est modifié et conditionné, se trouve du
ressort de la géométrie aussi-bien que de celui de l’analyse ;
… ».Il traite du problème ainsi posé en utilisant l’exemple du “jeu
du franc-carreau”. C’est dans la seconde partie de ce mémoire
qu’intervient “l’aiguille de Buffon” : « Je suppose que dans une
chambre, dont le parquet est simplement divisé par des joints
parallèles, on jette en l’air une baguette, et que l’un des joueurs
parie que la baguette ne croisera aucune des parallèles du parquet
, et que l’autre au contraire parie que la baguette croisera
quelques-unes de ces parallèles ; on demande le sort de ces
deux joueurs. On peut jouer ce jeu sur un damier avec une
aiguille à coudre ou une épingle sans tête…»
Par la suite, les travaux des mathématiciens, ceux de G. F.
Cantor (1845-1918) sur la théorie des ensembles, de E. Borel
(1871-1956), H. Poincaré (1854-1912), A. A. Markov, H.
Lebesgue, A. N. Kolmogorov… sur les probabilités, les processus
aléatoires et sur la théorie de la mesure, d’une part, et
d’autre part, les travaux des physiciens J. C. Maxwell et L.
Boltzmann sur la théorie des gaz (voir supra, p. 48), ont été
déterminants pour déployer l’approche stochastique dans l’étude
des phénomènes physiques.
Avant qu’elle n’en portât le nom, la méthode de Monte-Carlo fut
initialement utilisée par E. Fermi à Rome pour étudier le ralentissement
des neutrons [2].
Cette méthode prend son essor, dans le contexte de la Seconde
Guerre mondiale – mise au point de la bombe atomique à Los
Alamos, aux États-Unis – et celui de l’avènement des premiers
calculateurs électroniques et ordinateurs. Son nom – méthode
de Monte-Carlo – serait le nom de code donné à un travail secret
effectué au centre de recherche atomique de Los Alamos dans
le Nouveau-Mexique, aux États-Unis. Elle sera développée par
J. von Neumann, S. Ulam et N. C. Metropolis [3, 4]. La
méthode de Monte-Carlo voit son utilisation s’étendre avec l’accroissement
continu de la puissance des ordinateurs qu’accompagnent
des ouvrages et des articles qui la présentent [5, 6, 7,
8, 9, 10, 11]. Le développement du code de transport de particules
(neutron, gamma, électrons…) Monte-Carlo américain
MCNP*, s’inscrit dans l’héritage direct des pionniers de la
méthode de Monte-Carlo [12]. En France, les tout premiers logiciels
de transport des neutrons par la méthode de Monte-Carlo
– ZEUS, POKER – sont écrits au CEA, dans les années 60 [7,
8, 9]. Leur successeur, TRIPOLI*, voit sa première version sortir
dans le courant des années 70 [13].
Quelques références historiques
[1] Comte de BUFFON, Essai d’arithmétique morale, dans Histoire
Naturelle générale et particulière, Supplément, Tome Quatrième, pp.
95-105, 1777 (http://www.buffon.cnrs.fr/). En fait, ce travail mathématique
avait été antérieurement soumis à l’Académie des Sciences
française : le samedi 25 avril 1733, les mathématiciens A. Clairaut et
P. L. Moreau de Maupertuis « ont parlé ainsi sur un mémoire présenté
par M. Le Clerc : “Nous avons examiné par ordre de
l’Académie un Mémoire sur le jeu du Franc Carreau par M. Le
Clerc…” » (http://gallica.bnf.fr/ark:/12148/bpt6k55728h.f166).
Aux sources de la méthode de Monte-Carlo
Georges-Louis
Leclerc, Comte
de Buffon
(1707-1788).
Andrey
Andreyevich
Markov
(1856-1922).
Henri
Lebesgue
(1875-1941).
Andrey Nikolaevich
Kolmogorov (1903-1987).
John von Neumann
(1903-1957).
Nicholas
Constantine
Metropolis
(1915-1999).
Stanislaw
Ulam
(1909 -1984).
Dés
Antiquités égyptiennes,
Musée du Louvre. © D.R.

<!-- page 106 (PDF 64) -->
[22] P. J. DOSSANTOS-UZARRALDE, Automatisation de la recherche des
fonctions d’importance dans un code Monte-Carlo, Thèse de doctorat
, Université Paris 6, 1990 ; J.-P. BOTH, G. DEJONGHE, J.-C. NIMAL,
P. J. DOSSANTOS-UZARRALDE and T. VERGNAUD, “Automated importance
generation and biaising techniques for Monte-Carlo shielding techniques
by the TRIPOLI-3 code”, Proceedings of Physor 90
International Conference, (XII)-59–68, Marseille, France, April 1990 ;
J.P. Both, J.C. Nimal, T.Vergnaud, “Automated Importance Generation
and Biasing Techniques for Monte Carlo Shielding Techniques by the
TRIPOLI-3 code”, Progress in Nuclear Energy, 24, pp. 273-281, 1990.
[23] B.MORILLON, Méthode de Monte Carlo non analogue – Application
à la simulation des neutrons, Thèse de doctorat, Université Paris XI-
Orsay, Note CEA-N-2805, janvier 1996.
[24] E. DUMONTEIL, “On a New Variance Reduction Technique : Neural
Network Biasing – A Study of Two Test Cases with the Monte Carlo
Code TRIPOLI-4”, Nuclear Technology, 112, pp. 793-798, December
2009.
[25] A. ZOIA, E. BRUN, C. JOUANNE, F. MALVAGI, “Doppler broadening of
neutron elastic scattering kernel in TRIPOLI-4®”, Annals of Nuclear
Energy 54, 218-226, 2013.
[26] H. RIEF, “Generalized Monte Carlo Perturbation Algorithms for
Correlated Sampling and Second-Order Taylor Series Approach”,
Annals of Nuclear Energy, 11, 9, pp. 455-476, 1984.
[27] G. DEJONGHE, J. GONNORD, J.C. NIMAL, “Perturbation Calculations
by the Correlated Samples Method”, Proceedings of the International
Meeting on Advances Nuclear Engineering Computational Methods,
Knoxville, Tennessee, vol. 2, April 9-11, 1985).
[28] B. MORILLON, Perturbation dans le transport des neutrons par la
méthode de Monte-Carlo, Note CEA-N 2838, octobre 1998.
[29] Y. NAGAYA, T. MORI, “Estimation of reactivityworth with differential
operator sampling method”, Joint International Conference on
Supercomputing in Nuclear Applications and Monte Carlo 2010 (SNA
+ MC2010), Tokyo, Japan, October 17-21, 2010.
[30] A. MAZZOLO, “Probability density distribution of random line segments
inside a convex body: Application to random media”, Journal of
Mathematical Physics, V. 44, 853-863, 2003.
[31] K. SMITH, “Nuclear Mathematical and Computational Sciences: A
Century in Review, A Century A new.” Invited Keynote Speaker.
Gatlinburg, Tennessee, USA, May 2003.
[32] B. L. SJENITZER and J. E. HOOGENBOOM, “A Monte Carlo method for
calculation of the dynamic behaviour of nuclear reactors”, Progress in
Nuclear Science and Technology, 2, pp. 716-721, 2011.
[33] J. Eduard HOOGENBOOM, Aleksandar IVANOV, Victor SANCHEZ, C. M.
DIOP, “A flexible coupling scheme for monte carlo and thermal-hydraulics

codes”,
International
Conference
on
Mathematics
and
Computational Methods Applied to Nuclear Science and Engineering
(M&C 2011), Rio de Janeiro, RJ, Brazil, on CD-ROM, Latin American
Section (LAS) / American Nuclear Society (ANS) ISBN 978-85-63688-
00-2, May 8-12, 2011.
Cheikh M. DIOP, Éric DUMONTEIL,
François-Xavier HUGOT et Fausto MALVAGI
Département de modélisation des systèmes et des structures
[2] E. SEGRÈ, Les Physiciens modernes et leurs découvertes – Des
rayons X aux Quarks, Paris, Fayard, coll. “Le temps des Sciences”,
p. 304, 1984.
[3] N. METROPOLIS, S. ULAM, “The Monte-Carlo Method”, Journal of
the American Statistical Association, 247, 44, 335-34, 1949.
[4] N. METROPOLIS, “The Begining of the Monte-Carlo Method”, in Los
Alamos Science Special Issue, pp. 125-130, 1987.
[5] J.SPANIER, Monte-Carlo Methods and their Application to Neutron
Transport Problems, WAPD-195, AEC Research and Development
Report, Bettis Atomic Power Laboratory, Pittsburgh, Pennsylvanie,
USA, July 1959.
[6] J. SPANIER et E. M. GELBARD, Monte-Carlo Principles and Neutron
Transport Problems, USA, Addison-Wesley Publishing Company,
1969.
[7] J.-C. NIMAL, J. RASTOIN, Méthodes de Monte-Carlo, Note CEA-N-
533, 1965.
[8] C.DEVILLERS, S.KATZ, J.C.NIMAL, Quelques remarques sur la pondération
dans les méthodes de Monte-Carlo, Note CEA-N-644,
1967.
[9] J. M. LANORE, Utilisation d’une méthode de Monte-Carlo pour la
propagation des neutrons à grande distance, Note CEA-N-934,
1968.
[10] J. M. HAMMERSLEY, D.C. HANDSCOMB, Les Méthodes de Monte-
Carlo, Paris, Dunod, coll. « Monographies Dunod », 1967.
[11] J. H. HALTON, “A Retroscpective and Prospective Survey of the
Monte Carlo Method”, SIAM Review, 12, 1, 1-63, January 1970.
[12] G. W. MCKINNEY, J. W. DURKEE, J. S. HENDRICKS, M. R. JAMES,
D. B. PELOWITZ, L. S. WATERS, F. X. GALLMEIER, MCNPX Overview,
LA-UR-06-6206, 2006.
[13] S. KATZ, J. C. NIMAL, Programme de Monte-Carlo polycinétique
à trois dimensions : TRIPOLI-01, Note CEA-N-1919, 1976.
