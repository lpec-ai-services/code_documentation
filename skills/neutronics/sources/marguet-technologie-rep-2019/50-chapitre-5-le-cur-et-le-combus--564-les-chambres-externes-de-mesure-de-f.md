# Chapitre 5 Le cœur et le combustible du réacteur — 5.6 Surveillance du réacteur — 5.6.4 Les chambres externes de mesure de flux … 5.6.5 Les thermocouples
<!-- source PDF pages 675-694 -->

<!-- page 659 (PDF 675) -->
Fig. 5.133 – Position relative du collectron par rapport aux aéroballs dans un
assemblage EPR.

### 5.6.4 Les chambres externes de mesure de flux

Le système RPN, composé de chambres externes à la cuve, mesure le niveau absolu de
puissance et la distribution relative de puissance en temps réel. La mesure du niveau
de puissance est ajustée sur une mesure faite par bilan enthalpique au secondaire.
Un ajustement périodique (calibrage) est nécessaire car la proportionnalité entre la
mesure externe et le niveau de puissance réel du réacteur dépend de la composante
radiale de la distribution de puissance qui varie avec l’épuisement du combustible.
La mesure de la distribution relative de puissance est scindée en deux mesures, l’une
pour la composante radiale et l’autre mesurée en continu pour des questions de sûreté
pour la composante axiale (contre le risque d’instabilité Xénon).
Principe des chambres à dépôt de bore
Le principe de la détection des neutrons par les chambres à dépôt de bore 10
(Figure 5.134) contenu dans du BF3 ou par vapo-déposition de diborane B2H6 dont
le bore est enrichi à 99,9 % en bore 10, est basé sur l’ionisation d’un gaz sous une
pression d’environ 30 kPa, l’argon, par la particule alpha émise lors des réactions :
0n + 10
5B →7
3Li + 4
2He + 2, 785MeV
0n + 10
5B →7
3Li∗+ 4
2He + 2, 316MeV
En ce qui concerne la deuxième réaction, le lithium 7 produit est excité et se désintègre
sur son fondamental :
3Li∗→7
3Li + γ (0, 48MeV )
Le parcours des ions lithium, particules α ou des γ dans le gaz argon produit intensément
des paires ions-électrons et les électrons sont collectés par l’âme centrale du
détecteur : l’anode d’environ 25 μm de diamètre. Le courant ainsi collecté fournit une
indication du flux neutronique vu par la chambre après étalonnage.
L’inconvénient d’un tel type de chambre est qu’elle est sensible aux rayons gamma
qui la traversent et qui ionisent aussi l’argon. A priori, on peut récupérer ce problème
lors de l’étalonnage. Pour traiter plus correctement ce biais, on peut compenser la

<!-- page 660 (PDF 676) -->
Fig. 5.134 – Principe d’une chambre à dépôt de bore non compensée.
Fig. 5.135 – Principe d’une chambre à dépôt de bore compensée.
chambre. Pour se faire, on place à côté de la chambre à dépôt de bore, une chambre
sans dépôt de bore qui ne sera sensible qu’aux rayons gamma. Cette chambre additionnelle
crée un courant électrique uniquement dû aux gammas qui est compensé par
le courant gamma de la chambre à dépôt de bore. Un montage électrique adéquat permet
de ne mesurer que le courant créé par les neutrons (Figure 5.135, Figure 5.136).
Dans ce montage, l’électrode collectrice est commune aux deux chambres. Les électrodes
haute tension sont connectées à des potentiels de polarité opposée, tels qu’on
obtient deux courants inverses sur l’électrode centrale. La première chambre produit
un courant Ineutrons + Iγ,1, la deuxième chambre ne produit qu’un courant Iγ,2. En
ajustant Iγ,2 = Iγ,1 grâce à la valeur de la haute tension, on obtient par compensation
le courant uniquement dû aux neutrons.
La dérive des chambres au cours du temps impose de recalibrer celles-ci tous les
3 mois sur les mesures internes du RIC.

<!-- page 661 (PDF 677) -->
Fig. 5.136 – Chambre à dépôt de bore compensée : description.
Utilisation des chambres externes
Le réacteur dispose de plusieurs types de chambres externes utilisées en fonction
du niveau de puissance : les chaînes proportionnelles dites « source » ou CNS, les
chaînes à dépôt de bore d’ionisation compensée aux rayons gamma, dites « intermédiaires
» ou CNI et les chaînes d’ionisation non compensée de « puissance » dites CNP.
Les chambres sources et intermédiaires
En pratique, on utilise des chambres au bore comme chambre source (2 sur les paliers
antérieurs à l’EPR, 3 placées à 120◦sur l’EPR, Figure 5.143) pour une gamme de
flux mesurable de 1 à 106 n/cm2/s, sensibilité de 10 coups/n/cm2/s avec un bruit de
fond de 0,1 coup/s, durée de vie d’environ 6 ans. Les impulsions dues aux photons
sont éliminées par un bloc de traitement incorporé dans l’électronique du système.
À faible niveau de flux neutronique, c’est-à-dire tant que les fissions ne dégagent
pas significativement de la chaleur, il faut quand même pouvoir suivre la divergence
du réacteur. Si on effectue une divergence sans palier, c’est surtout la réponse aux
gammas des produits de fission, déjà présents dans le combustible, qui domine le signal
de réponse des chambres, produisant un signal constant en début de divergence qui
masque la réponse des chambres aux neutrons et aux gammas de fission (Figure 5.137).
En compensant la contribution gamma, on peut suivre correctement la divergence.
À très bas niveau de puissance (d’environ 10−9 % Pnom à 10−3 % Pnom), les
chaînes sources sont constituées de compteurs proportionnels à dépôt de bore, qui
permettent de différencier les neutrons des gammas.
Les CNS délivrent une alarme « flux élevé » qui est le seul moyen d’assurer la
surveillance de la réactivité pendant les phases d’arrêt. Cette alarme est réglée à au
moins trois fois la valeur du signal mesuré sur les CNS, sans tolérance. Sur le palier
CPY, ce sont des automaticiens qui interviennent dans les armoires RPN pour chaque
modification du seuil. En phase de décroissance, il faut veiller à baisser le seuil au
risque de se faire surprendre par une dilution intempestive. En phase de croissance du
flux, il faut réactualiser régulièrement le seuil pour éviter un AAR par dépassement
du seuil.

<!-- page 662 (PDF 678) -->
Fig. 5.137 – Comptage des chambres externes lors d’une divergence sans palier.
À niveau intermédiaire, les chambres intermédiaires sont constituées de chambres
d’ionisation compensées à dépôt de bore type CC80 de Merlin-Gérin selon un brevet
CEA. Dans cette gamme, le courant dû aux rayons gammas issus du cœur est important
par rapport au courant induit par l’effet des neutrons, d’où l’utilisation de deux
chambres : l’une à dépôt de bore sensible aux neutrons et aux gammas, et l’autre
sans dépôt de bore uniquement sensible aux gammas. La sensibilité aux neutrons est
d’environ 0,0007 ampère/n/cm2/s. La compensation des gammas par les produits de
fission est très efficace puisqu’on estime que le signal résiduel des gammas n’est que de
1 % par rapport à un signal non compensé. Pour simplifier l’installation dans les puits de
chambres, on monte dans un « assemblage » rigide cylindrique chargé en polyéthylène
(matière chargée d’améliorer la thermalisation des neutrons) un compteur CNS et une
chambre CNI (Figure 5.138, Photo 5.16). On s’arrange pour placer la chambre CNI
au niveau du plan médian, la CNS étant alors placée dans le quart inférieur, là où le
flux de neutrons est le plus important au démarrage et à proximité des sources fixes de
démarrage.
Les chambres de puissances
La mesure de la puissance du cœur est effectuée en continu via les chambres de puissance
non compensées (CNP ou CINC, gamme de mesure entre 5 × 102 n.cm−2.s−1
à 5 1010 n.cm−2.s−1 correspondant à une puissance comprise entre 10−1 % et 200 %
de puissance nominale), avec une sensibilité aux neutrons par section de chambre

<!-- page 663 (PDF 679) -->
Fig. 5.138 – Assemblage de chambres pour réacteur CPY : 3 câbles pour la CNI,
1 câble pour la CNS proportionnelle.
d’environ 1,2 × 10−13ampère/n/cm2/s. Comme le flux gamma des produits de fission
devient négligeable à haute puissance, il n’est plus nécessaire de compenser les
chambres. En ce qui concerne les gammas de fission instantanés, ils sont proportionnels
au flux de neutrons et n’ont donc pas besoin d’être compensés. Quatre chambres
d’ionisation à dépôt de bore enrichi sont placées à l’extérieur de la cuve dans chaque
quadrant du cœur (diagonales du cœur) à une distance de 30 cm de la cuve. Ces 4
chambres (RPN 10 MA, RPN 20 MA, RPN 30 MA et RPN 40 MA) sont étagées pour

<!-- page 664 (PDF 680) -->
Photo 5.16 – Installation d’une chambre externe dans son puits. Les chambres
sont placées autour de la cuve dans huit puits pratiqués dans le blindage primaire. Ces puits
s’étendent du bas du cœur jusque sous l’anneau support de cuve. Chaque puits est prolongé
par une cheminée verticale débouchant dans le fond de la piscine BR.
le CPY en 6 sections axiales : 3 pour la moitié supérieure et 3 pour la moitié inférieure.
Dans le cas des CPY, les 3 chambres supérieures sont mises en série ensemble (« tressées
»), de même que les 3 chambres inférieures, ceci fait qu’on obtient une mesure
globale pour la partie supérieure et une autre mesure globale pour la partie inférieure.
On ne connaît donc pas le signal émis par chaque chambre séparément. Une chambre
élémentaire est constituée d’une âme cylindrique interne dont on prélève le signal et
une électrode externe cylindrique qui est portée à une haute tension positive. Les
parties au regard des deux électrodes interne et externe sont recouvertes d’un dépôt
de bore amorphe enrichi en bore 10. Les charges électriques libérées dans le volume
gazeux par le passage des particules ionisantes (alpha produit par capture neutron
du bore 10) sont récupérées par l’électrode signal S (Figure 5.140). Deux types de

<!-- page 665 (PDF 681) -->
Fig. 5.139 – Principe des mesures de puissance et de delta I.
Fig. 5.140 – CNP de réacteur CPY (type CBL 15 tressée, 2 signaux) ou P4 (type
CBL 60, 6 signaux séparés).
chambres ont été utilisés sur le palier CPY : la CBL10 (chambre longue) utilisant
de l’azote comme gaz de remplissage, la CBL15 remplie à l’argon tenant mieux sous
irradiation, et utilisant des électrodes plus courtes et plus espacées pour une meilleure
vision du cœur.
La puissance nucléaire par chaîne q est donnée à partir de la mesure des courants
des chambres via une calibration (Figure 5.139) :
Pr (q) ≡Kq (Kq
HIq
H + Kq
BIq
B) ×
□
1 + γ
□
T q
0 −T q
f
□□

<!-- page 666 (PDF 682) -->
Le déséquilibre d’Index est donné par :
ΔI ≡AO × %Pnom ≡α (Kq
HIq
H −Kq
BIq
B)
Kq est un coefficient ajustable servant à recaler le signal mesuré sur le bilan thermique
BIL100.
Kq
H et Kq
B sont les sensibilités des chambres haute et basse, recalibrées périodiquement
(essais EP RPN 11 tous les 30 JEPP, où on calibre le système de protection
à l’équilibre xénon par mesure de carte de flux complète et EP RPN 12 où on réactualise
la matrice de transfert T du SPIN pour le palier 1300 et les coefficients, Kq,Kq
H,
Kq
B, et α, par une oscillation xénon, sur une carte de flux 1/8 tous les 90 JEPP).
L’essai RPN15 permet de recaler ces coefficients lorsqu’on ne recale pas le coefficient
Kq mais que le déséquilibre radial DPrad dépasse 2 %. Cet essai est réalisé tous les 30
JEPP avec une tolérance de 3 JEPP. Cet essai doit être effectué à puissance nominale
stable.
Iq
H et Iq
B sont les courants respectivement des trois sections hautes et des trois
sections basses tressées (cas du CPY).
γ est un coefficient de correction de température (déterminé par l’essai RPN15).
T q
0 −T q
f est l’écart de température de consigne froide dans les conditions de calibrage
à la température mesurée en branche froide dans la boucle au regard de la
chambre externe.
Dans le cas des 1 300 MWe, le courant de chacune des 6 chambres CBL60 est
mesuré séparément, ce qui fait que l’information axiale est plus riche. D’autre part,
la taille de chaque section (100 mm) est réduite par rapport aux chambres CPY.
On notera aussi que ces chambres sont placées dans un « assemblage » contenant
du polyéthylène (qui a toujours la fonction de thermaliser les neutrons rapides issus
du cœur, Figure 5.141) avec des fenêtres tournées vers le cœur et recouvertes en
Fig. 5.141 – Chambre CBL60 collimatée : principe.

<!-- page 667 (PDF 683) -->
Fig. 5.142 – Positionnement des chambres externes du palier CPY(détail).
face externe de cadmium pour collimater les neutrons rapides et ne conserver que
les neutrons venant du cœur. L’autre partie de la chambre tournée vers l’extérieur
du cœur comporte une plaque de cadmium mais cette fois située contre l’électrode,
ce qui fait que tous les neutrons rétrodiffusés vers la chambre sont d’abord ralentis
par le polyéthylène, puis capturés par le cadmium. On parle de chambre collimatée
puisqu’on privilégie les neutrons rapides qui n’ont pas été diffusés en sortant du cœur.
On notera que les chambres de puissance CBL15C du CP0 et CBL60 des paliers 1300
et N4 sont collimatées, alors que les chambres CBL10 et CBL15 du palier CPY ne le
sont pas.
La mesure des courants produits par les étages inférieurs et supérieurs permet de
remonter à la puissance basse et haute, d’où l’axial-offset et le différentiel d’index ΔI.
Les chambres sont ré-étalonnées tous les 90 JEPP à l’aide des mesures RIC et du
bilan enthalpique BIL100. Une des fonctions des chaînes de puissance est d’activer
la protection « haut flux neutronique » dont le seuil est placé à 109 % de la puissance
nominale. Le suivi des 4 quadrants permet de suivre le déséquilibre azimutal de
puissance du cœur. On définit la puissance moyenne du cœur vue par l’ensemble des
chambres en sommant sur les quadrants :
Pr (moy) ≡1
□
q=1
Pr(q)

<!-- page 668 (PDF 684) -->
Fig. 5.143 – Positionnement des chambres externes de l’EPR.
Le déséquilibre azimutal de puissance neutronique maximum est donné par
DPazn (max) ≡Pr(max) −Pr (min), quand le déséquilibre moyen est donné par :
DPazn (moy) ≡1
□
q=1
|Pr(q) −Pr (moy)|
Un déséquilibre azimutal excessif générera une alarme en salle de commande.
En plus des chambres de puissance, on dispose sur le palier CPY de 2 compteurs
proportionnels (CP, gamme de mesure entre 10−1 n.cm−2.s−1 à 105 n.cm−2.s−1) dans
la gamme source (4 sur le P4) qu’on appelle aussi détecteurs de niveau source, qui
permettent de suivre l’approche sous-critique de démarrage du cœur, et de 2 chambres
d’ionisation compensée (CIC, gamme de mesure entre 2,5 × 102 n.cm−2.s−1 à
2,5 × 1010 n.cm−2.s−1) dans la gamme intermédiaire (4 sur le P4). Les détecteurs de
niveau intermédiaires cohabitent avec les détecteurs de niveau source à raison d’un
détecteur source et un détecteur intermédiaire dans chaque container, ceux-ci étant
placés à la périphérie de la cuve sur les médianes du cœur (Figure 5.142, Figure 5.144,
Figure 5.145, Figure 5.147). La Figure 5.146 présente la localisation des chambres de

<!-- page 669 (PDF 685) -->
Fig. 5.144 – Positionnement des chambres externes.
Fig. 5.145 – Implantation des puits des chambres externes sur le palier CPY
(coupe radiale).

<!-- page 670 (PDF 686) -->
Fig. 5.146 – Localisation radiale des chambres de puissance de la centrale Virgil
Summer. Cette centrale de 966 MWe (2 900 MWth) est refroidie par 3 boucles. Elle a été
construite par Westinghouse en Caroline du Sud près de Jenkinsville, et mise en service en
1984. À partir de 2012, Westinghouse a commencé à construire sur le site deux AP1000,
mais la faillite de Westinghouse Electric Company en 2017 (9 milliards de dollars de perte !)
a provoqué l’arrêt total du projet.
puissance de la centrale Virgil C. Summer aux États-Unis au design très proche des
CP0 français avec bouclier thermique intégral.
Les chambres externes sont placées dans des puits et positionnées près de la cuve
par un système de pantographes, tel que montré sur les Figure 5.148, Figure 5.149 et
Figure 5.150.

<!-- page 671 (PDF 687) -->
Fig. 5.147 – Gamme de mesure des chambres externes.

<!-- page 672 (PDF 688) -->
Fig. 5.148 – Positionnement des chambres par pantographe.

<!-- page 673 (PDF 689) -->
Fig. 5.149 – Détail du déplacement d’une chambre RPN par pantographe (CPY)
(adapté de : [Instrumentation du cœur, 1977] p. 9).

<!-- page 674 (PDF 690) -->
Fig. 5.150 – Comparaison en coupe verticale des systèmes de pantographes des
réacteurs 1 300 MWe (à gauche) et 900 MWe (à droite).

<!-- page 675 (PDF 691) -->
Fig. 5.151 – Localisation des thermocouples et des chambres à fission mobiles de
la centrale Virgil Summer (966 MWe, Westinghouse, États-Unis).

<!-- page 676 (PDF 692) -->
Fig. 5.152 – Schéma d’implantation des thermocouples sur un réacteur CPY.

### 5.6.5 Les thermocouples

[McGee, 1988] p. 237
Généralités
Des thermocouples (TCs) (48 sur le CP0, 51 sur CPY, 54 sur le N4, Figure 5.153)
mesurent la température en sortie d’assemblages, en général au-dessus des dispositifs
de mélange qui servent à uniformiser les températures à la sortie des assemblages. Les
thermocouples sont solidaires mécaniquement des internes supérieurs. Ils pénètrent la
cuve à travers 4 pénétrations du couvercle de la cuve, et sont guidés à l’intérieur de la
cuve par des conduits en acier inoxydable (Z2 CN 19-10, diamètre extérieur : 7,9 mm,
diamètre intérieur : 4,8 mm) fixés de façon permanente aux équipements internes
supérieurs. Ces conduits sont courbés suivant un rayon de 152 mm. Un rétreint est
réalisé côté soudure chaude qui se situe au-dessus de la plaque supérieure de cœur.
L’autre extrémité est équipée d’un connecteur situé au-dessus du couvercle de cuve.
Les thermocouples sortent à l’extrémité des conduits et la soudure chaude des deux

<!-- page 677 (PDF 693) -->
conducteurs, formant un couple thermoélectrique 54. Ils sont positionnés par des goussets
situés légèrement au-dessus de la plaque supérieure du cœur au regard supérieur
d’un assemblage. Les conduits sont solidaires des colonnes entretoises des internes
supérieurs, entre leur partie inférieure et la plaque support des tubes guides, puis par
4 colonnes vissées à la plaque support des tubes guides, entre la plaque et l’extérieur.
Chacune de ces colonnes contient 13 conduits et sort de la cuve par une manchette
enchâssée dans le couvercle de cuve. Le cheminement des thermocouples est divisé
en une voie A et une voie B. Des connecteurs assurent la liaison électrique entre les
deux métaux conducteurs du thermocouple et des conducteurs de même nature d’un
câble souple dit « prolongateur » qui renvoie le signal. Ces prolongateurs cheminent
selon les deux voies séparées (A et B) jusqu’à deux platines porte-connecteurs. Depuis
les platines, les 28 câbles de prolongation du RIC vont jusqu’au boîtier de soudures
froides. Du boîtier sortent des câbles de prolongation en cuivre jusqu’au multiplexeur,
qui renvoie les informations de température en continu au calculateur RIC.
Les thermocouples ont la triple fonction de :
• permettre de calculer la marge à la saturation. Les deux fois 11 câbles de
prolongation des TCs de l’ébulliomètre cheminent séparément des TCs du
RIC jusqu’aux armoires SIP via les traversées électriques de l’enceinte du BR.
L’ébulliomètre est le système qui permet de connaître la sous-saturation de
l’eau. Il utilise 22 TCs dont 2 sous le dôme pour fournir la marge à la saturation ;
• mesurer la température sous le dôme (2 TCs), utilisés par l’ébulliomètre ;
• détecter d’éventuelles anomalies de distribution de puissance. Notons qu’en cas
de l’indisponibilité d’une des quatre chambres externes de puissance, on utilise
les TCs en remplacement de la chambre pour suivre l’évolution du tilt radial,
ce qui améliore la disponibilité de la tranche. Le calculateur de tranche KIT
peut calculer le tilt radial en ligne.
Notons aussi une utilisation systématique du suivi des TCs lors des problèmes des
doigts de gants des CFMs en mars 1987 sur Paluel 1 et 2, qui avaient conduit à
rendre indisponible le système RIC de CFMs pendant un temps. C’est donc grâce à
l’analyse des TCs qu’on a pu justifier la montée en puissance et le fonctionnement
au-delà de 50 % de puissance nominale.
Les thermocouples sont placés de façon dissymétrique (dans le cas du N4, 52 en
sortie d’assemblages et 2 dans le dôme). Dans le cas du P4, 28 TCs cheminent jusqu’au
boîtier de soudures froides situé dans l’espace annulaire et qui servent au calculateur
RIC en salle du calculateur. Dix en voie A sont traités par l’ « ébulliomètre voie A »
situé dans le local ULS voie A. Dix autres pour l’ « ébulliomètre voie B » en local
ULS voie B et 2 (une en voie A, l’autre en voie B) ont été remontés pour mesurer la
température dans le bas du volume du dôme sous le couvercle (contrôle d’une éventuelle
bulle piégée sous le dôme). Les mesures des 28 thermocouples RIC et des 2×11
thermocouples « ébulliomètre » sont transmises au traitement centralisé de l’information
(TCI) pour élaboration des cartes de températures, qui sont visualisables au
calculateur KIT en salle de commande et qui sont réactualisées toutes les 20 secondes
54 Le couple thermoélectrique utilisé est le couple Chromel-Alumel (nickel chrome/nickel allié
type K) gainé par de l’acier inoxydable (Z2 CND 17 12/ 316L, diamètre 3,17 mm, épaisseur 0,4 mm)
et isolé à l’alumine dont la précision est de +/ −1, 5 ◦C entre 0 ◦C et 375 ◦C et de +/– 0,4 % de
375 ◦C à 1 200 ◦C où ils subissent une dégradation irrémédiable. Des sondes à résistance permettent
d’assurer les corrections des soudures froides. Les gaines de thermocouple sont fabriquées par les
sociétés THERMOCOAX ou Câbles de Lyon. Les connecteurs sont de type THERMOELECTRIC
puis LEMO pour le CP0/CPY, et Deutsch pour le palier 1 300 MWe.

<!-- page 678 (PDF 694) -->
(durée de l’échantillonnage du KIT). Dans le cadre de l’ébulliomètre, le système fournit
, pour utilisation dans la conduite APE (Approche Par État) la température et
la marge cœur à la saturation à la sortie des assemblages et, sous le couvercle dans
le dôme, le niveau d’eau dans la cuve et le couple marge cœur/niveau cuve intervalidé
. Pour pouvoir être utilisé en accidentel, l’ébulliomètre prend en compte les deux
gammes des thermocouples : 0 −400 ◦C et 0 −1 200 ◦C (où la précision est moins
bonne).
Mesure du tilt radial
Les thermocouples (Figure 5.151 pour la centrale de Virgil Summer, Figure 5.152,
Figure 5.153, Figure 5.157, Figure 5.158) permettent en théorie de mesurer le tilt
radial, c’est-à-dire le déséquilibre radial de puissance. Cette mesure est normalement
acquise par les chambres RPN, mais les thermocouples sont mentionnés comme un
moyen palliatif à une situation de chambre indisponible. Néanmoins, des études
récentes 55 ont montré que l’échantillonnage dissymétrique induisait un tilt numérique,
quelle que soit la méthode de reconstruction des assemblages non instrumentés. Ce
problème est identique en utilisant les chambres à fission mobiles. Ce tilt numérique
ne peut être déconvolué qu’en utilisant des instrumentations symétriques, qui sont
en faible quantité dans le cœur. On peut utiliser les mesures de températures pour
calculer une puissance thermique par quadrant de manière identique aux chambres
externes de puissance. On pourra alors calculer un déséquilibre azimutal de puissance
thermique :
DPazt (moy) ≡1
□
q=1
|Pth(q) −Pth (moy)| .
Le déséquilibre radial de puissance est alors donné par :
DPrad ≡DPazt (moy) ≡Pth (moy) −Pr (moy)
Défaillances de thermocouples
Comme tout composant, les thermocouples subissent des défaillances. En premier lieu,
on a constaté une « maladie de jeunesse » apparue la première année d’utilisation,
dont les effets ont été une corrosion avec percement de la gaine du thermocouple et
perte de l’isolement (évaluée par la mesure de la résistance d’isolement en ohms). Les
défauts qui sont apparus sont des fissures traversantes perpendiculaires à l’axe de la
gaine, et amorcées par des piqûres ou des tâches de corrosion, toujours localisées dans
les parties droites horizontales des thermocouples situés entre deux cintres de rayon
152 mm. L’origine de cette corrosion pourrait être la présence de chlore dans l’huile
de tréfilage des conduits ou du solvant. La résolution de ce problème a été d’améliorer
la qualité de la fabrication. Le taux de « mortalité » a aussi augmenté au bout de
trois ans suite à des interventions en grand nombre entre 1988 et 1989 sur le palier
1 300 MWe et la mise en place d’un critère plus restrictif sur le seuil d’isolement.
La qualité des connecteurs montables sur site peut aussi poser des problèmes de
baisse de la résistance d’isolement (critère d’isolement fixé à 1 MΩ), ce qui rend indisponible
de nombreuses lignes de mesure. Les connecteurs ont un taux de défaillance
55 Patrick Erhard, communication personnelle, 2009.
