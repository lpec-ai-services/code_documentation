# Chapitre 7 Les principaux circuits — 7.5 L’injection de sécurité (RIS) … 7.7 Le circuit d’échantillonnage nucléaire (REN)
<!-- source PDF pages 903-919 -->

<!-- page 887 (PDF 903) -->
Photo 7.2 – Étrier de maintien d’un piquage de RRA fuitard pour éviter tout
déboîtement amplifiant la fuite (Dampierre, Photo issue de [Faburel, 2004] p. 247).

## 7.5 L’injection de sécurité (RIS)

[Coppolani et al., 2004] p. 167

### 7.5.1 Principe et généralités

Le circuit d’injection de sécurité (RIS) (Figure 7.39) est le circuit principal de sauvegarde
du réacteur, d’où un soin tout particulier à sa conception. Le rôle du RIS est
de fournir l’eau de refroidissement borée au cœur en situation incidentelle ou accidentelle
. Il doit pouvoir renoyer le cœur en situation d’APRP, injecter rapidement
du bore en situation de RTV et compenser des petites fuites primaires si le RCV est
inopérant. Il s’agit d’injecter le plus rapidement possible de l’eau fortement borée.
Accessoirement, le RIS permet de remplir la piscine réacteur lors des arrêts pour
rechargement via les pompes basse pression ISBP faisant transiter l’eau de la bâche
PTR vers la piscine réacteur. Le RIS sert aussi à l’épreuve hydrostatique du RCP en
faisant monter en pression le RCP grâce à la pompe de remplissage des accumulateurs
(pompe volumétrique, 6 m3/heure, 215 bars).

### 7.5.2 Constitution du RIS

Le RIS (Figure 7.40) comporte plusieurs systèmes d’injection qui interviennent selon la
pression du circuit primaire. Dans une situation à forte pression, l’injection de sécurité
haute pression (ISHP du palier CPY) a comme rôle de compenser les fuites accidentelles
et d’introduire de l’acide borique dans le circuit primaire au-dessus de 120 bars jusqu’à
155 bars, en pompant l’eau fortement borée (environ 2 500 ppm) depuis la bâche PTR.
Le RIS comporte aussi un accumulateur par branche, système passif dont la fonction est

<!-- page 888 (PDF 904) -->
Fig. 7.39 – Localisation des composants du RIS.
Fig. 7.40 – Fonction principale du RIS (CPY).

<!-- page 889 (PDF 905) -->
d’injecter de l’eau borée en dessous de 42 bars. Enfin, un système injection de sécurité
basse pression (ISBP à environ 8 bars) permet d’injecter un fort débit d’eau borée quand
le circuit primaire a atteint une pression basse (en dessous de 20 bars). Notons qu’à partir
du palier 1 300 MWe, une injection moyenne pression (ISMP) remplace l’ISHP. L’ensemble
des pompes RIS et des organes nécessitant maintenance est situé dans le BAN,
donc à l’extérieur de l’enceinte BR. Le RIS est connecté à chaque boucle primaire par une
ligne d’injection HP/BP en branche froide ainsi qu’une ligne de décharge des accumulateurs
, et une autre ligne d’injection HP/BP aboutissant à une branche chaude. Notons
qu’on peut ainsi alterner l’injection de bore en branche froide, puis en branche chaude
alternativement en phase moyen et long terme d’un APRP pour éviter la cristallisation
du bore lors de l’évaporation dans le cœur.
À partir du P4, on a complètement séparé les fonctions RIS et RCV, puisque c’était
initialement les pompes de charge RCV qui officiaient dans l’ISHP du palier CPY. La
fonction ISMP est assurée par deux files avec adjonction d’un contournement petit
débit sur les collecteurs ISBP et ISMP permettant une injection simultanée, d’un
contournement équipé d’une vanne réglante sur les collecteurs ISBP pour permettre
le réglage de la pression primaire en cas de petit brèche, d’une ligne de débit nul
(ISMP et ISBP) vers les puisards pour éviter le recours à la décharge du RCP en cas
de petite brèche, et d’une pompe de gavage sur chaque train d’ISMP (suppression du
gavage par l’ISBP).

### 7.5.3 L’injection de sécurité haute pression (paliers CP0 et CPY)

L’ISHP est une spécificité des paliers CP0 et CPY (Figure 7.41). L’ISHP est efficiente
dans les cas de dépressurisation faible, pour compenser les fuites et introduire de
l’acide borique. Le RIS-ISHP comporte trois pompes d’injection de sécurité haute
pression, qui sont en fait les pompes de charge du circuit RCV, et qui assurent cette
fonction. Au minimum, deux pompes doivent être en service et une seule pompe en
entretien. Ces pompes aspirent dans la bâche PTR. Les pompes centrifuges RCV ont
une pression de refoulement de 170 bars (supérieure à la pression d’ouverture des
soupapes du pressuriseur, ce qui n’est pas le cas avec l’ISMP des paliers ultérieurs
pour éviter toute perte d’eau utile au cœur), et présentent ainsi l’avantage de pouvoir
introduire de l’eau borée même à 155 bars de pression nominale (35 m3/h à 170 bars
et 150 m3/h à 45 bars). Notons que, dans le cas de la centrale des Ardennes Chooz A,
c’est une pompe spéciale dédiée haute pression qui assure l’injection RIS, et non les
pompes RCV, d’où une séparation (coûteuse) des fonctions charge et sûreté.
Ensuite, deux pompes d’injection basse pression prennent le relais. Tant que la bâche
PTR contient de l’eau, toutes ces pompes aspirent dans la bâche PTR. Lorsqu’elle est
vide, les pompes basse pression aspirent depuis les puisards du BR où l’eau s’est retrouvée
par gravité (en fuyant par la brèche du primaire), les pompes HP aspirent soit depuis
la PTR, soit au refoulement des pompes BP, si la PTR est vide. Le réservoir d’injection
RIS contient une solution de 3,4 m3 d’acide borique à 21 000 ppm de bore (sous 4 bars à
70 ◦C), qui est injectée par des pompes centrifuges d’acide borique concentré à 4,5 m3/h
sous 4 bars. Lors d’un APRP de forte section de brèche, la dépressurisation est tellement
violentequelespompesRIS-HPsonttotalementinefficaces.Ellespeuventdoncêtrearrêtées
rapidement. C’est cette constatation qui a vu la disparition de l’ISHP à faible débit
sur les paliers ultérieurs. C’est le cas inverse pour un APRP de faible section ou une RTV

<!-- page 890 (PDF 906) -->
Fig. 7.41 – Injection de sécurité haute pression (CPY). Le circuit ISHP dispose
de deux alimentations possibles : d’une part la bâche PTR, d’autre part le refoulement
des pompes basse pression. Deux collecteurs d’injection permettent de gaver les 3 branches
froides pour l’une, ou les 3 branches chaudes pour l’autre. La possibilité d’alterner l’injection
en branches froides ou en branches chaudes est intéressante pour éviter des problèmes
de cristallisation du bore. L’isolement est assuré sur chaque ligne par un clapet situé dans
l’enceinte BR, et sur chaque collecteur par deux vannes motorisées en parallèle situées à
l’extérieur de l’enceinte. Le collecteur d’injection en branches froides dispose d’un réservoir
contenant une solution d’acide borique très concentrée à 21 000 ppm de bore, appelé familièrement
« cartouche de bore » RIB. Ce réservoir est lui-même réchauffé à 70 ◦C pour éviter la
cristallisation du bore, et il comporte un système de brassage par recirculation (par pompe
centrifuge de débit nominal 4,5 m3/h sous 4 bars) pour garantir l’homogénéité de la solution
(voir plus loin). Le système RIB est complexe mais peut être valorisé au niveau des études
de sûreté, d’où son intérêt. Le choix d’injecter en branche froide s’explique par le fait d’être
en amont du cœur par rapport au sens de l’écoulement normal de l’eau du primaire (adapté
de [Installations de sauvegarde, 1977] p. 16).

<!-- page 891 (PDF 907) -->
puisque dans ces situations, ce sont les pompes RIS-BP qui n’ont pas assez de pression
de refoulement et qui peuvent être arrêtées. Notons qu’une pompe RIS-HP est toujours
en service pour assurer la fonction de charge du RCV.
Les pompes RIS-HP (ou RCV) sont des pompes centrifuges en acier inoxydable
d’un débit nominal de 35 m3/heure à 170 bars, avec un débit maximal de 150 m3/heure
à 45 bars.

### 7.5.4 Les accumulateurs (tous paliers)

Trois (quatre sur les paliers 4 branches) accumulateurs RIS pressurisés à l’azote sont
situés dans le BR pour assurer un service le plus immédiat et, dans la mesure où
les accumulateurs ne nécessitent pas de maintenance en cours de cycle, ils peuvent
décharger passivement leur contenu au-dessous de 42 bars chacun dans la branche
froide qui lui correspond (Figure 7.42, Figure 7.43). Les accumulateurs sont de forme
cylindrique (40 m3 CPY, 47 m3 P4), pressurisés à l’azote, un gaz incondensable. Un
accumulateur contient 26 m3 (CPY) d’eau borée à 2 500 ppm (30 m3 P4). Les accumulateurs
ont été historiquement introduits sur les REPs pour renoyer le cœur en
situation d’APRP grosse brèche, en attendant l’entrée en service de l’ISBP. Chaque
accumulateur est dimensionné pour pouvoir assurer 50 % du débit nécessaire au
renoyage du cœur. Le principe de l’accumulateur est qu’il ne peut se vider par un
clapet anti-retour que si la pression dans l’accumulateur est supérieure à celle du circuit
primaire. L’accumulateur présente l’avantage d’être un système totalement passif.
Les accumulateurs sont chargés en eau de la bâche PTR via une pompe hydrostatique
volumétrique. Une vanne d’isolement permet d’isoler chaque accumulateur du circuit
primaire si l’opérateur ne veut pas que la charge d’azote passe dans le circuit primaire
lorsque l’accumulateur est vide d’eau. En effet, l’azote, en tant qu’incondensable,
Fig. 7.42 – Isolement d’un accumulateur.

<!-- page 892 (PDF 908) -->
Fig. 7.43 – Système d’injection par les accumulateurs moyenne pression.
dégrade les échanges thermiques dans les épingles GVs, où il a tendance à s’accumuler
par effet de densité.
La bâche PTR est un gros réservoir de 1 600 m3 de remplissage des piscines à 2 500
ppm de bore, dont la température est maintenue entre 7 ◦C et 40 ◦C, qui sert de réserve
où vont aspirer les pompes RIS. Deux pompes d’acide borique concentré servent à
la recirculation en permanence à basse pression de l’acide borique et au remplissage
initial du réservoir d’injection de bore. Un réservoir d’acide borique concentré de
550 litres est lui maintenant à température par des résistances chauffantes.
Notons
que
la
centrale
des
Ardennes
(Chooz
A)
ne
comportait
pas
d’accumulateurs.

### 7.5.5 L’injection de sécurité moyenne pression (palier P4 et ultérieurs)

À partir du palier 1 300 MWe (Figure 7.44), on a abandonné le système d’injection
haute pression pour une injection moyenne pression, dans la mesure où, pour de

<!-- page 893 (PDF 909) -->
Fig. 7.44 – Injection de sécurité ISBP et ISMP du palier P4-P’4 (adapté
de[Centrales Nucléaires EDF de 1 300 MW, 1991] p. 31).
nombreux accidents en particulier de dépressurisation rapide, un système haute pression
à débit très faible était inefficace. D’autre part, il n’était pas forcément judicieux
d’injecter à une pression supérieure à la pression d’ouverture des soupapes de sûreté
du pressuriseur. On réduit aussi le risque d’une injection intempestive puisque la pression
d’injection (environ 110 bars) est inférieure à la pression nominale de 155 bars.
Cette injection moyenne pression est constituée de deux lignes équipées d’une pompe
et d’une pompe de gavage (245 m3/h pour une hauteur de 1 025 m CE) et prenant
l’eau dans la bâche PTR. Ces pompes peuvent injecter de l’eau borée pour une pression
inférieure à 110 bars. Les pompes ISMP et ISBP de chaque voie se réunissent
dans un collecteur commun à sortie unique. L’injection de sécurité en branche chaude
est dirigée vers les boucles 1 et 4. L’ISMP et l’ISBP en branche froide injectent par le
biais des lignes de décharges piquées en branche froide sur les 4 boucles. L’ISMP et
l’ISBP injectent chacune dans un collecteur commun qui se sépare en 4 lignes d’injection
séparées. Notons qu’un diaphragme de restriction de débit est présent sur chaque
ligne après le refoulement des pompes.

### 7.5.6 L’injection de sécurité basse pression (tous paliers)

L’injection de sécurité basse pression (Figure 7.45) est mise en œuvre dans le cas de
dépressurisation importante du primaire, historiquement l’accident d’APRP grosse
brèche. Son objectif est de renoyer durablement le cœur pour éviter la dégradation du
combustible et l’oxydation des gaines de combustible. Elle doit pouvoir être activée

<!-- page 894 (PDF 910) -->
Fig. 7.45 – L’injection de sécurité basse pression (CP0). Deux collecteurs permettent
d’injecter dans les 3 branches chaudes. Chaque ligne est isolable par un clapet et deux vannes
motorisées en parallèle sur chaque collecteur. Une liaison est possible avec l’aspiration des
pompes RIS HP. Cette liaison est mise en œuvre quand la pression primaire est supérieure à
la pression de refoulement des pompes BP et qu’on a atteint le niveau bas de la bâche PTR.
L’eau borée provient alors des puisards du BR.
pendant un temps très long pour évacuer la puissance résiduelle. L’alimentation en
eau borée de l’ISBP est assurée dans un premier temps par la bâche PTR, puis,
lorsque celle-ci se vide par une recirculation de l’eau prise dans les puisards situés en
partie basse du BR. On parle de phase de recirculation. À l’évidence, toute brèche
située dans le BR de toute partie du circuit primaire laissera fuir l’eau dans le BR,
eau qui ne manquera pas de se retrouver dans les puisards. Dans les deux phases
(avant et après recirculation), ce sont des pompes spécifiques qui refoulent l’eau à
une pression d’environ 7 bars. Ces pompes centrifuges, qui sont disposées en parallèle,
assurent la fonction d’injection de débit à 100 % chacune (débit nominal 700 m3/h,
débit maximal 910 m3/h), assurant une redondance totale. Notons le cas particulier
de la centrale des Ardennes Chooz A qui utilise une injection basse pression gravitaire
à une pression de 20 bars.
On voit sur la Figure 7.45 que l’eau de la PTR est injectée par 2 motopompes
dans les 3 branches chaudes (CPY) par l’intermédiaire de 2 collecteurs. Chaque ligne
est isolable par des clapets et les collecteurs par des vannes motorisées en parallèle.
Une liaison est possible vers l’aspiration des pompes haute pression de charge, qui
permet le gavage de l’ISHP. Les pompes, qui nécessitent plus d’entretien, sont situées
à l’extérieur du BR dans le BAN.

<!-- page 895 (PDF 911) -->
### 7.5.7 La cartouche RIB (CPY)

Le palier CPY dispose spécifiquement d’un système d’injection de bore à très forte
concentration (un réservoir RIS 004 BA à 21 000 ppm de bore naturel), appelé
familièrement « cartouche RIB » (Figure 7.46). Cette protection permet de prendre
en compte le cumul d’un accident de refroidissement (RTV, RTE) aggravé d’un blocage
de la grappe la plus antiréactive (en conformité avec le critère de défaillance
unique). Pour éviter toute cristallisation entre les vannes de ce réservoir, une boucle
de recirculation de l’acide borique est en service continu lors du fonctionnement normal
. Le système peut être connecté au système d’eau déminéralisée SED, qui sert à
remplir initialement le ballon RIS 021 BA qui est connecté à la ligne de recirculation.
Fig. 7.46 – Description de l’injection à forte concentration en bore (cartouche
RIB, CPY).
Cette cartouche RIB présente l’intérêt d’être valorisable aux niveaux des études
de sûreté, d’autant plus que le risque d’accident de dilution par le RIS nécessite le
cumul d’une ouverture erronée d’une des vannes RIS 032 à 035 VP (alors qu’on n’est
pas censé y toucher lors d’une connexion au circuit SED sur la boucle de recirculation
d’acide borique très concentré et que ces vannes sont condamnées administrativement
), à laquelle on ajoute une défaillance de la protection anti-dilution (PAD) de la
boucle de recirculation qui entraîne un isolement de la ligne sur signal de niveau haut
du réservoir d’expansion RIS 021 BA. Même si de l’eau du SED non borée se trouvait

<!-- page 896 (PDF 912) -->
en amont de la soupape RIS 215 VP qui serait bloquée ouverte (en haut à droite de
la Figure 7.46), l’eau claire s’écoulerait préférentiellement vers le circuit des purges et
évents RPE qui est non pressurisé. En conclusion, la cartouche RIB est extrêmement
robuste à tout problème de dilution intempestive.
Sur les paliers ultérieurs, on a remplacé le cartouche RIB par une injection automatique
de bore à 7 000 ppm (Fonction de borication automatique ou FBA), moins
complexe au niveau de la cristallisation du bore, mais non valorisable au niveau des
études de sûreté. La FBA utilise les systèmes RCV et REA-Bore. L’injection de bore
est initiée par le signal « très basse température en branche froide » (pour couvrir
un accident de RTV). La FBA entraîne la mise en service du RIS, le démarrage des
deux pompes REA et l’isolement de l’enceinte (1re phase). Les débits injectés sont de
l’ordre de 60 m3/h environ à 100 bars. C’est l’opérateur qui arrête manuellement la
FBA au bout d’une demi-heure.
La Figure 7.47 présente le lignage complet du RIS (CPY).
Fig. 7.47 – Lignage complet du RIS.

### 7.5.8 Engagement du RIS

En situation normale de fonctionnement, les circuits RIS doivent être toujours disponibles
en tant que systèmes de sûreté classés. Notons qu’une pompe haute pression
de charge est en marche pour assurer le débit d’appoint du RCV de compensation de
diverses fuites (fuites aux joints des pompes primaires, purges. . . ), les pompes basse
pression sont à l’arrêt, mais le circuit de recirculation du bore est en service permanent,
pour éviter tout problème de cristallisation. Différents signaux enclenchent le RIS
(Figure 7.48), en particulier la coïncidence d’un bas niveau du pressuriseur et de la

<!-- page 897 (PDF 913) -->
Fig. 7.48 – Critères d’engagement du RIS.
pression du pressuriseur (sauf au démarrage bien sûr), une pression élevée dans l’enceinte
du BR, une discordance de pression entre les différents GVs, la coïncidence d’un
fort débit de vapeur avec une pression de vapeur basse et une température moyenne
primaire faible. Les automatismes RIS engagent le démarrage de la deuxième pompe
HP du RCV, l’isolement de la recirculation du bore, l’ouverture des vannes d’isolement
en branche froide pour injecter l’eau fortement borée de la PTR, et la même
action en branche chaude avec un retard pour s’assurer que l’injection a bien eu
lieu. Côté accumulateurs, c’est la seule pression du primaire qui pilote le relâchement
d’eau fortement borée. En ce qui concerne l’injection basse pression, on démarre les
deux pompes BP sur débit nul (car la ligne d’injection est normalement fermée). On
ouvre les vannes d’isolement des collecteurs d’injection lorsque la pression primaire
est inférieure à la pression de refoulement des pompes BP. Bien entendu, le signal d’IS
entraîne un AAR avec isolement de l’enceinte par arrêt de la ventilation, déclenchement
de la turbine, isolement de l’ARE et passage sur ASG pour les générateurs de
vapeur, enfin démarrage des diesels de secours pour suppléer à une éventuelle perte
du réseau électrique.
Notons que le comportement du primaire est très dépendant du type d’incident
/accident en cours. Un APRP grosse brèche fait chuter fortement en quelques
dizaines de secondes la pression au-dessous de 20 bars, rendant l’ISHP quasi inefficace
(voire totalement), et dont les pompes peuvent être arrêtées très rapidement, pour
éviter qu’elles ne cavitent. Ce sont les pompes BP qui assurent le service à partir de
7 bars, il y a alors fermeture du débit nul. Dans le cas d’un APRP petite brèche, c’est
l’inverse, puisque la pression primaire peut rester largement au-dessus de la pression
de refoulement des pompes BP du fait de l’équilibre du primaire avec le secondaire.
On peut alors arrêter les pompes en surveillant le niveau de la bâche PTR et des

<!-- page 898 (PDF 914) -->
puisards. Il est temps de redémarrer une pompe BP lorsque le niveau d’eau dans les
puisards est suffisant. On peut alors redémarrer une pompe basse pression et ouvrir
la liaison entre le refoulement des pompes BP et l’aspiration des pompes HP. La
situation d’une RTV est identique au cas de l’APRP petite brèche puisque la pression
reste élevée.
Il faut éviter d’injecter de façon intempestive de l’eau à haute pression dans un
circuit « solide » (plein d’eau) pour d’évidentes raisons de tenue mécanique liée au
ballonnement du RCP. Cela conduirait à une augmentation du niveau d’eau dans le
pressuriseur à partir d’une quinzaine de minutes après le début de l’injection HP. Une
injection de sécurité est dite « surabondante » si l’ensemble des situations suivantes
est vérifié :
• la pression primaire est comprise strictement entre 138 bars relatifs (seuil P11)
et 161 bars relatifs (seuil d’ouverture des soupapes de décharge du pressuriseur) ;
• la marge à la saturation est telle que : Tsat −TRIC ≥40 ◦C ;
• la pression vapeur est équilibrée dans les boucles primaires ;
• le niveau pressuriseur est dans la gamme de mesure.
Il faut par contre bien entendu éviter d’arrêter volontairement une IS qui s’est déclenchée
automatiquement (cas de l’accident de TMI-2), en tout cas sans une bonne raison.
À la mise en service de l’injection de sécurité, on isole l’enceinte en première phase,
ce qui conduit à isoler le circuit de purge des GVs.
Le passage en recirculation est assuré sur l’activation des signaux indiquant que la
bâche PTR est en train de se vider (MIN2 et MIN3). On commande alors l’isolement
des lignes de débit nul vers le PTR avec, pour le palier 1 300 MWe, l’ouverture des
lignes de débit nul vers les puisards (pour ne pas contaminer la bâche PTR à la
recirculation), l’ouverture des vannes d’aspiration aux puisards, puis la fermeture des
vannes d’aspiration à la bâche PTR. La bascule d’injection en branches chaudes ou
branches froides est gérée manuellement.

### 7.5.9 Fuite du RIS

Le circuit RIS est d’une importance capitale pour la sûreté de la tranche ; c’est pourquoi
EDF a pris très au sérieux l’occurrence d’une fuite non isolable sur une tuyauterie
RIS en aval du dernier clapet d’isolement avant le circuit primaire (Dampierre 2 en
1992, Dampierre 1 en 1996). Cette fuite est apparue suite à une fissure circonférentielle
de faible amplitude en partie basse de la tuyauterie. Ces fuites se sont révélées à évolution
lente, permettant un arrêt de la tranche avant aggravation. L’analyse a montré que
la cause était liée à de la fatigue thermique créée par un vortex entre une arrivée d’eau
froideetl’eauchaudeà300 ◦C duprimaire.Cerisqueestappelérisque«Farley-Tihange»,
car il est apparu pour la première fois sur la tranche américaine de Farley et la tranche
belge de Tihange. L’arrivée d’eau froide peut être due à une fuite des vannes d’isolement
du RIS vis-à-vis du refoulement du RCV. Rappelons que sur les tranches CPY, RIS et
RCV sont intriqués, partageant les pompes HP, contrairement aux paliers ultérieurs où
lesdeuxsystèmessontséparés.Uncontrôlesystématiqueditde«pointzéro»surtoutesles
portions de tuyauteries susceptibles d’être concernées, et le remplacement systématique

<!-- page 899 (PDF 915) -->
sur indications d’amorçage de fissures, a permis d’éliminer le risque, qui justifie une
surveillance constante.

## 7.6 Le circuit de réfrigération intermédiaire (RRI)

[Coppolani et al., 2004] p. 195

### 7.6.1 Généralités

Le circuit de réfrigération intermédiaire (RRI) (Figure 7.49, Figure 7.50, Figure 7.51)
a pour fonction de séparer physiquement le circuit primaire et son extension en
Fig. 7.49 – RRI du palier CPY.

<!-- page 900 (PDF 916) -->
Fig. 7.50 – RRI du palier 1 300 MW e.
situation d’arrêt à savoir le RRA, qui véhiculent tous les deux une petite quantité
de matériaux radioactifs (produits d’activation, produits de fission en cas de défauts
des gaines combustibles. . . ), de l’eau brute provenant de la source froide. Le RRI,
circuit de découplage, fonctionne en boucle fermée véhiculant de l’eau déminéralisée,
et assurant une barrière supplémentaire vis-à-vis de la source froide. Le RRI assure
l’alimentation en eau de refroidissement déminéralisée de tous les réfrigérants de l’îlot
nucléaire, dont les réfrigérants des circuits de sauvegarde (RIS, EAS). L’eau du RRI
est elle-même refroidie via des échangeurs par le circuit d’eau brute secourue SEC.
Ce refroidissement doit être assuré au démarrage de la tranche, en fonctionnement
normal, en arrêt à chaud et en attente à chaud, pour la mise et le maintien en arrêt
à froid (dont le rechargement) et en situation accidentelle. Au fil des paliers, le RRI
a vu une amélioration de la séparation des fonctions.

<!-- page 901 (PDF 917) -->
Fig. 7.51 – RRI du palier N4.

### 7.6.2 Constitution et usages

En respect du critère de défaillance unique, la partie du RRI alimentant les circuits
de sauvegarde est composé de deux files indépendantes et pouvant assurer à 100 %
chacune la fonction. Chaque file dispose de 2 pompes 100 %, par contre les échangeurs
RRI/SEC ne sont pas doublés 100 % car ce sont des composants passifs dont
l’indisponibilité fortuite (hors nettoyage programmé) est très peu probable. Dans la
pratique, on a choisi une solution intermédiaire avec deux échangeurs 50 % pour faciliter
l’entretien en fonctionnement. Le RRI est un circuit basse pression (< 12 bars)
et basse température (< 65 ◦C). On ne craint donc pas de risque de pressurisation

<!-- page 902 (PDF 918) -->
ou de vaporisation. Le RRI assure la réfrigération des auxiliaires nucléaires à partir
de deux collecteurs banalisés (aller et retour) piqués sur les files de sauvegarde.
L’isolement entre les files est assuré par 4 vannes motorisées, une sur chaque aller et
chaque retour de chaque file. Ces vannes reçoivent un ordre de fermeture en cas de
signal haute pression enceinte. En fonctionnement normal, deux vannes d’une même
file sont ouvertes et assure l’alimentation d’un tronçon banalisé, appelé file commune.
C’est cette file commune qui alimente tous les auxiliaires utiles au fonctionnement normal
en puissance. Les collecteurs alimentant les auxiliaires protégés du séisme sont
installés dans des locaux adéquats. Les parties non calculées au séisme sont séparées
de celles résistant au séisme par deux vannes automatiques en série, qui se ferment
sur niveau très bas de la bâche de la file commune. Le RRI doit pouvoir évacuer la
puissance résiduelle même après l’arrêt du réacteur. En situation accidentelle, le RRI
a pour fonction de refroidir les échangeurs des systèmes d’aspersion de l’enceinte EAS,
les échangeurs de la ventilation de secours des locaux des pompes de charge DVH et
les échangeurs de la production d’eau froide des locaux électriques DEL, ainsi que les
échangeurs et pompes du circuit RRA. Les matériels réfrigérés peuvent être classés
en trois groupes :
• le groupe 1 : la réfrigération des matériels de sauvegarde indispensables face à
un accident ;
• le groupe 2 : les réfrigérants vitaux pour le matériel hors accident de référence ;
• le groupe 3 : les réfrigérants utilisés en marche normale.
La partie sauvegarde du RRI (groupe 1) est constituée de deux files indépendantes
(voie A et voie B), résistantes au séisme et géographiquement séparées. Chaque file
peut réfrigérer un échangeur et une pompe EAS, une motopompe d’injection de
sécurité HP ou MP selon le palier, et BP, un échangeur et une pompe RRA lors
de la mise en arrêt à froid de la tranche. Sur le CPY où l’ensemble RRI est commun
à deux tranches jumelles [Centre de production nucléaire du Bugey, 1986] p. 62,
chaque file comporte essentiellement deux pompes 6,6 kV de circulation en parallèle
de 1 600 m3/heure sous 50 m CE, pouvant assurer 100 % de la fonction, et débitant
vers deux échangeurs eux aussi en parallèle (on parle de demi-échangeur). Ces échangeurs
transfèrent la chaleur à l’eau brute de la source froide (SEB ou SEC, débit de
1 800 m3/heure), refroidissant l’eau du RRI de 49, 3 ◦C à 35 ◦C. La température de
l’eau du SEC passe, elle, de 21 ◦C en moyenne à 33, 7 ◦C. Le RRI refroidit plusieurs
circuits : RCV, RRA, EAS, moteurs de pompes primaires, traversée des cloisons des
circuits vapeur et eau alimentaire. . . Un réservoir d’expansion (10 m3) est situé en
parallèle des pompes RRI, collectant au refoulement de ces pompes et renvoyant l’eau
en amont des pompes. Ce réservoir permet de compenser les variations de volume et
de rajouter des produits inhibiteurs de corrosion (phosphates).
Le lignage vers les échangeurs EAS comporte sur chaque file : deux vannes
manuelles, une vanne pneumatique et un diaphragme. Le lignage vers les échangeurs
DVH comporte sur chaque file deux vannes manuelles et un diaphragme. Le lignage
vers les échangeurs RRA comporte sur chaque file 4 vannes manuelles, une vanne
motorisée et un clapet. Enfin, le lignage permettant le refroidissement des pompes
RRA comporte sur chaque ligne 6 vannes manuelles, une vanne motorisée et un clapet.

<!-- page 903 (PDF 919) -->
En fonctionnement normal (réacteur en puissance), une file SEC est en service
avec une pompe, mais si une baisse de pression est décelée au refoulement de la
pompe, on bascule automatiquement sur la pompe de la même file. C’est la perte
complète d’une file SEC qui va mettre en service automatiquement la pompe d’une
autre voie. En situation accidentelle, une pompe à l’arrêt sur l’autre file que celle en
fonctionnement est systématiquement démarrée. En situation accidentelle, dans la
situation où l’aspersion enceinte est engagée, on ouvre les vannes pneumatiques qui
isolent les échangeurs RRI/EAS. On concentre l’effet du RRI sur les seules files de
sauvegarde en fermant les autres utilisateurs banalisés. Si la situation accidentelle
fait intervenir le RRA, la mise en configuration des deux files RRA est faite depuis
la salle de commande, après ouverture manuelle des vannes de traversée enceinte des
lignes alimentant les échangeurs RRA. Les vannes motorisées du lignage RRI doivent
être ouvertes sur commande de l’opérateur. Les vannes manuelles du RRI, qui sont
normalement fermées après l’arrêt du RRA, doivent être ouvertes lors des opérations
de conditionnement du RRA.

## 7.7 Le circuit d’échantillonnage nucléaire (REN)

Il est prévu de pouvoir prélever des échantillons d’eau et de gaz du circuit primaire
pour effectuer des analyses chimiques et radiologiques. Des lignes de petit
diamètre sont placées sur des piquages et dirigent les prélèvements vers le local
d’échantillonnage. Les temps de transfert permettent un délai suffisant pour laisser
décroître significativement l’azote 16 (période 7,13 secondes), produit dans le cœur
par activation (n,p) de l’oxygène 16 de l’eau du primaire. La température et la
pression sont abaissées pour compatibilité avec les systèmes de mesure. Pour que
les échantillons soient significatifs de l’état courant de la chaudière, il faut purger
régulièrement les lignes de prélèvement. Ces purges sont envoyées dans le ballon
RCV. Des boucles de by-pass prélèvent de l’eau des branches froides et chaudes,
respectivement par un by-pass des pompes primaires et des générateurs de vapeur.
Chacune de ces deux lignes se regroupe dans une ligne de retour commune connectée
à la branche en U (entre le GV et la pompe primaire de la branche concernée).

## 7.8 Le circuit des purges et évents (RPE)

Le circuit des purges et évents (RPE, Figure 7.52) a pour fonction de récupérer les
eaux de purges et les évents du circuit primaire ainsi que de ses circuits auxiliaires
(by-pass des systèmes de mesure, RCV, RRA. . . ). Ces effluents peuvent donc contenir
de la radioactivité. Le RPE comporte un réservoir d’effluents primaires (RPE 01 BA)
et son alimentation en azote. Ce réservoir est alimenté par la vidange du RDP, des
fuites des joints 2 et 3 de chaque pompe primaire, de la collecte des fuites du joint
de cuve, de l’arrivée du soutirage excédentaire. Le RPE est relié avec les branches
en U de chaque boucle, et comporte des pompes de reprise et de recirculation. Une
ligne le connecte aux effluents primaires. Une ligne d’effluents résiduaires permet la
récupération de la soupape PTR 220 VB. Le RPE est aussi connecté à l’évent du
RDP, les réservoirs de mouillage des joints, la ligne des effluents hydrogénés vers
le TEG, le réservoir des effluents aérés (liaison évent cuve, évent pressuriseur), le
