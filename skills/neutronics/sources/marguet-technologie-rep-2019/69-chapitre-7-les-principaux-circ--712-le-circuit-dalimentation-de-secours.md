# Chapitre 7 Les principaux circuits — 7.12 Le circuit d’alimentation de secours des générateurs de vapeur (ASG) … 7.13 Le circuit d’aspersion de l’enceinte (EAS)
<!-- source PDF pages 937-956 -->

<!-- page 921 (PDF 937) -->
Les robinets réglants (classiquement appelés aussi vannes réglantes) permettent de
maintenir le niveau dans les GVs à la valeur de consigne grâce à une régulation.
À faible charge, seule la vanne « petit débit » est ouverte, à forte charge (> 20 %
Pnom), les deux vannes sont ouvertes. Ces vannes sont des robinets à soupape et à
cage équilibrée, pilotée par un servomoteur pneumatique à membrane et actionné par
la pression d’air comprimé. Un ressort de rappel permet de fermer la vanne en cas de
perte électrique. L’asservissement de la position du clapet se fait par un positionneur
pneumatique, précédé d’un convertisseur électropneumatique.
Les clapets anti-retour à battant sont actionnés par la pression de l’eau. Le battant
est ouvert en position normale et se ferme dès que la pression en aval devient supérieure
à la pression amont, pour s’opposer à un mouvement du fluide en sens inverse
de celui désiré. Ces inversions de débit peuvent être provoquées par le déclenchement
des turbopompes d’eau alimentaire, voire une rupture de conduite en amont du clapet
qui aspire l’eau en sens inverse. Notons que la fermeture rapide d’un clapet anti-retour
génère un coup de bélier (pression maximale de l’ordre de 5 fois la pression initiale !),
phénomène hydrodynamique classique qu’on rencontre dans les conduites forcées. La
solution à ce problème est d’utiliser des clapets amortis.
Les vannes d’isolement des vannes réglantes sont identiques aux vannes d’isolement
des vannes réglantes de décharge à l’atmosphère déjà vues sur les lignes
vapeur. Ce sont des vannes à sièges parallèles motorisées électriquement. Elles sont
pilotées par le système de protection du réacteur (RPR) contre les ruptures de
tuyauteries d’eau (RTE) ou de RTV. La fermeture rapide des vannes d’isolement
permet de limiter la vaporisation produite par les GVs, ce qui limite le coup de
froid et ralentit la montée en pression dans l’enceinte si la brèche est située dans le BR.

### 7.11.3 Le supportage des tuyauteries d’eau alimentaire

Le supportage des tuyauteries d’eau alimentaire (Figure 7.66 et Figure 7.67) comprend
les mêmes éléments que les lignes vapeur, sur lesquels nous ne reviendrons pas.
Le palier P4 dispose de plus de dispositifs écrasables, constitués de pions en acier
inoxydable et de bretelles à barres anti-fouettement, qui sont aussi des dispositifs
écrasables qui relient les parties hautes et basses horizontales d’une même tuyauterie
pour limiter leur déplacement relatif. En passant du palier CPY au palier P4, on
a pu minimiser le trajet des tuyauteries d’eau alimentaire en adoptant des sorties
radiales, ce qui diminue le risque de rupture.

## 7.12 Le circuit d’alimentation de secours des générateurs de vapeur (ASG)

[Coppolani et al., 2004] p. 180, [Installations de sauvegarde, 1977] p. 49

### 7.12.1 Principe

Le système d’alimentation en eau de secours du GV (ASG) a comme fonction d’amener
de l’eau secondaire au GV quand elle ne peut plus être amenée depuis le poste
d’eau via le circuit d’alimentation normale ARE. Le système ASG n’est donc pas

<!-- page 922 (PDF 938) -->
Fig. 7.66 – Le supportage du circuit ARE (P4).
Fig. 7.67 – Traversée de la double-enceinte d’une ligne d’eau alimentaire.
engagé en fonctionnement normal, mais doit toujours être disponible 23. Par sa fonction
, l’ASG refoule de l’eau à une pression allant de la pression atmosphérique à une
pression secondaire pouvant atteindre 170 bars en cas de surpression. L’ASG assure
23 Par disponible, on entend un volume minimum utile de 625 m3 (CPY) dans la bâche de
stockage ASG, pression d’azote de 1,13 bar, température entre 7 ◦C et 40 ◦C, les deux motopompes
à l’arrêt de même que la turbopompe, circuit vapeur d’alimentation de la turbopompe conditionné
jusqu’aux vannes automatiques de démarrage qui sont fermées, vannes d’isolement pneumatiques
VVP ouvertes, ballon séparateur en service évacuant les condensats du purgeur, vanne d’arrêt ouverte
soupape réglante (136 VV) d’admission vapeur sous régulateur, soupapes réglantes VD en position
100 % ouverte, poste de dégazage (01 DZ) normalement à l’arrêt (il ne sert que pour renflouer la
bâche de stockage), liaisons avec le condenseur avec les deux tranches de la paire normalement isolées.

<!-- page 923 (PDF 939) -->
aussi des fonctions non liées à la sûreté. L’ASG est utilisée en période de démarrage et
de montée en température du circuit primaire, quand le poste d’eau ne le permet pas,
en période d’arrêt à chaud ou pour passer en arrêt à froid et accrocher les conditions
de mise en service du RRA. L’ASG est aussi utilisée pour remplir les GVs initialement.
Le système ASG est principalement constitué :
• de deux ensembles de pompage et d’injection identiques, alimentant chacun une
paire de GVs (1 300 MWe), chaque ensemble comprenant une motopompe et une
turbopompe alimentaires de secours (à ne pas confondre avec les motopompes et
turbopompes de l’eau alimentaire du circuit ARE). Les pompes doivent pouvoir
fournir le débit requis à la pression du timbre des GVs (89,6 bars absolus pour
le P4). Les exigences fonctionnelles sur les pompes ASG imposent un délai
maximum de 60 secondes pour l’obtention du plein débit après un dépassement
du point de consigne. Ce temps tient compte de la temporisation du diesel (perte
électrique) et la mise en route des pompes ;
• d’une bâche de stockage d’eau déminéralisée dégazée dans laquelle aspirent les
pompes ASG. Les tuyauteries non classées sont naturellement piquées sur la
bâche à un niveau supérieur à celui de la réserve d’eau nécessaire au passage en
arrêt à froid, car cette fonction de la bâche est vitale. La bâche est protégée tant
en surpression qu’en dépression (système de garde d’eau ou système mécanique,
voire mixte). La bâche est protégée contre le gel (locaux antigel à partir du
palier P4) ;
• d’un ensemble de dégazage permettant la réalimentation en eau déminéralisée
dégazée retraitant l’eau à ramener dans la bâche, en ramenant les caractéristiques
de l’eau 24 dans les limites définies par les STEs. La fonction de dégazage
n’est pas secourue, puisque ce n’est pas une fonction de sauvegarde ;
• de vannes réglantes sur les lignes d’eau secourue. Les vannes réglantes du palier
CPY sont des soupapes réglantes de type égal pourcentage. La fonction de limitation
du débit à la brèche est assurée par un diaphragme placé à l’aval de
chaque soupape. Les vannes réglantes des paliers ultérieurs sont à détentes multiétages
assurant, sur mise en butée au démarrage, la limitation du débit à la
brèche et du débit requis vers les GVs sains, en cas de rupture de tuyauterie
d’eau alimentaire ou de vapeur.
Nous reviendrons plus en détail par la suite sur les caractéristiques des composants de
l’ASG. Lorsque les GVs sont alimentés normalement par les turbopompes alimentaires
via le poste d’eau, le système ASG est donc en attente, prêt à démarrer. Dans cette
situation normale, le niveau d’eau dans la bâche ASG de stockage doit normalement
se situer pour assurer un volume utile de 625 m3 (CPY, 1 032 m3 pour le P4), requis
par le service attendu de l’ASG, à savoir permettre d’atteindre les conditions de connexion
du RRA. Les motopompes ASG et la turbopompe ASG qui puisent l’eau dans
la bâche sont à l’arrêt, en attente d’un ordre prescrit par le système de protection RPR
du réacteur. Les vannes d’isolement pneumatiques du circuit de vapeur principal VVP
24 Les caractéristiques de l’eau de l’ASG sont : pH compris entre 8,8 et 9,2, chlorure < 0,15 ppm,
oxygène dissous < 0,1 ppm, impuretés solides < 0,5 ppm, température comprise entre 7 ◦C et 40 ◦C.

<!-- page 924 (PDF 940) -->
sont normalement ouvertes et le circuit d’alimentation en vapeur de la turbopompe
ASG est conditionné en permanence jusqu’aux vannes fermées d’alimentation pneumatiques
de la turbopompe ASG. Le ballon séparateur ASG est en service et évacue
via son purgeur les condensats correspondants en amont des vannes ASG. La vanne
d’admission vapeur de la turbopompe ASG (qui, rappelons-le, est arrêtée), est sous la
dépendance de son régulateur Woodward avec une consigne de vitesse présélectionnée
à 3 560 tours/min. Enfin, les vannes réglantes d’alimentation des GVs sont ouvertes
sous dépendance de leur commande analogique, et les vannes d’isolement ASG des
débits nuls des motopompes sont fermées. Telle doit être la situation du circuit ASG
avant sa mise en fonctionnement.
Le rôle essentiel de l’ASG est d’évacuer la puissance résiduelle après un AAR.
Plusieurs situations normales ou incidentelles sont concernées :
• au démarrage et pendant la montée en température du primaire si le poste
d’eau est indisponible. Pendant cette phase de démarrage, les motopompes ASG
servent à maintenir le niveau d’eau dans les GVs au voisinage du niveau de
consigne à charge nulle, soit 33 % de la gamme étroite, et à compenser les
pertes d’eau secondaire dues aux opérations de démarrage (environ 250 tonnes
CPY). Lors de ces opérations, il faut faire attention à ne pas faire fonctionner les
pompes ASG en sur-débit avec risque de cavitation. Cette situation se produit
en cas d’incident (manque d’air comprimé, manque de tension) ou de fausse
manœuvre, ce qui amène les soupapes réglantes en grande ouverture alors que
la pression au secondaire des GVs est inférieure à la pression nominale, c’est le
cas des motopompes en situation de remplissage des GVs ;
• en arrêt à chaud lorsqu’on ne peut plus utiliser l’ARE ;
• pour passer en arrêt à froid en descendant en pression pour se connecter au
RRA (32 bars), après un AAR ;
• en situation accidentelle, comme la perte des alimentations électriques extérieures
, la rupture de tuyauterie vapeur, la rupture de tuyauterie d’eau alimentaire
, l’accident de perte de réfrigérant primaire. . .
• toute situation de perte des systèmes engagés dans l’ARE : perte du CEX, ABP,
APP, VHP. . .
• les motopompes ASG servent aussi au remplissage des GVs suite à un arrêt
à froid, ou un premier remplissage, voire à injecter des réactifs dans l’eau du
secondaire. L’eau nécessaire est prélevée dans la bâche ASG dont on ajuste le
niveau par la mise en service d’un dégazeur (décrit plus loin), voire même d’une
liaison avec les pompes d’extraction d’une tranche voisine si on ne veut pas
mettre en service le dégazeur. Comme les GVs dans cette situation offrent une
très faible contre-pression, il faut veiller à ne pas faire fonctionner les pompes
ASG en surdébit (en jouant sur l’ouverture des soupapes réglantes).
Le système ASG est un système à commande centralisée dans la salle de commande,
avec possibilité d’action sur le panneau de repli. La mise en route des motopompes
ou de la turbopompe est soit automatique sur des critères d’engagement que nous
verrons par la suite, soit manuelle sur ordre de la salle de commande. Au démarrage,

<!-- page 925 (PDF 941) -->
les vannes de réglage s’ouvrent en grand, puis l’opérateur peut adapter le débit en
fonction du besoin.
Dans la situation où l’alimentation normale (ARE) est indisponible, les GV ne sont
plus refroidis et le niveau d’eau côté secondaire va diminuer au risque d’assécher les
GVs. Dans le même temps, la production de vapeur s’intensifie au risque d’engorger
le condenseur (le niveau va monter dans un délai plus long du fait de la grande
capacité du condenseur). L’ASG est dimensionné pour évacuer alors la puissance
résiduelle, ce qui sous-entend la chute des barres par AAR. Le risque d’engorgement
du condenseur peut être géré en évacuant la vapeur à l’atmosphère (GCTa). Dans une
autre situation où c’est le condenseur qui est indisponible (CEX), c’est la pression dans
le GV qui augmente et le niveau du condenseur qui diminue (plus lentement). Une
augmentation rapide de la pression du GV est dangereuse (si on atteint la pression
maximale admissible ou timbre 25) et il faut évacuer la vapeur au GCTa. Encore
une fois, la mise en route de l’ASG permet d’évacuer la puissance résiduelle par
vaporisation dans les GVs, toute la vapeur étant évacuée à l’atmosphère du fait de
l’indisponibilité du CEX. On voit dans ces deux exemples que le circuit ASG peut
être ouvert si on décharge la vapeur à l’atmosphère, ou fermé si le condenseur est
disponible et qu’on envoie la vapeur produite dans le circuit CEX.
On notera bien que le circuit ASG n’est pas utilisé en fonctionnement normal.
C’est d’ailleurs cette particularité qui fait que la centrale de TMI-2 a pu fonctionner
avec un circuit ASG non disponible, initiant la séquence accidentelle lors du passage
sur ASG au déclenchement de la turbine, ce qui allait conduire à la destruction du
cœur du réacteur suite à des erreurs humaines et des erreurs de conception.

### 7.12.2 Constitution de l’ASG

Le système ASG (Figure 7.68, Figure 7.70) est constitué de deux ensembles de pompage
assurant chacun 100 % de la fonction, et alimentant chacun une paire de GVs
(situation 1 300 MWe 26). Chaque ensemble comprend une motopompe et une turbopompe
(P4), un injecteur d’additifs chimiques, un échangeur et quatre rampes
d’aspersion en forme de tore et portant des pulvérisateurs. Une ligne d’essai des pulvérisateurs
permet de tester ceux-ci simplement à l’air comprimé. Chaque ligne dispose
d’une ligne de contournement des rampes d’aspersion qui permet de continuer
à refroidir l’eau des puisards sans aspersion enceinte. Le circuit d’additif chimique
comprend un réservoir de stockage, une pompe de brassage et les tuyauteries de liaison
jusqu’aux injecteurs. Chaque turbine d’entraînement des pompes est alimentée en
vapeur par des tuyauteries piquées en amont des vannes d’isolement vapeur des GVs
correspondants. Dans le cas du CPY, on dispose de deux motopompes demi-débit et
d’une turbopompe alimentaire de secours TPAS plein débit. Les motopompes sont
de type centrifuge à axe horizontal entraînées par un moteur électrique asynchrone
(6,6 kV, 315 kW, 1 500 tours/min), et tournent du fait d’un multiplicateur à une
vitesse de 3 000 tours/min. Les moteurs d’entraînement des motopompes sont alimentés
par des jeux de barres secourus (diesel), la première pompe par le diesel A
25 Le terme timbre provient du fait que l’administration imposait l’apposition sur les appareils à
pression d’une plaque comportant la pression maximale admissible, en particulier dans le décret du
9 octobre 1907, de la même manière qu’un timbre administratif sur les documents officiels.
26 Lorsque le circuit primaire est refroidi en thermosiphon, il est nécessaire de refroidir au moins
deux GVs sur 4 (2 × 100 m3/h) ou 3 sur 4 (3 × 50 m3/h) pour extraire la puissance résiduelle.
L’ASG du P4 est dimensionné pour pouvoir extraite 4 117 MWth.

<!-- page 926 (PDF 942) -->
Fig. 7.68 – Circuit ASG d’un réacteur 900 MW e (CPY). Le schéma à 3 pompes
est reconduit de la conception Westinghouse. L’alimentation de l’ASG en eau brute non
dégazée est un cas particulier qui peut survenir en cas de perte prolongée des alimentations
électriques extérieures (plus de 2 heures). Dans une telle situation où les pompes primaires
ne sont plus alimentées, le refroidissement du primaire s’effectue en thermosiphon et on peut
craindre une insuffisance de la réserve d’eau de l’ASG. Si on ne dispose plus du dégazeur
ASG et des pompes d’extraction de la tranche et de sa tranche jumelle, on peut utiliser de
l’eau brute (douce ! cas des réacteurs sur rivière) en faisant un appoint d’hydrazine pour
consommer l’excès d’oxygène dissous.
(LHA) et l’autre par le diesel B (LHB). La turbopompe est entraînée par une turbine
à action à simple roue tournant au nominal à 3 560 tours/min, soit 585 kW de puissance
à l’accouplement, et supportant une pression absolue de vapeur à l’amont des
vannes d’arrêt comprise entre 7,6 bars et 83,3 bars (CPY) pour un débit nominal de
160 m3/heure. Chacune des pompes (moto ou turbo) est de conception identique, et
est équipée d’une ligne à débit minimal qui est isolable automatiquement sur critère de
débit dans le cas des motopompes, et manuellement dans le cas des turbopompes. Les
pompes aspirent de l’eau déminéralisée, dégazée et tamponnée à un pH de 9, dans la
bâche ASG dégazée maintenue sous atmosphère d’azote 27 (1,15 bar absolu max pour
éviter un ré-oxygénation de l’eau par des entrées d’air, l’azote est délivré par le système
RAZ). Sur le palier CPY, le schéma à 3 pompes ASG et barillet double, préconisé
par Westinghouse, a été reconduit (Figure 68). Sur les paliers ultérieurs, le schéma
des pompes a fait l’objet d’une étude probabiliste de sûreté conduisant à l’adoption
de deux trains entièrement séparés comportant chacun une motopompe et une turbopompe
débitant dans une paire de GVs (Figure 69). L’eau, aspirée dans la bâche,
est refoulée dans les tuyauteries principales d’alimentation ARE en aval du clapet de
27 La présence d’azote dans le ciel de bâche génère un risque particulier en cas d’intervention
humaine sur la bâche (l’azote pur étant mortel !).

<!-- page 927 (PDF 943) -->
Fig. 7.69 – ASG des paliers P4, P’4 et N4. Il diffère notablement du palier CPY
par le principe de deux files totalement séparées, chacune comportant une motopompe et
une turbopompe. Les deux files sont séparées géographiquement, de même que pompe et
motopompe d’une file sont aussi séparées l’une de l’autre. La séparation est complète jusqu
’aux traversées d’enceinte, hormis la bâche de stockage qui est commune aux deux files.
L’isolement des lignes de traversées d’enceinte est assuré sur chaque ligne de secours par un
clapet intérieur, redondé par un clapet extérieur, comme sur le palier CPY. Signalons que
le clapet extérieur a été supprimé sur le N4. Les soutirages de vapeur sur les lignes VVP
alimentant les turbopompes s’effectuent en amont des vannes d’isolement vapeur de façon à
pouvoir alimenter les turbopompes en cas d’accident avec isolement vapeur. Ces soutirages
sont donc entre l’enceinte et les vannes vapeur. L’alimentation de la turbopompe de chaque
voie s’effectue par de la vapeur prélevée sur 2 GVs en amont des vannes d’isolement à une
pression maximale de 90 bars. Pompes et moteurs sont refroidis par le fluide pompé et sont
donc autonomes en termes de ventilation.
non-retour de ces tuyauteries. Il n’y a donc qu’un piquage d’alimentation en eau côté
secondaire des GVs, et non un piquage spécifique ASG. Par contre, le piquage de l’ASG
sur l’ARE s’effectue au plus près des GVs, pour éviter un mode commun en cas de
rupture d’une tuyauterie ARE, sur les paliers CPY et 1 300 MWe. L’analyse du retour
d’expérience a montré que des phénomènes de stratification thermique apparaissent
dans le tronçon commun ARE/ASG, ce qui a conduit à séparer complètement pour
le palier N4 les deux systèmes jusqu’à l’intérieur du GV. Or, on a constaté, avec de
l’instrumentation spécifique, que ce phénomène de stratification était toujours observable
aux faibles débits, induisant un facteur d’usage thermique anormalement élevé.
On lénifie le problème par des régulations améliorées, une conduite dite « douce » et
des vannes réglantes les plus étanches possible. L’aspiration à la bâche des pompes

<!-- page 928 (PDF 944) -->
Fig. 7.70 – Schéma simplifié du lignage de l’ASG (CPY) (adapté de [Installations de
sauvegarde, 1977] p. 55). Sur le palier CPY, la turbopompe est alimentée par prélèvement
sur les 3 GVs à une pression maximale de 76 bars.
ASG d’un même ensemble de pompage (motopompe ou turbopompe) s’effectue par
une tuyauterie commune. Chaque pompe refoule l’eau vers chacun des 2 GVs qui lui
sont associés et chacune des deux lignes d’injection est équipée d’un organe de réglage
de débit assurant aussi le rôle d’orifice limiteur de débit, d’un clapet anti-retour et d’un
organe d’isolement manuel. En aval de ces organes d’isolement, les lignes d’injection
de la motopompe et de la turbopompe, associées à un GV donné, sont regroupées pour
constituer la ligne d’alimentation en eau de secours de ce GV. Sur certaines tranches
(Paluel, Flamanville), une liaison, normalement obturée, permet de relier l’aspiration
des pompes ASG aux réserves d’eau brute douce du site (système SEI) si nécessaire.
La bâche ASG est construite en béton comportant un revêtement métallique
interne. Elle est dimensionnée en volume (CPY : maximum 635 m3) pour assurer
l’extraction de la puissance résiduelle jusqu’à ce qu’on puisse connecter le RRA, ce
qui requiert une autonomie d’environ 6 heures, à savoir : le maintien en état d’arrêt à
chaud pendant 2 heures (consommant environ 250 tonnes d’eau), puis le passage en
état d’arrêt à froid en 4 heures jusqu’à une température de 177 ◦C et une pression inférieure
à 32 bars, conditions de connexion du RRA (consommant environ 375 tonnes
d’eau). Cette bâche est placée dans un local antisismique et antimissile, et elle est
maintenue hors gel par le rejet de calories du système DVG (ventilations des locaux

<!-- page 929 (PDF 945) -->
de commande de grappes et pompes ASG). La bâche est protégée de surpression par
une soupape de sûreté et des très basses pressions par un casse-vide. L’eau de la bâche
est maintenue sous matelas d’azote pour éviter son regazage. L’azote est fourni par
le système RAZ au travers d’un détendeur. La pression maximale est réglée par un
déverseur pour évacuer les surpressions d’azote. L’alimentation de la bâche ASG s’effectue
soit à partir du système de distribution d’eau déminéralisée SER à l’aide d’une
pompe, normalement après passage dans le poste de dégazage ou, si nécessaire (en cas
d’indisponibilité du poste de dégazage), par by-pass de celui-ci par une vanne. Cette
alimentation peut s’effectuer dans certains cas par gravité ; soit à partir du condenseur
de la tranche ou de la tranche jumelle par l’intermédiaire des circuits et des pompes
CEX. Les opérations d’appoint de la bâche peuvent être commandées à distance ou
manuellement, et arrêtées automatiquement sur une alarme de niveau trop haut dans
la bâche. La vidange de la bâche s’effectue manuellement vers le circuit SEK.
Les pompes ASG puisent dans la bâche ASG. L’eau de la bâche est utilisée
pour évacuer la puissance résiduelle par les GVs tout en évitant que les soupapes
de décharge du pressuriseur fonctionnent en eau (pressuriseur presque « solide ») et
que la plaque tubulaire d’un GV soit asséchée. Une seule motopompe de 80 m3/h
(CPY) suffit à remplir cette fonction. Deux motopompes de 80 m3/h et une turbopompe
de 160 m3/h permettent de respecter les besoins en respect du critère de
défaillance unique (CDU). La turbopompe est alimentée par une fraction du débit de
vapeur produite par les GVs, l’autre fraction est évacuée au GCTa à l’atmosphère. Le
fonctionnement nominal de la turbopompe correspond à la pression nominale de la
vapeur à charge nulle (70,3 bars, CPY) et la pompe entraînée fournit alors son débit
nominal de 160 m3. L’alimentation en vapeur de la turbine est assurée par 3 piquages
situés sur chacune des lignes de vapeur principale sortant des GVs et en amont des
vannes d’isolement principales (VVP). Un seul de ces piquages est suffisant pour alimenter
la turbine et ces lignes sont munies d’une vanne d’isolement pneumatique
permettant d’isoler une ligne vapeur contaminée par une fuite primaire/secondaire.
Si ce sont les motopompes qui assurent le gavage des GVs, toute la vapeur produite
est évacuée au GCTa. Les pompes doivent pouvoir fournir leur débit nominal à la
pression maximale à l’ouverture des soupapes de sécurité des GVs (74 bars).
Notons qu’une liaison peut être réalisée en ultime secours pour alimenter les
pompes à partir des réserves d’eau douce du site.
La Figure 7.70 montre le dédoublement des lignes d’alimentation de secours des
GVs. Chaque motopompe ou turbopompe dispose de ses propres lignes d’alimentation
en eau déminéralisée ou en eau brute, et ses propres lignes de distribution (soupapes
réglantes comprises) vers les 3 GVs (CPY). Comme ce circuit est un circuit de secours,
qui doit pouvoir fonctionner en situation accidentelle où l’accès au BR est impossible
du fait de la radioactivité, les vannes et l’instrumentation sont situées à l’extérieur du
BR. Les piquages des tuyauteries d’ASG sont raccordés sur les tuyauteries principales
de l’ARE, mais à l’intérieur du BR et au plus proche des GVs. La réserve d’eau
déminéralisée (600 m3, CPY), située dans une bâche antisismique (bâche ASG), assure
une autonomie d’environ 5 à 6 heures. Ce délai permet dans les scénarios simples
d’atteindre les conditions de connexion au RRA (32 bars) qui assurera la relève. En
cas de vidange complète de la bâche ASG, on passe sur de l’eau brute issue de la
source froide.

<!-- page 930 (PDF 946) -->
La quasi-totalité des matériels du système ASG est installée dans le bâtiment combustible
BK, au niveau +0,00, pour profiter des aspects antisismiques et antimissiles
du BK, à l’exception :
• des matériels situés au-delà des traversées d’enceinte (liaisons avec ARE) ;
• des robinets d’isolement et des clapets situés sur les lignes d’alimentation vapeur
des turbines ASG (liaisons avec VVP). Toutefois la partie située en aval des
séparateurs inclus est située dans le BK ;
• les silencieux des turbines, installés à l’extérieur du BK ;
• les tuyauteries de liaison de l’ASG avec les systèmes APG, CEX, REN, SEI,
SEO, SER, SIR, SIT et SVA.

### 7.12.3 Engagement de l’ASG

La Figure 7.71 précise les conditions d’engagement de l’ASG, en particulier que ce
soit via la turbopompe ou les motopompes. Les causes d’engagement de l’ASG sont
de deux natures : soit un incident sur le circuit ARE d’origine mécanique (problèmes
de tuyauterie ou de vannes) ou électrique (oblitérant le fonctionnement des pompes
d’extraction par exemple lors d’un îlotage raté), soit la perte de la réserve d’eau
au condenseur par circuit CEX indisponible (perte des pompes de circulation, perte
du vide au condenseur. . . ), ou bien le déclenchement de la turbine consécutif à une
perte du réseau et l’impossibilité du contournement turbine. L’engagement de l’ASG
doit obligatoirement mener à un AAR dans la mesure où l’ASG n’est pas du tout
dimensionné pour évacuer la puissance nominale, mais moins d’un dixième de celleci
, et l’absence de l’arrêt du réacteur conduirait à une vidange très rapide des GVs
uniquement alimentés par l’ASG.
Le débit d’ASG a été dimensionné pour pouvoir évacuer la puissance résiduelle
(débit d’eau vaporisée Qs), mais aussi pour maintenir le niveau d’eau dans les GVs audessus
de l’altitude de l’arrivée d’eau et au niveau du séparateur centrifuge. Ce niveau
d’eau permet un fonctionnement efficace du GV qui ne doit pas être asséché en partie
haute pour être efficient. D’autre part, un assèchement plus important risquerait de
détériorer la plaque tubulaire par choc thermique. Ce débit de sauvegarde du matériel
Qm doit être environ du double de Qs, soit un débit minimal d’environ 3 fois Qs. On
estime à environ 2 heures le temps d’arrêt à chaud (consommant environ 250 tonnes
d’eau), puis 4 heures pour atteindre les conditions de connexion du RRA (32 bars,
177 ◦C) à une vitesse maximale de 28 ◦C/heure pour éviter un choc thermique sur
la cuve, soit une consommation supplémentaire d’environ 375 tonnes d’eau. On peut
augmenter l’autonomie en mettant en service le dégazeur ou par une liaison avec le
condenseur de la tranche voisine. Le poste de dégazage est dimensionné pour pouvoir
réalimenter la bâche de stockage ASG et conserver la réserve de sécurité pour passer en
arrêt à froid. Mais en cas de perte des alimentations électriques externes, le dégazage,
commun à une paire de tranches jumelles, est indisponible et c’est le secours par
diesel des pompes du poste de dégazage qui permet de réalimenter la bâche ASG en
eau déminéralisée. Rappelons que l’intérêt du dégazage est de maintenir une teneur
en oxygène dissous dans l’eau du secondaire inférieure à 0,005 ppm, pour limiter
les phénomènes d’oxydation du côté secondaire. Le poste de dégazage peut produire

<!-- page 931 (PDF 947) -->
Fig. 7.71 – Condition d’engagement de l’ASG (sur CPY). On retrouve les incidents
résultant de la perte d’eau alimentaire à savoir un niveau très bas dans un ou deux des GVs,
détecté en logique 2/4 par les chaînes de niveau GV ; les incidents conduisant à la perte d’ARE
à savoir le déclenchement des turbopompes alimentaires principales (TPAs), auquel cas les
deux motopompes ASG reçoivent un signal d’enclenchement automatique, ou la perte des
alimentations électriques (baisse de tension 6,6 kV des pompes d’extraction ou des pompes
primaires), auquel cas turbopompe et motopompes sont engagées ; les incidents provoquant
l’isolement de l’ARE à savoir un niveau très haut dans au moins un des GVs, détecté en 2/4
par les chaînes, auquel cas l’automatisme de protection réacteur provoque la fermeture des
soupapes et vannes motorisées des lignes d’ARE, puis l’enclenchement des motopompes ASG,
ou l’injection de sécurité puisque le signal d’IS provoque l’enclenchement des turbopompes
alimentaires et la fermeture des soupapes et vannes d’isolement, puis l’enclenchement des
motopompes ASG. Notons que la réserve d’eau de la bâche ASG doit pouvoir assurer le
refroidissement du réacteur pendant environ 6 heures, utiles au passage en arrêt à froid.
Notons aussi que l’ASG peut être directement démarré par le contrôle-commande en manuel
(2 motopompes) ou le panneau de repli.
60 m3/heure à 40 ◦C en consommant environ 4 tonnes/heure de vapeur à 4 bars et
à 160 ◦C. L’eau déminéralisée à dégazer entre dans un échangeur à une température
entre 7 ◦C et 20 ◦C, et elle en sort à une température de l’ordre de 75 ◦C pour être
pulvérisée dans une colonne de dégazage. La pression dans le dégazeur est maintenue
constante à 1,2 bar par la régulation du débit de vapeur de réchauffage. Un débit
d’évacuation des incondensables est maintenu à 60 kg/h par un orifice diaphragme.
L’eau dégazée à 105 ◦C est reprise par une pompe et refoulée vers un échangeur qui
la refroidit à moins de 50 ◦C. Le débit d’eau dégazée est de 60 tonnes/h. Les calories
de réchauffage de l’eau à dégazer sont fournies par la vapeur auxiliaire SVA qui se
condense dans un faisceau de tubes noyés dans la partie inférieure de la colonne de
dégazage.

<!-- page 932 (PDF 948) -->
L’ASG est un système qui ne s’engage qu’en condition accidentelle, à savoir tous
les incidents conduisant à une perte de l’ARE. L’énergie évacuée des GVs sous forme
de vapeur est évacuée soit par contournement de la turbine au condenseur si celui-ci
est disponible, soit par décharge de vapeur à l’atmosphère. Le démarrage de l’ASG
est motivé par la détection d’un niveau très bas dans un des GVs, détecté en logique
2/4 par les chaînes de mesure de niveau : la protection du réacteur agit pour fermer
les soupapes et les vannes motorisées des lignes d’ARE. Dans cette situation, les deux
motopompes suffisent dès que le signal de fermeture de l’ARE est acquis. Si deux
GVs sont affectés, on doit aussi lancer la turbopompe. L’ASG s’engage aussi dans
le cas de la perte des turbopompes alimentaires principales de l’ARE, ou bien dans
le cas de la perte des alimentations électriques (baisse de tension sur les tableaux
6,6 kV des pompes d’extraction ou des pompes primaires). Le signal d’injection de
sécurité provoque aussi le déclenchement de l’ARE (fermeture des soupapes et vannes
d’isolement), et le démarrage des motopompes ASG. Celles-ci ne sont arrêtées que
sur commande manuelle depuis la salle de commande.

### 7.12.4 Fonction de sûreté de l’ASG

L’ASG, par sa fonction de circuit de sauvegarde, est classé important pour la sûreté,
ce qui se traduit par une sécurité de l’alimentation accrue et de son fonctionnement.
On a donc prévu un dédoublement complet (voie A et voie B) des organes moteurs,
de leur source d’alimentation en énergie et de leur contrôle-commande. Tant que de
la vapeur est fournie par les GVs, la turbopompe peut assurer à elle seule le service
de refroidissement des trois GVs (CPY), et deux motopompes 50 % sont redondantes.
Lorsqu’il n’y a plus de vapeur disponible, une seule motopompe peut assurer le service,
puisque la puissance résiduelle à évacuer a logiquement diminué. L’alimentation en
eau est assurée par un dédoublement des lignes sur la plus grande partie du parcours,
les lignes ASG étant raccordées aux lignes ARE très près des GVs. Pour pouvoir
fonctionner après un accident, les vannes et l’instrumentation sont situées en dehors du
BR en zone accessible. La source d’eau de l’ASG a aussi plusieurs origines possibles :
la bâche ASG d’eau déminéralisée désaérée, l’eau déminéralisée désaérée d’appoint du
poste de dégazage, l’eau déminéralisée issue des postes d’eau (CEX) de la tranche ou
de sa jumelle, et l’eau déminéralisée des réserves SER par les pompes du poste de
dégazage. Il y a même possibilité d’usage d’eau brute pour les sites en eau douce. Une
indisponibilité de l’ASG entraîne un repli sous 24 heures.
Les matériels ASG sont aptes à tenir aux séismes 28 et les composants du système
ASG sont tous situés au-dessus du niveau 0 vis-à-vis du risque d’inondation (protection
contre la crue millénaire). Le risque incendie présente une acuité plus forte
dans le cas des turbopompes que des motopompes, car elles contiennent plus d’huile
(environ 500 litres au lieu de 180 litres) et que la température de la vapeur dépasse
celle de l’inflammation de l’huile (environ 200 ◦C), d’où des mesures particulières
(porte coupe-feu, aspersion du groupe par vanne consignée fermée pour éviter les
intempestifs).
28 Conformément au Regulatory Guide 1.48 de l’AEC dans le cadre de la licence Westinghouse.

<!-- page 933 (PDF 949) -->
## 7.13 Le circuit d’aspersion de l’enceinte (EAS)

[Coppolani et al., 2004] p. 182, p. 274 ; [Installations de sauvegarde, 1977] p. 31

### 7.13.1 Principe

La fonction du circuit d’aspersion de l’enceinte (EAS) est relative au contrôle de la
pression à l’intérieur du bâtiment réacteur. En cas d’accident d’APRP interne au BR,
l’eau liquide à 155 bars est vaporisée instantanément à la brèche par le différentiel
de pression. On parle du phénomène de « flashing ». Cette vaporisation concourt à
l’augmentation rapide de pression, qui peut être limitée par l’aspersion d’eau froide
issue de la bâche PTR. L’eau borée est injectée par deux rampes d’aspersion circulaires
accrochées en partie haute du BR, via des buses d’aspersion. Ces buses permettent
de maximiser le volume d’enceinte aspergé en rendant maximale la hauteur de chute
et par l’orientation des jets. Ces buses assurent une pulvérisation aussi homogène que
possible. L’eau froide pulvérisée permet la condensation de la vapeur chaude grâce à
l’amélioration des échanges thermiques (la surface de contact entre l’eau liquide et la
vapeur dans l’enceinte est augmentée), et les condensats sont récoltés par les puisards
en partie basse puis réinjectés dans le système. En plus de l’action de condensation,
la pluie fine dans l’enceinte rabat les produits de fission vers les puisards, ce qui
est particulièrement efficace sur les aérosols. L’aspersion provoque un refroidissement
de l’air, donc une baisse de la pression totale approximativement selon la loi des
gaz parfaits et une condensation de la vapeur, donc une diminution de sa pression
partielle.
Le système EAS (Figure 7.72, Figure 7.73), système de sauvegarde classé sismique
à alimentation électrique secourue, est composé de deux files redondantes à
100 % 29, comportant chacune une pompe (et sa ligne de test, 450 kW par pompe,
1 500 tours/minute), un éjecteur (36 t/h à 29 bars max) et un échangeur refroidi par
le RRI. La pompe peut être alimentée soit par une ligne d’aspiration dans le réservoir
PTR 30 (850 m3/h par pompe CPY), soit par une ligne d’aspiration dans les puisards
de l’enceinte du BR (1 015 m3/h en recirculation). Il est mis en route automatiquement
sur signal haute pression dans l’enceinte (> 2,6 bars), ou alors sur commande
de l’opérateur. L’EAS est dimensionné pour que la pression dans l’enceinte n’atteigne
pas la pression de calcul relative à l’accident de référence (4,8 bar absolu pour le
CPY), avec, comme objectif complémentaire, de ramener la température dans le BR
à 60 ◦C après un délai d’une heure suite à l’ouverture de la brèche.
Dans une première phase, les pompes aspirent dans le même réservoir PTR que
les pompes d’injection de sécurité avec un débit minimum de 850 m3/h (par pompe,
CPY). Puis, dans un deuxième temps au bout d’environ 25 minutes, l’aspiration
passe sur les puisards de l’enceinte, sur signal bas niveau du réservoir PTR. Cette
opération est appelée « passage en recirculation ». L’échangeur avec le RRI est alors
mis en service. Le passage en recirculation est inévitable dès que la bâche PTR est
pratiquement vide. D’où l’importance du bon fonctionnement des pompes (il faut en
29 Certaines tranches dans le monde (mais pas en France) utilisent un système combiné aspersion
+ ventilation ou condenseur à glace. L’aspersion comporte en général deux files mais n’assurant
que 50 % de la fonction.
30 Rappelons que la bâche PTR d’un CPY a une contenance de 1 600 m3 à pression atmosphérique
et à température extérieure, concentration en bore de 2 500 ppm. Le bore cristallisant naturellement
à 7 ◦C, il faut aussi être en mesure de réchauffer l’eau du PTR en situation de grand froid.

<!-- page 934 (PDF 950) -->
Fig. 7.72 – Représentation fonctionnelle du circuit EAS (CP0). On prendra garde
au fait que les rampes d’aspersion sont circulaires et placées sur la face interne du dôme du
BR, et pas étagées en altimétrie telle que représenté sur la figure.
Fig. 7.73 – Circuit EAS du palier P4 (1 300 MW e) (adapté de [Centrales Nucléaires
EDF de 1 300 MW, 1991] p. 32).
particulier s’assurer du risque de défaut d’éventage des lignes de recirculation où une
poche d’air d’environ 50 litres suffirait à désamorcer les pompes), ou que les puisards
eux-mêmes ne soient pas bouchés par des débris (par du calorifuge des lignes par
exemple ou des boues de peinture), ce qui est assuré par des grilles anti-débris.

<!-- page 935 (PDF 951) -->
Étant donné que la mise en service de l’EAS va « polluer » l’ensemble de l’enceinte
en acide borique, nécessitant par la suite de longues et fastidieuses opérations
de nettoyage, on évite soigneusement les déclenchements intempestifs de ce système
de sauvegarde. Même au niveau de la gestion d’un accident d’APRP, on distingue les
petites brèches qui pourraient être traitées sans l’usage de l’EAS, des grosses brèches
où le système est indispensable. Si la pression primaire se stabilise à une valeur inférieure
à la pression du secondaire, c’est que la brèche est de taille importante et que
l’engagement de l’EAS ne pourra être évité. Dans cette situation, le refroidissement du
primaire par la décharge de vapeur par les GVs ne pourra être suffisamment efficace,
les épingles GV étant partiellement dénoyées.

### 7.13.2 Refroidissement et injection de soude

En phase de recirculation de l’aspersion, l’eau des puisards est refroidie par des échangeurs
d’aspersion (Photo 7.3) selon deux lignes séparées. Deux échangeurs refroidis
par de l’eau brute (SEB) assurent chacun 100 % du service. Chaque échangeur, situé
dans le BAN (CPY) ou le BAS (P4), peut assurer la fonction à 100 % et transférer
une puissance de 44 MW (côté EAS : 1 000 m3/h, entrée à 117 ◦C, sortie à 78 ◦C ;
côté RRI : 1 900 m3/h, entrée à 40 ◦C, sortie à 60 ◦C).
Photo 7.3 – Un échangeur EAS de Fessenheim (Photo EDF).
Un réservoir d’additifs chimiques de 11 m3 à pression atmosphérique (40 ◦C)
permet d’injecter de la soude à 30 % massique, dont l’objectif est d’augmenter le
pH et de favoriser les réactions chimiques permettant de capter certains produits
de fission comme l’iode en phase liquide, tout particulièrement dans les puisards.
Un pH élevé limite aussi la corrosion dans une atmosphère chaude et humide. Une
pompe de mélange (15 m3/heure, 50 ◦C) est activée toutes les 8 heures automatiquement
pendant 20 minutes, pour brasser le réservoir d’additif qui contient la soude, et

<!-- page 936 (PDF 952) -->
homogénéiser la solution de soude. Le dimensionnement du réservoir d’additifs permet
d’injecter via deux éjecteurs environ 6 000 ppm massique de soude par rapport à la
masse d’eau totale (Figure 7.74). Le réservoir de réactifs est dimensionné pour pouvoir
assurer une concentration de 0,6 % massique de soude dans l’eau, conduisant à un
pH compris entre 8,3 et 9,3 dans l’eau des puisards. Rappelons que le volume d’eau
à neutraliser par la soude est d’environ 2 000 m3 (PTR : 1 600 m3 + accumulateurs
120 m3 + primaire 250 m3 + réservoir de bore 6 m3) pour le CPY, et de 2 750 m3
pour le P’4 -PTR : 2 200 m3 + accumulateurs 124 m3 + primaire 430 m3). Le dimensionnement
est tel que l’injection de soude se termine après le début de la phase de
recirculation. L’injection de soude est faite automatiquement sur signal haute pression
enceinte (2,4 bars), après une temporisation de 5 minutes. La fermeture des vannes
de soude installées à l’aspiration du réservoir de soude s’effectue sur un niveau bas ou
sur demande de l’opérateur.
Fig. 7.74 – Injection de soude dans l’EAS.
Il existe plusieurs possibilités de lignage du refroidissement en phase de recirculation
. Soit on utilise des échangeurs EAS/SEB où le fluide froid est de l’eau brute, soit
on utilise les échangeurs RRA/RRI en mettant en série ou en parallèle les pompes
RRA et EAS (Figure 7.75, Figure 7.76).

### 7.13.3 Fonctionnement

En situation normale, le système EAS est hors service avec les vannes d’aspiration
dans la bâche PTR ouvertes et les lignes remplies d’eau, les pompes (motopompes et

<!-- page 937 (PDF 953) -->
Fig. 7.75 – Différents lignages du refroidissement de l’EAS (adapté d’après [Installations
de sauvegarde, janvier 1977] p. 38).
Fig. 7.76 – Lignage d’alimentation de l’EAS, soit par la bâche PTR, soit par les puisards
(adapté d’après [Installations de sauvegarde, janvier 1977]). Chaque échangeur SEB (pour
la phase de recirculation) peut assurer 100 % de la fonction.
turbopompe) sont à l’arrêt (prêtes à être démarrées soit en automatique (Figure 7.77)
par le système de protection du réacteur (RPR), soit en manuel (Figure 7.78) depuis
la salle de commande ou le panneau de repli), et la vanne d’isolement des réactifs

<!-- page 938 (PDF 954) -->
Fig. 7.77 – Critères d’engagement de l’EAS.
est fermée. La recirculation par les puisards est fermée, de même que l’alimentation
depuis le RRI des échangeurs de chaleur. Les échangeurs sont isolés côté eau brute
et conservés en état à sec. Les lignes de refoulement vers le BR sont aussi fermées.
En cas d’incident, le système EAS se met automatiquement en fonctionnement sur
signal haute pression dans l’enceinte à 2,6 bars absolus, soit environ 80 secondes après
le début de l’APRP grosse brèche. L’injection, de soude a lieu 5 minutes après le
démarrage de l’EAS. Pour éviter d’injecter de l’air depuis la bâche d’additifs, les
vannes de liaison entre ce réservoir et les pompes se ferment automatiquement sur
signal « bas niveau » du réservoir d’additifs. Lorsque le signal « bas niveau PTR »
indique que la bâche PTR est vide, on passe automatiquement en recirculation sur
les puisards. À ce moment, les lignes d’aspiration des pompes depuis la PTR sont
fermées, et les lignes d’aspersion depuis les puisards sont ouvertes. On estime que la
température maximale du circuit EAS est de 120 ◦C à cet instant. Rappelons que les
puisards gavant aussi le système RIS en recirculation, il faut impérativement que cette
eau soit fortement borée. L’EAS sera arrêté par l’opérateur quand les conditions de
température et de pression seront revenues à la normale (1 bar) après environ 24 heures
pour un scénario sans perte nouvelle de système de sûreté.
Les motopompes EAS se doivent d’être refroidies. Sur le CP1, les garnitures de
pompes sont refroidies par un petit aéroréfrigérant situé dans le local des échangeurs
EAS, car la température près de la pompe est trop élevée. Les moteurs sont refroidis
par le système de ventilation DVS. Le débit nul (minimum) de recirculation a été
supprimé et la pompe démarre en même temps que les vannes d’isolement enceinte
commencent à s’ouvrir. Sur le palier 1 300 MWe, les moteurs 6,6 kV sont refroidis
directement par de l’eau du RRI. La ligne de débit nul a aussi été supprimée par
remplacement par la ligne d’essai en motorisant les vannes de la ligne d’essai.

<!-- page 939 (PDF 955) -->
Fig. 7.78 – Critères de mise en service manuelle de l’EAS en fonction de la température
dans l’enceinte et du temps après mise en service de l’injection de sûreté.

### 7.13.4 Essais périodiques des lignes EAS

L’EAS injectant dans l’enceinte de l’eau borée, il n’est pas question de réaliser des
essais injectant de l’eau du PTR, au risque de devoir nettoyer entièrement le BR
pour éliminer l’acide borique qui se dépose sur les surfaces au contact, et qui est
corrosif. Néanmoins, on teste mensuellement les pompes séparément, train par train
pour toujours laisser l’autre disponible en cas de signal d’engagement de l’EAS. Les
rampes d’aspersion sont testées avec de l’air comprimé à chaque rechargement du
cœur. Des contrôles périodiques sont effectués sur la qualité de la solution de réactifs
(homogénéisation de la soude).

### 7.13.5 Efficacité de l’aspersion

L’efficacité de l’EAS est due à l’absorption de la chaleur par pulvérisation de
gouttelettes d’eau froide, ce qui fait baisser la température du BR et permet la

<!-- page 940 (PDF 956) -->
condensation de la vapeur. Huang et Ayyaswamy ont modélisé le comportement
thermique d’une goutte d’eau chutant depuis la rampe d’aspersion d’un BR. En
introduisant l’écart de température normalisé :
θb ≡
Tb−T0
T∞−T0 où Tb est la température moyenne et T0 la température initiale de la
goutte.
Ils ont montré par le calcul et confirmé par comparaison à l’expérience, que la
goutte atteint un régime asymptotique au bout d’environ de 5 secondes (Figure 7.79),
Fig. 7.79 – Variation de la température moyenne de la goutte en fonction du
temps. Comparaisons expériences/calcul. (D’après les travaux 31 de L.J. Huang et P.S.
Ayyaswamy).
au-delà desquelles elle ne s’échauffe plus. Sa vitesse asymptotique est de l’ordre de
2 m/s, soit 10 m parcourus en 5 secondes. Sur cette distance, atteignable dans
un BR de REP de puissance, sa température augmente d’environ 50
◦C, soit,
pour une goutte de taille constante de 1,4 mm de rayon, une absorption d’énergie
correspondant à :
3πR3 × ρH2O × Cp,H2O × (T∞−T0) ≈1000 kg
m3 × 4180
J
kg.K × 50K = 2, 4J
Cette goutte va aussi condenser à sa surface la vapeur d’eau présente dans le BR et
grossir en taille. Cette condensation est très efficace vis-à-vis de la baisse de pression
puisque chaque mole de vapeur (22 400 cm3) ne tiendra plus qu’un volume d’eau
liquide après condensation d’environ 18 cm3. Connaissant le débit de l’EAS (environ
400 kg/s pour une pompe EAS de CPY) et en supposant que les gouttes formées sont
toutes de 1,4 mm, on obtient un ordre de grandeur de la puissance évacuable par le
système.
31 Lin Jie Huang, P. S. Ayyaswamy : Heat transfer of a nuclear reactor containment spray drop,
Nuclear Engineering and Design, n ◦101, pp. 137-148, 1987.
