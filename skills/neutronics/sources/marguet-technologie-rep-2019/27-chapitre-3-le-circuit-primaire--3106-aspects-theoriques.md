# Chapitre 3 Le circuit primaire — 3.10 Les pompes primaires — 3.10.6 Aspects théoriques … 3.10.11 Caractéristiques détaillées d’une pompe primaire
<!-- source PDF pages 346-360 -->

<!-- page 330 (PDF 346) -->
Fig. 3.36 – Étanchéité de l’arbre de la pompe : systèmes de mesure (d’après
[Système de contrôle volumétrique et chimique, 1978] p. 33).
technologie actuelle de pompe à rotor noyé, à faible rendement et à faible inertie
propre, ne permet pas de dépasser environ 2 MW par pompe, ce qui est notoirement
insuffisant vis-à-vis des 5 MW requis. À équivalence de service, il faudrait placer
plusieurs pompes à rotor noyé par branches, d’où une forte complexité du tracé du
primaire. De fait, cette technologie n’est pas encore utilisée dans le contexte. Par
contre, l’usage de joints hydrodynamiques, utilisés dans la conception de certaines
pompes primaires à l’étranger, offre l’intérêt d’une plus longue longévité.

### 3.10.6 Aspects théoriques

Les équations fondamentales régissant le fonctionnement des pompes dérivent du théorème
de Bernoulli en mécanique des fluides. Soit une pompe située à une hauteur z
au-dessus de l’eau d’un bassin à surface libre où règne une pression Patm, dont la

<!-- page 331 (PDF 347) -->
Fig. 3.37 – Étanchéité de l’arbre de la pompe : débits comparés (d’après [Système
de contrôle volumétrique et chimique, 1978] p. 61).
pompe aspire l’eau par une conduite verticale (Figure 3.43) :
He + v2
e
2g + z = Hatm −ΔH
He = Pe/ (ρg) est la hauteur de d’eau correspondant à la pression à l’entrée de la roue
de la pompe, Hatm est la hauteur d’eau correspondant à la pression atmosphérique du
niveau libre à la pression Patm, ΔH est la perte de charge de la conduite d’aspiration
exprimée en hauteur d’eau, Hasp = z + ΔH est la hauteur d’aspiration de la pompe.
D’où la pression absolue He à l’entrée de la pompe (exprimée en hauteur d’eau) :
He = Hatm −Hasp −v2
e
2g
On parle classiquement de hauteur d’aspiration, à savoir la différence d’altitude entre
le point d’aspiration de la conduite d’aspiration de la pompe et l’altitude du point de
refoulement de la pompe. En parallèle, on parle de hauteur de refoulement comme la
différence d’altitude du point de refoulement de la pompe et le niveau atteint verticalement
par l’eau refoulée dans la conduite de refoulement. La hauteur géométrique
totale est la somme de ces deux hauteurs. Ces hauteurs ne tiennent pas compte des

<!-- page 332 (PDF 348) -->
Fig. 3.38 – Localisation de la barrière thermique d’une pompe primaire (adapté
de 21). On voit aussi la bague thermique. Début 1987, des fissures radiales et circonférentielles
jusqu’à 5 mm ont été observées sur un arbre de pompe sous la bague thermique. Cette
dernière a pour fonction de protéger l’arbre contre les chocs thermiques dus à la rencontre
de l’eau d’injection RRI (basse température 40 ◦C) et l’eau du primaire à 286 ◦C. L’origine
de ces fissures est un phénomène de faïençage thermique. En fait, la bague thermique perd
son frettage initial lors des inévitables transitoires de rétablissement d’injection aux joints,
d’où l’existence d’un débit alterné d’eau chaude montante et d’eau froide descendante sous la
bague, conduisant au faïençage thermique. Le microbillage de la surface interne de la bague
permet de regagner des marges à la fissuration.
pertes de charges par frottement de l’eau dans les conduites. D’où la notion de hauteur
manométrique qui prend en compte la mesure de la pression (par manomètre)
à l’aspiration et au refoulement. Dans la pratique, la hauteur manométrique totale
(refoulement-aspiration) est plus haute que la hauteur géométrique totale, du fait des
pertes de charge. C’est la hauteur manométrique qui caractérise le travail réel fourni
par la pompe. On sait depuis des temps très anciens, qu’il n’est pas possible, si le
rejet de la pompe est à pression ambiante (1 atmosphère), de faire monter l’eau froide
21 J. Bediou, C. Bore, T. Chator, J.J. Engel, M.T. Pascal, A. Verry : Pompes primaires des REP
900, Études mécaniques récentes, Séminaire EDF de mécanique des structures, Milly-la-Forêt, 25 et
26 avril 1990, 1990.

<!-- page 333 (PDF 349) -->
Fig. 3.39 – Étanchéité de l’arbre de la pompe : alarmes et sécurité (d’après [Système
de contrôle volumétrique et chimique, 1978] p. 62).
à une hauteur supérieure à 10,33 mètres (sans tenir compte de la perte de charge).
C’est équivalent à la hauteur maximale qu’on peut atteindre dans un baromètre avec
la seule pression atmosphérique. Au-delà de cette hauteur, de la vapeur va se former
par cavitation à l’entrée de la roue de la pompe. Physiquement, cela se traduit par
l’équation :
He = Hatm −Hasp −v2
e
2g > Hvapeur
Hvapeur est la hauteur équivalente correspondant à la tension de vapeur saturante
de l’eau. En étant plus précis, on s’aperçoit que le point de plus basse pression dans
une pompe ne se situe pas à l’entrée de la pompe, mais au niveau de l’intrados des
aubages mobiles. La pression est supérieure au niveau de l’extrados qui pousse l’eau.
C’est donc au niveau de l’intrados que les bulles vont apparaître. La différence de
pression entre l’entrée de la pompe et l’intrados de l’aube dépend de l’angle de la
tangente de l’aube et de l’angle de l’écoulement : on parle de dépression dynamique
qu’on peut traduire par :
He −Hmin = λv2
relative
2g

<!-- page 334 (PDF 350) -->
Fig. 3.40 – Étanchéité de l’arbre de la pompe primaire (d’après [Pompes primaires,
1977] p. 35).
vrelative est la vitesse relative du fluide par rapport à l’aube, λ est le coefficient de
dépression dynamique qui est lié à l’écart entre les angles d’entrée réels du fluide dans
l’aubage et l’angle du métal d’entrée choisi pour le rendement optimal de la pompe.
Ce coefficient varie paraboliquement en fonction du débit comme les pertes de charge
par choc à l’entrée de la roue.

### 3.10.7 Cavitation des pompes primaires

[de Kovats et Desmur, 1971] p. 67
La cavitation est un phénomène qui apparaît quand la pression diminue dans un circuit
hydraulique, et devient inférieure à la tension de vapeur du liquide correspondant

<!-- page 335 (PDF 351) -->
Fig. 3.41 – Détail des joints d’une pompe Jeumont-Schneider CPY.
[Franc et al., 1995]. La mise en vitesse de l’eau dans une pompe conduit à une diminution
de sa pression statique en accord avec le théorème de Bernoulli. Toute pompe
refoulant un liquide susceptible de bouillir peut subir ce phénomène si un point quelconque
de la pompe voit sa pression chuter par trop grande hauteur d’aspiration ou
par l’augmentation de la vitesse du fluide dans son trajet. Le phénomène de cavitation
se traduit par la formation de poches de vapeur (Photo 3.6). Lorsque ces poches sont
transportées par le liquide vers des zones de plus forte pression, elles implosent violemment
, en quelques microsecondes. Si cette implosion se produit proche d’une paroi,
cela engendre un micro-jet et une onde de choc, créant localement des surpressions
qui peuvent dépasser la limite élastique des matériaux les plus durs 22.
22 Jean-Marc Dorey, Alain Verry, Pierre Grison : Une meilleure maîtrise de la cavitation, EPURE,
n◦25, janvier 1990, pp. 13-21.

<!-- page 336 (PDF 352) -->
Fig. 3.42 – Schéma de la collecte des fuites à travers les joints 1 et 2.
La cavitation dans les pompes est particulièrement redoutée car, outre le fait
qu’elle dégrade les performances de la pompe, elle induit des phénomènes mécaniques
(vibrations, compression/décompression du gaz. . . ) qui peuvent sévèrement endommager
les aubes des pompes (Figure 3.44, Photo 3.7, Photo 3.8).
Ce sont les impacts répétés dus à l’implosion des bulles de vapeur près des parois
qui créent dans le temps une dégradation des matériaux, avec érosion de matière.

<!-- page 337 (PDF 353) -->
Fig. 3.43 – Pompe aspirante au-dessus d’une surface libre.
Le phénomène apparaît dans les organes où la vitesse du fluide est localement importante
comme les pompes, les turbines, les vannes et les diaphragmes. On se situe
ici clairement à l’interface entre la mécanique des fluides et le comportement des
matériaux, d’où une complexité certaine dans la modélisation des phénomènes que
la rapidité rend encore plus difficile à appréhender. L’effet de la cavitation diffère
d’après la grandeur de la roue et le nombre d’ailes, c’est-à-dire d’après les dimensions
d’une part, et la pression spécifique d’autre part. Les poches de vapeur, qui se produisent
aux points où la pression absolue atteint la valeur de la tension de vapeur,
ont approximativement les mêmes dimensions. Si la poche occupe tout l’espace de la
section d’une petite roue, elle peut empêcher le passage du fluide. La cavitation pour
deux roues homothétiques se produit aux mêmes vitesses et occupera relativement
une plus grande partie de la section de la petite roue par rapport à la grande. Il vaut
donc mieux utiliser une pompe à roues avec des ailes moins nombreuses mais plus
longues. Dans les roues à grande vitesse spécifique et à surface d’aile réduite pour
diminuer la perte de charge, la pression spécifique sur les ailes est importante, d’où
une dépression élevée sur une grande longueur d’aile, ce qui favorise la cavitation [de
Kovats et Desmur, 1971] p. 70.
Avec nos notations, la condition de non-cavitation s’écrit :
Hmin = He −λv2
relative
2g
= Hatm −Hasp −v2
e
2g −λv2
relative
2g
> Hvapeur
On peut définir en tout point d’un circuit hydraulique la hauteur d’aspiration disponible
, en anglais NPSH pour Net Positive Suction Head, qui correspond à l’écart
entre pression exprimée en mètres de colonne d’eau et Hvapeur. Tant que la NPSH

<!-- page 338 (PDF 354) -->
Photo 3.6 – Mesure expérimentale de la cavitation sur une aube (tiré de Dorey et
al., op. cit.)
Fig. 3.44 – Zone de fonctionnement autorisée des pompes primaires. La limite à
27 bars est consécutive à la tenue des joints à basse pression.

<!-- page 339 (PDF 355) -->
Photo 3.7 – Une impressionnante photo des effets de la cavitation sur une surface
interne de pompe en bronze (tirée de [de Kovats et Desmur, 1971] p. 69).
est positive, on évite la cavitation. On parle de NPSH disponible si la colonne d’eau
à aspirer est immobile (comme dans un tube vertical par exemple). Dans le cadre
d’un liquide en mouvement possédant un débit comme dans une pompe, il faut
une dépression supplémentaire pour aspirer l’eau, on parle de NPSH requis qui est
une caractéristique de la pompe, classiquement fournie par le fabricant de la pompe
(Figure 3.45).
NPSHrequis ≡v2
e
2g + λv2
relative
2g
Au final, la condition de non-cavitation s’écrit :
NPSHdisponible ≡Hatm −Hasp −Hvapeur > NPSHrequis
En théorie, c’est le nombre de Thomas, appelé aussi indice de cavitation, qui rend
compte pour un écoulement donné du développement de la cavitation au sein de
l’écoulement 23 :
σ[−] ≡P −Psat
2ρV 2
Dans cette formule, P est la pression, V la vitesse de l’écoulement local, Psat la pression
de vapeur saturante et ρ la masse volumique de l’eau. Ce nombre adimensionnel
permet de faire des études en similitude de façon correcte, mais avec des écarts dus au
type de cavitation : cavitation de poche liée au développement de la couche limite ou
Jean-Marc Dorey, M. Caulier : L’érosion par cavitation, Séminaire EDF de mécanique des
structures, Milly-la-Forêt, 25 et 26 avril 1990, 1990.

<!-- page 340 (PDF 356) -->
Photo 3.8 – Effets intenses d’érosion par cavitation dans une pompe (tiré de
Dorey et al., op. cit.)
g
ve
g
vrelative
requis
NPSH
H
Débit
Q
Fig. 3.45 – Caractéristique d’une pompe : hauteur en fonction du débit.
cavitation par bulles par présence de germes de cavitation. Mais plusieurs grandeurs
dérivées plus pertinentes sont proposées selon le type d’organe :
σ[−] ≡NP SH
V 2
g
pour les pompes.
σ[−] ≡
Haspiration−Psat
ρg
H
avec H la hauteur de chute et Haspiration la hauteur à
l’aspiration pour une turbine.
σ[−] ≡Paval−Psat
ΔP
pour les organes de pertes de charge.

<!-- page 341 (PDF 357) -->
Pour une valeur σ donnée, la taille des structures de vapeur est fixée et leur nombre
est proportionnel à la vitesse. L’effondrement des structures de vapeur (implosion) et
la transformation en impulsions subies par la paroi sont un problème très complexe
pas encore parfaitement élucidé. Tout au plus, on sait que c’est la pression à implosion
qui gouverne le phénomène. Les vitesses de fluide en fin d’implosion sont de l’ordre
de ≈10
□
(P −Psat) /ρ, ce qui conduit à des vitesses de l’ordre de 100 m/s pour une
surpression d’à peine 1 bar. On comprend alors la violence du phénomène pour des
surpressions supérieures. Il y a alors émission d’une onde de choc à la paroi de quelque
2 000 bars pendant quelques microsecondes ! Ces ordres de grandeurs sont accrédités
par des mesures expérimentales, qui confirment la multitude de sollicitations très
ponctuelles et très courtes. L’attaque des parois peut créer des déformations visibles
à l’œil nu de quelques millimètres. Dans la pratique, la vitesse de perte de masse est
d’abord nulle (phase d’incubation) car le matériau encaisse les impacts et se plastifie
sans perte de masse. Puis la vitesse augmente rapidement (phase d’accélération) pour
saturer à une vitesse de perte de masse constante (phase asymptotique). Le phénomène
de cavitation s’accompagne de bruit et de vibrations qui quantifient l’agressivité du
phénomène. Chaque pompe est équipée de deux chaînes de mesure de vibrations qui
déclenchent des alarmes en cas de vibration excessive, synonyme de défaut interne ou
de cavitation.
D’une manière générale, on arrête les pompes primaires dès que la pression est
inférieure à 88 bars absolus, synonyme d’un APRP. On limite ainsi les problèmes de
cavitation, et surtout on évite de pomper de l’eau liquide vers la brèche, limitant
ainsi un dénoyage important du cœur lors d’une petite brèche. Au démarrage, pour
des problèmes de joints tournants (en particulier le joint n◦1 hydrodynamique à fuite
contrôlée qui nécessite une certaine pression pour « décoller » avec un différentiel de
pression de 19 bars, soit 27 bars au primaire), il faut que quelle que soit la température,
la pression soit donc supérieure à 27 bars, pression située en dessous de la pression de
déconnexion du RRA (32 bars).
Tant que les pompes primaires tournent, il n’y a pas de dénoyage du cœur et,
même en cas d’écoulement diphasique, le débit est suffisant pour refroidir le cœur. Les
analyses historiques de Westinghouse montrent qu’on a intérêt à arrêter les pompes
dans tous les cas lorsque la détection de l’APRP est confirmée.

### 3.10.8 Risque d’incendie des pompes primaires

Les pompes primaires sont des composants qui cumulent friction des paliers et joints,
haute température et présence de courant électrique. Les paliers de moteurs sont lubrifiés
à l’huile et le circuit d’huile comprend un groupe d’injection d’huile, les cuves
d’huile des paliers supérieur et inférieur, les échangeurs de chaleur d’une capacité
d’environ 1 120 litres d’huile (CPY). Un défaut de refroidissement quelconque peut
rapidement amener un incendie d’huile. Les locaux des casemates des pompes primaires
sont munis de dispositifs de détection d’incendie (un incendie d’huile génère
rapidement une intense fumée) et de dispositifs fixes d’aspersion alimentés par le circuit
de protection incendie de l’îlot nucléaire JPI. Pour éviter une propagation de
l’incendie aux câbles, on veille à bien séparer physiquement les câbles de puissance,
de contrôle et de mesure.

<!-- page 342 (PDF 358) -->
### 3.10.9 Surveillance des pompes primaires

Chaque pompe primaire dispose d’une instrumentation de mesure des températures
d’eau (au niveau du palier et au niveau du premier joint), de température du corps
de pompe (palier supérieur, inférieur, patins de butée axiale supérieur, inférieur),
de température de l’enroulement stator, de la pression et température d’huile, qui
renseignent l’opérateur en salle de commande. Celui-ci devra arrêter la pompe sur
signal « très haute température ». On mesure aussi la vibration des pompes par
des capteurs montés sur la bride inférieure du support-moteur, avec une mesure de
déplacement d’arbre de pompe. Une mesure très importante est la mesure de la vitesse
par deux capteurs avec commutateur de transfert d’un capteur sur l’autre pour plus
de fiabilité. Cette mesure est utilisée par les chaînes de protection contre d’éventuelles
variations de tension ou de fréquence du réseau. La mesure est basée sur le principe
de la détection d’un ergot placé sur l’arbre et qui délivre une impulsion au détecteur
à chaque passage, le signal étant ensuite traité par un tachymètre électronique. En
fonction des vitesses mesurées, le système fournit un signal d’îlotage, voire un signal
d’AAR, qu’on détaille dans le paragraphe suivant.
Les mesures des débits d’injection et de fuite au premier joint permettent d’élaborer
un signal « bas débit au joint » ou un signal « très bas débit au joint » qui
verrouille le démarrage de la pompe si celle-ci n’était pas en service.
Le débit des pompes primaires doit se situer entre le débit hydraulique de conception
, qui provient du dimensionnement de refroidissement nécessaire du cœur, et le
débit mécanique de conception, valeur pour laquelle sont effectués les calculs de tenue
des assemblages et des équipements internes de la cuve (force d’envol de la poussée
hydraulique contrée par le poids et les calages supérieurs). On a eu à ce sujet des
surprises au démarrage du palier N4 (Chooz B1) pour lequel les GMPPs étaient de
conception purement française. En effet, on a constaté un sur-débit lié à une augmentation
de la hauteur manométrique des pompes, provoqué par la physico-chimie de
l’eau et l’évolution de l’état de surface interne des pompes, un phénomène constaté
à l’international mais de plus faible ampleur jusqu’alors. La valeur finale reste quand
même en deçà du débit mécanique de conception. Pour garantir cette limite, on a
installé en salle de commande un système de surveillance avec alarmes scrutant le
débit dans la cuve. Cet événement montre qu’il y a toujours un risque à s’écarter d’un
design connu et qui a fait ses preuves.
D’une manière générale, les pompes primaires se sont révélées être des composants
très fiables, provoquant une indisponibilité d’à peine 10 à 20 heures par tranche et
par an [Hutin, 2016] p. 456, ce qui est objectivement très faible, dont une large part
est due à des erreurs humaines au remontage après inspection.

### 3.10.10 Protection contre le bas débit primaire

La baisse du débit primaire peut avoir des conséquences très fâcheuses sur le rapport
de flux critique. Cette baisse peut avoir deux causes : d’une part une baisse de
la fréquence du courant ou de la tension, consécutif à un incident sur le réseau de
transport électrique, d’autre part une cause mécanique sur la pompe elle-même. On
attend des pompes primaires qu’elles puissent fonctionner jusqu’à 47 hertz, et qu’elles
acceptent les incidents fugitifs de perte de réseau. Le système de protection initial du
palier CP0 conduisait à une séparation du réseau en dessous de 48 hertz ou lorsque

<!-- page 343 (PDF 359) -->
la tension reste en dessous de 0,7 fois la tension nominale pendant un temps cumulé
de 0,9 seconde pour une période de 2 secondes (la tension de décrochage des pompes
primaires est d’environ 0,55 Unorm). Ces critères historiques, basés sur les travaux de
la licence Westinghouse, sont finalement mal adaptés aux besoins de sûreté réels, qui
portent en fait sur le débit primaire. Celui-ci est en fait une fonction complexe de la
fréquence et de la tension aux bornes de la pompe. C’est pourquoi il est plus judicieux
de mesurer le débit réel des pompes pour renseigner le système de protection.
Si on analyse les différentes classes d’incidents pouvant survenir, on décompte les
transitoires de classe 1, en l’occurrence des perturbations fugitives pouvant annuler
éventuellement la tension, mais dont la durée est limitée par les protections du réseau
(1 à 2 secondes), et dont la présence d’un volant d’inertie conséquent sur les
pompes permet l’innocuité. Certaines perturbations plus longues liées au déséquilibre
entre production et consommation, se traduisent par une variation de fréquence évoluant
entre 47 hertz (surconsommation) et 51 hertz (surproduction) et une tension
comprise entre 0,9 et 1,1 la tension normale. Ces transitoires ne doivent pas voir la
centrale coupée du réseau par ses protections. Pour des transitoires de classe 2 qui
vont au-delà des limites de la classe 1, la tranche doit pouvoir être îlotée pour s’autoalimenter
, c’est-à-dire subir une baisse de charge (îlotage) rapide jusqu’au minimum
technique (environ 30 % Pnom). La persistance du défaut doit conduire à un AAR.
Les transitoires de classe 3 induisent une diminution de débit correspondant à un
taux de ralentissement de 5 à 8 %/s (soit –4 hertz/s correspondant à un taux de ralentissement
à couple moteur nul, c’est-à-dire admission vapeur coupée, et un couple
résistant maximal (à débit maximal) de la vitesse des pompes. Les transitoires de
classe 4 conduisent à une baisse rapide du débit suite à un blocage de rotor de la
pompe. Dans tous les cas de classe 2 et 3, le RECmin doit toujours être supérieur
à 1,3 avec la corrélation de flux critique initiale de Westinghouse. On admet qu’une
petite proportion de crayons puisse dépasser le flux critique en classe 4. Les critères
de protection bas débit portent aujourd’hui sur le débit de chacune des branches et la
vitesse de chacune des pompes, complémentés par une information sur l’ouverture du
disjoncteur d’alimentation de chaque pompe. Un seuil ωilo sur la vitesse des pompes
permet d’engager l’îlotage sur un critère de logique 2 sur 3 pompes (CPY). Un seuil
ωAAR < ωilo sur la vitesse des pompes permet d’engager l’AAR aussi sur un critère
2 sur 3. La mesure du débit QAAR d’une branche (au-dessus d’un seuil P8 lié au fait
que les pompes primaires sont arrêtées en dessous de 24 bars) permet d’activer l’AAR
en 1/3 (ou 2/3) en fonction du niveau de puissance. La même logique d’engager de
l’AAR porte sur l’état des disjoncteurs de pompes (Figure 3.46).
Notons que la vitesse des pompes intervient aussi dans les chaînes de protections
ΔTtemp´erature et ΔTsurpuissance du CPY.

### 3.10.11 Caractéristiques détaillées d’une pompe primaire

Nous reprenons dans le tableau suivant les caractéristiques détaillées d’une pompe de
type CPY (Tableau 3.3).

<!-- page 344 (PDF 360) -->
Fig. 3.46 – Protection bas-débit d’un réacteur CPY.
