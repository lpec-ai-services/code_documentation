# Chapitre 6 Le circuit secondaire — 6.12 Les turbo-pompes alimentaires … 6.13 La corrosion-érosion dans le secondaire
<!-- source PDF pages 821-830 -->

<!-- page 805 (PDF 821) -->
Fig. 6.97 – Deuxième phase de l’îlotage : les soupapes MP se ré-ouvrent lentement et
la vitesse de la turbine se stabilise.

## 6.12 Les turbo-pompes alimentaires

### 6.12.1 Généralités sur les TPAs

Les turbo-pompes alimentaires (TPAs) utilisent de la vapeur soutirée par un piquage
au barillet vapeur avant la turbine haute pression, pour pomper l’eau du circuit ARE
en provenance de la bâche ADG (Figure 6.98). L’eau est envoyée vers les réchauffeurs
HP, puis vers les GVs. Un réacteur CPY possède deux TPAs et une turbopompe
alimentaire de secours TPAS sur le circuit ASG d’alimentation de secours des GVs, qui
peut pomper en secours de deux autres motopompes électriques l’eau de la bâche ASG.
La turbine d’une TPA entraîne directement la pompe principale et, par l’intermédiaire
d’un réducteur, la pompe nourricière (Figure 6.99, Photo 6.15). En régime nominal,
les TPAs sont exclusivement alimentées par la vapeur prise en sortie des sécheurssurchauffeurs
R6 pour le palier CP0-CP1 (Figure 6.98), puis de la bâche alimentaire
à partir du CP2. La pression de cette vapeur est à peu près proportionnelle à la
puissance du groupe GTA. Une TPA peut assurer 50 % du service, cela veut dire
qu’en régime nominal, il faut obligatoirement les 2 TPAs en service. Si on perd une
TPA, on peut transitoirement faire fonctionner la TPA restante en surrégime (jusqu’à
75 %), mais il faudra obligatoirement baisser la charge, auquel cas on risque un AAR
par bas niveau GV, les GVs n’étant plus suffisamment alimentés en eau secondaire. Si
on perd une pompe d’extraction, la mise en route de la seconde permet de continuer
à fonctionner. Par contre, si on perd les deux pompes d’extraction, on risque de faire
caviter les pompes TPAs, d’où un repli nécessaire.

<!-- page 806 (PDF 822) -->
Fig. 6.98 –
Position
des
turbo-pompes
alimentaires
dans
le
système
de
réchauffage de l’ARE.
Photo 6.14 – Pompe alimentaire d’une TPA (EDF/DR).

<!-- page 807 (PDF 823) -->
Photo 6.15 – Pompe nourricière d’une TPA (EDF/DR).
La réduction de charge du GTA entraîne la baisse de l’écart d’enthalpie utilisable
dans les turbines entraînant les TPAs. En dessous d’un certain niveau de puissance
(environ 40 %), la vapeur moyenne pression devient insuffisante pour entraîner les
TPAs. Un organe d’admission de vapeur HP, prise à la sortie des GVs, s’ouvre en cascade
avec l’organe d’admission MP qui reste grand ouvert. Dans la zone de puissance
comprise entre 40 % et 15 %, les TPAs sont alimentées en parallèle par de la vapeur
MP et HP jusqu’à l’aval du premier étage où le mélange s’effectue pour continuer la
détente dans le reste des étages de la turbine TPA. En dessous de 15 % de puissance
nominale, la pression MP devient trop faible pour participer à la détente parallèle, et
c’est de la vapeur HP seule qui alimente les TPAs.

<!-- page 808 (PDF 824) -->
Photo 6.16 – Turbopompe alimentaire d’une tranche N4. On voit le corps de la
turbine TPA de couleur orange, placée devant la pompe alimentaire d’où arrivent et partent
les grosses tuyauteries (photo EDF).
Un groupe turbo-pompe alimentaire d’une tranche N4 (Photo 6.16), dont l’étude
par Alsthom a commencé en 1980, est constitué 41 :
• d’une pompe pré-alimentaire dite « pompe de gavage » ou « pompe nourricière »
(Figure 6.99), tournant à faible vitesse (1 289 tours/min), et ayant de bonnes
qualités à l’aspiration ; à son régime nominal (1 400 tours/min), cette pompe
absorbe une puissance de 4 MW ;
• un réducteur qui permet de passer de la vitesse nominale de la turbine à vapeur
(4 580 tours/min), à celle de la pompe de gavage (1 280 tours/min) ;
• une turbine à vapeur à condensation alimentée à une pression de vapeur de
10 bars, et la restituant à l’échappement à 50 mb environ ;
• une pompe alimentaire (Photo 6.14) à roue double de 0,49 m de diamètre, et
tournant à la même vitesse que la turbine à vapeur. Cette pompe absorbe à sa
vitesse nominale (4 000 tours/min) une puissance de 13 MW.
Cette pompe alimentaire présente donc une puissance spécifique élevée (17 MW) pour
une masse de 10 tonnes ; un rendement très élevé de 90 % ; une absence d’amorce
41 Alain de Tonnac, J. Fremann : L’industrie française face à l’évolution du programme nucléaire,
Revue Générale Nucléaire, n ◦1, janvier 1988, pp. 37-45.

<!-- page 809 (PDF 825) -->
Fig. 6.99 – Schéma d’une turbopompe TPA.
Fig. 6.100 – Schéma technique d’une turbopompe alimentaire (Fessenheim).

<!-- page 810 (PDF 826) -->
de cavitation sur toute sa plage de fonctionnement. Elle comporte des roues frettées
sur l’arbre sans clavette, malgré l’importance du couple transmis ; des pivoteries
sur paliers et butées à l’huile, à patins oscillants ; une garniture d’étanchéité de
la pompe principale de type mécanique, avec boîte à eau et réfrigérant intégré ; un
supportage sur plaques de base directement intégrées à une structure en béton. La
Figure 6.100 montre le schéma technique d’une TPA de conception plus ancienne
(CP0). Le Tableau 6.9 présente les caractéristiques des TPAs du palier P’4.

### 6.12.2 Éléments de physique des TPAs

On peut simuler le comportement de la turbopompe par des équations simples sur
l’enthalpie vapeur en utilisant le rendement isentropique ηh :
hsortie
vapeur = hentr´ee
vapeur −ηh
hentr´ee
vapeur −hisentropique
La conservation du débit implique que :
Qsortie
vapeur = Qentr´ee
vapeur
Le calcul du débit de sortie utilise le rendement mécanique ηm (Figure 6.101) et la
puissance de la pompe WT P A :
Qsortie
vapeur =
WT P A
ηm
hentr´ee
vapeur −hsortie
vapeur
Si la sortie vapeur de la pompe TPA est dirigée vers un condenseur auxiliaire extrayant
une puissance par condensation WCond, on obtient :
Qsortie
vapeur =
WCond
ηm
hsortie
vapeur −hentr´eeCondenseur
liquide
L’échange thermique dans le condenseur (supposé adiabatique et sans perte de charge)
s’écrit :
WCond
=
Cp(T entr´eeCondenseur
liquide
) × Qentr´eeCondenseur
liquide
×
T sortie
vapeur −T entr´eeCondenseur
liquide
×
1 −e−NUT □
NUT est le nombre d’unité de transfert du condenseur, classiquement rencontré
en théorie des échangeurs de chaleur. La puissance à la turbine couplée au condenseur
est alors donnée par :
WT P A = ηmQsortie
vapeur
hentr´ee
vapeur −hsortie
vapeur

### 6.12.3 Réglage de la vitesse des TPAs

C’est la régulation du niveau GV qui agit sur les soupapes alimentaires, mais pour
que ces soupapes fonctionnent dans leur gamme, il faut modifier la perte de charge
des soupapes en fonction de la charge. On règle dans les faits la différence de pression
entre le barillet vapeur qui collecte la vapeur de l’ensemble des GVs, et le collecteur
(barillet) d’eau alimentaire. C’est cet écart de pression qu’on va comparer à
la consigne qui augmente avec la charge, donc le débit de vapeur sortant des GVs
(Figure 6.102).

<!-- page 811 (PDF 827) -->
Tab. 6.9 – Caractéristiques des TPAs (palier P’4).
Alsthom
Saint
Cattenom
Belleville
Erreur
Alban
limite
Débit (kg/s)
file 1
1075,54
982,0
1064,7
1041,3
± 20
file 2
1075,54
1104,0
1086,4
1051,9
± 20
Δp (bar)
file 1
72,13
72,02
73,57
± 0,80
file 2
72,00
72,21
73,14
± 0,80
Δt ( ◦C)
file 1
1,45
1,56
2,28
1,36
± 0,75
file 2
1,45
1,89
2,13
1,08
± 0,75
Puissance effective (MW)
file 1
9,3
7,90
8,50
8,55
± 0,15
file 2
9,3
8,87
8,67
8,58
± 0,15
total
18,6
16,77
17,17
17,13
± 0,20
Puissance accoup. (MW)
file 1
9,97
10,72
10,59
± 0,18
file 2
11,01
10,93
10,62
± 0,18
total
20,98
21,65
21,21
± 0,25
Rend. total groupe (%)
84,5
79,5
± 1,5
Débit de vapeur soutiré
(kg/s)
file 1
16,5
17,8
17,5
± 0,2
file 2
17,5
17,6
-
± 0,2
total
35,4
-
± 0,2
Rend,
isentropique
de
détente (%)
TPA 1
71,7
76,0
75,0
75,5
± 2
TPA 2
71,7
75,5
75,5
-
± 2

## 6.13 La corrosion-érosion dans le secondaire

La circulation d’eau ou de vapeur dans le secondaire provoque une action mécanique
et chimique. L’érosion mécanique, conduisant à des pertes d’épaisseur de quelques
mm pour 10 000 heures de fonctionnement, est prépondérante à basse température
. Le dessin des conduites (coudes, chanfrein. . . ) est déterminant sur l’érosion, de
même que la quantité de gouttes d’eau transportées dans le cas de vapeur. Les effets
chimiques de corrosion prennent de l’importance à plus haute température du fait que
les lois d’Arrhenius qui pilotent les phénomènes d’oxydation sont exacerbées par la
température. D’un point de vue phénoménologique, l’eau liquide oxyde le fer contenu

<!-- page 812 (PDF 828) -->
Fig. 6.101 – Rendements d’une TPA en fonction du débit (palier P’4).
dans les aciers par les réactions 42 :
Fe ↔Fe++ + 2e−
2H2O ↔2H+ + 2OH−
2H+ + 2e−↔H2(gaz)
Auquel on peut rajouter le phénomène de formation/destruction de la magnétite
Fe2O4 :
Fe2O4 + 6H+ + H2(gaz) ↔3Fe++ + 4H2O
Dans un liquide au repos, la formation d’ions Fe++ se produit jusqu’à un équilibre
et les ions vont s’associer à l’eau à la surface du fer pour produire de la magnétite.
Ainsi, le fer va se couvrir d’une couche de magnétite protectrice qui va « isoler »
le métal de l’eau, tout comme la zircone dense protège le zirconium de l’oxydation.
Dans un liquide en mouvement, les ions Fe++ « solubles » sont évacués par le mouvement
de l’eau, et la couche de magnétite se forme plus difficilement car les conditions
de sa formation ne sont plus réunies. La cinétique de corrosion est exacerbée entre
50 ◦C et 200 ◦C. Au-delà, la formation de magnétite s’intensifie et protège l’acier. La
concentration en Fe++ dans l’eau dépend aussi du pH (la corrosion diminue très sensiblement
quand le pH augmente légèrement) et du type de conditionnement de l’eau
42 M. Cerdan : Expérience d’exploitation des tranches nucléaires françaises 900 MW à eau sous
pression, Journée « expériences d’exploitation des tranches nucléaires françaises », 2esession : Généralités
sur les difficultés dues au phénomène d’érosion-corrosion, 20 juin 1984, Paris, SFEN (1984).

<!-- page 813 (PDF 829) -->
Fig. 6.102 – Réglage de la vitesse des TPAs (adapté de [Circuit secondaire, 1978]
p.48).
(ammoniaque NH4OH ou morpholine 43 C4H9NO). Le conditionnement à l’ammoniac
alcalin permet d’obtenir un pH de l’ordre de 9 favorable pour lutter contre la corrosion
, mais l’ammoniaque volatil a tendance à passer en phase vapeur au détriment de
43 Le conditionnement aux phosphates de l’eau du secondaire, initialement préconisé par Westinghouse
, a été à l’origine de divers phénomènes de corrosion de l’alliage Inconel 600, qui ont affecté les
premières tranches REPs proposées par ce constructeur. Mais ce mode de conditionnement n’a jamais
été utilisé en France au profit d’un emploi de réactifs alcalinisants volatils de type ammoniaque ou
morpholine. On parle alors de « conditionnement volatil ». D’une manière générale, la corrosion sous
contrainte de l’Inconel 600 de nombreux composants a amené à l’introduction de l’Inconel 690 plus
résistant. Le coefficient de partage eau-vapeur de la morpholine est proche de 1, ce qui signifie que
le réactif est équi-réparti entre la phase liquide et vapeur. On cible un pH compris entre 9,1 et 9,3
à 25 ◦C avec une teneur en morpholine supérieure à 4 mg/kg d’eau et une teneur en ammoniaque
inférieure à 0,3 mg/kg d’eau. Notons que l’ammoniaque est aussi produite par décomposition de
l’hydrazine à haute température. L’hydrazine (N2H4), un puissant réducteur qui est aussi utilisé
dans le primaire, est injectée dans le secondaire pour dégazer chimiquement l’oxygène dissous afin
de réduire la corrosion. Cette hydrazine est injectée en amont de la turbine BP pour augmenter le
temps de contact avec l’oxygène car son efficacité dépend du temps de contact et de la température.
L’objectif est d’éviter que les oxydes ne soient véhiculés dans le GV à un état d’oxydation supérieur
à l’état stable représenté par Fe3O4 ou Cu qui sont les états les moins nocifs pour le GV.

<!-- page 814 (PDF 830) -->
l’eau. Le conditionnement de l’eau alimentaire du secondaire à la morpholine permet
d’obtenir des valeurs de pH plus élevées à chaud, pour une même valeur à froid (9,2).
La nuance de l’acier influence aussi la corrosion, qui est réduite en présence de chrome,
de cuivre ou de molybdène. Au final, le calcul de la corrosion chimique quand le fluide
débite, s’avère extrêmement complexe.
Au niveau des générateurs de vapeur, les oxydes de fer et, dans une moindre
mesure, les oxydes de cuivre et de zinc se déposent plus particulièrement dans le faisceau
tubulaire, au-dessus de la plaque tubulaire et dans les interstices entre les tubes
et les plaques entretoises. De plus, des polluants peuvent s’introduire accidentellement
dans le circuit secondaire. Ces polluants se concentrent dans les générateurs de vapeur
car ils sont moins emmenés en phase gazeuse. Ce phénomène de concentration rend
les GVs particulièrement sensibles aux problèmes de corrosion.
La mesure en continu de la conductivité cationique et de la concentration en
sodium permet de suivre le niveau de corrosion des GVs. Ces mesures sont réalisées
à la purge des GVs, mais aussi au condenseur. Si ces mesures sont « mauvaises »,
on peut être amené à baisser la charge pour déstocker les produits corrodants par
diminution du flux thermique. La quantité d’ions sodium et la valeur de la conductivité
mesurées à la purge des GVs permettent éventuellement de discriminer l’origine de
la contamination. En effet, une augmentation de la concentration en sodium seule
peut s’expliquer par une entrée de soude en provenance du poste d’eau déminéralisée
ou bien du traitement des purges des GVs. La soude provient de la décomposition
à chaud des carbonates contenus dans l’eau brute au condenseur. Elle est relâchée
par les résines échangeuses d’ions. A contrario, une pollution acide provoque une
augmentation de la seule conductivité cationique détectable (la baisse du pH étant
plus difficile à détecter si la pollution est faible). Entre ces deux cas de figure extrêmes,
l’insertion d’eau de refroidissement (eau brute), ou de phosphate trisodique, conduit
à une augmentation simultanée du sodium et de la conductivité. Cette augmentation
est corrélée linéairement s’il s’agit d’une entrée d’eau brute. On peut donc identifier le
type de pollution du secondaire en suivant la concentration en ions sodium (ou plutôt
son écart par rapport à la norme) et la conductivité cationique (Figure 6.103). Les
Figure 6.104 et Figure 6.105 montrent les mesures de suivi de la qualité de l’eau du
secondaire.
Le choix du pH du circuit secondaire à retenir est un compromis entre plusieurs
choix aux conséquences antagonistes. D’une part, il faut éviter un pH trop basique qui
attaquerait les alliages cuivreux dont sont faits les tubes des condenseurs de rivière
et de certains réchauffeurs à tubes. D’autre part, il faut éviter les pH trop acides
qui endommageraient les aciers au carbone non alliés des tuyauteries et des corps de
réchauffeurs. Enfin, il faut limiter la quantité de réactifs adjuvants pour maintenir une
bonne efficacité des résines de rétention (résines échangeuses d’ions) et pour limiter les
rejets en polluants. Le Tableau 6.10 montre qu’un pH basique légèrement supérieur
à 9 à 25 ◦C est le choix optimal, surtout pour les tranches en bord de mer. Un
pH de 9,2 est retenu pour un conditionnement à la morpholine pour les centrales
de rivière (Tableau 6.11), sans dépasser 9,3 pour éviter une corrosion ammoniacale.
Pour les centrales de mer, on préférera un pH de 9,7 avec un conditionnement à
l’ammoniaque et de 9,5 avec un conditionnement à la morpholine (en prenant garde
à la décomposition de la morpholine en acides organiques).
