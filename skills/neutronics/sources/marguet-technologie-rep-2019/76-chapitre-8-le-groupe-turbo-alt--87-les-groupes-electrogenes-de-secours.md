# Chapitre 8 Le groupe turbo-alternateur et la production d’électricité — 8.7 Les groupes électrogènes de secours … 8.8 Un exemple de perte d’alimentation électrique : Dampierre (2007)
<!-- source PDF pages 1059-1066 -->

<!-- page 1043 (PDF 1059) -->
## 8.7 Les groupes électrogènes de secours

### 8.7.1 La conception de base

En cas de perte de la ligne principale, on tente un îlotage. Mais ce transitoire sensible
nécessite un réglage très fin des régulations par les automaticiens pour empêcher
un AAR. Si l’îlotage échoue, la défense en profondeur veut qu’on dispose d’un autre
moyen d’approvisionnement électrique, c’est le rôle de la ligne auxiliaire qui provient
d’un autre site de production par des lignes séparées de la ligne principale. Mais en dernier
ressort, si même la ligne auxiliaire est défectueuse (situation dite MDTE, Manque
de tension externe), on s’en remet à deux groupes électrogènes de secours à moteurs
diesels 29 (LHP et LHQ) qui font tourner des générateurs de courant alternatifs 30,
et qui vont fournir le courant 6,6 kV qui fait défaut pour les auxiliaires nucléaires
(Figure 8.64, Figure 8.65). Ces diesels (caractéristiques Tableau 3), dont l’usage réel
est en fait très rare en situation réelle, sont bien entendu testés et vérifiés périodiquement
(tous les deux mois). Leurs conditions d’utilisation sont très particulières, dans
la mesure où ils doivent subir des démarrages rapides (de l’ordre de 10 secondes), et
que la prise de charge est aussi très rapide (crans de 5 secondes entre les paliers de
charge). Ces situations particulières sont rarement rencontrées pour les diesels dans
Fig. 8.64 – Alimentation des auxiliaires nucléaires par les diesels : cas du CPY.
29 Conçus et fabriqués par la société Wärtsilä France (ex-SACM avant 1989). Historiquement,
Wärtsilä est un important constructeur naval finlandais depuis 1935.
30 Sur les générateurs de courant alternatif, on consultera avec intérêt [Ames, 1990].

<!-- page 1044 (PDF 1060) -->
Fig. 8.65 – Alimentation des auxiliaires nucléaires par les diesels : cas du 1 300
MWe.
d’autres industries. La chronologie normale (cas du CP1) de l’engagement des diesels
en cas d’îlotage réussi commence à la détection de la baisse de tension (t0 −ε) pour
U < 0,8 Unom, le top zéro t0 de référence est celui correspondant à U < 0,7 Unom, le
démarrage effectif des diesels correspond à t0 −ε + 0,9 s (attention ! Le démarrage
ne correspond pas au couplage, il faut attendre la montée en puissance du diesel et
son synchronisme pour pouvoir basculer sur le diesel), la prise en compte du manque
de tension par basculement sur le transformateur auxiliaire s’effectue à t0 + 0,9 s,
l’îlotage par basse vitesse des pompes primaires (ouverture du disjoncteur de ligne)
intervient à t0 + 1,2 s, et le rétablissement de la tension est effectif à t0 + 1,2 s
+ 0,7 s. Comme la tension est rétablie avant 5 s, il n’y a pas de déclenchement de la
turbine, ni de tentative de basculement sur le transformateur auxiliaire. Si la basse
vitesse des pompes primaires n’était pas atteinte, l’îlotage serait tenté à 2,5 s sur un
critère de basse tension et la tension serait rétablie en 3,2 s. Une deuxième possibilité
est l’îlotage manqué mais avec basculement sur source auxiliaire réussie. Dans
ce cas, si après l’ouverture du disjoncteur de ligne la tension n’était pas rétablie, la
chronologie s’établit comme suit : à t0 + 1,2 s + 1,5 s, il y a déclenchement turbine
et ouverture des disjoncteurs d’alimentation par le transformateur de soutirage,
à t0 + 1,2 s + 1,5 s+ 1,5 s, il y a fermeture des disjoncteurs d’alimentation par
transformateur auxiliaire. Si la tension revient au bout de 7 s, le basculement sur TA
est alors réussi. En troisième possibilité, si le basculement sur TA est impossible, le
basculement définitif sur diesel est tenté au plus tôt à 7 s après son démarrage si le
synchronisme le permet. Auquel cas la chronologie est la suivante : t0 −ε + 0,9 s
pour le démarrage des diesels, t0 −ε + 0,9 s+ 7 s pour l’ouverture du disjoncteur
d’alimentation de LHA/LHB par le TS ou le TA, et t0 −ε + 0,9s+ 7s+ 1,5 s pour

<!-- page 1045 (PDF 1061) -->
la fermeture du disjoncteur d’alimentation de LHA/LHB par diesel. La tension sur
LHA/LHB est alors retrouvée au plus tôt 9,4 s après la détection de basse tension au
plus tard 12,4 s après cette détection.
En cas d’îlotage rapide, le passage effectif sur diesels n’intervient qu’après avoir
épuisé les possibilités de secours de réalimentation par TS ou TA. Si la dégradation
de tension est lente, on peut se retrouver dans une situation où l’un des tableaux
LHA/LHB est alimenté par diesel alors que l’autre est alimenté par basculement sur
le TA, voire même tranche en puissance.
Le démarrage des diesels est assuré par de l’air comprimé. Deux systèmes indépendants
, qui interviennent à chaque démarrage, insufflent de l’air dans la moitié des
cylindres. Cependant, chacun des systèmes agissant seul est capable d’assurer 5 démarrages
réussis en 10 secondes maximum. Sur le palier N4, le réservoir d’air comprimé est
important (6 m3 par ligne à 30 bars). Des régulateurs de vitesse permettent d’assurer
différents régimes de fonctionnement des diesels (Photo 8.17). En cas de basculement de
source, les groupes doivent démarrer en moins de 10 secondes, se coupler puis prendre
la charge par crans successifs. Ce type de démarrage est très rude pour le matériel, dans
la mesure où la vitesse maximale est atteinte avant que la lubrification soit totalement
efficace. Pour les essais périodiques des diesels, on choisit un démarrage adouci où la
vitesse est montée progressivement, pour ne pas dégrader les diesels. Les groupes diesels
du CPY ont un seul circuit de graissage. Ceux des paliers ultérieurs ont deux circuits
de graissage car il existe un circuit spécifique à la culbuterie. Les diesels sont équipés de
deux circuits de refroidissement : un circuit d’eau dit « haute température » qui refroidit
les chemises du moteur et les enveloppes des turbosoufflantes de suralimentation, et
un circuit d’eau « basse température » qui refroidit le circuit d’huile de lubrification et
qui fournit de l’eau aux échangeurs air/eau qui refroidissent l’air après son passage dans
les turbosoufflantes de suralimentation. L’eau est mise en mouvement par une pompe
attelée. Pour les paliers ultérieurs au CPY, un circuit supplémentaire d’eau refroidit les
injecteurs. L’eau se refroidit dans des aéroréfrigérants munis de ventilateurs installés
sur le toit du bâtiment des diesels. Le diesel est alimenté (Figure 8.66) en combustible
liquide 31 (du gazole de haute qualité stocké en souterrain, sans additif dont le point de
filtrabilité est de –13 ◦C) selon deux circuits indépendants : le premier comprend une
pompe attelée au moteur, le second une motopompe qui commence à débiter 15 secondes
après le démarrage du groupe. En fonctionnement normal, la pompe attelée alimente le
moteur, tandis que la motopompe évacue son débit vers le réservoir relais. Si la pompe
attelée défaille, c’est la motopompe qui assure alors le service, ce qui signifie que les deux
pompes fonctionnent ensemble.
La disponibilité des diesels est donc de première importance sur le niveau de sûreté
d’une tranche. Fin 2010, des avaries de diesel ont été constatées sur plusieurs tranches,
causées par des grippages de vilebrequin lorsque le coussinet lubrifié (une bague d’acier
d’environ 10 cm de diamètre) dans lequel l’arbre tourne se dégradait. L’analyse de ces
situations a montré que ces défaillances pouvaient être anticipées en suivant la teneur
en plomb de l’huile. En effet, du plomb recouvre la face interne en régule du coussinet
au contact avec l’arbre, et des particules de plomb polluent l’huile lorsque le coussinet se
dégrade. Defait,ilsuffitdesuivrelateneurenplombpoursavoirs’ilfautchangeruncoussinet
bien avant grippage. La technologie des coussinets est en train d’évoluer (contrôle
très strict de l’ovalisation des bagues) pour une tenue opérationnelle plus longue.
31 Sur les combustibles liquides et le diésel en particulier lire [Belakhowsky, 1966].

<!-- page 1046 (PDF 1062) -->
Photo 8.17 – Un diesel de marque SACM à régulateur de vitesse.
Fig. 8.66 – Alimentation en combustible liquide des groupes électrogènes de
secours.
Il est aussi apparu au cours du temps, du fait des cyclages thermiques de démarrage
/arrêt, des petites fissures au niveau des pontets séparant les soupapes de la
culasse (en fonte à graphite lamellaire dite « GIL300 »). Ce problème a inquiété

<!-- page 1047 (PDF 1063) -->
Tab. 8.3 – Caractéristiques des diesels des paliers jusqu’au P’4.
Fessenheim (CP0)
Bugey (CP0)
CPY
1 300 MWe
Type de moteur
SACM AGOV
SACM AGOV SACM AGOV
ALSTHOM
16 E SHR
16 E SHR
16 E SHR
ATLANTIQUE
PC 2 5 SE
Puissance nominale (Chevaux)
4 000
4 000
5 700
10 400
Puissance fournie par l’alternateur
(kW) cosφ = 0, 8
2 816
3 090
4 000
7 200
Vitesse nominale (tours/min)
1 500
1 500
1 500
les Autorités de sûreté, car une fissure traversante pourrait mettre en connexion
la chambre d’eau de refroidissement et les soupapes, noyant le moteur diesel, alors
incapable d’assurer sa fonction. Pour autant, les 40 années de retour d’expérience
du fabricant de diesel ont montré que ces fissures ne se développaient pas après
amorçage, et des calculs fins de contraintes ont prouvé que, même dans des conditions
très défavorables, les fissures atteignaient à peine 1 mm de profondeur, bien
loin des 8 mm d’épaisseur à traverser. Ce genre de problème montre que même les
essais/inspections 32 peuvent dégrader les matériels, d’où une réflexion à mener sur la
périodicité des tests.
En plus des diesels de secours, les tranches disposent :
• d’une turbine à combustion TAC (gaz combustible) dite aussi TAG, constituant
le système LHT à 6,6 kV (CP0, P4, P’4, N4). Pour le CPY, le LHT est constitué
d’un autre groupe électrogène d’ultime secours (GUS, 4 MWe) ;
• d’un groupe turbo-alternateur d’ultime secours 380 V utilisant de la vapeur
d’eau produite par les GVs (si elle est encore disponible et si la pression de
vapeur n’est pas trop basse) : le TAS-LLS.
Chacun des moyens de production d’électricité suffit à lui-seul à produire le courant
nécessaire aux systèmes de sauvegarde.

### 8.7.2 Le diesel d’ultime secours (DUS)

Suite aux mesures Post-Fukushima où l’ensemble des 13 diesels de secours avaient
été noyés par le tsunami, on a décidé d’installer à partir de 2017, sur demande de
l’Autorité de sûreté, un diesel d’ultime secours (DUS, Figure 8.67) par tranche, placé
sur des plateformes en béton de 5 mètres de haut, dont le radier ferraillé fait 1,40 m
d’épaisseur, disposant d’une autonomie de 72 heures, et robustes à des agressions
de niveaux bien supérieurs à ceux des référentiels de conception. Cette obligation
conduit à concevoir un bâtiment « bunkerisé » (L : 24 m, l : 12 m, H : 25 m) avec
des dispositions particulières comme des plots parasismiques, un plancher bas audessus
du niveau d’inondation de référence ou encore une structure et des équipements
extérieurs résistant à la tornade de référence. Chaque diesel comporte deux cuves à
fioul de 12 tonnes de 63 m3 de fioul chacune. Chaque DUS produit une puissance de
3,5 MW, suffisante pour les systèmes de sauvegarde.
32 Il est par exemple classique d’abîmer un joint de pompe au remontage après démontage d’inspection
, du fait d’un trop fort couple de serrage.

<!-- page 1048 (PDF 1064) -->
Fig. 8.67 – Structure du diesel d’ultime secours (DUS).

## 8.8 Un exemple de perte d’alimentation électrique : Dampierre (2007)

À titre d’illustration, la centrale de Dampierre a été le théâtre d’un incident électrique
notable le 9 avril 2007. À 20 h 37, le réacteur 3 est à 65 % de puissance nominale quand
une surintensité sur un relais de protection conduit à la perte totale du tableau de
distribution électrique LHA, ce qui inhibe la possibilité d’un recours au groupe électrogène
diesel de secours de la voie A. Les auxiliaires de protection et de sauvegarde ne
sont plus disponibles que sur la voie B. La procédure de repli consiste à baisser la puissance
, découpler l’alternateur, puis arrêter le réacteur. La procédure de l’Approche
par état (APE) à appliquer est la conduite primaire de l’état physique non dégradé
ECP1, à savoir basculer sur la voie B (LHB) et un repli aux conditions de connexion
du RRA (pression inférieure à 32 bars), arrêt de la turbine quand la puissance est
descendue en dessous de 10 % (à 21 h 25). Toutefois, la situation se dégrade quand
un dysfonctionnement de l’interrupteur-enclencheur en sortie d’alternateur (système
GSY) fait que le couplage ne s’est pas ouvert assez vite, d’où une ouverture automatique
du disjoncteur de la ligne principale, privant le réacteur n◦3 de son alimentation
électrique par le réseau externe haute tension (400 kV). La ligne 225 kV est censée

<!-- page 1049 (PDF 1065) -->
prendre le relais, mais la procédure ECP1 stipule que, pour économiser l’alimentation
électrique, on coupe les batteries du tableau LBJ alimentées par LHA, or ce tableau
LBJ a comme rôle d’alimenter les actionneurs de bascule du transformateur de soutirage
(TS) de l’alimentation principale au transformateur de l’alimentation auxiliaire
(TA). En clair, en cas de perte de la ligne 400 kV, on ne peut plus basculer sur la ligne
225 kV. Comme il n’y a plus de courant externe (plus de ligne 400 kV, ni 225 kV), on
perd l’alimentation externe du tableau LHB, seul disponible depuis la perte du LHA,
ce qui entraîne un AAR sans possibilité d’îlotage, et un arrêt des GMPPs conduisant
à une situation de thermosiphon dans le réacteur. Le manque de tension du tableau
électrique secouru de la voie B encore disponible déclenche le démarrage du groupe
électrogène diesel LHQ qui va alimenter les auxiliaires nucléaires.
À 22 h 10, le plan d’urgence interne (PUI) est déclenché. Le primaire est en
thermosiphon et refroidi par le circuit secondaire alimenté par l’ASG. Notons que le
groupe électrogène d’ultime secours (GUS) du site sera connecté de manière préventive
à 1 h 30. La récupération de l’alimentation auxiliaire 225 kV permet de remettre en
marche une pompe primaire pour forcer le refroidissement du cœur. Le remplacement
du matériel défectueux est réalisé dans la nuit du 9 au 10 avril, et le tableau LHA est
remis en service le 10 au matin. L’incident a été parfaitement maîtrisé par EDF en
respect des procédures, comme le confirme l’ASN. L’incident est classé 1 sur l’échelle
INES, aucun rejet radioactif n’ayant dû être effectué.
Cet incident, heureusement sans conséquence, montre l’importance de la redondance
des moyens de secours dans la défense en profondeur. Dans une situation encore
plus dégradée (perte du LHB), on atteint un état de perte totale des sources électriques
(situation H3), seuls restent opérationnels l’injection de sécurité passive des
accumulateurs RIS, et les systèmes fonctionnant avec la vapeur produite par les GVs
(turbopompe ASG, turbo-alternateur LLS de secours). Notons que le GCT peut facilement
évacuer la vapeur correspondant à 10 % de Pnom (puissance résiduelle). En
cas de perte totale des alimentations électriques, le contournement vers le condenseur
n’est plus disponible, mais le contournement vers l’atmosphère continue à être opérationnel
grâce à des ballons d’air comprimé qui permettent de conserver la commande
des vannes du GCTa. Ces ballons permettent un fonctionnement pendant environ
une heure, après quoi seul l’ASG permet de refroidir les GVs. En ce qui concerne le
contrôle des fuites aux joints des GMPPs, c’est le turbo-alternateur LLS qui produit
le courant nécessaire à créer la contre-pression aux joints. Une éventuelle perte du
LLS conduit donc à une fuite aux joints de pompe dont le débit maximal estimé est
de l’ordre de 60 tonnes/heure par pompe. Le dénoyage du cœur ne peut alors être
retardé que par l’injection des accumulateurs (vers 42 bars), et on va à la fusion du
cœur en cas de perte de l’ASG, dans la situation la pire une heure après l’incident.
Ce scénario catastrophe prend en compte l’impossibilité pour les opérateurs de rétablir
une quelconque source externe d’alimentation électrique. La création de la Force
d’action rapide (FAR), dans le cadre des dispositions post-Fukushima de l’EDF, vise
à pouvoir acheminer, par voie des airs (hélicoptère) s’il le faut, des groupes diesels de
secours en provenance de bases logistiques régionales pour remédier à ce problème.

<!-- page 1050 (PDF 1066) -->

