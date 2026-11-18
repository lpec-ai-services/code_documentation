# La démarche du neutronicien
<!-- source PDF pages 9-12 -->

<!-- page 51 (PDF 9) -->
# La démarche du neutronicien

Les études de conception et d’exploitation des réacteurs
s’appuient sur la simulation numérique. Il est donc impératif
d’élaborer des méthodes de calcul à la fois très précises,
rapides et robustes.
Pour résoudre l’équation de Boltzmann et les équations de
Bateman généralisées le neutronicien doit choisir les voies de
calcul les mieux adaptées au réacteur étudié.
Trois facteurs s’opposent à une résolution aisée des équations
de Boltzmann et Bateman :
• La complexité technologique (dimensions, structures…) et
de fonctionnement d’un cœur de réacteur nucléaire ;
• le nombre élevé de variables dont dépendent les équations :
elles sont au nombre de sept ;
• le caractère évolutif, souligné plus haut, des sections efficaces
macroscopiques, Σ ()□, E, ,) = N ()□, ,) σ (E, ,), qui varient
dans le temps, avec des échelles très différentes :
- quand la température du système évolue (par une excursion
de puissance, par exemple) la densité du milieu varie,
ainsi que les sections efficaces microscopiques (par effet
Doppler*) ; la géométrie peut également être modifiée ;
- quand le combustible est irradié, sa composition en
nucléides s’en trouve modifiée.
De surcroît, les échelles de temps diffèrent considérablement
selon les phénomènes étudiés :
• de l’ordre de la microseconde pour la contre-réaction
Doppler ;
• de l’ordre de quelques dizaines de minutes à quelques
heures pour l’empoisonnement* du cœur (par le xénon*
135 ou le samarium* 149) ;
• de l’ordre de quelques années pour la durée de passage des
combustibles en cœur.
Lorsque le réacteur est finement décrit en énergie, angle et
espace, l’équation de Boltzmann nécessite la prise en
compte de près de 1 000 milliards d’inconnues (voir infra,
p. 62-63, « Discrétisation de l’espace des phases »). La
puissance actuelle des ordinateurs ne permet pas toujours
de résoudre des problèmes d’une telle dimension. Il est donc
indispensable d’introduire des simplifications et des découplages
en relation avec la physique particulière de la filière
calculée. Le choix de ces simplifications et découplages
consiste en la définition de ce que les physiciens des réacteurs
appellent le schéma de calcul*.
Le neutronicien tire parti des observations fondamentales suivantes
:
1) la densité de neutrons dans un réacteur est suffisamment
faible pour considérer qu’il n’y a pas d’interaction neutronneutron
. L’équation de Boltzmann est alors linéaire en flux, à
condition de considérer les sections efficaces macroscopiques
indépendantes du flux, ce qui constitue une approximation
tout à fait valide, dans la mesure où l’évolution des
situations du cœur peuvent être modélisées par une succession
d’états stationnaires.
2) Lorsque le réacteur est critique ou proche de la criticité,
l’équation de bilan (équation de Boltzmann en régime stationnaire
) traduit qu’en tout point la production de neutrons est
égale aux disparitions (fuites + absorptions).
3) Dans la résolution de l’équation de bilan neutronique, on
peut remplacer un milieu hétérogène par un milieu homogène
équivalent, si celui-ci ne perturbe pas le calcul de son environnement
.
4) La solution de l’équation de Boltzmann sur la configuration
hétérogène finement discrétisée peut être utilisée pour obtenir
des grandeurs neutroniques moyennées en espace et en
énergie ; ces grandeurs peuvent elles-mêmes être utilisées
dans une nouvelle formulation homogène de l’équation de
Boltzmann qui respectera chacun des termes du bilan : production
, fuites et absorptions.
Il en résulte qu’un calcul déterministe du réacteur peut être
effectué en deux étapes principales. La première est le calcul
fin des assemblages combustibles supposés se répéter à l’infini
. Il fournit les grandeurs neutroniques représentatives de
l’assemblage qui sont utilisées dans la seconde étape. Celleci
est dédiée aux calculs des échanges neutroniques entre
assemblages avec prise en compte des conditions aux limites
réelles du cœur.
Les méthodes de la neutronique

<!-- page 52 (PDF 10) -->
pensable de procéder à une étape dite « d’équivalence* »
entre les deux, qui permet de corriger les manques d’une
simple homogénéisation / condensation* [1], [2].
C’est toutefois le seul type de schéma qualifié, actuellement
opérationnel, pour traiter un cœur en trois dimensions en prenant
en compte l’usure du combustible et les contre-réactions.
En effet :
• Le calcul « direct » par résolution en trois dimensions (3D)
de l’équation du transport par la méthode déterministe sur
le cœur entier d’un réacteur de grande taille est encore
hors de portée sans simplifications du modèle spatial
et / ou énergétique. Les seuls calculs directs possibles (et
réalisés) sont en 2D et concernent de petits réacteurs
(réacteurs expérimentaux) ou une partie de grands réacteurs
(1/8e du cœur d’EPR, par exemple). Ces calculs sont
encore très longs, même si l’on ne prend pas en compte
l’évolution du combustible.
• Le calcul « direct » par résolution en trois dimensions (3D) de
l’équation du transport par la méthode de Monte-Carlo couplée
à un code d’évolution déterministe est réalisable.
Cependant, cette méthode impose le calcul des taux de
réactions avec une incertitude statistique partout acceptable
et pose le problème du traitement de la propagation de ces
incertitudes dans les calculs couplés transport/évolution.
Le travail du neutronicien consiste ainsi à concevoir des modélisations
et des schémas de calcul permettant d’obtenir les
grandeurs physiques recherchées, tout en optimisant le rapport
précision / coût de calcul.
Dans la pratique, selon les échelles de temps considérées
pour la description de l’état neutronique d’un réacteur, le neutronicien
distingue habituellement :
• le comportement « statique » du système physique étudié
pour lequel l’équation de Boltzmann est résolue en régime
stationnaire (indépendant du temps), voir infra, p. 56-59 ;
• l’évolution temporelle « lente » de la composition du combustible
nucléaire gouvernée par les équations de Bateman,
voir infra, p. 107-113 ;
• les phases transitoires « rapides » gouvernées par les équations
de la cinétique durant lesquelles les neutrons retardés
jouent un rôle prépondérant, voir infra, p.59-60 et p.115-124.
La distinction de ces différentes échelles de temps permet de
poser les hypothèses pertinentes facilitant la résolution des
équations concernées.
Ainsi :
• La première étape, dite « calcul d’assemblage* » consiste
en un calcul détaillé (tant en espace qu’en énergie) d’un motif
élémentaire du cœur (un assemblage combustible, un assemblage
de contrôle, etc.).Ce calcul d’un objet, à l’échelle du libre
parcours moyen* d’un neutron (quelques cm), est réalisé en
résolvant l’équation du transport sur une coupe horizontale de
l’assemblage, donc à deux dimensions, et en supposant que
ce motif se répète à l’infini ou qu’il occupe la totalité de l’espace
(calcul en « milieu infini »).L’essentiel de l’hétérogénéité
est ainsi pris en compte, à condition que les hétérogénéités
soient moins marquées axialement que radialement (c’est
généralement le cas). Ce calcul fin permet de procéder à une
« réduction de données » qui fournit les caractéristiques neutroniques
(sections efficaces macroscopiques) d’une « pâte »
homogène dite « équivalente » qui représente, soit l’assemblage
complet (homogénéisation totale), soit chaque type de
portion d’assemblage (par exemple, crayon combustible et
modérateur/caloporteur qui l’entoure) le constituant (homogénéisation
par morceaux). Cette « homogénéisation* » spatiale
s’accompagne d’une « condensation* » en énergie : le
nombre de groupes* utilisés pour décrire la variation en énergie
de ces sections efficaces « homogénéisées » est fortement
réduit par rapport au nombre de groupes de la bibliothèque
multigroupe d’entrée. Le facteur de réduction dépend
du type de réacteur, notamment des variations spatiales du
spectre* des neutrons.
• La seconde étape (le calcul de cœur proprement dit)
consiste à résoudre, en deux ou trois dimensions, une équation
exacte ou approchée de l’équation du transport (équation
de la diffusion, par exemple) en remplaçant dans le cœur
chaque assemblage ou chaque type de cellule par la « pâte»
homogène équivalente définie lors de la première étape. On
traite ainsi un objet de grande taille, mais avec un modèle
réduit tant en espace qu’en énergie. C’est à partir de ce calcul
qu’on fournit les différentes grandeurs utiles (réactivité,
efficacité des absorbants, coefficients de contre-réactions,
distribution de taux de réaction, isotopie…).
Dans ces deux étapes, le neutronicien est amené à détailler
quels modèles, quels solveurs, quelles discrétisations seront
les plus adaptés pour résoudre efficacement et précisément le
problème qui lui est posé. Les avancées de l’informatique et
des méthodes numériques ouvrent régulièrement des perspectives
d’amélioration.
Ce type de schéma n’est pas exempt de limitations, parmi lesquelles
on peut citer, d’une part l’hypothèse de calcul en
réseau infini des constantes d’un assemblage – ce qui permet
de découpler le calcul fin dans l’assemblage du calcul
d’échange de neutrons entre assemblages – et, d’autre part,
les approximations de l’équation du transport (diffusion, transport
simplifié) éventuellement retenues dans la seconde étape.
Les différences des modélisations utilisées durant les deux
étapes du calcul de cœur font qu’il est, le plus souvent, indis-

<!-- page 53 (PDF 11) -->
L
a résolution de l’équation du transport sous sa forme continue
(en énergie, en espace, en angle, en temps) n’est pas
compatible avec les exigences des études industrielles de
routine ou de projet qui doivent être réalisées en des durées
contraintes. Certains calculs doivent pouvoir délivrer des résultats
en quelques secondes. Pour répondre à ce défi, le neutronicien
a mis au point diverses techniques de résolution de
l’équation du transport, s’appuyant toutes sur une discrétisation
de l’espace des phases et des méthodes numériques sophistiquées
[1], [2] se rattachant à des paradigmes de modélisation
déterministes brièvement rappelés ci-après. Ces paradigmes
concernent notamment le traitement en énergie de la propagation
des neutrons, le traitement de l’hétérogénéité géométrie /
composition du réacteur, le couplage entre traitements énergétique
et spatial, la reconstruction de la distribution fine de la puissance
dégagée par le cœur du réacteur. Ils font intervenir le
concept fondamental d’équivalence qui spécifie la nécessité
de préserver les taux de réaction lorsque l’on passe de la
configuration réelle à la configuration modélisée du réacteur
nucléaire.
• Le traitement multigroupe de l’équation du transport. Il
s’agit du passage de l’équation continue en énergie à celle discrétisée
en énergie. À l’équation continue, on substitue un
ensemble d’équations dites « multigroupes » dont le nombre
est celui du nombre de groupes d’énergie partitionnant le
domaine d’énergie des neutrons, de 0 à 20 MeV. En effet, les
équations multigroupes sont obtenues par intégration de
l’équation continue sur chacun des groupes d’énergie. Les
grandeurs physiques continues sont alors remplacées par des
grandeurs correspondantes multigroupes. Ce passage du
continu au discret conduit, en particulier, à remplacer les sections
efficaces continues en énergie par des sections efficaces
constantes dans chaque groupe d’énergie : ce sont les sections
efficaces multigroupes [3],[4]. La problématique alors
posée est la détermination de ces sections efficaces multigroupes
, de façon que les taux de réactions multigroupes préservent
les taux de réaction prédits par l’équation continue. On
désigne cette problématique par l’expression de « mise en
groupes* des sections efficaces ». La difficulté réside ici
dans le fait que la détermination des sections efficaces multigroupes
permettant d’assurer la préservation des taux de réaction
issus de la résolution de l’équation continue suppose de
connaître le flux angulaire des neutrons, celui-ci étant justement
l’inconnue du problème à résoudre. De ce fait, les sections
efficaces multigroupes qui seraient ainsi définies ne correspondraient
plus à celles de milieux isotropes, car elles
dépendraient de l’angle et de l’espace.
La mise en groupes affecte également les lois de transfert d’un
neutron d’un groupe dans un autre par diffusions élastique et
inélastique discrète pour lesquelles l’énergie et la direction après
collision sont complètement corrélées : elle a pour effet de créer
une anisotropie artificielle du transfert entre les groupes [5],
d’autant plus marquée que le découpage en groupes d’énergie
est fin.
La modélisation du phénomène d’autoprotection des résonances
occupe une place centrale dans la problématique générale
de la mise en groupes. Dans le domaine des résonances,
la mise en groupes des sections efficaces peut être réalisée par
différentes méthodes dont la méthode de Livolant-Jeanpierre
[6] et la méthode des sous-groupes [7], [8].Elles permettent de
produire des sections efficaces multigroupes dites « autoprotégées
» dans un découpage énergétique à groupes relativement
larges (en énergie) et en nombre relativement réduit, 100 à 500,
adaptés à des calculs de transport en géométries homogènes et
hétérogènes bi-dimensionnelles (voir infra, p. 64-67).
• Les techniques d’homogénéisation pour les calculs de
cœurs [9 à 17]. Le calcul tridimensionnel déterministe du cœur
d’un réacteur nucléaire de puissance oblige à imaginer de nouvelles
modélisations adaptées à des systèmes complexes de
grande taille, comportant un nombre important de composants
hétérogènes, pour lesquels un calcul direct n’est guère possible
ou bien nécessite un temps et/ou des ressources de calcul
(puissance et nombre de processeurs des ordinateurs…) prohibitifs
pour des études de routine ou de projet. Le but de l’homogénéisation
est de remplacer les composants hétérogènes
par des composants homogènes, de façon que le calcul du
système homogénéisé donne des valeurs moyennes précises.
La solution du problème homogénéisé ne peut pas préserver
dans le détail la solution du problème hétérogène original.Il s’ensuit
que le processus d’homogénéisation s’accompagne d’une
perte d’information et que seules les valeurs moyennes de la
solution pourront être préservées.
Calcul industriel des réacteurs nucléaire : paradigmes de modélisation
(d’après R. Sanchez et P. Reuss)
Schéma de principe de l’équivalence sur l’exemple d’un calcul
de cœur 3D hétérogène.
Dans l’état actuel des capacités de calcul, le point O ne peut
encore être calculé directement (c’est un objectif à atteindre).
Grâce à une équivalence, on approche la solution exacte en
effectuant les calculs C, M et R qui, eux, sont réalisables.
C
M
O
R
Problème réel modélisé :
calcul 2D hétérogène
Problème simplifié
modélisé :
calcul 2D homogène
Problème réel :
calcul 3D hétérogène
?
Problème simplifié :
calcul 3D homogène
(dit « de référence »)
Facteurs d’équivalence
Solution du problème réel

<!-- page 54 (PDF 12) -->
Les techniques d’homogénéisation sont mises en œuvre au
niveau des assemblages. Elles reposent sur :
- La définition et la réalisation du (ou des) calcul(s) de référence
hétérogènes qui spécifient les valeurs que doit préserver
l’opération d’homogénéisation ;
- l’utilisation conjointe de la théorie du mode fondamental et
du concept de fuites critiques ;
- des méthodes d’équivalence où interviennent des facteurs
de discontinuité du courant (FDC) ou du flux (FDF) des neutrons
entre assemblages homogénéisés.
• La reconstruction du flux hétérogène. Le but d’un calcul de
cœur est d’obtenir des taux de réaction et la distribution de puissance
spatialement détaillés et, en particulier, de prédire le pic
de puissance dans le cœur. En conséquence, une fois que le
calcul de cœur a été effectué, une méthode de reconstruction
doit être employée pour obtenir les résultats détaillés désirés. Il
s’agit d’un problème inverse qui est résolu avec l’une des techniques
suivantes :
- la technique de factorisation,
- la reconstruction par le transport,
- la technique multi-échelle,
qui combinent, chacune de manière différente, les résultats provenant
du calcul de cœur avec ceux issus du calcul de transport
de référence.
Il existe une méthode plus précise mais plus coûteuse, appelée
« homogénéisation dynamique », qui détermine le flux de
neutrons du transport détaillé en homogénéisant itérativement
les assemblages de manière à prendre en compte les échanges
inter-assemblages moyens du calcul de cœur. Cette méthode,
qui fait converger simultanément le calcul de cœur et celui des
assemblages en transport, ne nécessite donc pas de reconstruction
.
Depuis quelques années, les calculs Monte-Carlo fournissent
des résultats de référence qui offrent la possibilité d’une « validation
numérique » des méthodes ci-dessus. Cela est détaillé
infra, p. 165-170.
□Références
[1] R. SANCHEZ, J. MONDOT, Z. STANKOVSKI, A, COSSIC, I. ZMIJAREVIC,
“APOLLO2: a user oriented, portable, modular code for multigroup
transport assembly calculations”, Nuclear Science and Engineering,
100, pp. 352-362, 1988.
[2] R. SANCHEZ, I. ZMIJAREVIC, M. COSTE-DELCLAUX, E. MASIELLO, S.
SANTANDREA, E. MARTINOLLI, L. VILLATTE, N. SCHWARTZ, N. GULER,
“APOLLO2 Year 2010”, Nuclear Engineering and Technology, vol.
42, no 5, pp. 474-499, October 2010.
[3] N. HFAIEDH, Nouvelle Méthodologie de Calcul de l’Absorption
Résonnante. Thèse de doctorat, Université Louis Pasteur
Strasbourg I, 2006.
[4] P. MOSCA, Conception et développement d’un mailleur énergétique
adaptatif pour la génération des bibliothèques multigroupes des
codes de transport, Thèse de Doctorat, Université Paris Sud 11,
Orsay, France, 2009.
[5] A. CALLOO, Développement d’une nouvelle modélisation de la loi
du choc dans les codes de transport multigroupes : application au
calcul des réacteurs de Génération III et IV, Thèse de Doctorat de
l’Université de Grenoble, France 2012.
[6] M. LIVOLANT, F. JEANPIERRE, Autoprotection des résonances dans
les réacteurs nucléaires, Rapport CEA-R-4533- 1974.
[7] G. RIMPAULT et al., “The ERANOS Code and Data System for Fast
Reactor Neutronic Analysis”, Proc. Int. Conf. PHYSOR 2002, Seoul,
Korea, October 7-10, 2002.
[8] M. COSTE, S. MENGELLE, “Implementation of a sub-group method
for self-shielding calculations in APOLLO2 code”, International
Conference on the Physics of Reactors, PHYSOR 96, Vol I, pp. 323-
331, Mito, Ibaraki, Japan,1996.
[9] D.S.SELENGUT, “Diffusion coefficients for heterogeneous systems”,
Transactions of the American Nuclear Society, 3, 398, 1960.
[10] E.W.LARSEN, “Neutron transport and diffusion in inhomogeneous
media”, I. J. Math. Phys. 16 (7), pp. 1421-1427, 1975.
[11] A.KAVENOKY, ”The SPH Homogenization Method”, AIEA, Comité
technique en physique des réacteurs, Würenlingen, Suisse, 1978 ;
Proc. Specialists Meeting on Homogenization Methods in Reactor
Physics, AIEA, Lugano, 1978.
[12]
A.
HÉBERT,
Développement
de
la
méthode
SPH
:
Homogénéisation de cellules dans un réseau non uniforme et calcul
des paramètres de réflecteur, Thèse de Doctorat, Université Paris
Sud XI, Orsay, 1980, Note CEA-N-2209, 1981.
[13] P. BENOIST, Homogenization, Theory in Reactor Lattices, Note
CEA-N-2471, février 1986.
[14] K.S.SMITH, ”Assembly homogenization techniques for light water
reactor analysis”, Progress in Nuclear Energy, 17 (3), pp. 303-335,
1986.
[15] R. SEKKOURI, Analyse des techniques d’homogénéisation et des
schémas de calcul pour les réacteurs à eau, Thèse de Doctorat,
Université Paris Sud XI, Orsay, 1994.
[16] Ph. MAGAT, Analyse des techniques d’homogénéisation spatiale
et énergétiques dans la résolution de l’équation du transport des
neutrons dans les réacteurs nucléaires, Thèse de Doctorat,
Université Aix-Marseille I, 1997.
[17] R. SANCHEZ, “Assembly homogenization techniques for core calculations
”, Progress in Nuclear Energy, 51, pp. 14-31, 2009.
Richard LENAIN et Anne NICOLAS
Département de modélisation des systèmes et structures
