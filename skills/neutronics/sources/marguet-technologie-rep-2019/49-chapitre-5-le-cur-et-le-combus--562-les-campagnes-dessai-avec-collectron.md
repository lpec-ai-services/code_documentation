# Chapitre 5 Le cœur et le combustible du réacteur — 5.6 Surveillance du réacteur — 5.6.2 Les campagnes d’essai avec collectrons … 5.6.3 L’instrumentation interne de l’EPR
<!-- source PDF pages 661-674 -->

<!-- page 645 (PDF 661) -->
Fig. 5.123 – Exemple de traces axiales d’activité mesurées par les CFMs.

### 5.6.2 Les campagnes d’essai avec collectrons

Historiquement, on doit au physicien russe M. G. Mitelhan 48 en 1961, puis au
Canadien J. W. Hilborn de l’AECL, l’utilisation opérationnelle 49 du principe du
collectron (Self Powered Neutron Detector, SPND en anglais) dans les années 1960,
accompagnée d’un dépôt de brevet 50. L’originalité du collectron est de ne pas nécessiter
de polarisation électrique. L’émetteur est un matériau qui conduit les charges
48 G. Mitelhan, R. S. Erofeev, N. D. Rozenblyum : Transformation of the Energy of short-lived
radioactive isotopes, Soviet Journal of Atomic Energy 10, n◦1 (1961).
49 J. W. Hilborn : Self-Powered Neutron Detectors for flux monitoring, Nucleonics 22, 2, 69
(1964).
50 J. W. Hilborn : Self-Powered Neutron Detector, U.S. Patent 3, 375, 370 (March 26, 1968).

<!-- page 646 (PDF 662) -->
Fig. 5.124 – Description d’une chambre collectron.
électriques. La réaction nucléaire utilisée est la capture de neutron sur une cible absorbante
qui s’active en un isotope radioactif β−, puis les électrons produits sont collectés
via un câble, ce qui forme un signal dont on mesure l’intensité en ampères. Les aspects
théoriques sont plus largement développés par M. Grin 51.
Dans le cadre de l’expérimentation MARINE (Marge Améliorée par la Réalisation
d’une Instrumentation Nucléaire Evoluée) liée à un éventuel déploiement du système
de surveillance des cœurs US3D (Unité de Surveillance 3D de Framatome), EDF a
décidé, suite à une décision de juin 1999 du Directoire de gestion des cœurs, d’installer
sur le réacteur Cattenom 1 (tranche 1 300 MWe en gestion GEMMES) une nouvelle
instrumentation expérimentale « in-core » fixe, dite « collectron » (Figure 5.124),
un néologisme signifiant « collecteur d’électrons ». En anglais, on utilise plutôt le
terme Self-Powered Neutron Detector (SPND), qui signifie bien que le système n’a
pas besoin d’une source électrique pour fonctionner. Cette décision fait suite à une
phase d’expérimentation sur Golfech 2, où deux cannes collectrons au rhodium avaient
été installées dans les assemblages H-02 et J-10 pendant le cycle 4 52.
La chambre collectron (au rhodium) consiste en une âme cylindrique en rhodium
de 400 mm de long et de 0,45 mm de diamètre qu’on appelle émetteur et qui délivre,
par activation du rhodium 103 puis radioactivité β−du rhodium 104 des électrons
collectés par un fil conducteur en inconel. Le rhodium est noyé dans un isolant électrique
constitué d’alumine (céramique Al2O3) enfermé dans un collecteur en Inconel.
Cet isolant minéral ne doit pas se détériorer sous un fort rayonnement et sous une
température d’environ 300 ◦C. Un fil conducteur de compensation permet par différence
de courant de ne mesurer que les électrons vraiment produits par le rhodium (il
produit un courant a priori identique à celui du fil conducteur seul). Le diamètre extérieur
de la chambre ne dépasse pas 1,4 mm. L’instrumentation comporte 16 cannes
de 8 chambres « collectron » étagées axialement de mesure de flux de neutrons par
activation de l’âme de rhodium (Figure 5.125). L’activation (n,γ) du rhodium 103
produit dans 93 % des cas du rhodium 104 fondamental, lui-même radioactif β−avec
une période de 42,3 secondes :
0n + 103
45Rh
→
145 barns
45Rh + γ
→
42,3s
□
46Pd + 0
−1e−
99, 551%
44Ru + 0
1e+
0, 449%
51 M. Grin : Collectrons, Self-powered neuron flux detectors, Part 1 : Theoretical considerations,
Rapport EUR 4775 e, Commission of the European Communities, 37 pages (1972).
52 Au sujet des essais sur Golfech 2, on lira avec profit le mémoire de Gilles Sardier : « Unité de
surveillance 3D en ligne et instrumentation interne fixe, étude des performances des collectrons au
rhodium », mémoire de CNAM, 27 octobre 2000.

<!-- page 647 (PDF 663) -->
Fig. 5.125 – Schéma axial d’une canne collectron.
Dans certains cas (7 % des captures), la capture neutronique donne un état métastable
radioactif (période 4,34 minutes) du rhodium 104, s’en suit une production de
rhodium 104 fondamental conduisant encore à une production d’électrons :
0n + 103
45Rh
→
11 barns
104m
Rh + γ
→
4,43 min
45Rh + γ′
Le rhodium 104 de la précédente équation est radioactif β−comme nous l’avons déjà
vu. Notons aussi que les photons émis par les réactions précédentes peuvent créer
instantanément des électrons par effets Compton et photoélectrique. Cette production
instantanée d’électrons est estimée à 6 %, ce qui fait qu’on peut décomposer
approximativement la production d’électrons en 87 % de production d’électrons avec
une période de 42,3 s, 7 % avec une période de 4,43 minutes et 6 % instantanée, ce
qui fait apparaître une composante prompte (les 6 %) et retardée (le reste) du signal.
Comme la composante est essentiellement retardée, on parle de collectrons à réponse
lente. On trouve dans cette catégorie (Tableau 5.7) les collectrons au rhodium (en
moyenne 68 s), en argent (51 s) ou au vanadium (5,4 minutes). Certains collectrons

<!-- page 648 (PDF 664) -->
Tab. 5.7 – Caractéristiques générales de différents types de collectrons usuels.
La consommation (usure sous rayonnement) du collectron est d’autant plus importante que
la section de capture est forte.
Émetteur
Rhodium
Argent
Vanadium
Cobalt
Platine
Abondance
isotopique
100 %
51,3 %
48,7 %
99 %
100 %
Nombreux
isotopes
Capture à
2 200 m/s
(barns)
5,66
Période des
isotopes
formés
42 s.
4,3 min.
(99,9 %)
2,3 min.
24, 2 s.
270 j
(5 %)
3,76 min.
5,26 ans
10,5 min.
+
négligeable
Réponse
complexe
(environ
20 % du
signal)
Sensibilité
(A/n.V/cm)
10−22
Ame en mm
(âme de
0,5 mm)
5,5
(0,5 mm)
2 (1 mm)
3,5
(1,5 mm)
0 ,7 (1 mm)
1,25
(1,4 mm)
0,2
(0,5 mm)
dont 80 %
de
gammas
Temps de
réponse à
63 %
68 s.
51 s.
5, 4 min.
Celui de la chaîne demesure
Consommation
de l’émetteur
en % pour un
flux de 1013
n.cm−2.s−1
3,9
2,4
0,16
1,12
0,2
Réponse lente
Réponse rapide
ont une réponse essentiellement prompte, comme le cobalt, le platine ou le hafnium,
du fait que le signal est principalement dû aux électrons Compton et photoélectrique
(environ 50 ms).
Dans le cas des collectrons au rhodium, on estime que la contribution instantanée
est donc de l’ordre de 6 %, et donc de 94 % pour la contribution retardée. Les électrons
émis par radioactivité, dont le spectre est continu, ont une énergie maximale suffisante
(2,44 MeV) pour traverser l’isolant et atteindre la gaine en créant un courant électrique
différé Iβ−. Les photons issus de la capture radiative arrachent des électrons
par effet photoélectrique ou effet Compton. Ces électrons peuvent aussi atteindre la
gaine et créent un courant instantané Iγ. Le courant mesuré est la somme de ces
deux courants Itotal = Iβ−+ Iγ. Si la composante retardée (créée par les électrons
issus de la radioactivité β−) est plus importante que la composante instantanée créée
par le rayonnement de photons, le détecteur est classé dans la catégorie des « collectrons
lents ”. C’est le cas des collectrons au rhodium ou au vanadium (la période du
vanadium 51 est de 3,76 minutes) qui fonctionnent sur le même principe. D’autres
collectrons utilisant le cobalt ou le platine sont des collectrons rapides où Iγ > Iβ−.
La gamme de courant attendue d’un collectron au rhodium est de 2 × 10−8 ampère
(correspondant à un collectron usé placé en périphérie d’un cœur à 5 %Pn) jusqu’à 8
× 10−6 ampère (pour un collectron neuf placé au centre d’un cœur à 109 %Pn). Le
courant de compensation varie quant à lui de 3 × 10−10 ampère à 5 × 10−7 ampère.
On estime que le courant émetteur diminue d’environ 70 % au cours de la vie du

<!-- page 649 (PDF 665) -->
Fig. 5.126 – Implantation des cannes collectrons dans Cattenom 113.
collectron (environ 8 ans) alors que le courant de compensation reste constant. Le
courant émetteur et le courant de compensation d’un même collectron sont amplifiés
et convertis en tension dans deux circuits de même gain. Le signal du collectron corrigé
est obtenu en soustrayant le signal de compensation du signal de l’émetteur. Un
filtrage analogique élimine ensuite le bruit et un convertisseur analogique/numérique
numérise le signal. Après numérisation, on déconvolue par un filtre de Kalmann le
signal pour prendre en compte le retard dû à la radioactivité du rhodium 104.
Ces considérations sur le retard du signal amènent un commentaire important : si
le collectron est lent, comme dans le cas du rhodium ou du vanadium, c’est-à-dire que
le courant retardé est prédominant sur le courant instantané produit par les photons,
le traitement du signal permet de remonter à l’activation neutronique de l’émetteur.
Si, par contre, le collectron est rapide comme dans le cas du cobalt (période du cobalt
60 : 5,27 ans), le courant instantané créé par les photons prédomine alors sur le courant

<!-- page 650 (PDF 666) -->
créé par l’activation par neutron. On accède donc alors à une production d’électrons
sous flux de photon. Hors ces photons proviennent partiellement de l’ensemble du
réacteur, en tout cas des assemblages proches (pour environ 15 % de la réponse du
collectron). En effet, le flux de photons est plus homogène que le flux de neutrons
car ils ont une portée plus lointaine que les neutrons. On parle d’effet lissant. Il n’est
pas exact de considérer que le flux de photons est proportionnel stricto sensu au flux
local de neutrons. Les collectrons au cobalt sont pilotés par le flux de photons dans la
mesure où la période du cobalt 60 produit par capture neutronique est de 5,27 ans, un
temps suffisamment long pour que la composante retardée soit faible. Ils proposent
donc une image plus floue du flux neutronique. En conclusion, plus la période de
l’émetteur β−est faible, plus l’image du flux de neutrons sera précise.
Les collectrons sont placés à des positions axiales fixes situées entre les grilles
des assemblages (Figure 5.125). Les cannes ont été introduites dans l’intercycle 12-13
et ont fonctionné depuis le 1er novembre 2003 au cours du cycle 13 (Figure 5.126),
placées dans 16 tubes d’instrumentations qui n’ont plus été disponibles pour les CFMs
du RIC. De fait, seules 42 positions sur les 58 habituelles restaient disponibles pour
le RIC, justifiant d’une appellation de « RIC dégradé ».
La réponse des signaux des collectrons est interprétée par un code de calcul
embarqué dans une unité de surveillance 3D dite « US3D », qui déploie en 3D les
erreurs de calcul par rapport aux mesures des collectrons pour déterminer des marges
d’exploitation. Dans la mesure où le RIC n’est pas complètement disponible (42/58),
on a affecté une pénalité au système SPIN de surveillance des marges en protection
du réacteur, pour prendre en compte ce RIC dégradé.

### 5.6.3 L’instrumentation interne de l’EPR

Le réacteur EPR dispose de deux systèmes internes de mesures d’activité. D’une
part, un système dit « Aéroball » de scrutation ponctuelle, d’autre part un système
de cannes collectrons au cobalt de scrutation continue, dont le principe a déjà été
présenté dans le cadre de l’expérimentation MARINE.

### L’instrumentation « aéroball »

Le système Aéroball est basé sur l’introduction dans le cœur actif de plusieurs trains
de billes. Des trains de petites billes d’acier dopé au vanadium, introduits depuis le
sommet de la cuve, sont transportés pneumatiquement (poussés par de l’azote) dans le
cœur (à l’intérieur de certains tubes guides d’assemblages, Figure 5.127, Figure 5.128).
Après un séjour dans le cœur de trois minutes, les trains de billes sont dirigés vers un
banc de comptage où l’activation de chacun d’eux est mesurée sur 30 points, en cinq
minutes. On obtient ainsi des valeurs locales d’activation qui permettent de remonter
par calcul au flux neutronique. Un traitement numérique permet de reconstituer la
distribution de puissance tridimensionnelle dans le cœur.
Ce système de mesure permet in fine l’élaboration des cartes de flux pendant le
fonctionnement de l’EPR. Il permet aussi le calibrage des détecteurs collectrons fixes.
Ces collectrons sont capables de délivrer une mesure de flux en continu et assurent la
fonction Protection (automatisme intervenant dans un délai très court), initialement
dévolue aux chambres externes des paliers précédents REP 900, 1300, et N4.

<!-- page 651 (PDF 667) -->
Fig. 5.127 – Principe des aéroballs.
Les trains de billes circulent dans des conduits et pénètrent dans la cuve du réacteur
nucléaire par le couvercle. Ils sont insérés et éjectés de la cuve par de l’azote
comprimé. Chaque train de billes circule dans un conduit qui lui est propre et indépendant
. La mesure de flux repose sur l’activation du vanadium contenu dans les
billes lorsqu’elles sont placées sous flux neutronique. Le comptage de l’activité de ces
billes se fait au moyen de détecteurs fixes placés sur des râteliers situés à l’extérieur
de la cuve, tout en restant dans le bâtiment réacteur. Les billes sont faites d’un alliage
d’acier avec 1,5 % de vanadium. Leur diamètre est de 1,7 mm. Elles circulent sous
forme de trains dans des tubes creux de 3 mm de diamètre extérieur. Il faut environ
2 500 billes pour couvrir la hauteur d’un cœur de réacteur EPR. Il y a autant de
trains de billes que d’assemblages à explorer soit 40 sur un réacteur EPR. Tous les
trains de billes sont insérés et éjectés de la cuve en même temps, ce qui veut dire qu’il
suffit d’une seule passe pour effectuer une carte de flux complète du cœur, contre onze
passages pour les CFMs du palier N4.
Sous flux neutronique, le vanadium 51 produit du vanadium 52 qui est radioactif
β−avec une période de 3,75 min en produisant du chrome 52 stable.

<!-- page 652 (PDF 668) -->
Fig. 5.128 – Emplacement de l’instrumentation interne l’EPR.
0n + 51
23V →52
23V + γ
23V
→
3,75m
24Cr + 0
−1e−
Le temps de séjour dans le cœur est approximativement de trois minutes. Le vanadium
a été choisi parce que sa période est courte, ce qui permet d’attendre peu de temps
pour que sa décroissance soit complète avant de refaire une carte de flux et d’enchaîner
éventuellement plusieurs cartes de flux toutes les quinze minutes.
Les valeurs de l’activation de ces billes sont proportionnelles au flux neutronique
dans le cœur. Après activation des billes en cœur, les trains sont envoyés vers des
râteliers de comptage (Figure 5.129). Il est important de noter que le nombre de râteliers
de comptage est inférieur au nombre de trains de billes. Il existe 10 râteliers
pour 40 trains de billes sur l’EPR. Comme on ne peut mesurer l’activité que d’un seul
train de billes à la fois par râtelier, il s’ensuit que ces trains de billes doivent attendre
leur tour avant de pénétrer dans le râtelier. Pour éviter la complexité mécanique liée
à des aiguillages qui permettraient de faire passer un train de billes de son conduit
d’attente au conduit de mesure, il a été décidé que les trains de billes resteraient
toujours dans le même conduit depuis le cœur jusqu’au râtelier. Le conduit de circulation
dans le cœur, le conduit de liaison entre le cœur et la position d’attente, et le
conduit de liaison entre la position d’attente et le râtelier de comptage ne font qu’un
afin d’assurer une continuité mécanique tout au long du parcours. Ceci a pour consé-

<!-- page 653 (PDF 669) -->
Fig. 5.129 – Schéma d’un râtelier de comptage.
quence que chaque râtelier de comptage ne possède pas un conduit de mesure, mais
quatre disposés à égale distance du détecteur. Il suffit ensuite de gérer la séquence de
comptage pour qu’un seul train de billes soit présent par râtelier lors du comptage.
Ainsi, les 10 râteliers peuvent mesurer simultanément un seul train de billes, ce qui
explique la nécessité de réaliser 4 mesures par râtelier correspondant aux 4 trains de
billes alloués à chaque râtelier. Les mesures de l’ensemble des trains ne sont donc pas
simultanées.
L’activité des billes est une image (retardée) de la distribution de flux dans
l’assemblage. La gamme de mesure du flux neutronique total est comprise entre
1012 et 5.1015 n.cm−2.s−1. La précision dans la gamme de flux de la valeur du flux
neutronique mesuré est inférieure à 1 %. Dans chaque râtelier, la mesure du taux de
comptage est assurée par 36 détecteurs indépendants les uns des autres (Figure 5.129).
Ces détecteurs sont collimatés de telle sorte que l’activité des billes voisines n’interfère
pas avec la mesure faite par le détecteur voisin. De même, les râteliers de comptage
sont séparés par des blindages appropriés. Les mesures des taux de comptage, soit
36 valeurs par trace axiale, sont envoyées à un calculateur. Chaque valeur d’une
trace axiale correspond à une hauteur active mesurée de 50 mm. Chaque centre de
détecteur est espacé avec un pas de 116 mm. Notons que la précision de la position
axiale de ces mesures est inférieure à 1,5 cm. Le dépouillement des mesures suit le
même principe que celui des chambres à fission mobiles (CFMs). Il faut donc passer de
la mesure d’une activité à une puissance. Des corrections sont faites pour tenir compte :
– du temps de transit dans le cœur de chaque bille puisque celui-ci dépend de la
position de la bille dans le train (la première bille d’un train est la première
à être introduite et la dernière à être retirée) ; problème de décroissance
radioactive des billes hors du cœur et prolongation de l’irradiation des billes
inférieures encore dans le cœur ;
– du temps de transit entre le cœur et la position d’attente (décroissance du
vanadium 52) ;
– du temps écoulé en position d’attente (toujours décroissance du vanadium 52).
Le processus complet incluant l’activation dans le cœur, les temps de transit, d’attente
, de comptage et de stockage informatique des mesures est de l’ordre de quinze
minutes. La très faible valeur du temps d’activation dans le cœur permet de faire une
véritable photographie instantanée du cœur et celui-ci n’a pas besoin d’être placé dans
des conditions parfaites de stabilité contrairement aux CFMs (36 heures à puissance

<!-- page 654 (PDF 670) -->
nominale). Ce temps de quinze minutes correspond effectivement à la décroissance
quasi complète du vanadium, ce qui permet d’enchaîner les cartes de flux si besoin.
La réalisation d’une séquence complète est entièrement automatique. Les trains de
billes sont stockés à l’extérieur de la cuve et des râteliers de comptage en dehors des
campagnes de mesure. Le calibrage des détecteurs utilisés sur les râteliers est assisté et
réalisé par ordinateur au moyen de sources gamma connues. Cette opération est effectuée
durant l’arrêt de tranche pour rechargement en combustible, soit une fréquence
comprise entre douze et dix-huit mois.
Concrètement, les trains de billes pénètrent dans la cuve par le couvercle et sont
ensuite acheminés à travers les internes supérieurs de cuve dans 40 assemblages, ce
qui représente une proportion d’environ 17 % d’assemblages instrumentés, soit 40
sur 241 assemblages formant le cœur EPR complet (contre 60 sur 205 assemblages
pour le N4 correspondant à 30 %). L’intérêt mécanique des trains de billes est leur
absence totale de rigidité, ce qui permet de circuler dans des conduits qui possèdent
des rayons de courbure très forts tels qu’on les rencontre dans les internes supérieurs.
Ces conduits, dont le diamètre extérieur est de 3 mm, sont placés dans des conduits
concentriques qui vont assurer le passage du gaz comprimé. Le diamètre extérieur
du conduit extérieur est de 6 mm. Ces conduits sont regroupés en sous-ensembles
de trois ou quatre introduits à l’intérieur d’une colonne verticale. Chaque colonne
est connectée à une lance horizontale à l’intérieur de laquelle chemine la grappe de
conduits. Ces conduits vont se séparer pour descendre ensuite verticalement dans
un doigt de gant fixé à la lance. Il y a autant de doigts de gant que de conduits
dans la colonne et la lance. La différence fondamentale avec l’instrumentation CFM
habituelle est que le doigt de gant est inséré dans l’un des vingt-quatre tubes guides
situés à son aplomb et non en position centrale de l’assemblage. On rappelle que
le tube central est effectivement remplacé dans un assemblage EPR par un crayon
combustible traditionnel.
Les colonnes traversent le couvercle et les orifices de sortie sont munis de joints
d’étanchéité. Il y a douze colonnes et douze lances dans un cœur de réacteur EPR.
À la sortie des colonnes, les conduits assurant le transport des billes et du gaz se
séparent et sont connectés, suivant leur fonction, à d’autres tubes dits tubes de liaison
installés à demeure réalisant, pour les uns la liaison mécanique avec les positions
d’attente et les râteliers de comptage, pour les autres la liaison avec le système de
mise en pression en azote.
Lors des opérations de déchargement, les connexions entre les conduits et les tubes
de liaison sont défaites, les joints d’étanchéité entre les colonnes et le couvercle sont
desserrés et le couvercle enlevé. L’ensemble colonne-lance-doigts est extrait hors du
cœur de manière solidaire. L’encombrement vertical total est d’environ onze mètres.
De cette façon, aucun raccord ni connexion, électrique ou mécanique, ne se trouve
dans la cuve, sous eau. Les opérations inverses sont effectuées pour le rechargement.
L’ensemble colonne-lance-doigts est introduit après avoir positionné les internes supérieurs
au-dessus du cœur. Un dispositif de guidage permet d’introduire les doigts de
gant dans les tubes guides des assemblages. Pour être tout à fait complet, il faut
ajouter que les lances comportent un doigt spécifique (donc un conduit) occupé par
une tige creuse à l’intérieur de laquelle sont installés les six collectrons au cobalt mentionnés
plus haut. Nous pouvons enfin noter que tous les assemblages comportant des
collectrons contiennent un aéroball.

<!-- page 655 (PDF 671) -->
Tab. 5.8 – Principales différences technologiques entre aéroballs et CFMs.
Aeroballs dans l’EPR
CFMs du palier N4
Assemblages instrumentés
40 sur 241 assemblages
soit 17 %
60 sur 205 assemblages soit 30 %
Positions axiales mesurées
par assemblage
Durée d’une campagne de
mesure
15 minutes
1 heure
Stabilisation en puissance
Pas nécessaire
Obligatoire pour carte complète
Pénétration en cuve
Couvercle
Fond de cuve
Sonde
Bille en acier à 1,5 % en
vanadium (99,7 % 51V)
Chambre
à
fission
à
l’oxyde
d’uranium enrichi à 90 % en
235U
Acquisition des mesures
Ex core
In core
Fréquence d’utilisation
maximale
Toutes les 15 minutes
Toutes les 76 heures
Intercalibration
Non
Obligatoire
On peut comparer le système Aéroball avec les CFMs des paliers actuels afin de
pouvoir comparer ces deux technologies (Tableau 5.8). Lors de la conception originelle
des réacteurs de type REP, on s’est rendu compte qu’il est très difficile, compte
tenu des difficultés technologiques que représente la mesure du flux neutronique
à l’intérieur du réacteur, de mesurer par le même système le niveau absolu et la
distribution spatiale de la puissance, tout en respectant les exigences de précision
et de temps de réponse souhaitées. Il a paru plus simple de séparer les fonctions en
faisant appel à deux systèmes d’instrumentation :
– l’un serait conçu et optimisé pour mesurer avec une très bonne précision et un
« moins bon » temps de réponse la distribution de puissance en trois dimensions ;
– l’autre serait chargé de mesurer la distribution de puissance et le niveau de
puissance avec un très bon temps de réponse et une « moins bonne » précision.
C’est pourquoi un système interne, mesurant le flux neutronique à l’intérieur du
cœur (système RIC utilisant les CFMs), et un système externe placé à l’extérieur de
la cuve (chambres RPN), coexistent dans les REPs français.
Il peut paraître surprenant que le nombre d’assemblages instrumentés dans
l’EPR soit inférieur à celui des anciens paliers. Pour des raisons économiques et de
complexité technologique, on a cherché à minimiser le nombre d’aéroballs. Une étude
paramétrique réalisée par Framatome a montré que l’impact sur le facteur du point
chaud du passage de 58 à 40 aéroballs est inférieur à 2 %.
Le temps mis pour l’élaboration d’une carte de flux complète peut donc durer
jusqu’à 48 heures avec les CFMs, en comptant la durée de stabilisation parfaite du
cœur en puissance (de quelques heures à 2 jours) et la durée d’acquisition des mesures
(environ une heure). Le temps de mesure par les aéroballs est donc significativement
inférieur, étant donné que les toutes les billes en acier ne restent en cœur que trois
minutes. Aucune stabilisation n’est nécessaire pendant la mesure. La réalisation d’une
carte de flux complète ne prend pas plus que quinze minutes. La non-stabilisation en
puissance du cœur permet aussi à l’exploitant d’effectuer un suivi de charge qui n’est
pas possible pendant les campagnes de mesures avec les CFMs.

<!-- page 656 (PDF 672) -->
L’instrumentation interne fixe de l’EPR
L’instrumentation fixe est constituée de détecteurs de neutrons appelés collectrons
et de thermocouples 53, pour mesurer les distributions radiale et axiale du flux neutronique
dans le cœur, et la distribution radiale de la température à sa sortie. Les
mesures neutroniques sont utilisées pour le pilotage de la distribution axiale de puissance
et pour la surveillance et la protection du cœur. Les thermocouples mesurent
en continu la température en sortie des assemblages de combustible. Ils fournissent
des signaux utilisés pour la surveillance du cœur (détection de perte d’eau primaire).
Ils fournissent aussi des informations sur la distribution radiale de puissance et sur
les conditions thermohydrauliques locales.
Les collectrons au cobalt
Un collectron au cobalt se présente sous la forme d’un câble coaxial de très petit
diamètre de l’ordre de 1 à 2 mm. Nous ne reviendrons pas ici sur le principe de
fonctionnement d’un collectron que nous avons déjà présenté dans un paragraphe
précédent sur l’expérimentation MARINE. Comme nous avions présenté en détail les
collectrons au rhodium, nous nous intéresserons plus ici aux collectrons au cobalt.
Notons que la sensibilité des collectrons dépend des paramètres physiques suivants :
– section efficace de l’émetteur ;
– volume et forme géométrique de l’émetteur ;
– nombre et énergie des particules β−;
– spectre γ de capture ;
– épaisseur massique de l’isolant ;
– auto-absorption de l’émetteur.
Sensibilité et durée de vie sont deux paramètres antagonistes, car la durée de vie
d’un collectron est inversement proportionnelle à la section efficace de l’émetteur.
Le temps de réponse d’un collectron est gouverné par les phénomènes physiques mis
en jeu dans l’émetteur. Les collectrons, dont la réponse est majoritairement due à
une ou plusieurs voies de désintégration β−, subissent l’influence de la période de
désintégration. Les collectrons qui produisent des électrons par effet Compton ont un
temps de réponse immédiat. Il faut aussi tenir compte des caractéristiques de la liaison
électrique : résistance et capacité globales, qui déterminent la constante de temps du
circuit RC, dépendent du produit longueur par résistance et capacité linéiques. Le
temps de réponse d’un collectron au cobalt est inférieur à 100 ms ; il peut atteindre
des valeurs de l’ordre de 1 min pour le rhodium, de 5 min pour le vanadium.
Le problème du bruit sur le signal collectron est un problème délicat car les sources
de bruit sont nombreuses : les principales sont liées à l’activation des matériaux voisins
, aux rayonnements β et γ des produits de fission et aux rayonnements γ de fission
et de capture. De plus, une certaine catégorie de rayonnements γ étant différée, l’influence
de ceux-ci se traduit par une dégradation du temps de réponse. La conséquence
est que, dans tous les cas, le rapport signal sur bruit d’un collectron est plus mauvais
que celui d’une chambre à fission. On distingue le bruit sur l’émetteur et le bruit sur
le câble. Tous les composants sont affectés : l’émetteur, le fil conducteur dans le câble,
l’isolant et la gaine. Dans le cas des collectrons au cobalt, au signal prompt, se superpose
un signal parasite retardé dont l’amplitude varie avec le temps, proportionnelle
53 Sur la technologie des thermocouples, on lira avec intérêt [Asch et al., 2006] p. 231.

<!-- page 657 (PDF 673) -->
à la fluence reçue, dû à la formation dans l’émetteur de cobalt 60 qui est un isotope
radioactif β−. Cette composante parasite va croître jusqu’à représenter plus de la
moitié du signal utile. Cependant, la période du cobalt 60 étant d’environ 5,3 ans,
l’influence de cet isotope peut être considérée comme nulle sur la dynamique utile du
signal. Il suffit alors de la retrancher périodiquement du courant total, en particulier
avant chaque divergence après rechargement. Cette correction peut se faire soit par
une compensation analogique, soit par logiciel. Les réacteurs construits par la société
Siemens sont équipés de cannes cobalt pour une utilisation s’apparentant à une utilisation
en protection. Les données suivantes se rapportent au collectron au cobalt
développé par Siemens pour le réacteur allemand Konvoi (Tableau 5.9, Figure 5.130,
Figure 5.131).
Tab. 5.9 – Composition d’un collectron au cobalt.
Élément
Matériau
Composition
Densit(g/cm3)
Émetteur
Cobalt
59Co
8,7
Isolant
Al2O3
Mélange isotopique :
3,57
20 %27Al
30 % 16O
Collecteur
Inconel 600
Mélange massique :
64,56% Chrome naturel
8,2
33,32 % Fer naturel
2,08 % 55 Mn
0,03 % Nickel naturel
Fig. 5.130 – Schéma d’un collectron au cobalt.
Le collectron au cobalt voit sa composition en cobalt 59 diminuer du fait de la
capture neutronique de ce dernier en cobalt 60 (Figure 5.132). Cet épuisement est
suffisamment significatif pour modifier la réponse du collectron.
Les collectrons se trouvent dans 12 assemblages tous instrumentés avec le système
Aéroball. Cette proximité permet en effet le calibrage des collectrons par les aéroballs.
Pour finir, ces collectrons sont placés diamétralement opposés aux aéroballs dans les
assemblages (Figure 5.133). Le cobalt 59 présent dans cette technologie modifie aussi
le flux neutronique. Certains assemblages sont donc doublement dissymétriques de
par la présence des aéroballs et des collectrons.

<!-- page 658 (PDF 674) -->
Fig. 5.131 – Coupe radiale de la modélisation d’un collectron au cobalt.
Fig. 5.132 – Chaîne du cobalt.
