# Chapitre 6 Le circuit secondaire — 6.5 Le groupe turbo-alternateur (aspects vapeur) … 6.6 Les groupes sécheurs-surchauffeurs
<!-- source PDF pages 749-760 -->

<!-- page 733 (PDF 749) -->
### 6.4.7 Fuite primaire-secondaire

[Hutin, 2016] p. 403
Étant donné la surface considérable d’échange et le nombre de tubes GV, l’importante
différence de pression entre primaire-secondaire, l’aspect corrosif de l’eau du primaire
(acide borique), il est logique de se poser la question d’une éventuelle fuite primairesecondaire
. Sans parler de rupture de tube de GV en cas d’accident, des fuites liées
à des fissurations de tubes GV apparaissent, sans qu’il n’y ait pour autant de conséquences
sur la sûreté. Ces fissures peuvent d’ailleurs « respirer » en fonction du niveau
de charge en se refermant, voire se colmater par dépôts d’oxydes métalliques 19. Selon
les STEs, le débit de fuite limite autorisé est de 72 litres/heure. Au-delà, il faut inspecter
le GV « fuitard » et condamner en les bouchant les tubes GV incriminés 20,
avec une limite de 10 % du total des tubes à ne pas dépasser. Au-delà de ces 10 %, il
faut remplacer le GV.
La surveillance du taux de fuite est basée sur la mesure en continu de l’activité de
l’azote 16 dont on détecte facilement le rayonnement gamma très énergétique (émetteur
bêta – de 7,13 s de période, émettant principalement un photon de 6,1 MeV).
Cet azote 16 est produit par activation neutronique (n,p) de l’oxygène 16 stable de
l’eau du primaire lors du passage dans le cœur actif :
0n +16
8 O ⇒16
7 N +1
1 p
La faible période de l’azote 16 est intéressante vis-à-vis du temps de transfert de l’eau
dans le circuit primaire de l’ordre de 20 secondes, car l’azote 16 ne s’accumule pas
indéfiniment dans le primaire.

## 6.5 Le groupe turbo-alternateur (aspects vapeur)

[Bloch et Singh, 2000], [Durr, 1983], [Pluviose, 2010] p. 99

### 6.5.1 Généralités

La vapeur est dirigée vers le groupe turbo-alternateur qui comporte un corps haute
pression (HP), deux (CP2 à 4 soupapes d’admission) ou trois corps (CP0, CP1
Figure 6.35, P4 à 6 soupapes d’admission - Figure 6.36) basse pression (BP). Le
palier N4 comporte même un corps moyenne pression (MP). Le corps HP bénéficie
d’une vapeur à environ 285 ◦C avec un titre de 0,9947 (exemple tiré d’un P4). En
sortie du corps HP, la vapeur résiduelle passe dans un sécheur puis un surchauffeur
qui permet d’alimenter en vapeur sèche les corps BP. Il est très important que la
vapeur n’emporte pas des gouttes d’eau qui abîmeraient rapidement les aubages des
turbines.
La turbine tourne à 1 500 tours/minute. Au total, 5 440 tonnes/heure de vapeur
entrent dans la turbine et 3 000 tonnes/heure sortent vers le condenseur, le différentiel
étant les 6 soutirages de vapeur qui servent à réchauffer l’eau d’admission. Le corps HP
19 Comme le GV fonctionne en bouilleur, il concentre les produits de corrosion métalliques qui se
concentrent dans la partie secondaire du GV, d’où l’importance du conditionnement chimique volatil
du secondaire (pH, oxygène, chlorure. . . ).
20 En pratique pour un GV non fuitard, on inspecte en surveillance seulement une partie des
tubes (1 sur 8) lors des arrêts pour rechargement, et l’ensemble des tubes lors des visites décennales.

<!-- page 734 (PDF 750) -->
Fig. 6.35 – Point de fonctionnement nominal d’une turbine CP1 (1 corps HP, 3
corps BP, 6 soupapes d’admission, 6 soutirages) construite par Alsthom-Belfort.
En sortie du corps HP, la vapeur est séchée par un séparateur et surchauffée pour un meilleur
rendement dans les corps BP. Le poste d’eau est sans bâche alimentaire
Fig. 6.36 – Schéma fonctionnel et bilan thermodynamique du GTA d’un P’4.

<!-- page 735 (PDF 751) -->
comporte deux étages identiques et symétriques de sept roues montées en diabolo. La
vapeur est admise dans la partie centrale de la turbine et fuit par les deux extrémités.
Les trois corps BP comportent eux aussi deux étages chacun.
Des soupapes d’admission (6 pour CP0, CP1, P4, N4 ; 4 pour CP2) introduisent
la vapeur dans la turbine (Figure 6.37, Figure 6.38).
Fig. 6.37 – Principe de l’admission vapeur par vannes d’admission.

<!-- page 736 (PDF 752) -->
Fig. 6.38 – Détail d’une vanne d’admission turbine.

### 6.5.2 Régulation de la turbine

[Bloch et Singh, 2000] p. 137
La modulation de charge, du fait que les réacteurs ne fonctionnent pas forcément à
puissance nominale, s’impose en suivi de réseau. Ce suivi de réseau peut générer des
amplitudes jusqu’à 70 % de puissance nominale (le réacteur baisse alors à 30 % Pnom).
Le téléréglage impose aussi des variations, bien que plus faibles mais plus rapides. Ces
besoins imposent un automatisme de contrôle de la turbine (Figure 6.39).
Les régulateurs sont des automatismes analogiques réalisés à partir de cartes électroniques
. Ils sont constitués de modules qui forment un chaînage entre les capteurs
qui recueillent les mesures expérimentales, et l’actionneur dont ils élaborent la commande
. Chaque module a une fonction élémentaire particulière (filtre passe-haut,
filtre passe-bas, régulateur, sommateur, intégrateur, limiteur. . . ) alimentés par des
paramètres (gain, constante de temps. . . ) classiques en automatisme : on parle de
contrôle-commande pour décrire l’ensemble de ces régulateurs. Le régulateur de turbine
d’une tranche CP1 comprend environ 200 cartes électroniques, 12 vérins hydrauliques
de commande des soupapes vapeur, avec leur asservissement de position associé.
Le tout est implanté dans quatre armoires électroniques de 2,20 m
× 0,60 m
×
0,60 m. Le régulateur de turbine est examiné à chaque arrêt de tranche pour révision
générale en injectant un signal échelon pour vérifier si la réponse est cohérente à ce

<!-- page 737 (PDF 753) -->
Fig. 6.39 – Régulation de la turbine.
qu’on attend du composant. On contrôle aussi les vérins et des essais d’îlotage 21 sont
régulièrement effectués pour vérifier le comportement des régulations.

### 6.5.3 Régulation de la température moyenne par le contournement de la turbine

[Transfert des connaissances n ◦603, Transitoires normaux de grande amplitude,
1985] p. 4
Le réglage de la puissance, et donc de la température moyenne cuve, s’effectue grâce au
positionnement des groupes de compensation de puissance (GCP), mais une régulation
supplémentaire intervient en support au réglage de la température moyenne cuve par
les GCPs. On parle de régulation en mode température. Cette régulation intervient en
particulier lors d’un îlotage ou d’un déclenchement de la turbine sans AAR. Enfin, elle
intervient pour évacuer la puissance résiduelle dans la phase juste après un AAR. En
situation « turbine enclenchée », et dans le cas d’un îlotage, la température moyenne
cuve mesurée est comparée avec la température de référence (celle du programme de
température en fonction du niveau de puissance), calculée en utilisant la puissance
obtenue par mesure de pression à l’admission turbine (cette pression est une image
fidèle de la puissance produite par la turbine). L’écart entre ces deux valeurs de
températures moyenne cuve est envoyé à un régulateur proportionnel dont la sortie
commande l’ouverture modulée de quatre groupes de quatre vannes. Cette commande
21 L’ilotage est le transitoire normal d’exploitation le plus sévère (en matière de soudaineté et de
gamme de variation des paramètres physiques de la chaudière). Un essai d’ilotage est réalisé à la fin
des essais physiques de redémarrage avec toutes les chaînes de contrôle-commande en automatique,
pour voir comment l’ensemble se comporte. Le transitoire doit laisser des marges suffisantes vis-àvis
des protections d’AAR et des seuils d’ouverture des soupapes VVP. Tout mauvais réglage des
protections sera sanctionné par un échec de cet essai.

<!-- page 738 (PDF 754) -->
Photo 6.5 – Une publicité pour les sécheurs-surchauffeurs de Stein Industrie
(1978) (collection Marguet).
présente une bande morte quand la valeur absolue de l’écart est inférieure à 2, 8 ◦C, et
l’ouverture est totale quand l’écart atteint 13, 9 ◦C. Cet écart est aussi envoyé à quatre
relais à seuil étagés qui provoquent l’ouverture rapide des quatre vannes associées. La
vapeur contourne alors la turbine, pour aller se condenser dans le condenseur. Pour
opérer ce contournement, il faut bien entendu que le condenseur soit disponible.

<!-- page 739 (PDF 755) -->
En situation « turbine déclenchée », la température de référence est celle à charge
nulle (286 ◦C). À ce moment, l’écart de température est envoyé à un régulateur
proportionnel sans bande morte, qui commande uniquement l’ouverture des deux
premiers groupes de vannes (au total 8 vannes). Si l’écart est supérieur à 11 ◦C,
les 8 vannes en question sont ouvertes totalement. Dans cette situation, il n’y a pas
d’ouverture rapide. Notons qu’à basse charge, le mode température bascule sur une
régulation de la pression.
Il existe parallèlement au mode température un mode pression, dont la fonction
est la même, mais qui utilise la pression mesurée au barillet-vapeur. Le barillet-vapeur
récolte la vapeur de l’ensemble des GVs de la tranche avant de l’envoyer à la turbine.
L’évolution de la pression en fonction du temps est envoyée à un dérivateur (calcul
de la dérivée de la pression). Le signal de dérivée en fonction de son importance
commande l’ouverture des soupapes de contournement (50 % pour le premier groupe,
75 % pour le deuxième, 100 % pour le troisième et 125 % pour le quatrième). Ce
cas de figure est une ouverture rapide, qui n’intervient pas en cas d’AAR. Il existe
aussi une ouverture modulée dont la commande est élaborée à partir de l’écart entre
la pression barillet et une valeur de consigne en fonction de la pression d’admission.
Dans tous les cas, le mode pression est plus intéressant que le mode température car
il permet de n’avoir qu’une seule chaîne de régulation (pas de bascule à basse charge
comme indiqué plus haut).

## 6.6 Les groupes sécheurs-surchauffeurs

[Hutin, 2016] p. 621

### 6.6.1 Principe des sécheurs-surchauffeurs

[Leclercq, 1988] p. 250
Les groupes sécheurs-surchauffeurs (GSS) (Figure 6.41, Figure 6.43, Figure 6.44,
Figure 6.46, Figure 6.47, Photo 6.5) permettent de reconditionner la vapeur en sortie
du corps haute pression avant de l’envoyer vers les corps basse pression (Figure 6.40,
Figure 6.42 et Figure 6.48). On évite ainsi une humidité excessive de la vapeur en
sortie du corps HP et qui nuirait au rendement des corps BP, dans la mesure où la
vapeur en sortie du corps BP va être déjà humide du fait d’une température relativement
basse (si on compare à une tranche thermique conventionnelle). Les GSS
sont installés sur le plancher de la salle des machines de part et d’autre de la turbine
(4 pour les CP0 et CP1, 2 à double faisceau pour les paliers ultérieurs).
Les réchauffeurs à double faisceau comporte deux faisceaux disposés tête-bêche,
et deux boîtes à vapeur, une de chaque côté de l’appareil. On obtient ainsi un gain de
compacité non négligeable et un rendement plus intéressant qu’un réchauffeur à un
faisceau unique.
La vapeur de chauffe provient d’un piquage sur la vapeur vive après le barillet
vapeur et avant le corps HP.
La performance des groupes de sécheurs-surchauffeurs (Tableau 6.5) est caractérisée
par l’efficacité moyenne de séchage (rapport entre le débit d’eau purgé divisé par
le débit d’eau entrant dans les sécheurs), le coefficient moyen d’échange thermique
caractérisé par le pincement des températures côté fluide chaud, la perte de charge

<!-- page 740 (PDF 756) -->
Fig. 6.40 – Implantation des groupes sécheurs-surchauffeurs du palier N4.
moyenne. Les mesures d’essais montrent que le taux d’humidité en sortie de sécheurs
est quasiment nul.
La Figure 6.43 et la Figure 6.44 montrent des écorchés de sécheurs-surchauffeurs
qui produisent une vapeur sèche ne mettant pas en danger d’érosion les aubes des
turbines basse pression. La Figure 6.45 présente le fonctionnement des sécheurssurchauffeurs
lors d’un transitoire très sensible d’îlotage.

### 6.6.2 Régulation des surchauffeurs

La régulation du débit de chauffe (Figure 6.48) est imposée par la technologie des
corps BP et utilise l’écart entre la température à l’admission BP et une consigne. On
doit faire face à trois situations différentes. En premier lieu, il faut régler la surchauffe
pour gérer le démarrage à froid des corps BP. En effet, ces corps sont à fûts et à disques
rapportés, et le décollement des disques apparaît à 1 500 tours/minute pour un écart
de température entre le fût et le disque de 100 ◦C [Circuit secondaire, 1978] p. 51. Il
faut donc régler la surchauffe pour tenir compte de ces données techniques. Une fois

<!-- page 741 (PDF 757) -->
Fig. 6.41 – Un sécheur-surchauffeur Alstom (publicité Alstom Power).
Fig. 6.42 – Sécheurs-surchauffeurs de type Alsthom-Stein avec traitement des
condensats.

<!-- page 742 (PDF 758) -->
Tab. 6.5 – Caractéristiques des surchauffeurs du palier P’4.
Theorie
saint
Cattenom
Belleville
Erreur
Alban
limite
T de surchauffe ( ◦C)
266,85
269,7
266,8
271,1
±2
Δt surchauffeur ( ◦C)
15,5
17,3
13,7
±2
Δp surchauffeur (mbar)
±100
Type de
–
Tubes
Tubes
Tubes
faisceau
lisses
lisses
à ailettes
Z2CN18-10
Z2CN18-10
Z2CT18
Fig. 6.43 – Coupes horizontale et radiale détaillées d’un sécheur-surchauffeur
(modèle CP0-CP1).

<!-- page 743 (PDF 759) -->
Fig. 6.44 – Sécheur-surchauffeur de type STEIN Industrie (tranches 900 MWe).
Fig. 6.45 – Fonctionnement d’un groupe sécheur-surchauffeur pendant un îlotage
de tranche.
la turbine démarrée en dessous de 30 % Pnom, la régulation du débit de vapeur du
surchauffeur est faite par une vanne auxiliaire de telle façon que la température de la
vapeur suive une consigne linéaire entre 110 ◦C à
◦%Pnom et 238 ◦C à 30 % Pnom.
Enfin, au-dessus de 30 % Pnom, une vanne Tout Ou Rien est ouverte et le surchauffeur
fonctionne alors comme réchauffeur.
En situation de démarrage après un arrêt à chaud, on constate que les disques se
refroidissent plus vite que le fût. Il y a donc intérêt à injecter une vapeur à une température
supérieure ou égale à celle des disques afin de ne pas accroître les contraintes
de serrage par dilatation thermique différentielle. Comme la turbine est chaude, on
peut monter plus vite en charge.

<!-- page 744 (PDF 760) -->
Fig. 6.46 – Détail d’un groupe sécheur-surchauffeur du palier CP2.
Fig. 6.47 – Écorché commenté d’un sécheur-surchauffeur de CP2.

### 6.6.3 Protection des sécheurs-surchauffeurs

Ces appareils sont protégés sur les tranches CP1 par 6 soupapes à clapet pilote
du type SPV-A fabriquées par la société Criss-Crosby. Au cours du début des
années 1980, des anomalies ont été constatées sur ces soupapes, dont certains refus
d’ouverture. Alsthom Atlantique a alors effectué des modifications pour assurer un
