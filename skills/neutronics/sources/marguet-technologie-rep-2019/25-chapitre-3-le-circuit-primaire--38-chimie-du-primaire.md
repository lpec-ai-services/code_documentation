# Chapitre 3 Le circuit primaire — 3.8 Chimie du primaire … 3.9 Activité du primaire
<!-- source PDF pages 317-325 -->

<!-- page 301 (PDF 317) -->
où PGV (boucle) est la puissance thermique produite par le générateur de vapeur de
la boucle considérée et Pperte+apport est le bilan net de la puissance des pertes (comptées
positives comme les fuites thermiques à travers les calorifuges du primaire, la
consommation de l’échangeur non régénérateur, les barrières des pompes primaires,
les échangeurs de paliers et moteurs des pompes primaires) et des apports (comptées
négatives comme la puissance des pompes, les pompes de charges, les chaufferettes
du pressuriseur). Au bilan, on obtient des pertes globalement constantes au cours de
la vie de la tranche, à savoir 11 MWe sur le palier CPY (8 MWe pour Fessenheim),
17 MWe sur le 1 300 MWe et 20 MWe sur le N4.
La puissance thermique PGV en [kW] échangée dans un GV s’écrit :
PGV =
□
hsortie vapeur GV
m´elange
−hARE
liq
□
QARE −hpurge
liq
Qpurge
où QARE est le débit de l’eau secondaire (ARE) du GV [kg/s], Qpurge est le débit
de la purge [kg/s], hsortie vapeur GV
m´elange
est l’enthalpie du gaz à la sortie du GV vers la
turbine en [kJ/kg] qui dépend du titre X [%] en vapeur et de la pression au secondaire
(quasiment sèche à 99,9 %) :
hsortie vapeur GV
m´elange
= X hsortie vapeur GV
vap,sat
+ (1 −X) hsortie vapeur GV
liq,sat
hpurge
liq
est l’enthalpie de l’eau liquide à la purge du GV [kJ/kg] et Qpurge le débit
massique à la purge [kg/s]. hARE
liq
est l’enthalpie de l’eau alimentaire secondaire du
GV [kJ/kg].
Le titre de la vapeur humide est mesuré au démarrage de la tranche ou au
changement de GV, mais il a tendance à se dégrader suite à une perte progressive de
l’efficacité des sécheurs. L’enthalpie de l’eau primaire alimentaire du GV est calculée
à partir des pressions et des températures amont des diaphragmes introduits pour les
mesures de débit (par différence de pression amont/aval du diaphragme). Le débit
massique des purges des GVs est de l’ordre de 1 % du débit ARE alimentaire du GV,
mesuré par une tuyère ou un diaphragme. Notons que le débit primaire QARE est
mesuré par un diaphragme où on mesure la différence de pression et les températures
amont et aval.

## 3.8 Chimie du primaire

[Cohen, 1969] p. 40, [Huntz-Aubriot et Pieraggi, 2003], [Rodier, 1971], [Roth, 1968]

### 3.8.1 Généralités

L’eau du primaire n’est pas pure. Elle contient du bore entre 10 ppm et 1 500 ppm
selon l’instant dans le cycle d’irradiation, mais aussi de l’hydrogène dissous (environ
25 à 50 mL d’H2 par kg d’eau), un peu d’oxygène (environ 10 μg/kg), et du lithium.
L’eau d’appoint du primaire provient de la station de déminéralisation du circuit d’eau
brute SEB qui est clarifiée par un précipité d’hydroxyde de fer, puis décantée et filtrée,
et enfin passée sur des lits de résines échangeuses d’ions (résines cationiques faibles
et anioniques faibles économiques et à forte capacité, puis cationiques et anioniques

<!-- page 302 (PDF 318) -->
fortes plus chères mais à forte sélectivité). Ce traitement produit une eau déminéralisée
de bonne qualité (oxygène dissous < 0,1 ppm, chlorures et fluorures < 0,1 ppm,
matières solides en suspension < 0,1 ppm, silice < 0,1 ppm, aluminium < 0,02 ppm,
calcium < 0,02 ppm, magnésium < 0,02 ppm, potassium < 0,015 ppm, sodium
< 0,015 ppm).

### 3.8.2 L’acide borique

[Cohen, 1969] p. 220
L’acide borique H3BO3, un acide faible à froid dont la constante de dissociation
diminue en plus avec la température (donc un acide très faible à plus forte
température), s’est révélé historiquement l’absorbant neutronique le plus facile à
utiliser, dilué dans l’eau. L’acide borique rend l’eau légèrement plus dense que
l’eau pure (1 % en poids, soit par exemple 1 750 ppm qui donnent une densité de
1,0045 à 15 ◦C). Seul l’isotope 10 du bore est très absorbant par réaction (n, α),
mais il produit du tritium radioactif selon les réactions 10B (n, 2α) 3H et 10B (n,
α) 7Li (n, nα) 3H. Le bore naturel 9 contient 19,9 % de 10B et 80,1 % de 11B.
L’utilisation de bore enrichi en 10B jusque dans les années 1990 va se généraliser dans
l’EPR avec un enrichissement de 39 %. L’acide borique est un acide moyennement
soluble à température ambiante (50 g/l à 20 ◦C), c’est pourquoi on le prépare
dans des citernes réchauffées à 80 ◦C où sa solubilité est de 200 g/l. Le risque
à surveiller est le bouchage de tuyauterie par précipitation de l’acide borique si
la température baisse de façon à atteindre la limite de solubilité (Figure 3.13).
L’acide borique dilué dans l’eau se transforme en ions borates sous différentes formes
polymérisées, à savoir B(OH)−
4 , B3O3(OH)−
et B4O5(OH)−
4 . En tant qu’anions,
les ions borates saturent les résines anioniques qui sont incluses dans les pots de
résines à lit mélangés pour moitié de résines anionique et l’autre moitié de résine cationique
. Ainsi, faire passer l’eau primaire sur ces lits est un moyen de déborater l’eau.

### 3.8.3 La lithine

La lithine LiOH est une base qui maintient le pH basique, pour contrer l’acidité du
fait de l’introduction volontaire d’acide borique pour le contrôle de la réactivité, afin
de limiter la corrosion, surtout à froid. Car en fait, à chaud (300 ◦C), la fonction
acide de l’acide borique est quasiment inexistante, et la lithine se comporte dans l’eau
comme si elle était seule, mais son introduction d’environ 1 ppm (entre 0,7 et 2,2 ppm)
dans l’eau du primaire, garde un intérêt pour réduire les dépôts de magnétite sur les
assemblages, ce qui diminue l’activation des produits de corrosion. À froid où son
action basique contre l’acidité de l’acide borique, une eau primaire basique corrode
moins les alliages ferreux et le Zircaloy.
La lithine a été préférée à la soude NaOH car le sodium 23Na s’active notablement
en 24Na radioactif (période 15,03 heures), et du fait que la soude concentrée dans des
zones d’ébullition attaque rapidement l’acier. L’ammoniac est parfois utilisée dans les
réacteurs VVER. La potasse KOH a été rejetée pour des raisons identiques. Rappelons
que le pH est la mesure de la concentration en ions hydrogène dans un liquide
9 Sur les propriétés thermochimiques du bore : [Cordfunke et Konings, 1990] p. 78.

<!-- page 303 (PDF 319) -->
Fig. 3.13 – Solubilité de l’acide borique naturel dans l’eau en fonction de la
température.
(pH = –log([H+]). Pour de l’eau neutre où par définition [H+] = [OH−], ce pH est de
7 dans la mesure où, à 25 ◦C, le produit [H+] × [OH−] vaut 10−14.
Le lithium de la lithine utilisée en réacteur est enrichi à 99,9 % en lithium 7 pour
éviter la production de tritium radioactif par capture radiative sur le lithium 6, l’autre
isotope du lithium naturel 10.
La méthode d’injection de lithine sur les paliers 900 et 1 300 MWe s’effectue par
le balayage d’un ballon de préparation par de l’eau du REA. Le débit est fixé par un
diaphragme sur le palier 900 et par une vanne préréglée sur le palier 1 300. Il faut être
très prudent lors de la phase d’injection puisqu’on injecte aussi de l’eau non borée en
même temps que la lithine, d’où un risque de dilution si on ne contrôle pas la durée
d’injection.
10 L’abondance du lithium naturel est de 7,4 % pour 6Li et 92,6 % pour 7Li.

<!-- page 304 (PDF 320) -->
### 3.8.4 L’hydrazine

L’oxygène libre oxyde les parois métalliques du primaire et les gaines. La limitation de
la teneur en oxygène est effectuée par adjonction d’une solution d’hydrazine 11 N2H4
(jusqu’à 10 ppm) selon la réaction :
N2H4 + O2 →N2 + 2H20
L’hydrazine est une base faible qui est un puissant réducteur en milieu basique. Elle
capte l’oxygène pour le transformer en eau et maintient la concentration en oxygène
libre à moins de 0,1 mg/kg. L’hydrazine est une base qui alcalinise l’eau (pH = 9,9 pour
de l’eau à 1 % d’hydrazine). La réduction n’est vraiment efficace qu’à partir de 65 ◦C
(c’est pourquoi elle n’est introduite dans le primaire qu’en dessous de 120 ◦C). Par
contre, au-dessus de 150 ◦C, l’hydrazine de décompose par thermolyse en produisant
de l’ammoniac selon la réaction :
3N2H4 →4NH3 + N2
Voire même une production d’hydrogène au-delà de 250 ◦C :
2N2H4 →2NH3 + 2N2 + 3H2
L’oxygène est lui-même produit par radiolyse de l’eau (dissociation de la molécule
d’eau sous l’effet des rayonnements [Roth, 1968] p. 437, [Cohen, 1969] p. 89, et on
en introduit aussi volontairement dans certaines phases de passivation du primaire
vis-à-vis des produits de corrosion. L’hydrogène ne doit pas dépasser 35 mL/kg sur
une longue période pour ne pas fragiliser les gaines par hydruration.
L’hydrazine est un produit dangereux car inflammable et irritant. Celle utilisée en
centrale est une solution d’eau à 35 % d’hydrazine.

### 3.8.5 L’hydrogène

On maintient en fonctionnement normal un excès d’hydrogène d’au moins 15 ml
TPN/kg d’eau pour combattre les effets de la radiolyse de l’eau. Cette concentration
en hydrogène permet de déplacer la réaction d’équilibre chimique de recombinaison
avec l’oxygène pour former de l’eau. Cette radiolyse provient de la dissociation de la
molécule d’eau au-dessus de 150 ◦C sous l’action du rayonnement :
H2O →
←
2O2 + H2
Dans la pratique, on cible une concentration d’hydrogène de 25 à 35 ml TPN/kg. Il
faut faire attention à ne pas introduire trop d’hydrogène pour éviter l’hydruration des
tubes GV, voire des gaines combustibles. Lors des arrêts avec oxygénation, on veille à
éliminer progressivement l’hydrogène juste avant l’arrêt (< 3 ml TPN/kg) pour éviter
tout risque d’explosion.
L’hydrazine a aussi été testée dans le circuit secondaire en protection de l’effet de denting
des tubes de générateur de vapeur. On prendra garde que dans le cas de tranches comportant des
organes cuivreux (condenseur), la teneur maximale en hydrazine doit être limitée fortement du fait de
la décomposition en ammoniac. Pour les centrales en bord de mer dont les condenseurs ne contiennent
pas de cuivre, ce problème disparaît. L’action bénéfique de l’hydrazine a par ailleurs été clairement
démontrée sur le degré d’oxydation des matières en suspension.

<!-- page 305 (PDF 321) -->
Cet oxygène libre va transformer la couche protectrice dense d’oxyde de fer Fe3O4
(magnétite), qui s’est naturellement formée sur les aciers à l’air ou à froid, par oxydation
en hématite Fe2O3 poreuse, ce qui va relancer l’oxydation. Rappelons que
l’oxydation se traduit par une loi d’évolution temporelle plus ou moins parabolique
de la couche d’oxyde (liée à la diffusion de l’oxygène dans le métal), et une couche
initiale dense protège donc bien le reste du métal. L’effet Evans de formation d’un
couple oxydo-réducteur par aération différentielle de l’eau 12 (cathode = zone aérée,
anode = zone non aérée) peut aussi aggraver la corrosion électrochimique des matériaux
, tout particulièrement dans les recoins à eau stagnante. En présence d’azote,
l’oxygène libre peut former de l’acide nitrique HNO3 agressif.
Une surpression d’hydrogène favorise la recombinaison de l’oxygène en eau. Par
contre, il ne faut pas excéder 50 ml TPN/kg d’eau, au risque d’accroître l’hydruration
accentuant la corrosion sous contrainte (tube en Inconel 600).

### 3.8.6 Contrôle chimique de l’eau primaire

[Cohen, 1969] p. 268
L’eau primaire, bien que déminéralisée, contient des sels dissous. Les plus actifs sont
les ions chlores qui favorisent la corrosion, et les sels de cuivre, de cadmium, de cobalt
, d’or, de plomb et de manganèse, qui forment des dépôts métalliques provoquant
une corrosion électrochimique bi-métallique. Le contrôle chimique de l’eau du primaire
est assuré par des prélèvements réguliers et la concentration en sels solubles
est réduite en faisant passer une partie de l’eau dans un circuit d’épuration comportant
des filtres et des résines échangeuses d’ions. À titre d’illustration, sur le palier
CPY, des prélèvements sont effectués sur les branches chaudes n◦2 et n◦3, en phase
liquide et vapeur du pressuriseur et dans la phase vapeur du réservoir de décharge du
pressuriseur (RDP).

## 3.9 Activité du primaire

[Cohen, 1969] p. 144, [Roth, 1968]
En absence de défaut de gainage, il n’y a pas de produits de fission qui peuvent
transiter à travers les gaines (Tableau 1). Par contre, il y a toujours une contamination
résiduelle d’oxyde d’uranium à la surface externe des gaines provenant du processus
de fabrication. Cette contamination, de l’ordre de la fraction d’un gramme pour un
crayon, est bien entendu extrêmement faible, mais va contribuer par fission à l’activité
du primaire, lors de la mise sous flux neutronique. On estime cette activité à quelques
dizaines de MBq/tonne d’eau primaire. Une particularité de cette contamination est
qu’elle apparaît dès la mise sous flux du cœur. Elle est maîtrisable en amont par
une propreté rigoureuse à la fabrication (nettoyage poussé des crayons fabriqués).
Une partie de cette contamination est éliminée principalement par les déminéraliseurs
(purges), le dégazage au circuit TEP, d’éventuelle chasse gazeuse du RCP et les
appoints d’eau au RCV.
Le couple réducteur de l’eau est de 0,401 V . On peut donc créer une pile uniquement par
variation de la pression d’oxygène dans deux cavités d’eau reliées par des électrodes. Le phénomène
est contré par la formation de rouille.

<!-- page 306 (PDF 322) -->
Tab. 3.1 – Caractérisation de la contamination du circuit primaire.
État du cœur
Critères
Commentaires
Activité par tonne d’eau du
primaire
Pas de défaut – cœur propre
133Xe
≤
185 MBq/tonned′eau
Pas de pic d’iode ou de césium
lors de transitoires de puissance
Pas de défaut – cœur sans
défaut
185 MBq/tonne <133 Xe ≤
1000 MBq/tonne
Pas de pic d’iode ou de césium
lors de transitoires de puissance
133Xe/135Xe ≤0, 9
Petits défauts – assemblages
douteux
131I/133Xe ≥0, 5
Activité
due
aux
PFs
à
vie
longue. Pics d’iode et de césium
lors des transitoires
133Xe/135Xe ≥3
Gros défauts – assemblages
non étanches
131I/133I ≈0, 3
L’activité
due
aux
PFs
à
vie
courte
augmente.
Pas
de
pic
d’iode significatif lors des transitoires

133Xe/138Xe ≈1
Très gros défauts – assemblages
non étanches
0, 1 ≤131 I/134I ≤0, 5
L’activité
due
aux
PFs
à
vie
courte augmente
Défauts
disséminant
de
la
matière fissile
133Xe ≥2000 MBq/tonne
Problème de fretting sur des assemblages
à fort taux de combustion

Le cas de présence de défaut de gainage peut contribuer à polluer significativement
l’eau du primaire. Dans la liste des isotopes présents dans l’eau du primaire en cas de
perte d’étanchéité du combustible, on retrouve généralement des gaz 13 : xénon 133
(5,2 jours), xénon 133 m (2,3 jours), xénon 135 (9,2 heures), xénon 138 (17 minutes),
krypton 85 (10,4 ans), krypton 85 m (4,4 heures), krypton 87 (1,8 heure), krypton
88 (78 minutes) ; mais aussi des produits solubles 14 : iode 131 (8,05 jours), iode
132 (2,3 heures), iode 133 (21 heures), iode 134 (53 minutes), iode 135 (6,7 heures),
césium 134 (2,2 ans), césium 136 (13 jours), césium 137 (3 ans), césium 138 (32
minutes) ; et des produits solides : lanthane 140 (40,2 heures), baryum 140 (12,8 jours),
neptunium 239 (2,36 jours). Notons que les produits à période trop courte (de l’ordre
de la minute, à comparer avec la vingtaine de secondes que met l’eau du primaire
à parcourir un tour complet de circuit primaire), ne sont pas détectables facilement
par prélèvement classique à moins d’installer un système de détection particulier en
cas d’enjeu fort de sûreté (cas de l’azote 16 (période 7,16 secondes) par exemple pour
suivre les fuites primaire-secondaire). Il en est de même pour les isotopes à période
très longue (supérieure à un siècle).
Le circuit de purification et de déminéralisation des REPs est conçu pour réduire
l’activité des polluants en solution par une utilisation continue. Pour les isotopes
de l’iode, les rendements de fission sont proches de 7 % [Marguet, 2018]
p. 1057, sauf celui de l’iode 131 qui est proche de 3 %. Pour cet isotope particulier à
période longue (8 jours) par rapport aux autres iodes, la déminéralisation est plus
efficace sur l’activité, car l’isotope disparaît naturellement moins rapidement par
Sur les propriétés thermochimiques du xénon : [Cordfunke et Konings, 1990] p. 463, du
krypton : [Cordfunke et Konings, 1990] p. 209.
Sur les propriétés thermochimiques de l’iode : [Cordfunke et Konings, 1990] p. 192, du
césium[Cordfunke et Konings, 1990] p. 88, du lanthane[Cordfunke et Konings, 1990] p. 210, du
baryum [Cordfunke et Konings, 1990] p. 37.

<!-- page 307 (PDF 323) -->
radioactivité. Avec le débit RCV d’un seul orifice sur les déminéraliseurs, l’activité
de l’iode 131 à l’équilibre est réduite d’un facteur 20 par rapport au fonctionnement
sans déminéraliseur, alors qu’il n’est que de 1,1 pour l’iode 134. En ce qui concerne
les gaz insolubles ou peu solubles, le problème est plus complexe car il dépend à la
fois du dégazage par le dégazeur TEP, les chasses d’eau du ballon RCV, le renouvellement
de l’eau par le REA eau. . . d’où une dépendance des conditions d’exploitation
(charge. . . ). Avec une contamination seule sans défaut de gainage, le xénon 138 est
plus actif que le xénon 135 ; lui-même plus actif que le xénon 133. Le lanthane 140 et
le baryum 140, insolubles, sont rapidement éliminés par filtration.
L’efficacité des déminéraliseurs sur la baisse d’activité dépend donc de la période de
l’isotope considéré. Pour le césium 137 (3 ans), on fait passer l’eau sur un lit cationique
décrit lors de la présentation du circuit RCV (fonction filtration). Le passage du débit
de décharge du RCV de un à deux orifices sur les déminéraliseurs réduit encore les
activités des produits de fission solubles à vie courte (d’environ 8 % par rapport à un
orifice pour l’iode 134, d’environ 50 % pour l’iode 131, et de 100 % pour les isotopes à
vie très longue). Bien entendu, le renouvellement d’eau par le REA-eau fait diminuer
l’activité du primaire. Les chasses du ballon RCV permettent de réduire l’activité des
PFs gazeux. On peut aussi ligner la phase gaz du pressuriseur vers le TEG, ce qui
aura un effet similaire. Le renouvellement de l’eau par le TEP dégazé diminue aussi
l’activité des gaz de l’eau primaire.
Une bonne part de l’activité de l’eau du primaire provient de la désintégration de
l’azote 16 (période 7,13 s) qui produit un gamma extrêmement pénétrant de 10,419
MeV ( !). Cet azote 16 est produit par réaction (n,p) sur l’oxygène 16 de l’eau du
primaire. Sa période est à comparer avec le temps de transit de l’eau primaire dans
le circuit primaire, qui est de l’ordre de 20 secondes.
L’activité du primaire est aussi due aux produits d’activation [Cohen, 1969] p. 369,
principalement des produits de corrosion en suspension ou dissous dans l’eau du primaire
, provenant des surfaces internes des composants du primaire. Une part de l’activité
est due à la présence de cobalt 60 (période 5,27 ans), du fait de ses deux raies
gamma très pénétrantes à 1,17 MeV et 1,33 MeV. Bien qu’on évite à tout prix de placer
des alliages de cobalt dans le cœur actif, la portée de certaines vannes du primaire
est en stellite, un acier durci par adjonction de cobalt, et c’est l’usure des portées
de vannes qui véhicule du cobalt dans le primaire. Ce cobalt s’active durablement en
passant dans le cœur actif. On comprend aussi l’intérêt évident d’utiliser des aciers
très résistants à la corrosion. Les premiers acquis en matière de suivi de l’activité du
primaire en France proviennent du retour d’expérience de la centrale de Chooz A 15.
Ainsi, lors de l’arrêt de juin 1971 à la fin du premier cycle, l’activité dans la boîte à eau
des GVs était de l’ordre de 2 à 3 rem/h, et l’activité du cobalt 60 déposée sur les tubes
de ces mêmes GVs de l’ordre de 0,75 microCurie/cm2. Ce cobalt provient de certains
aciers alliés au cobalt, utilisé par exemple pour les portées stellitées des vannes de
robinet pour les durcir. L’activité de l’eau (exemples Figure 3.14 et Figure 3.15) est
donc principalement due au cobalt 58, cobalt 60 et manganèse 54, et reste à peu près
constante en fonctionnement nominal, avec des changements sensibles pendant les variations
de charge. On constate par exemple une très forte montée de l’activité (× 200
sur le manganèse 54 !) après arrêt du réacteur, pendant la phase de refroidissement et
G. Frejaville, A. Marchal, P. Beslu, A. Lalet : Activité du circuit primaire de la centrale de
Chooz due aux produits de corrosion, IAEA/SM-178/11, Experience from operating and fueling of
nuclear power plants, Symposium du 8-12 octobre 1973, Vienne, Autriche.

<!-- page 308 (PDF 324) -->
Fig. 3.14 – Activité classique d’une tranche sans défaut (Saint-Laurent-des Eaux
117). On constate que l’activité est faible et largement corrélée aux baisses de charge, donc
aux mouvements d’eau.
Fig. 3.15 – Exemple du suivi de l’activité du circuit primaire (Dampierre 319).
Cette activité correspond à une contamination intrinsèque et la présence de défauts de petites
tailles.
d’augmentation de la concentration en bore, car les particules déposées sur les surfaces
du primaire semblent se remettre en suspension (solubilité des dépôts en fonction de
la température, effet du pH de l’eau, contraintes mécaniques. . . ).
En ce qui concerne les gaz, c’est le dégazeur du circuit de traitement des effluents
primaires (TEP) qui officie principalement, mais il faut tenir compte aussi des chasses
du ballon RCV et du renouvellement de l’eau par les appoints RCV.

<!-- page 309 (PDF 325) -->
Fig. 3.16 – Altimétrie du primaire.
