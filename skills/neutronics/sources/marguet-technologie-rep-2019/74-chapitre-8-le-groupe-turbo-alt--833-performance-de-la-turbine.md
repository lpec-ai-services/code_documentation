# Chapitre 8 Le groupe turbo-alternateur et la production d’électricité — 8.3 La turbine — 8.3.3 Performance de la turbine … 8.3.8 Rupture d’une ailette de turbine
<!-- source PDF pages 1023-1039 -->

<!-- page 1007 (PDF 1023) -->
Fig. 8.27 – Principe d’un clapet d’interception (adapté de [Turbines à vapeur, 1968]
p. 66).
La vapeur transmise par les soupapes est dirigée vers un tore d’admission qui est
une chambre annulaire d’alimentation des premiers aubages fixes (Figure 8.26).
Si la technologie a amélioré notablement ces différents organes de commande, le
principe en est resté le même.

### 8.3.3 Performance de la turbine

Notion de cycle thermodynamique
Quelques éléments de thermodynamique sont nécessaires pour comprendre la production
d’énergie à partir de la force motrice de la vapeur d’eau. Un cycle idéal

<!-- page 1008 (PDF 1024) -->
Fig. 8.28 – Principe d’une soupape modératrice (adapté de [Turbines à vapeur, 1968]
p. 67).
de Carnot 15 présente comme caractéristique essentielle que son rendement est
indépendant du fluide utilisé. En pratique bien sûr, la nature du fluide est importante
. Dans le cas qui nous intéresse, l’eau liquide est chauffée par le réacteur et cède
15 Nicolas Léonard Sadi Carnot (1796-1832) : physicien français (à ne pas confondre avec le
président de la République française Marie François Sadi Carnot), il est le fils de Lazare Carnot,
lui-même mathématicien, physicien et homme politique connu (surnommé « l’organisateur de la
Victoire »). Polytechnicien en 1814, c’est grâce à son unique ouvrage de 1824 de 120 pages tiré à
ses frais à 200 exemplaires chez l’éditeur Bachelier « Réflexions sur la puissance motrice du feu
et sur les machines propres à développer cette puissance ” qu’on le considère comme le père de
la thermodynamique moderne. Ses travaux portent sur les machines à vapeur. Il établit qu’il est
impossible de produire de la puissance motrice à moins qu’on ne dispose à la fois d’un corps froid et
d’un corps chaud, ce qui n’est autre qu’une expression du deuxième principe de la thermodynamique,
et décrit dans son ouvrage un moteur parfait régi par un cycle idéal parfaitement réversible, ce qu’on
appellera plus tard le cycle de Carnot. Après sa mort, on a retrouvé dans ses effets un texte de 1823
intitulé « Recherche d’une formule propre à représenter la puissance motrice de la vapeur d’eau »
qui est l’ébauche du premier principe de la thermodynamique sur l’équivalence entre le travail et la
chaleur. Le théorème de Carnot précise que « Deux moteurs thermiques réversibles qui fonctionnent
avec deux sources de chaleur dont les températures de source froide sont égales et celles de source
chaude aussi, ont le même rendement ».
Sadi Carnot peint par Louis Léopold Boilly.

<!-- page 1009 (PDF 1025) -->
son énergie au circuit secondaire par l’intermédiaire des générateurs de vapeur, puis
la vapeur se détend dans la turbine. Les calories permettant le retour à l’état liquide
sont cédées au condenseur alimenté par la source froide (rivière ou l’eau de l’aéroréfrigérant
). Les transformations adiabatiques (ou quasi adiabatiques dans la réalité) se
font dans la turbine et dans les pompes alimentaires. Si T1 est la température de la
vapeur et T2 celle de la source froide idéale, le cycle de Carnot est représenté dans le
diagramme (Température-Entropie) par un rectangle (Figure 8.29).
Fig. 8.29 – Différents cycles thermodynamiques dans le diagramme températureentropie
. À gauche le cycle de Carnot, au milieu le cycle de Rankine, à droite le cycle de
Hirn (adapté du cours Turbomachines de M. Riollet, École centrale des Arts et Manufactures,
1972).
Par rapport au cycle idéal de Carnot, l’utilisation d’un fluide réel dégrade les
performances. En effet, l’échauffement isobare s’effectue à une température inférieure
à T1, comme on le voit sur le trajet BC du cycle de Rankine 16. Si on cherche à
améliorer le rendement du cycle en augmentant la température de vaporisation T1,
on s’aperçoit qu’on diminue le palier CD au profit de l’échauffement isobare. Ce palier
va même disparaître à la température du point critique de l’eau (374 ◦C), alors que
les matériaux de la chaudière pourraient supporter des températures supérieures 17.
Enfin, le fluide se charge en eau liquide au cours de la détente et la masse croissante
d’eau condensée introduit de l’irréversibilité dans la détente de la turbine, ainsi que
16 William John Macquorn Rankine (1820-1872) est un ingénieur et physicien écossais. Rankine
vulgarisa la théorie des machines à vapeur au travers de plusieurs manuels largement utilisés dans
l’industrie. À partir de 1840, il produit une abondante littérature scientifique faite d’articles et de
communications dans des domaines aussi variés que les mathématiques, la botanique ou la résistance
des matériaux. On lui doit la relation entre température et pression de vapeur saturante (formule de
Rankine).
William Rankine
17 Ce qui pourrait suggérer l’utilisation éventuelle de fluide à température plus élevée (vapeur de
mercure, hexane. . . ), ce qui présente bien sûr d’autres inconvénients majeurs à l’échelle des grandes
puissances.

<!-- page 1010 (PDF 1026) -->
des risques d’érosion mécanique. En dernier lieu, il y a d’inévitables pertes calorifiques
par les parois des composants (turbine, condenseur, pompes. . . ). En combinant tous
ces effets négatifs, le rendement du cycle de Rankine ne peut espérer dépasser dans
la pratique 0,3. On améliorera notablement le rendement en introduisant la notion
de surchauffe de la vapeur dans le cycle de Hirn (trajet DE). De cette façon, le
titre en fin de détente se rapproche de l’unité et est supérieur au titre obtenu dans
le cycle de Rankine. Le cycle de Hirn 18 augmente l’irréversibilité du chauffage et le
rendement dit exergétique diminue. En augmentant la pression maximum, on améliore
le rendement du cycle de Hirn. On peut imaginer plusieurs resurchauffes, mais dans
les faits, l’efficacité demeure constante, le gain portant alors sur la teneur en eau qui
est réduite. Dans le cas des turbines nucléaires, la surchauffe est effectuée en prélevant
de la vapeur directement depuis les lignes vapeur en sortie de GV. En plus du gain de
rendement, cette surchauffe diminue l’humidité de la vapeur, ce qui protège les aubes
de la turbine.
Il est possible de rendre équivalent un cycle de Rankine à un cycle de Carnot grâce
à un réchauffage continu de l’eau d’alimentation. L’idée est de soutirer du fluide au
même niveau thermique, c’est-à-dire en cours de détente. Comme il n’est pas techniquement
réalisable de mettre tout le débit de vapeur réchauffant l’eau d’alimentation,
le réchauffage peut être néanmoins effectué par des soutirages étagés au cours de la
détente. Ce réchauffage discontinu permet de libérer une certaine quantité de vapeur
qui va libérer la chaleur utilisée par un étage de réchauffage. L’exemple présenté en
Figure 8.30 utilise des réchauffeurs par mélange (l’indice i représentant les débits),
P1 est la pompe d’extraction du condenseur et les Pi des pompes de charge.
La configuration d’un poste d’eau industriel (Figure 8.31) tire parti de la configuration
des réchauffeurs, et minimise le nombre de pompes en n’utilisant qu’une pompe
d’extraction à la sortie du condenseur et une pompe alimentaire qui récupère l’eau
en sortie de la bâche alimentaire. La bâche alimentaire sert de réservoir tampon pour
encaisser d’éventuelles baisses de charge.
Application à une turbine de réacteur nucléaire
La Figure 8.32 présente les caractéristiques physiques en régime nominal de l’eau et de
la vapeur au cours du passage dans la turbine. La pression à l’échappement des corps
18 Gustave-Adolphe Hirn (1815-1890) est un ingénieur et physicien français, auteur d’une Théorie
mécanique de la chaleur, exposition analytique et expérimentale de la théorie mécanique de la
chaleur, Tome 1, Gauthier-Villars en 1875. Hirn s’intéressa à la chaleur et à la thermodynamique,
mais aussi à la mécanique, l’hydrodynamique (Explication d’un paradoxe hydrodynamique, Gauthier-
Villars, 1881), la cosmologie (Constitution de l’espace céleste, Gauthier-Villars, 1889). Sa statue par
le sculpteur Bartholdi siège dans sa ville : Colmar.
Gustave-Adolphe Hirn et son ouvrage

<!-- page 1011 (PDF 1027) -->
Fig. 8.30 – Principe du réchauffage de l’eau alimentaire par soutirages discontinus
(adapté du cours Turbomachines de M. Riollet, École centrale des Arts et Manufactures,
1972).
Fig. 8.31 – Poste de réchauffage d’une turbine industrielle de puissance (adapté
du cours Turbomachines de M. Riollet, École centrale des Arts et Manufactures, 1972).
BP n’est plus que de 50 à 70 mbars, ce qui signifie que la pression dans le condenseur
est très inférieure à la pression atmosphérique (on parle même par abus de langage de
« vide » au condenseur). Notons que la mise sous vide du condenseur crée des efforts
considérables (dits « poids du vide ») reportés sur la dalle (le condenseur accostant
la dalle par le dessous), que la conception du supportage doit prendre en compte.
D’un point de vue rendement thermodynamique, plus la pression de condensation
est basse, et plus l’énergie récupérée à partir de la vapeur est importante, d’où une

<!-- page 1012 (PDF 1028) -->
Fig. 8.32 – Fonctionnement nominal d’une turbine CPY.
amélioration du rendement. On gagne encore en rendement si on réchauffe l’eau en
sortie de condenseur avec de la vapeur soutirée aux corps BP en cours de détente.
On parle de réchauffage de l’eau alimentaire avant passage dans les GVs où elle sera
revaporisée en cycle fermé.
On définit conventionnellement la consommation spécifique de chaleur du groupe
turbo-alternateur par la formule :
Cs[kJ/kW h] ≡Qv
Hv −He
We + WT P A
Avec Qv le débit de vapeur à l’entrée de la turbine, Hv est l’enthalpie de la vapeur à
l’entrée de la turbine, He est l’enthalpie de l’eau à l’entrée du GV, We est la puissance
électrique brute pour une valeur de déphasage cos ϕ de 0,9 et WT P A la puissance sur
l’arbre des turbopompes alimentaires. La valeur de la consommation spécifique est
classiquement exprimée en kJ/kWh et vaut environ 10 000 kJ/KWh pour un réacteur
du palier P’4 pour une valeur du vide au condenseur de 52 mbars (pression d’échappement
BP). La consommation spécifique de chaleur du GTA est sensible à de nombreux
paramètres : qualité du vide au condenseur, débit des purges APG, débit de surchauffe,
et même une fuite des faisceaux de surchauffe des groupes sécheurs/surchauffeurs qui
peut modifier la puissance de la tranche de plusieurs dizaines de MW. Les conditions
aux limites du GTA sont le titre en eau de la vapeur d’admission à l’entrée de la
turbine haute pression (HP) 19, la pression de vapeur à l’entrée de la turbine HP et
la pression de vapeur à l’échappement de la turbine basse pression (BP).
Le régime nominal de conception est décrit par le concepteur dans les conditions
d’utilisation normalisées à savoir, pour un groupe P’4 par exemple : 3 817 MWth de
19 Le titre en sortie de turbine HP peut être mesuré par traçage radioactif ou par mesure d’humidité
, et vaut environ 14 % pour un P’4.

<!-- page 1013 (PDF 1029) -->
Fig. 8.33 – Effet du débit des purges APG sur la puissance électrique (en MWe)
par rapport à la référence (à purges nulles) et sur la consommation spécifique de chaleur (en
kJ/KWe) du GTA.
charge thermique nominale, les purges GV sont isolées (circuit APG fermé, le débit
des purges APG joue sur la puissance électrique de la tranche), la surchauffe est au
débit nominal (200 kg/s), le débit d’appoint est isolé et sans secours en service.
La puissance électrique fournie par une turbine est donnée à partir de la puissance
turbine par :
P´electrique[MW e] = η´electrique × ηm´ecanique × Pturbine[MW th] = ηglobal × Pturbine[MW th]
Le rendement mécanique ηm´ecanique dépend de la charge, le rendement électrique
η´electrique dépend de la puissance électrique et du déphasage (cosφ ≈0, 9). On donne
dans le Tableau 8.1 suivant les ordres de grandeur pour une turbine Alsthom de CP0 :

<!-- page 1014 (PDF 1030) -->
Fig. 8.34 – Effet du débit de surchauffe sur la puissance (en MWe) par rapport à la
référence (à 200 kg/s) et sur la consommation spécifique de chaleur (en kJ/KWe) du GTA.
Tab. 8.1 – Rendements de la turbine ALSTHOM lors des essais de démarrage de
Saint-Laurent B1 pour plusieurs paliers de puissance (dans l’ordre : puissance turbine en
MWth, puissance électrique en MWe, rendement global, rendement mécanique, rendement
électrique).
100% Pn
943,14
925,6
0,9812
0,9892
0,9920
70% Pn
663,09
647,9
0,9771
0,9897
0,9873
50% Pn
476,4
462,8
0,9714
0,9890
0,9822
30% Pn
290,2
277,7
0,9568
0,9868
0,9696

<!-- page 1015 (PDF 1031) -->
### 8.3.4 Détente du fluide dans la turbine

Le rendement isentropique d’une détente d’une pression P0 à une pression P1 plus
basse (Figure 8.35) est donné par :
ηisen[%] ≡
h0 −h1
h0 −hisen
Fig. 8.35 – Définition du rendement isentropique.
La difficulté pour évaluer cette quantité est de définir une ligne de détente de référence
pour le fluide. Des essais utilisant des traceurs radioactifs pour mesurer le titre
en eau de la vapeur en sortie de turbine HP (essai sur Saint-Alban, Figure 8.36) ont
conduit à une valeur de 13,9 %. On sait que le rendement isentropique est globalement
proportionnel au taux d’humidité. On arrive ainsi à des rendements isentropiques
d’environ 86 %, 82 % et 79 % pour les 3 étages successifs du corps HP et 91 %, 90 %,
87 % et 89 % pour les 4 étages successifs du corps BP, toujours dans l’exemple du
P’4. Le rendement de la détente est sensible au premier ordre au taux d’humidité X
de la vapeur, ce qui nécessite une correction par rapport à une mesure lors d’un essai,
selon la loi de Bauman :
ηisen[%] ≡ηessai[%]
Xth´eorique
Xessai

### 8.3.5 Érosion dans la turbine

Une des conséquences extrêmement néfastes du taux d’humidité de la vapeur sur les
pales de la turbine est l’érosion. Si les gouttelettes d’eau qui se forment pendant la
détente sont de tailles suffisamment petites pour être entraînées par l’écoulement,
l’eau et la condensation sur les parties fixes (dont les ailettes fixes du stator) de
la turbine produisent de grosses gouttes en se détachant. La vitesse de la vapeur
est approximativement de direction tangente aux surfaces des ailettes mobiles quand
les gouttelettes d’eau viennent s’écraser sur le bord d’attaque des ailettes, ce qui
produit une intense érosion mécanique du bord d’attaque. Plus la vitesse périphérique
des roues d’aube est importante (c’est-à-dire au niveau des derniers étages de la
turbine), et plus l’érosion est intense puisque la vitesse relative de l’eau est plus grande,
donc une énergie cinétique à l’impact plus grande. C’est cet argument principalement

<!-- page 1016 (PDF 1032) -->
Fig. 8.36 – Courbe de détente de la turbine de Saint-Alban 1, essai du 5 février
1987.
qui fait que la vitesse de la turbine est limitée à 1 500 tours/minute, pour assurer
une certaine longévité à la turbine. Des traitements mécaniques de l’acier du bord
d’attaque (comme le stellitage) permettent d’améliorer la résistance à l’érosion.
Bien entendu, il est utile de diminuer au maximum le taux d’humidité de la vapeur.
Comme le type de GV Westinghouse n’autorise pas la surchauffe de la vapeur, la
déshumidification par les cyclones et les chevrons dans le corps supérieur des GVs,

<!-- page 1017 (PDF 1033) -->
est très importante, mais ne suffira pas pour obtenir une qualité correcte de vapeur
dans les étages basse pression et de toute façon de l’eau liquide apparaît lors de la
détente dans le corps HP. D’où le rôle de la surchauffe de la vapeur après l’étage haute
pression, en prélevant de la vapeur juste après le barillet vapeur. Dans la mesure où
la baisse d’enthalpie disponible, du fait de la relativement basse température de la
vapeur (environ 280 ◦C à 70 bars) par rapport à la vapeur d’une centrale thermique
traditionnelle à combustible fossile (environ 565 ◦C à 163 bars), fait que pour une
puissance identique, une turbine REP devra disposer d’un débit de vapeur environ
deux fois plus important pour compenser la baisse de rendement observé sur un REP
(environ 33 %). Cela conduit à un dimensionnement plus important de la section
d’échappement de la turbine, des tuyauteries vapeur, du volume du condenseur et du
poste d’eau (pompes et réchauffeurs). Le mauvais rendement de la turbine peut être
notoirement amélioré en soutirant de la vapeur au cours de la détente dans les corps.
Cette vapeur soutirée est intéressante pour réchauffer l’eau d’alimentation des GVs
(circuit ARE), permettant d’augmenter le point de fonctionnement des GVs. Cette
vapeur, qui est « détournée » progressivement (6 soutirages sur Fessenheim : 3 sur
le corps HP et 3 sur les corps BP) de la turbine, permet une réduction favorable des
sections d’échappement de la turbine, du volume du condenseur, du débit d’eau de
circulation et du débit des pompes d’extraction d’eau condensée.

### 8.3.6 Ouverture du débit d’une turbine

La caractérisation d’un corps de turbine peut se faire via le nombre de Stodola 20 St,
défini par :
Q ≡St
□
P 2
O −P 2
T0
Dans l’exemple d’une turbine P’4, ce nombre a pour valeur approximative 2,6 pour
le premier étage du corps HP, puis 6 et 8,3 pour les étages suivants du corps HP et
11, 30, 115 et 413 environ pour les étages du corps BP.

### 8.3.7 Régulation de la turbine

Réglage primaire
Le groupe turbo-alternateur est soumis à deux couples : le couple moteur assuré par
le débit de vapeur, et le couple résistant créé par les consommateurs à l’extrémité
20 Aurel Boreslav Stodola (1859-1942) est un physicien slovaque, professeur à l’École polytechnique
fédérale de Zurich, où il enseigne le génie mécanique entre autres à Albert Einstein. Il publie
en 1903 un traité sur les turbines à vapeur. On lui doit la loi relative à la variation de pression dans
une turbine, et un nombre sans dimension relatif au débit d’une turbine à vapeur qui porte son nom.
Aurel Stodola

<!-- page 1018 (PDF 1034) -->
du réseau. La vitesse du GTA est constante à l’équilibre de ces deux couples. Si le
couple résistant augmente du fait de la croissance de la consommation, la vitesse du
GTA diminue, et inversement si le couple résistant diminue. La puissance fournie par
la vapeur peut être modulée en jouant sur les soupapes d’admission vapeur. On s’est
arrangé pour qu’une variation de 1 hertz (bande totale de 2 hertz) par rapport à
la consigne nominale de 50 hertz, correspondant à une variation de vitesse de 4 %,
induise une ouverture des soupapes de 0 à 100 %. La régulation dite « primaire »
ou « réglage primaire » (Figure 8.37), consiste à mesurer la vitesse de l’arbre, à la
comparer par rapport à une vitesse de consigne (1 500 tours/minute), et à appliquer
l’écart à un régulateur à action proportionnelle dont le gain (K = 25) correspond à
une action sur la vitesse de 4 %. Ainsi, pour une variation de 2 hertz, l’ouverture des
soupapes passe de 0 à 100 %. La droite liant charge et fréquence est appelée « droite
de statisme » (Figure 8.38).
Fig. 8.37 – Principe général de la régulation turbine en fonction de la fréquence.
Mais assurer l’égalité en production et consommation n’assure pas que la vitesse
du GTA soit à sa valeur de consigne optimale. Ceci est assuré par une action manuelle
appelée « plus ou moins vite » (Figure 8.39). Une impulsion sur le + (resp. –) provoque
une ouverture (resp. une fermeture) des vannes d’admission vapeur, d’où une
augmentation (resp. diminution) de la vitesse. Cette variation de vitesse est détectée
par la régulation primaire qui ramène le couple moteur au couple résistant en
refermant (resp. rouvrant) les soupapes d’admission. Le résultat de cette action est
une translation vers la droite (resp. vers la gauche) de la droite de statisme. Dans la
pratique d’un réseau couplé à plusieurs moyens de production, il faut s’assurer que la
production sera suffisante. Pour ce faire, chaque groupe reçoit d’un jour sur l’autre une
consigne de puissance dite « P0 », évaluée sur le plan national en fonction des capacités
des autres tranches et du retour d’expérience acquis dans l’analyse des consommations
des années précédentes. Cette consigne prévisionnelle ne doit pas s’imposer à
la régulation primaire, qui est prioritaire pour égaliser production et consommation.
Pour ce faire, la consigne de puissance est décalée de la valeur KΔF d’écart de fréquence
imposée par la régulation primaire. La mesure de puissance est alors égale à la
valeur de consigne à laquelle a été ajoutée la correction primaire. Cette correction est

<!-- page 1019 (PDF 1035) -->
51 Hertz
50 Hertz
49 Hertz
Charge et ouverture
des soupapes
0 %
50 %
100 %
Fig. 8.38 – Droite de statisme d’un GTA.
51 Hertz
50 Hertz
49 Hertz
Charge et ouverture
des soupapes
0 %
50 %
100 %
Point optimal de
fonctionnement
Point initial de
fonctionnement
après régulation
primaire
Fig. 8.39 – Correction de vitesse par action « plus ou moins vite ».
enfin retranchée au signal de commande d’ouverture des vannes d’admission pour
compenser en dynamique l’action proportionnelle du régulateur proportionnel
intégral (PI).
Supposons qu’une tranche CPY (900 MWe) produise 750 MWe (83,33 % Pnom)
selon la demande, et que le réseau soit équilibré à 50 hertz. Un gros consommateur
apparaît brusquement sur le réseau et la fréquence chute de 0,1 hertz. Un écart

<!-- page 1020 (PDF 1036) -->
apparaît entre la vitesse de la turbine qui ralentit et la consigne. La régulation primaire
s’engage pour effectuer une augmentation de puissance égale à :
ΔP = Pnom ×
ΔF
2Hertz = 900 × 0, 1
= 45MWe
Dans le même temps, la consigne de puissance réelle est augmentée à 795 MWe et le
signal de KΔF = 45MWe. On notera que la consigne de puissance affichée reste à
750 MWe, mais que la consigne réelle est bien de 795 MWe.
L’opérateur dispose de trois modes de fonctionnement. En mode manuel
(Figure 8.40), l’opérateur agit avec la commande « plus ou moins vite » déjà
décrite. Il peut ouvrir ou fermer partiellement les vannes d’admission sur demande du
dispatching, mais la régulation primaire reste effective. Le mode direct ressemble au
mode manuel, mais les variations de charges sont effectuées en utilisant le générateur
de pentes du consignateur de puissance à la place du « plus ou moins vite ». C’est en
quelque sorte une graduation préprogrammée du « plus ou moins vite », mais sans
asservissement de la puissance par la régulation primaire. En mode automatique, le
réglage est totalement automatisé (Figure 8.41). La mesure de fréquence est comparée
à la consigne et le signal d’ouverture/fermeture des vannes d’admission VVP est
généré par un régulateur PI de manière à ce que l’écart devienne nul. La régulation
primaire reste engagée (Figure 8.42).
Fig. 8.40 – Régulation en mode manuel ou direct.
Réglage secondaire
Une variation de fréquence importante ne peut être reprise par une seule tranche,
mais nécessite une action simultanée d’un grand nombre de tranches, voire de l’ensemble
du parc. Cette action simultanée sur plusieurs tranches ne peut être effectuée
qu’automatiquement par un signal unique émis par un organisme centralisé
(le dispatching national) : c’est le téléréglage. La fréquence du réseau national est
mesurée et comparée par rapport à une consigne (50 hertz). Par un intégrateur, on
en déduit un signal unique de niveau N (t) en fonction du temps, signal qui varie
entre +1 et –1. Ce signal est envoyé par onde porteuse sur le réseau et reconnu par
les tranches en production (Figure 8.43). Chaque tranche possède un commutateur

<!-- page 1021 (PDF 1037) -->
Fig. 8.41 – Schéma général de la régulation turbine.
Fig. 8.42 – Régulation du GTA avec consigne de puissance.
permettant de régler sa contribution au téléréglage. Cette contribution peut être nulle
ou au maximum de ± 5 % Pnom. La consigne de puissance est alors décalée d’une
valeur qui dépend du niveau et du taux de contribution réglé par le commutateur.

<!-- page 1022 (PDF 1038) -->
Fig. 8.43 – Régulation en téléréglage.
La consigne réelle de puissance est alors égale à la consigne affichée à laquelle on
ajoute le KΔF et le téléréglage N(t) × 5 % × participaton.
Notons enfin que la loi d’ouverture des vannes VVP n’est pas une droite en
fonction de leur débit, ce qui fait que, pour que le signal de commande corresponde
à la consigne de charge, il faut linéariser le débit vapeur par rapport au signal de
commande (par l’adjonction de cames électroniques dans le cas du CP1), ce qui
nécessite une régulation supplémentaire de la position des organes d’admission. Cette
position est mesurée et asservie au signal de commande.

### 8.3.8 Rupture d’une ailette de turbine

Un accident redouté est la rupture d’une ailette de turbine, dont l’effet missile peut
être dévastateur. L’accident survenu à la centrale américaine de Donald C. Cook en
septembre 2008, en est un exemple symptomatique.

<!-- page 1023 (PDF 1039) -->
Le 20 septembre 2008 à 20 h 05, l’opérateur enregistre de très fortes vibrations des
paliers de la turbine, qu’on peut entendre auditivement en salle de commande. Il active
l’arrêt d’urgence en 5 secondes et la turbine s’arrête en moins de 2 minutes. Mais un
feu d’hydrogène (refroidissement de l’alternateur) se déclenche dans l’alternateur, qui
sera arrêté à 20 h 28 par les pompiers, malgré quelques défaillances non vitales du
système incendie. Le feu a endommagé sévèrement l’alternateur et l’excitatrice.
L’analyse post-mortem a montré que trois ailettes (n◦40, 56 et 189) du corps
basse pression B (Figure 8.44) avaient été arrachées, provoquant une déformation du
capot de corps visible à l’œil nu (Photo 8.10), mais sans éclatement du capot.
Fig. 8.44 – Présentation générale de la turbine de DC Cook.
Photo 8.10 – Effet de l’impact de l’éjection de l’ailette n◦40 sur le capot du
corps basse pression B (d’après une présentation à la NRC de Joe Jensen, vice-président
d’American Electric Power, exploitant de DC Cook).
Les paliers de turbine présentent des dommages nombreux et un total de
cinq ailettes (trois éjectées et deux arrachées par les autres) a été finalement éjecté.
L’analyse des restes d’ailettes (Photo 8.11) a permis d’incriminer le design de ces
ailettes à cette position, ne laissant pas assez de marges de sûreté vis-à-vis de la
contrainte.
Les travaux de réparation ont duré un an et demi, pour un coût total de
300 millions de dollars, ce qui met en évidence le fort impact de cet accident où,
heureusement, personne n’a été blessé, car personne n’était en SDM à ce moment-là
et le capot de turbine a servi de protection. Notons que cet accident a conduit à
la plus forte demande de remboursement à une assurance dans l’industrie nucléaire
américaine à ce jour.
