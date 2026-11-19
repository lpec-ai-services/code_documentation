# Chapitre 5 Le cœur et le combustible du réacteur — 5.4 Le système de contrôle des barres de commandes (RGL) — 5.4.3 Constitution des grappes de commande … Les pas extraits cumulés
<!-- source PDF pages 609-623 -->

<!-- page 593 (PDF 609) -->
### 5.4.3 Constitution des grappes de commande

Barres noires AIC
Les grappes sont constituées d’absorbants neutroniques. Pour les barres très absorbantes
(dites noires), on utilise un mélange dit AIC d’argent (85 %), indium (10 %)
et de cadmium (5 %), gainé en acier 304 (Figure 5.64, Figure 5.65). Le cadmium
est un puissant absorbant de neutrons thermiques et l’indium et l’argent absorbent
grâce à des résonances décalées les neutrons épithermiques. Le mélange absorbant,
sous forme de barreau continu (pas des pastilles comme le combustible !), se trouve
dans une gaine en acier austénitique Z2CN18-10 (diamètre : 9,7 mm, épaisseur CPY :
0,45 mm, épaisseur P4 : 0,98 mm).
Fig. 5.64 – Un crayon AIC (Argent-Indium-Cadmium) d’un CPY.

<!-- page 594 (PDF 610) -->
Fig. 5.65 – Schéma d’implantation des crayons absorbant d’une barre noire CPY
et P4/N4.
Barres grises
Dans le mode G, on utilise des barres de compensation de puissance dites grises
composées d’acier inoxydable (Figure 5.66, Figure 5.67). Ces barres, qui sont moins
absorbantes que les barres noires, permettent de ne pas trop déformer la trace axiale
de flux, donc l’axial-offset.
Barres hybrides
Sur le palier 1 300 MWe, on a introduit des grappes mixtes noires composées de
crayon AIC dont la partie supérieure est en carbure de bore B4C (Figure 5.68,
Figure 5.69). L’objectif est d’augmenter le poids neutronique de la barre sans que
la partie inférieure, souvent présente dans le cœur, soit en carbure de bore. En effet,

<!-- page 595 (PDF 611) -->
Fig. 5.66 – Barre en acier inoxydable (groupe G1 et G2 du mode G).

<!-- page 596 (PDF 612) -->
Fig. 5.67 – Schéma d’implantation des crayons absorbants dans une grappe grise
(CP et-P4).
le carbure de bore peut gonfler par production d’hélium (réaction (n,alpha) sur le
bore 10) de façon inopportune sous flux neutronique (c’est pourquoi on n’en met que
dans la partie supérieure de la grappe).

### Barres bouchons

On notera que les assemblages qui ne sont pas grappés dans le cœur disposent
chacun d’une grappe « bouchon » (Figure 5.70, Figure 5.71). Il s’agit de tubes d’acier
inoxydables de 30 cm de hauteur qu’on place pour obturer les trous d’eau. Ils ont

<!-- page 597 (PDF 613) -->
Fig. 5.68 – Crayon mixte AIC (partie basse)-B4C (partie haute) pour les 1 300
MWe.

<!-- page 598 (PDF 614) -->
Fig. 5.69 – Schéma d’implantation des barres grises du N4.
comme fonction d’éviter un débit d’eau par les trous d’eau qui by-passerait le cœur, et
qui exercerait une poussée hydrodynamique différente des assemblages grappés. Les
assemblages contenant des crayons pyrex ou hafnium n’ont pas besoin de ce dispositif.

### Barres fixes

Signalons aussi l’usage de grappes en boro-silicate dit pyrex pour diminuer la
réactivité des premiers cœurs (Figure 5.71). Ces grappes fixes dans le cœur sont
ensuite enlevées au deuxième chargement pour retrouver de la réactivité. À partir

<!-- page 599 (PDF 615) -->
Fig. 5.70 – Une grappe bouchon.
Fig. 5.71 – Comparaison des différents types de grappes.
de 2018, on a aussi introduit sur Tricastin des barres fixes en hafnium dans les
assemblages de bout de médiane du CPY, pour réduire encore plus la fluence cuve.
La technique va se généraliser sur tout le palier CPY.

<!-- page 600 (PDF 616) -->
### 5.4.4 Système de comptage des pas de groupe

L’instrumentation
Un système de mesure des positions de grappe est placé sur les carters logeant les tiges
de barres au-dessus des adaptateurs de couvercle. Les tiges de commandes de grappe
sont constituées d’acier inoxydable magnétique, alors que les carters (ou gaine de tige)
sont en acier non magnétique. Le capteur de mesure est constitué de deux enroulements
concentriques autour de la gaine. La tension recueillie sur la bobine secondaire
dépend de la présence ou de l’absence de la tige. La connexion des différentes bobines
secondaires à chaque niveau permet de mesurer le nombre de spires qui « voient » la
tige de barre, et donc on peut en déduire sa position de façon absolue, mais avec une
incertitude de plusieurs pas (Figure 5.72, Figure 5.73).
L’usage est de définir la position axiale des groupes de barres en pas extraits.
Cette convention fait que la position totalement extraite d’une barre d’un réacteur
900 MWe est de 225 pas et de 260 pas pour les 1 300 MWe et le N4. Cette valeur
est couramment appelée AMPAS à EDF. La hauteur d’un pas est de 1,5875 cm
soit 1,6 inch. Il faut attendre l’EPR pour que le pas vaille enfin 1 cm pour un
AMPAS de 413.

### Le paramètre P(1)

Lorsque les barres des différents groupes de compensation de puissance (GCP : les
groupes D, C, B, A en mode A et les groupes G1, G2, N1, N2 en mode gris) bougent
selon une loi de puissance, on a défini la notion de paramètre P(1) (on dit oralement
paramètre P un). La définition numérique du paramètre P(1) permet de faire correspondre
de façon univoque une position donnée à tous les GCPs. Le paramètre P(1)
est donc une façon condensée de définir la position des groupes. Quand le paramètre
P(1) progresse de un pas, tous les groupes en recouvrement qui sont dans le cœur sans
être en position basse, peuvent s’insérer chacun de un pas. Le calcul du paramètre
Fig. 5.72 – Règle de calcul des cotes axiales par rapport au milieu du cœur
(CPY).

<!-- page 601 (PDF 617) -->
Fig. 5.73 – Système de mesure de la position axiale d’une barre.
P(1) est utilisé dans la formule :
cote(groupe1) ≡P(1)
cote(groupei+1) = cote(groupei) + AMPAS −AREC(i)
où cote est la position en pas des groupes et AREC(i) le recouvrement entre le
groupe i+1 et le groupe i.

<!-- page 602 (PDF 618) -->
Recouvrement nul
Fig. 5.74 – Insertion de barres à recouvrement nul.
On prendra garde à ne pas confondre le paramètre P(1) avec le groupe variable
P1 de l’EPR.

### Les recouvrements

Le recouvrement est le nombre de pas extraits du groupe i + 1 insérés dans le cœur
au moment où le groupe i commence à rentrer dans le cœur. On numérote les groupes
dans l’ordre de leur entrée dans le cœur. La façon la plus simple de visualiser le
problème de l’insertion des barres est d’imaginer par la pensée que les barres ont
un recouvrement nul et se déplacent vers le bas de concert. Dans l’exemple de la
Figure 5.74, cela revient à imaginer que le deuxième groupe de barres de couleur verte
est situé totalement au-dessus du groupe rouge, ce qui est impossible physiquement,
les barres étant, bien entendu, en rideau et affleurant le haut du cœur actif lorsqu’elles
sont extraites du cœur.
À partir de cette situation imaginaire, il est plus facile d’imaginer une situation
tout aussi fictive où les groupes se déplacement toujours ensemble avec un recouvrement
de 100 pas par exemple (Figure 5.75). Ce recouvrement correspond à la zone

<!-- page 603 (PDF 619) -->
Recouvrement 100 pas
Recouvrement 100 pas
Fig. 5.75 – Insertion de barres avec un recouvrement de 100 pas.
où les deux groupes de barres sont au regard dans leur déplacement respectif. On
définit à partir de cette notion les plages de recouvrement ou chevauchement, à savoir
le nombre de pas sur lesquels les deux groupes « successifs » (dans leur entrée dans le
cœur) bougent simultanément, que ce soit en insertion ou en extraction. On parlera
ainsi de la plage de recouvrement entre les groupes G1 et G2, notée G1/G2, puis
G2/N1 et enfin N1/N2, dans le cas du mode G. On parle de seuils de recouvrement
en début d’extraction pour décrire les positions des groupes G2, N1, N2 en dessus
desquelles les groupes G1, G2, et N1 s’extraient simultanément. De même, on définit
les seuils de recouvrement en début d’insertion pour décrire les positions des groupes
G1, G2, N1 en dessous desquelles les groupes G2, N1, N2 s’insèrent simultanément.
Enfin, on définira les écarts des groupes en chevauchement comme le nombre de pas
d’écart entre la position des bouts de barres de deux groupes en chevauchement, qu’on
notera G2-G1, N1-G2, N2-N1.
Pour un 900 MWe, la valeur minimale du paramètre P(1) correspond à l’insertion
maximale de tous les quatre groupes qui auraient eu des recouvrements nuls entre
eux, soit – 675 (3 fois 225). Pour un 1 300 MWe, cette valeur minimale est de –
780 et de – 1 040 pour le N4. La valeur maximale du paramètre P(1) pour un 900
MWe correspond à l’ensemble des barres extraites (Figure 5.76), soit + 225. On parle
aussi de paramètre P(2) pour la position du groupe R de régulation en mode gris.
La courbe de calibrage des GCPs est la fonction qui relie le paramètre P(1) avec le
niveau de puissance. Cette courbe de calibration G3, dite aussi parfois CONVG3,
est mesurée expérimentalement par des essais de baisse de puissance rapide (l’essai
physique RGL4) et doit être réévaluée en cours de cycle. Le dé-calibrage, appelé
aussi facteur correctif, consiste à effectuer une translation constante dans le sens des

<!-- page 604 (PDF 620) -->
Recouvrement nul
P(1)= - 675
Recouvrement nul
Recouvrement nul
P(1) = + 225
Fig. 5.76 –
Valeurs
extrêmes
du
paramètre
P(1)◦
pour
un
900MWe
à
recouvrement nul.
puissances croissantes de la courbe de calibrage. Le dé-calibrage est limité à 20 % de
la puissance nominale et conduit à des positions de grappes toujours plus extraites
que la calibration standard.

<!-- page 605 (PDF 621) -->
Les recouvrements utilisés sur le parc français sont de :
• 100 pas entre G1 et G2, 90 pas entre G2 et N1, 90 pas entre N1 et N2 sur le
palier CPY ;
• 75 pas entre G1 et G2, 85 pas entre G2 et N1, 100 pas entre N1 et N2 sur le
palier 1 300 MWe (1re campagne) ;
• 65 pas entre G1 et G2, 85 pas entre G2 et N1, 100 pas entre N1 et N2 sur le
palier 1 300 MWe (2e campagne) ;
• 75 pas entre G1 et G2, 85 pas entre G2 et N1, 100 pas entre N1 et N2 sur le
palier 1 300 MWe (3e campagne et suivante) ;
• 208 pas entre P1 et P2, 208 pas entre P2 et P3, 208 pas entre P3 et P4 et 208
pas entre P4 et P5 pour le mode T de l’EPR, avec le fait que selon la situation,
des groupes peuvent être alignés avec le groupe P5 pour former le groupe H.
Insertion maximale de pilotage
Dans la pratique, les tubes guides comportent une partie inférieure rétrécie qui sert de
dashpot quand la barre tombe par gravité. Lorsque la barre est insérée par le système
RGL, on impose qu’elle ne puisse descendre plus bas qu’une cote dite PBASSE de
5 pas d’insertion (9 pas pour l’EPR). On notera qu’en cas d’arrêt automatique réacteur
(AAR), tous les groupes chutent dans le cœur par gravité sans respecter la cote basse
PBASSE, et descendent jusqu’à 0 pas extrait, qui n’est pas situé au bas du cœur actif
mais légèrement plus haut (pour le CPY, les 225 pas insérés correspondent à 225 ×
1,5875 = 357,1875 cm, soit, pour une hauteur active de 365,76 cm, un niveau 0 situé
à 8,5725 cm au-dessus du bas du cœur actif).
Le chevauchement
Malgré une utilisation très répandue du paramètre P(1) dans les codes de calcul, il
existe un usage sur site de comptage de l’insertion des barres en pas de chevauchement.
La course maximale de ce compteur est égale au nombre de pas que peuvent effecter
tous les groupes de compensation de puissance indépendamment les uns des autres,
moins le nombre de pas sur lesquels deux groupes bougent simultanément (i.e. la
plage de recouvrement). Si NG est le nombre de GCPs, la course maximale est donc
donnée par :
Coursemax = Ng (Seuil haut −Seuil bas) −
Ng−1
□
i=1
AREC(i)
Si PBASSE = 5 pas, alors Seuil haut – Seuil bas = 255 pas pour un P4. Lorsque
toutes les barres de compensation de puissance sont hors du cœur, le nombre total de
pas de chevauchement est de 615 pas (pour un CPY, Figure 5.77). Si toutes les barres
sont insérées, on devrait être à 5 pas de chevauchement (soit la position PBASSE),
mais cette situation n’arrive pas physiquement puisqu’en attente à chaud à 0 %Pnom,
toutes les barres ne sont pas insérées (environ 264 pas de chevauchement en début
de campagne et 206 pas de chevauchement en fin de campagne). On constate que
ce compteur de pas de chevauchement Cchevauch est un compteur translaté d’une
constante depuis le compteur P(1). En l’occurrence, la translation s’écrit :
P(1) = Cchevauch −(Coursemax −Seuil haut)
Notons pour finir qu’il existe un compteur de position généralisée, utilisé uniquement
sur le palier N4, qui correspond à une somme pondérée des positions des sous-groupes

<!-- page 606 (PDF 622) -->
Fig. 5.77 – Équivalence entre pas extraits et pas de chevauchement pour un CPY
(avec un recouvrement G1/G2 de 100 pas, G2/N1 de 90 pas, N1/N2 de 90 pas). On retrouve
la valeur de PBASSE de 5 pas sur la figure, cote d’insertion maximale des groupes.
envoyées par le système RGL au KIC, et qui vaut :
Cg´en´eralis´e = 2 × X1 + 2 × X2 + X31 + X32 + X41 + X42 + X51 + X52
Le demi-pas
Pour un pilotage très fin (correction d’axial-offset par exemple), il est assez classique
que les opérateurs désalignent volontairement les sous-groupes R1 et R2 constitutifs
du groupe R, groupe noir qui agit en régulation prioritaire fermée sur la température
moyenne de la cuve en mode G. Ils font cela manuellement en écoutant en salle de
commande le bruit (en fait un clic de synthèse pour restitution produit par un hautparleur
, pas le bruit réel des cliquets bien sûr) que font les cliquets des grappins de
commande de grappe : un premier clic correspond au mouvement d’un pas de R1, puis
le deuxième clic correspond au mouvement d’un pas de R2 dans le même sens (à la
montée ou à la descente), et ainsi de suite. On désaligne d’un pas unique le groupe R2
par rapport au groupe R1 en faisant cliquer à l’oreille 3 fois le groupe R1 et 2 fois
seulement le groupe R2, puis en faisant en sens contraire cliquer 2 fois le groupe R1 et
2 fois le groupe R2. L’idée est qu’il est très difficile de contrôler un clic unique de R1
(on est surpris par le deuxième clic de R2), alors que l’oreille s’habitue au rythme des
clics sur 5 clics ou sur 4 clics (Figure 5.78). Au final, R1 se retrouve décalé d’un pas
au-dessus ou en dessous de R2. On utilise le terme (inexact dans les faits) de demi-pas
pour imager cette situation. Ces actions de demi-pas sont fréquentes sur les paliers à

<!-- page 607 (PDF 623) -->
Fig. 5.78 – Tactique de désalignement d’un pas à l’insertion du groupe R1 par
rapport à R2 (infographie : Patrick Bodet).
partir du P4 où les assemblages sont plus hauts que sur le CPY, et qui présentent des
instabilités d’axial-offset lié au xénon, instabilités qui peuvent être divergentes sans
contrôle.

### Les pas extraits cumulés

Dans le cadre de l’EPR, qui comporte les groupes P1 à P5, on a pris l’habitude de
raisonner en Pas Extraits Cumulés (PEC ou PCUM). La définition du PCUM est
donnée par la formule suivante :
PCUM ≡P1 +
□
i=2
min(Pi, AMPAS −AREC(i) + PBASSE)
P1 à P4 correspondant au nombre de pas extraits des groupes P1 à P4. Le groupe
P5 sert de groupe référent dans la mesure où aucun des autres groupes ne peut se
retrouver placé au-dessus de P5. Cela signifie que si P4 se retrouve à l’extraction au
même niveau que P5, il devient solidaire de P5, de même que pour les autres groupes
P1 à P3. On peut diviser macroscopiquement parlant les groupes P1 à P5 en deux
macrogroupes P et H. Le groupe H, groupe lourd qui est variable dans sa composition
en fonction de la situation, contient les groupes qui sont en rideau avec P5, et le
groupe P, lui aussi variable, contient les autres groupes qui sont en recouvrement.
Cette gestion complexe des barres permet d’assurer un double contrôle de la criticité
et de l’axial-offset par le mouvement des groupes et la dilution/borication. Pour l’EPR,
le nombre de pas extraits maximal AMPAS est de 413 pas actifs (416 pas atteignables
mais avec 3 pas hors du cœur), dans la mesure où les groupes ne peuvent pas s’enfoncer
en suivi de charge à plus de PBASSE = 9, les recouvrements AREC sont de 208 pas
entre P1 et P2, P2 et P3, P3 et P4, P4 et P5.

### 5.4.5 Implantation des groupes de barres

L’implantation des groupes de barres dépend du palier considéré. La particularité des
REPs réside dans le fait que les neutrons migrent dans le cœur peu par rapport aux
réacteurs à eau lourde ou aux UNGG. De fait, il faut répartir un grand nombre de
barres dans l’ensemble du cœur, que ce soit pour le pilotage ou les barres d’arrêt.
