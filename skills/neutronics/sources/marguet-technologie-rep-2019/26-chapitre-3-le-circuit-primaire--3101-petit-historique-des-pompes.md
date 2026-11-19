# Chapitre 3 Le circuit primaire — 3.10 Les pompes primaires — 3.10.1 Petit historique des pompes … 3.10.5 Étanchéité des pompes primaires
<!-- source PDF pages 326-345 -->

<!-- page 310 (PDF 326) -->
C’est le dimensionnement radiochimique du circuit de traitement des effluents
TEP qui limite l’exploitation du cœur. Il existe ainsi un seuil d’arrêt sur augmentation
de l’activité de l’iode 134 depuis 1997. Une augmentation significative de cette
activité signifie concrètement une dissémination de matière fissile dans l’eau du primaire
. On surveille aussi la somme des gaz de fission, ce qui permet de remonter 16
approximativement au taux de combustion du crayon fuitard, donc une suspicion sur
les assemblages présentant le défaut. Il existe un seuil dit « rupture de gaine sérieuse
» de 4 Bq d’activité alpha par litre d’eau primaire, mais qui ne concerne que
le conditionnement et le stockage des fûts de déchets.
L’activité du tritium (période 12,32 ans) est soigneusement suivie dans la mesure
où cet isotope apparaît explicitement dans les autorisations de rejets. La source de
tritium dans l’eau provient pour presque 85 % de l’acide borique dilué dans l’eau du
primaire. Environ 15 % proviennent de l’hydroxyde de lithium utilisé pour contrôler
le pH ((n,α) sur le lithium 6), et à peine 1 % provient de l’activation neutronique
(n,γ) de deutérium de l’eau. C’est le bore 10 fortement absorbant neutronique qui est
la source principale du tritium par des réactions (n, 2α), (n,tritium) ou (n, tritium
α). Du tritium issu de fission ternaire dans le combustible peut s’ajouter à ces voies
de production en cas d’inétanchéité des gaines. Notons que le tritium est très mobile
dans l’acier, mais peu dans le Zircaloy 4, d’où son intérêt pour le gainage des crayons
combustibles.

## 3.10 Les pompes primaires

[Coppolani et al., 2004] p. 115, [Faisandier, 1970] p. 70, [Hutin, 2016] p. 445, [de
Kovats et Desmur, 1971]

### 3.10.1 Petit historique des pompes

[Appareils accessoires de machines à vapeur, 1908]
Un petit historique des pompes permet de comprendre les principes de base d’une
pompe et de préciser le vocabulaire technique. Depuis des temps immémoriaux,
l’Homme a voulu pouvoir disposer d’eau dans sa proximité. Pas toujours disponible
au niveau du sol, cette eau peut être pompée grâce à une pompe à main (Figure 3.17
à gauche), où l’eau pénètre dans le corps de la pompe depuis une crépine, grâce à
une soupape. La pompe foulante (Figure 3.17, à droite) présente déjà l’amélioration
de proposer un débit d’eau continu, sans chocs et d’élever la hauteur de refoulement
désiré, grâce au principe du vase rapporté.
Toutes ces réalisations se heurtent au principe qu’on ne peut faire monter à n’importe
quelle hauteur l’eau pompée, du fait de la cavitation, que nous étudierons en
détail plus loin. Ce phénomène physique empêche de faire monter l’eau à plus d’environ
10 mètres à pression atmosphérique.
À EDF, c’est l’application MERLIN qui permet une évaluation de l’état du gainage. En
utilisant la quantité de gaz de fission détectée, on peut remonter à une taille de brèche et un nombre
de défauts, et même la puissance linéique de l’endroit où se trouve le défaut. En effet, l’ordre de
grandeur et la distribution des produits de fission relâchés dans le primaire sont liés à la gravité d’un
défaut et aux conditions de fonctionnement. On peut en particulier savoir si le défaut est porté par
un assemblage UOX ou MOX.

<!-- page 311 (PDF 327) -->
Fig. 3.17 – Une pompe aspirante à main de la fin du XIXe siècle (à gauche) et
une pompe foulante (à droite).
À partir du xixe siècle, le développement des machines à vapeur (pour les chemins
de fer, les navires à vapeur, les turbines à vapeur. . . ) génère un important travail sur
la normalisation des composants et les règles de sûreté sur les appareils à pression.
Les pompes bénéficient de ces améliorations et de nouveaux concepts apparaissent :
la pompe à air qui développe l’usage de l’air comprimé (Figure 3.17), et des pompes
à eau entraînées par des moteurs électriques ou thermiques (Figure 3.18).
La technique a rapidement évoluée au xxe siècle et des pompes de plus en plus puissantes
sont apparues : pompes centrifuges, pompes multicellulaires. . . (Figure 3.20,
Photo 3.3, Photo 3.4), pour aboutir à des pompes utilisées dans la technologie nucléaire
(Figure 3.21).

### 3.10.2 Généralités sur les pompes primaires

Les groupes motopompes primaires (GMPP, principe de la pompe centrifuge en Figure
3.4) ont pour fonction de faire circuler l’eau dans le circuit primaire, dans la
mesure où la convection naturelle serait largement insuffisante pour assurer cette
fonction en régime nominal (Figure 3.22). Elles assurent aussi une légère remise en
pression de l’eau pour vaincre les pertes de charges du circuit primaire. Par un piquage
astucieux au refoulement des pompes où la pression est maximale, elles assurent aussi
le fonctionnement de l’aspersion du pressuriseur sans pompe additionnelle, en jouant
sur la différence de pression entre le pressuriseur et le refoulement de la pompe.
Les pompes sont des composants lourds (89 tonnes pour le CPY, environ 100
tonnes pour les paliers ultérieurs) et massifs (plus de 8 mètres de hauteur) qui doivent
être particulièrement fiables dans la mesure où elles doivent pouvoir tourner en continu
pendant plus d’une année sans maintenance extérieure, puisque les pompes primaires

<!-- page 312 (PDF 328) -->
Fig. 3.18 – Pompe à air double effet : l’air est comprimé à la fois à la descente du piston
et à la remontée (d’après [Appareils accessoires de machines à vapeur, 1908] p. 173).
Fig. 3.19 – Une pompe alimentaire marchant à moteur par entraînement (d’après
[Appareils accessoires de machines à vapeur, 1908] p. 174).

<!-- page 313 (PDF 329) -->
Fig. 3.20 – Différents types de pompe : le type centrifuge simple, largement utilisé
dans le cadre des pompes primaires, et le type multicellulaire.
sont localisées dans le BR inaccessible en fonctionnement. Le primaire d’un CPY
comporte trois pompes, quatre pour les paliers français ultérieurs, à raison d’une
pompe par branche. Ces pompes sont construites par la société Jeumont-Schneider
sous licence Westinghouse. Notons que certaines tranches étrangères disposent de
plusieurs pompes par branche (à l’exemple de Three Mile Island avec deux pompes
par branche pour deux branches). Les pompes tournent entraînées par un moteur
asynchrone à raison de 1 485 tours/minute, à la fréquence de 50 hertz, et délivrent
une puissance thermique entre 5 et 7 MWth selon les modèles. Cette puissance est
évacuée dans l’eau du primaire (c’est d’ailleurs un moyen de chauffer l’eau du primaire
au démarrage, quand il n’y a pas encore de fission nucléaire).

### 3.10.3 Tenue des bâtis de pompes

Les pompes primaires sont physiquement placées sur des béquilles articulées dans le
bâtiment réacteur autour de la cuve (Figure 3.23, Figure 3.24, Figure 3.25). Ces béquilles
sont dimensionnées pour reprendre les efforts d’origine sismique. Ces béquilles
sont des supports verticaux à pieds articulés dont les rotules supérieures sont fixées
sur trois pattes de volute. Latéralement, ce sont des plaques à quatre tirants précontraints
qui guident la pompe dans l’axe de la branche froide. Les pompes sont reliées
au bâti par des amortisseurs-bloqueurs (1 pour le CPY, 3 pour le P4) pour maintenir
la stabilité en cas de rupture ou de séisme. Les bloqueurs sont fixés sur le goujon liant

<!-- page 314 (PDF 330) -->
Photo 3.3 – Publicités du début des années 1950 pour les pompes Guinard
(gauche) et Schneider-Westinghouse (droite) (collection Marguet).
Photo 3.4 – Une pompe hélico-centrifuge Westinghouse 1953 (collection Marguet).
la béquille à la patte de volute, le tout étant solidaire du bâti par les quatre tirants
déjà cités (Figure 3.24). La Figure 3.25 présente les fixations des pompes EPR.

### 3.10.4 Description des pompes primaires

[Hutin, 2016] p. 450, [Leclercq, 1988] p. 242
Quel que soit leur nombre (généralement entre 2 et 4), elles sont placées sur
les branches froides pour bénéficier de l’abaissement de la température du fluide

<!-- page 315 (PDF 331) -->
Fig. 3.21 – Vue extérieure d’une pompe de Fessenheim (CP0) de technologie
Westinghouse.
(amoindrissement des phénomènes d’oxydation, de contraintes thermiques). Ce sont
des pompes centrifuges dont l’axe de rotation est vertical et qui comprennent de bas
en haut (Figure 3.26, Photo 3.5) : la volute de pompe (roue et diffuseur 17) de forme
tulipe, qui est une pièce moulée monobloc en acier austéno-ferritique sans molybdène
pour des raisons de corrosion, avec pattes de supportage intégrées. L’aspiration de
l’eau se fait verticalement par la partie inférieure dans l’axe de la roue et le refoulement
tangentiellement dans le plan médian horizontal de la volute. À l’intérieur de la volute,
le canal d’aspiration est matérialisé par un guide fixé mécaniquement au diffuseur.
Ensuite, on trouve le support moteur et le moteur électrique asynchrone 6 600 V triphasé
, 50 Hz à démarrage direct (Figure 3.27). Un volant d’inertie est situé au sommet
de la pompe (Figure 3.30), il assure une continuité relative de fonctionnement en cas
de coupure électrique (pendant une minute après le déclanchement). La fabrication
de ce volant à deux plaques est particulièrement soignée pour éviter la possibilité de
17 Le diffuseur a pour fonction de transformer une partie de l’énergie cinétique de l’eau communiquée
par la pompe en pression.

<!-- page 316 (PDF 332) -->
Fig. 3.22 – Localisation d’une pompe primaire dans le circuit primaire (une seule
branche représentée).
création de projectile aux survitesses accidentelles. Enfin, un dispositif anti-dévirage
est intégré au moteur, permettant d’éviter que la pompe soit entraînée en sens inverse
lorsqu’elle est arrêtée, alors que les autres pompes sont en fonctionnement.
D’une manière générale, la pompe est conçue pour avoir un diamètre le plus important
possible toujours pour des considérations d’inertie. Sur tous les paliers réacteurs,
elles sont de type hélico-centrifuge mono-étagée avec joints tournants à fuite contrôlée,
la fuite s’effectuant de l’extérieur de la pompe vers l’intérieur en injectant de l’eau à
une pression légèrement supérieure à celle du circuit primaire, pour empêcher l’activité
de l’eau de contaminer l’extérieur. Le stator du moteur électrique est composé
de segments de tôle à haute teneur en silicium, isolés et empilés par l’intermédiaire
de broches, puis comprimés à l’aide d’une presse et bloqués par deux plateaux en
acier dans un souci de rigidité (Figure 3.27, Figure 3.28 et Figure 3.29). Le rotor est
constitué d’un empilement de tôles en couronnes d’acier à haute teneur en silicium,
bien ventilé par des caissons de ventilation, et bloqué par des tirants et des joues
d’extrémité, le tout claveté sous pression. La cage électrique est constituée de barres
en cupro-alliage et deux anneaux de court-circuit en cuivre, qui sont enfermés par une
frette en acier non magnétique à haute résistance mécanique. Le moteur électrique est
refroidi par l’air ambiant. L’huile du moteur est refroidie par un échangeur huile/eau.
Pour éviter une montée progressive de la température dans la pièce où se trouve la
pompe, l’air est refroidi en sortie de moteur par un échangeur air-eau du RRI.
Les pompes primaires (écorchés en Figure 3.30, Figure 3.31 et Figure 3.32) doivent
faire circuler pendant des mois l’eau à un débit considérable de plusieurs milliers de

<!-- page 317 (PDF 333) -->
Fig. 3.23 – Pompe primaire CPY sur ses trois béquilles.
m3/h chacune. La forte pression du circuit primaire impose une très bonne étanchéité.
Historiquement, on a d’abord développé des pompes monobloc chemisée à joint statique
, dont le démontage était complexe. On s’est ensuite intéressé à des joints d’arbre
hydrostatiques à fuite contrôlée par une contre-pression, permettant un démontage
plus aisé. Le joint n◦2 est situé au-dessus du palier immergé, il est du type à film d’eau
courante entre deux anneaux d’alumine. Ce film d’eau est simplement provoqué par
la différence de pression et n’exige aucune rotation pour se mettre en place. Les joints
n◦2 et n◦3 sont de nature classique à surfaces frottantes (alumine sur graphite). Les
débits de fuite sont décroissants en passant du joint n◦1 (environ 10 l/min) au joint
n◦3 (environ 0,1 l/h).
Dans un autre registre, les pompes doivent pouvoir être encore actives même
pendant des microcoupures électriques, ou ralentir progressivement en cas de coupure
prolongée. Pour ce faire, on les a donc dotées d’un important volant d’inertie de 6,5
tonnes pour éviter un arrêt brutal de la pompe. La conception stricte du volant prend
en compte un possible effet missile si le volant était éjecté.
Les pompes doivent encore assurer 93 % de leur débit nominal à l’instant de
la chute des barres soit 1,2 s après le signal de scram. Une pompe de réacteur CPY
assure un débit de 22 700 m3/h, pour une hauteur manométrique de 78 m. La hauteur
manométrique correspond à la hauteur maximale où une pompe peut encore aspirer

<!-- page 318 (PDF 334) -->
Fig. 3.24 – Détail des amortisseurs et encrage des béquilles d’une pompe P4. Le
supportage comprend trois pieds fixés en partie supérieure de la volute et munis de rotules
permettant des déplacements horizontaux du fait de la dilatation thermique des tuyauteries.
La pompe est aussi arrimée à trois dispositifs auto-bloquants (DAB), deux dans l’axe de la
branche froide et un dans l’axe de la branche en U.
(ou refouler). La pression minimale à l’aspiration doit être de 27 bars 18. La courbe qui
donne la pression de l’eau produite par la pompe en fonction du débit de celle-ci est
appelée « caractéristique de la pompe » et ne dépend que de la pompe. Une pompe
seule absorbe 5,3 MW (cosϕ = 1) en fonctionnement en continu à chaud (7,2 MW à
18 Les conditions exactes de démarrage d’une pompe P4 sont : disposer d’un NPSH (Net Pressure
Suction Head) suffisant à l’aspiration, la pression différentielle du joint n◦1 doit être de 19 bars, ce
qui correspond à une pression de 21 bars absolus à froid, le débit mesuré sur la ligne de reprise des
fuites du joint n◦1 est au moins de 50 litres/heure.

<!-- page 319 (PDF 335) -->
Fig. 3.25 – Encrage des béquilles d’une pompe EPR.
froid, cosϕ = 0, 748 19), puissance du moteur asynchrone à cage d’écureuil, alimenté
en 6,6 kV (50 Hz). Cette puissance est dissipée principalement dans l’eau, ce qui fait
qu’on peut les utiliser pour monter la température du circuit primaire uniquement en
brassant l’eau, un usage auquel on ne penserait pas immédiatement. La montée en
température doit être soigneusement contrôlée pour éviter un choc thermique sur la
cuve. Dans le cas du palier 900 MWe, le circuit primaire ne doit pas évoluer avec un
gradient de plus de 28 ◦C/heure, que ce soit en chauffage ou en refroidissement, et
55 ◦C/heure pour le pressuriseur.
Les pompes primaires sont donc toutes de type hélico-centrifuge (avec 7 ou 4
ailettes, Tableau 3, Figure 3.33, Figure 3.34) à axe vertical et pèsent environ 90
tonnes d’acier chacune. Dans le cas des paliers 1 300 et N4, l’eau du primaire entre
par la partie inférieure de la volute par un orifice d’aspiration axial. Un guide d’eau
Pour le premier CP0, Fessenheim, les valeurs de puissance nominale sont de 4,65 MW, et de
6,1 MW à froid. Le débit nominal de Fessenheim est d’ailleurs plus faible.

<!-- page 320 (PDF 336) -->
Photo 3.5 – Une pompe Jeumont-Schneider du palier N4.
prolonge à l’intérieur de la volute l’orifice d’aspiration jusqu’à l’ouïe de la roue de la
pompe. L’eau est mise en mouvement par la roue et passe dans le diffuseur pour sortir
par un orifice de refoulement radial. Dans le cas du palier 900, le refoulement se fait
par contre tangentiellement via une volute dans le plan médian horizontal.
Une barrière thermique (Figure 3.38) en matière isolante empêche l’échauffement
de la partie supérieure de la pompe par le flux de chaleur débité par l’eau du primaire
[Hutin, 2016] p. 451. Cette barrière est constituée d’un échangeur thermique à
serpentin qui entoure l’arbre sans le toucher, et dans lequel on fait débiter de l’eau
froide en provenance du RCV. La barrière thermique est contenue dans un corps en
acier austénitique fixé verticalement à la pompe grâce à une bride par 24 goujons
en Inconel placés concentriquement. Le corps qui entoure l’échangeur fait aussi office
d’écran thermique. On peut imaginer que la dégradation par fissuration de la barrière
thermique 20 et de son corps, qui sont soumis à d’importants gradients thermiques
(286 ◦C côté primaire, 65 ◦C côté joint), pourrait laisser tomber des fragments sur les
aubes de la pompe en mouvement, générant des missiles par rebond sur les ailettes,
voire même des morceaux d’ailettes qui se seraient arrachées sous le choc. Des calculs
relativement simples de mécanique avec une vitesse de rotation de 1 500 tours par
minute montrent qu’un morceau de 10 grammes possède l’énergie cinétique suffisante
pour fissurer la conduite côté froid. D’où l’importance d’un examen approfondi de
l’état de la barrière thermique au démontage de la pompe. Pour assurer l’étanchéité
du corps de pompe, on injecte au joint via le circuit RCV une pression d’eau froide
20 On a déjà constaté des fissurations dans le congé de l’enveloppe de la barrière thermique sur
des pompes de centrales américaines (Sainte Lucy 1 et 2, Turkey Point 3 et 4, Crystal River 3),
puis françaises, rendant le scénario de rupture de l’enveloppe crédible. En ce qui concerne le volet
français de ce dossier, voir F. Ribes, V. Maupu : Analysis of cracks in thermal barrier cover of
900 MWe PWR primary pumps, 14th International Conference on Structural Mechanics in Reactor
Technology, Lyon (1997).

<!-- page 321 (PDF 337) -->
Fig. 3.26 – Vue d’ensemble d’une pompe primaire de REP (le supportage n’est pas
à l’échelle en axial).
légèrement supérieure à celle du circuit primaire, ce qui fait que l’on pilote une fuite
permanente au niveau du joint, mais toujours vers l’intérieur du circuit primaire.
Deux tiers du débit injecté partent dans le circuit primaire et le reste alimente la
fuite du joint. Ainsi, l’eau radioactive du primaire ne contamine pas le reste de la
pompe. Cet ingénieux système présente néanmoins un inconvénient. Si on perd l’injection
aux joints de pompe, on crée une fuite du circuit primaire de section le jeu
du joint, c’est-à-dire une très petite brèche qui peut être difficile à repérer si les automatismes
du réacteur la compense efficacement (par le RCV notamment). Un suivi
de la température des joints donne néanmoins une indication précieuse si la barrière
est défaillante. En fonctionnement normal, la pression du primaire appliquée à l’arbre
de la pompe produit une poussée vers le haut supérieure au poids du rotor. Il y a
donc une butée haute, de même que basse quand le rotor repose à l’arrêt. Les butées
sont lubrifiées à l’huile. De nombreuses mesures de température, de niveaux d’huile,
de vibrations et de vitesse de rotation permettent d’ausculter une pompe primaire en
fonctionnement. En situation accidentelle, les pompes sont conçues pour résister à un
régime de température et de pression correspondant à un séisme majoré de sécurité,

<!-- page 322 (PDF 338) -->
Fig. 3.27 – Écorché du moteur électrique de la pompe.

<!-- page 323 (PDF 339) -->
Fig. 3.28 – Détail du palier inférieur (adapté de [Pompes primaires, 1977] p. 21). Le
métal antifriction des paliers et butées est tel que la possibilité de rotation par inertie est
maintenue même en cas de simultanéité de séisme et de perte des alimentations électriques
[Éléments de sûreté et de radioprotection des centrales nucléaires de 1 300 MWe, 1982] p. 68.
suivi d’un accident de perte de réfrigérant primaire. Par résister, on attend qu’elles
doivent garder leur intégrité, mais plus forcément assurer leur fonction.
Avant le démarrage des pompes, des pompes de graissage injectent de l’huile pour
produire un premier film d’huile permettant de soulever la partie mobile assurant le
décollage du premier joint. Ces pompes de graissage sont démarrées manuellement
(par bouton TPL en salle de commande) avant le démarrage des pompes primaires
elles-mêmes, puis elles sont stoppées lorsque les pompes primaires fonctionnent.
La mise en marche des pompes primaires requiert que les pompes de graissage
fonctionnent et qu’une certaine pression d’huile soit disponible, que le débit de fuite
au premier joint soit supérieur à 50 l/h (rappelons que c’est ce débit qui « lubrifie »
le palier à ce niveau). Si la vitesse des pompes diminue au-dessous d’un seuil, repéré
en logique 2/3 (CPY) en coïncidence avec le permissif P7, les trois pompes primaires
déclenchent simultanément.
Les pompes primaires débitent dans la branche froide qui est connectée à la cuve.
Tous les piquages des divers circuits sont effectués en aval des pompes (Figure 3.35).

<!-- page 324 (PDF 340) -->
Fig. 3.29 – Détail du palier supérieur et de la butée (adapté de [Pompes primaires,
1977] p. 22). La butée est à double effet dans la mesure où en marche normale, la force
de pression sur la surface verticale de l’arbre de la pompe (différentiel de 45 tonnes vers le
haut) est très supérieure à son poids augmenté de la force dynamique de la pompe, alors qu’à
l’arrêt ou à basse pression (25 tonnes vers le bas), c’est le poids de la pompe qui prédomine.
D’où une poussée possible vers le haut ou vers le bas, dont doit tenir compte la butée.

### 3.10.5 Étanchéité des pompes primaires

[Hutin, 2016] p. 452, [Randrianarivo, 2018] p. 42
Lorsque les pompes sont à l’arrêt, des résistances chauffantes permettent de maintenir
un isolement correct en chauffant les enroulements, leur mise en service est automatique
dès l’ouverture des disjoncteurs des pompes primaires. C’est l’assemblage de la
volute, de la barrière thermique et du support moteur qui constitue la partie en pression
de la pompe. Cet ensemble comporte 18 goujons (CPY) suffisamment serrés pour
éviter des attaques par l’acide borique de l’eau du primaire, et un joint d’étanchéité
logé dans une gorge ménagée dans le plan de joint de la volute. En fonctionnement,
l’étanchéité des pompes primaires est constituée (Figure 3.40) le long de l’axe par la
barrière thermique, le palier, puis de 3 joints à fuite contrôlée en série (Figure 3.40).

<!-- page 325 (PDF 341) -->
Fig. 3.30 – Nomenclature d’une pompe primaire centrifuge (CPY). L’eau est
refoulée par la roue dans le diffuseur tangentiellement. Elle est diffusée radialement dans le
cas d’une pompe P4.
La barrière thermique (Figure 3.38) est alimentée en eau de refroidissement intermédiaire
(RRI) et permet de refroidir les remontées d’eau primaire vers le palier en
cas de défaut d’alimentation en eau d’étanchéité. Le palier de pompe est constitué
d’un coussinet à bagues de graphite. Pour résister au frottement du coussinet, l’arbre

<!-- page 326 (PDF 342) -->
Fig. 3.31 – Motopompe primaire, palier P4-P’4.

<!-- page 327 (PDF 343) -->
Fig. 3.32 – Écorché de pompe primaire d’un REP CP0 type Fessenheim.
rotatif est stellité au niveau du palier. Entre le palier et le joint n◦1, on effectue
une injection d’eau du RCV à une pression légèrement supérieure à celle du primaire,
ce qui fait qu’environ 2/3 du débit rentre de haut en bas dans le primaire par surpression
, assurant la non-contamination, et le 1/3 restant part de bas en haut dans
le joint n◦1 pour le lubrifier. Le joint n◦1 est placé après la barrière thermique et
le palier de pompe. Il est constitué d’un film d’eau courante entre deux anneaux en
alumine. L’écoulement s’effectue de l’extérieur vers l’intérieur comme nous l’avons
déjà indiqué. On mesure la pression différentielle du joint 1 pour vérifier son bon
comportement, ainsi que la température de l’eau du primaire au niveau du palier de
chaque pompe. Les joints n◦2 et n◦3 sont à surfaces qui frottent l’une sur l’autre
(système à glaces tournantes) : graphite sur alumine (l’alumine a par la suite été

<!-- page 328 (PDF 344) -->
Fig. 3.33 – Inter-comparaison des pompes primaires, à gauche P4/CPY, à droite
P4/N4.
Tab. 3.2 – Comparaison des caractéristiques géométriques des GMPPs.
GMPP
CPY
P4
N4
Nombre d’aubes roue
Nombre d’aubes diffuseur
Volute
Basse
Haute
Basse
remplacée par du carbure de chrome). Ils sont dimensionnés pour supporter la rupture
du joint n◦1 (et donc pour encaisser toute la pression du primaire). La Figure 3.37
montre les différents débits autour de joints et les Figure 3.36 et 3.39 montrent les
différents systèmes de mesure et les alarmes associées.
L’inétanchéité du joint de volute (Figure 3.40) des pompes primaires peut être
source de fuites d’eau borée. L’eau borée corrode alors les goujons de serrage de la
volute sur le corps de la pompe. Seul le palier CPY est concerné par ce problème, dans
la mesure où la conception et le montage des joints sont différents sur les paliers plus
récents, et excluent le problème. C’est pourquoi depuis 1997, de nouveaux types de
joints permettant une meilleure étanchéité ont progressivement remplacé l’ancienne
technologie.
Les vannes d’isolement des fuites du premier joint de pompe permettent d’isoler
le retour des fuites du joint vers le RCV. Ces vannes pneumatiques, pilotées par une
électrovanne, sont fermées soit sur commande manuelle en salle de commande, soit
automatiquement sur seuil « très haut débit de pompes ». Une fermeture intempestive
de cette vanne est signalée en salle de commande (« très bas débit de fuite du premier
joint »). Ces vannes restent en position ouverte en cas de perte électrique ou de perte
d’air comprimé (on estime que la perte d’air comprimé, en concomitance avec une
fuite importante du joint, est très peu probable).

<!-- page 329 (PDF 345) -->
Fig. 3.34 – Données techniques générales d’une pompe CP0.
Fig. 3.35 – Localisation des piquages sur branche froide en aval d’une pompe
primaire (image de synthèse).
Le problème d’étanchéité des joints est un problème complexe car cette barrière
est éventuellement mise en défaut dans une situation de pertes de sources électriques
externes H3, puisque le circuit RCV ne peut plus assurer la contre-pression nécessaire.
L’idée d’utiliser des pompes à rotor noyé est séduisante, puisqu’elle règle le problème
de fuite, de lubrification continue, voire même le risque d’incendie. Néanmoins, la
