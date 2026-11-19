# Chapitre 6 Le circuit secondaire — 6.4 Le générateur de vapeur côté secondaire — 6.4.4 Le circuit APG de purge des générateurs de vapeur … 6.4.6 Corrosion des tubes GV côté secondaire
<!-- source PDF pages 738-748 -->

<!-- page 722 (PDF 738) -->
### 6.4.4 Le circuit APG de purge des générateurs de vapeur

L’importante recirculation de l’eau au pied du riser et la géométrie spécifique de la
partie basse du GV provoquent une concentration d’impuretés (produits de corrosion,
fuite d’eau brute au condenseur, éventuelles fuites primaires) en pied de faisceau
de tubes. C’est pourquoi un circuit de purge APG permet de soutirer de l’eau du
secondaire en pied de faisceau, de façon continue pour déconcentrer les impuretés. À
la partie inférieure du faisceau sont disposées deux rampes tubulaires destinées à la
vidange et à la purge continue des matières dissoutes dans l’eau du secondaire. C’est
aussi en partie inférieure que sont situés deux « trous de poing » (Photo 6.3) qui
permettent une inspection visuelle de la face supérieure des GVs et un nettoyage par
lançage de produits chimiques. Cette eau prélevée, après refroidissement au travers
d’un échangeur avec le RRI, est directement envoyée au circuit de rejet TER si elle
n’est pas radioactive (par contrôle via le REN), ou filtrée et déminéralisée auparavant
(Figure 6.29).
Photo 6.3 – Serrage de couvercle de trou de poing de GV (SKF).
Le rôle du circuit APG est de purger en continu et à débit variable de l’eau
du secondaire au-dessus de la plaque tubulaire, de refroidir cette purge par le RRI
(< 60 ◦C pour un fonctionnement correct des déminéraliseurs) et de détendre l’eau
ainsi purgée, de la purifier avant son renvoi dans le condenseur. Des dérivations
permettent d’assurer certaines fonctions auxiliaires : vidange de la partie secondaire
des GVs si besoin, soutirage permanent de l’eau pour échantillonnage, alimentation en
azote de brassage des réactifs chimiques de l’eau des GVs lorsque ceux-ci sont en stockage
de longue durée, recyclage des effluents d’échantillonnage provenant du REN
et non pollués chimiquement. Le débit de purge est de 50 tonnes/h pour le CPY,
80 tonnes/h pour le 1 300 MWe, 87 tonnes/h pour le N4, soit 1 % du débit d’eau
alimentaire.
Le contrôle en continu de la conductivité cationique des purges et de leurs concentrations
en sodium fournit un indicateur essentiel de la pollution du circuit eau-vapeur,
puisque c’est dans le GV que les polluants se concentrent. Si les mesures indiquent
une pollution importante, on est amené à baisser la charge, ce qui amènera à un relâchement
des polluants stockés dans les GVs (nous reviendrons sur ce phénomène dans

<!-- page 723 (PDF 739) -->
Fig. 6.29 – Traitement des purges APG (CPY) (adapté de [Stockage et traitement
des effluents, 1977], p. 38).
le chapitre sur la corrosion du secondaire). Un niveau de pollution qui continuerait à
augmenter est un indicateur d’une entrée d’eau brute dans le secondaire.

### 6.4.5 Éléments de thermohydraulique d’un générateur de vapeur

On peut séparer un générateur de vapeur de type REP en plusieurs zones distinctes
selon l’altimétrie d’un GV (Figure 6.31) : le down-comer annulaire qui voit le fluide
secondaire descendre autour du faisceau tubulaire, le faisceau tubulaire central qui
contient les tubes GV, le cyclone dont la fonction est de séparer l’eau de la vapeur,
le dôme du GV. En indiçant les grandeurs par les acronymes traditionnels, on peut
écrire les différents bilans pour chacune des zones 9 :
dmDC
dt
= WF eed + (1 −XCycl) Wvap,Cycl −WDC
Équation 1 : Bilan de masse du down-comer
dmDChDC
dt
= WF eedhF eed + (1 −XCycl) Wvap,CyclhCycl −WDChDC −pvap
dVliq,DC
dt
Équation 2 : Bilan d’énergie du down-comer
9 Mankit Ray Yeung, Ping Lam Chan : Development and validation of a steam generator simulation
model, Nuclear Technology, Vol. 92, pp. 309-314 (1990).

<!-- page 724 (PDF 740) -->
XCycl est la qualité de la vapeur à la sortie du cyclone, pvap la pression de vapeur
et Vliq,DC le volume de liquide dans le down-comer. Dans le faisceau tubulaire, les
variations des masses liquide et vapeur sont liées par les débits d’entrée et de sortie
et le débit de vaporisation :
dmliq,fasiceau
dt
= Wliq,in −Wliq,outl −Wvaporisation
Équation 3 : Bilan de masse liquide du faisceau
dmvap,fasiceau
dt
= Wvap,in −Wvap,outl −Wvaporisation
Équation 4 : Bilan de masse vapeur du faisceau
Pour le bilan d’énergie, on calcule la variation d’enthalpie du mélange m :
dmm,fasiceauhm,fasiceau
dt
= Wm (hin −hout) + ΦAfasiceau −qdrift
Équation 5 : Bilan d’énergie du faisceau
Φ est le flux transféré du primaire au secondaire, on le calcule en fonction de
l’écart de température entre primaire et secondaire, qu’on peut affiner en discrétisant
la longueur des tubes :
ΦAfasiceau ≡hsimplephase (Tprimaire −Tsecondaire) + hdoublephase (Tprimaire −Tsecondaire)
Afasiceau est la section d’échange du faisceau et qdrift est modélisé par un modèle
de drift-flux, classiquement du type :
qdrift = V hliq/vap
vliqvvap
∂
∂z
□α
ρ [(C0 −1j + Vvap,j)]
□
Les coefficients d’échange simple phase et double phase tiennent compte de la conductivité
du métal du tube GV (de rayon extérieur re et de rayon intérieur ri) et des
coefficients d’échange côté secondaire (convection forcée et ébullition nucléée) et côté
primaire (convection forcée simple phase en régime nominal modélisée par la corrélation
de Dittus-Boelter, double phase en condition accidentelle par la corrélation de
Chen ou de Thom par exemple) :
h =
re
ri
hprimaire
+
re
km´etal
Log re
ri
+
hsecondaire
Rappelons que la corrélation de Dittus-Boelter pour les échanges monophasiques turbulents
à la paroi s’écrit :
hDittus−Boelter[W/m2/K]
=
0, 023 × Re0,8 × Pr0,4 ×
kH2O
Dhydraulique
et
Φ
=
hDittus−Boelter × (Tparoi −Tfluide)
Le liquide entre dans le riser du GV à l’état sous-saturé et est d’abord réchauffé
dans le bas du riser par la partie montante des épingles qu’on appelle classiquement

<!-- page 725 (PDF 741) -->
« jambe chaude » (la partie descendante où l’eau du primaire est plus froide, est appelée
« jambe froide », le distinguo entre partie montante et descendante est relativement
arbitraire), où on peut appliquer la corrélation de Dittus-Boelter (cette hauteur de
chauffe dépend de la charge). Ensuite commence la zone d’ébullition nucléée saturée,
où on peut appliquer des corrélations comme Jens et Lotte, Thom, Chen. . .
Thom modélise l’échange à la paroi avec le fluide saturé par un coefficient
d’échange de la forme :
hT hom[W/m2/K2] = 1975 × e
Pbars
43,43 etΦ = hT hom × (Tparoi −Tsat)2
Pour l’Inconel 600 des épingles primaires, la conductivité du métal est donnée par :
kInconel600[W/m/K2] = 14, 334 + 0, 0148 × Tparoi[ ◦C]
À comparer avec la valeur de la conductivité d’un acier standard :
kInconel600[W/m/K] ≈45W/m/K
On trouvera dans [Incropera et De Witt, 1996] le détail des corrélations précitées.
Dans le riser, se produit un glissement entre la phase vapeur et le liquide, la vapeur
montant plus vite que le liquide. Ce glissement est limité par l’effet de mélange des
plaques entretoises qui tiennent le faisceau d’épingles (Figure 6.30).
Par contre, après la dernière entretoise et les séparateurs cyclones, ce glissement
devient prépondérant. On modélise classiquement le glissement entre phases dans le
GV par la corrélation d’Armand-Masséna donnée par ;
γ ≡Vg
Vl
= 1
K + 1 −K
K
ρl
ρg
X
1 −X
Où Vg est la vitesse du gaz, Vl est la vitesse du liquide, ρg la masse volumique du gaz,
ρl la masse volumique du liquide, X le titre en vapeur et K le paramètre de Bankoff
tel que :
K ≡0, 833 + 0, 167 × X
Avec cette corrélation, le taux de vide est donné par :
α ≡
KXVg
XVg + (1 −X) Vl
Il existe une corrélation dite « Armand-Masséna » modifiée où on apporte des corrections
sur le taux de vide en multipliant le taux de vide par une fonction corrective
dépendant du titre :
α ≡
KXVg
XVg + (1 −X) Vl
×
⎧
⎪
⎪
⎨
⎪
⎪
⎩
−79, 719X3 −62, 181X2 −7, 533X + 1
si
X < 0, 15
−22, 649X2 −6, 221X + 1, 424
si
0, 15 ≤X < 0, 186
19, 766X2 + 9, 305X + 0, 003
si
0, 186 ≤X < 0, 25
−0, 125X + 1, 125
si
0, 25 ≤X
La vapeur dans le dôme doit être traitée comme un fluide compressible :
dmvap,dome
dt
= dρvap,domeVvap,dome
dt
= Wvap,cyclXcycl −Wvap,dome
Équation 6 : Bilan de masse du dôme

<!-- page 726 (PDF 742) -->
Fig. 6.30 – Différents types de plaques entretoises dans les GVs (d’après Bilan du
développement et de l’exploitation des générateurs de vapeur EDF, comité de gestion prévisionnelle
, Commission scientifique et technique, 1986). Les plaques entretoises supérieures
subissent un phénomène de corrosion-érosion avec pertes de matière au niveau des trous de
circulation du fluide. Par calcul, on peut accéder, de façon satisfaisante par rapport aux
mesures, à la vitesse de corrosion au niveau des plaques en fonction des vitesses liquides,
du titre en vapeur et du conditionnement de l’eau secondaire (ammoniaque, hydrazine et
morpholine).
dmvap,domehvp,dome
dt
=
Wvap,cyclXcyclhvap,cycl −Wvap,domehvap,dome
−pvap,dome
dVvap,dome
dt
Équation 7 : Bilan d’énergie du dôme
Le débit de vapeur sortant du dôme vers la turbine peut être modélisé par une loi
de perte de charge :
Wvap,dome = K
□
pdome −pturbine
vvap,dome

<!-- page 727 (PDF 743) -->
Fig. 6.31 – Altimétrie d’un GV de réacteur CP0.

### 6.4.6 Corrosion des tubes GV côté secondaire

[Bénard et al., 1984]
Le GV, en tant que siège des échanges de chaleur entre primaire et secondaire, voit
la concentration de certaines espèces chimiques augmenter, d’une part du fait de la
vaporisation associée à un coefficient de partage 10 sélectif entre la phase liquide du
secondaire et la phase vapeur (les principaux polluants comme le sel NaCl ou la soude
10 Le coefficient de partage est défini comme le rapport entre la concentration du polluant dans
la phase vapeur et celle dans l’eau. Ce coefficient est de l’ordre de 10−4 pour les sels et les espèces
fortement ionisées, ce qui signifie que ces impuretés restent massivement dans l’eau. En tenant
compte des débits respectifs, la concentration des polluants dans l’eau du GV est environ 10 fois plus
importante que dans celle de l’ARE, rien que par l’effet de vaporisation.

<!-- page 728 (PDF 744) -->
Fig. 6.32 – Surconcentration des polluants dans le GV (adapté de F. Nordmann,
EDF).
NaOH étant plus ou moins solubles dans l’eau et très peu solubles dans la vapeur),
d’autre part à cause des phénomènes de surchauffe locale en zone de circulation réduite
mettant en œuvre l’ébullioscopie, à savoir le fait qu’à une pression donnée, l’ajout
d’un polluant chimique dans l’eau augmente la température d’ébullition par rapport
à l’eau pure (Figure 6.32). La surchauffe locale et l’ébullioscopie concentrent de façon
très importante les impuretés près de la paroi chauffante par rapport à la purge.
Des facteurs de concentration jusqu’à un million peuvent apparaître dans les zones
confinées comme en pied de tube GV ou au niveau des strictions de passage des
entretoises (soude jusqu’à 500 g/L au niveau de la 1re et 2nde entretoise !), et jusqu’à
100 pour un tube libre.
On constate expérimentalement que la montée en charge s’accompagne d’une
baisse de la quantité de sels présents dans l’eau, ce qui suggère un phénomène de
séquestration par précipitation des sels dans les interstices et les zones encaissées
(zones de boues contenant du CuO, PbO2, Fe2O3). Le phénomène inverse de relâchement
apparaît quand la charge baisse. Les fortes concentrations locales de soude
(10 g/kg d’eau) vont provoquer de la corrosion intergranulaire induisant des fissures
de plusieurs centaines de microns en à peine 1 000 heures de fonctionnement. Ces
fortes concentrations ne sont pas forcément vues par l’analyse chimique des purges.

<!-- page 729 (PDF 745) -->
Par contre, un fort relâchement pendant une phase de baisse de charge pour atteindre
une attente à chaud indique qu’il faut rester à l’arrêt jusqu’à élimination des polluants.
Malgré le choix de l’Inconel 600 comme matériau de tube, il est rapidement apparu
de nombreux incidents dus à la corrosion sous contrainte, appelée aussi « corrosion
sous tension », ou effet Coriou, déjà vu côté primaire 11. Cette corrosion se caractérise
par une fissuration sous l’action combinée de contraintes en extension et d’un milieu
corrosif, qui peut même être de l’eau pure. Cette corrosion peut être spectaculairement
rapide, et a impacté l’industrie nucléaire à la fin des années 1970 12.
En face interne des tubes, le conditionnement de l’eau primaire fait intervenir
du bore (entre 0 et 2 500 ppm pour le contrôle neutronique), de la lithine (environ
1,5 ppm, limitant les dépôts de produits de corrosion) conduit à un pH légèrement
alcalin. Notons qu’on introduit en plus de l’hydrogène (environ 30 cm3/kg d’eau à
TPN) pour éliminer la teneur en oxygène libre (très oxydant) et pour limiter l’effet
de la réaction de radiolyse de l’eau (qui produit de l’oxygène libre). En face externe
côté secondaire, l’introduction d’ions chlorure lors d’entrée d’eau brute au condenseur,
un événement relativement fréquent, faisait qu’on traitait jusqu’en 1974 le circuit
secondaire avec du phosphate di- ou tri-sodique (de même que dans les tranches
thermiques conventionnelles). Ce phosphate de sodium avait pour but de réduire la
corrosion des aciers noirs, d’éviter les dépôts de sels de calcium insolubles et agissait
comme tamponnage chimique de l’eau. Ce traitement a ensuite été abandonné car il
pouvait conduire à l’apparition de phosphate acide ou bien de soude libre exacerbant la
corrosion des fissures, et dans tous les cas une difficulté à contrôler la concentration en
ion sodium. On a donc préféré au phosphate de l’ammoniaque puis de la morpholine,
avec de l’hydrazine 13 pour réduire la concentration en oxygène.
L’Inconel 600, riche en nickel, est plus résistant à la corrosion que les aciers inoxydables
standards. D’où sa généralisation dans les premiers types de GVs en remplacement
de l’acier inoxydable non allié au nickel. Pourtant, dès 1959 14, Henri Coriou et
des chercheurs en laboratoire (CEA) se sont aperçus que l’Inconel 600 restait sensible
à la corrosion intergranulaire sous contrainte vers 300 ◦C, même avec de l’eau déminéralisée
. La période « d’incubation » peut être longue et l’ajout de lithine retarde
le phénomène. Par contre, la présence de soude augmente la sensibilité à la fissuration
intergranulaire de l’Inconel 600. La cinétique de corrosion est estimée entre 0,004
micron/heure et 0,04 micron/heure selon le pH et la teneur en sulfate.
11 René Boudot, Denis Buisine, François Vaillant : La corrosion de l’alliage 600, EPURE, n ◦44,
octobre 1994, pp. 72-78.
12 Henri Coriou : Les problèmes de corrosion localisée dans les réacteurs à eau légère, 22nd Nuclear
Congress of Rome, Italy, 24-25 March 1977, CEA-CONF-3949, pp. 1-23.
13 L’hydrazine est un liquide incolore de formule H2N-NH2, dont le point d’ébullition est de
113, 5 ◦C, légèrement plus dense que l’eau. Découvert en 1889 par Julius Wilhelm Theodor Curtius
1857-1928, professeur de chimie à l’université d’Heidelberg, l’hydrazine est produit par oxydation de
l’ammoniac par l’hypochlorite de sodium, et enfin par distillation. L’hydrazine est un puissant réducteur
, utilisé comme réactif dans l’industrie chimique, et pour réduire de faibles quantités d’oxygène
dissoutes dans les eaux de chaudières, dont les chaudières nucléaires. L’hydrazine est aussi utilisé
comme combustible pour moteurs de missile, car on le fait réagir avec de l’oxygène liquide ou du
péroxyde d’hydrogène (eau oxygénée).
14 H. Coriou, L. Grall, Y. Le Gall, S. Vettier : Corrosion sous contrainte de l’Inconel dans l’eau
à haute température, 3e colloque de métallurgie sur la corrosion, Saclay, North Holland Publishing,
Amsterdam, pp. 161-169, 1959. Voir aussi le rapport CEA des mêmes auteurs reprenant la publication
en congrès : Corrosion fissurante sous contrainte de l’Inconel dans l’eau à haute température, rapport
CEA n ◦1521, 1960.

<!-- page 730 (PDF 746) -->
La première fissuration d’un tube en Inconel 600 est apparue dans le réacteur suédois
d’Agesta dès 1966. Les premières fuites sérieuses (300 l/heure), avec des fissures
initiées côté secondaire situées 2 cm au-dessus de la plaque tubulaire, ont eu lieu dans
le réacteur de Connecticut Yankee aux États-Unis en 1970. On citera aussi le réacteur
de Beznau 1 (365 MWe, 1969, Suisse), où en août 1971, plusieurs fuites ont été détectées
, localisées dans des zones à présence de fortes bases et de dépôts importants de
magnétite. En décembre 1971, jusqu’à 20 % des tubes des deux GVs révélaient des fissures
traversantes par examen aux courants de Foucault ! Fissures toujours localisées
juste au-dessus de la plaque tubulaire en pied côté chaud de tube. Sur les premières
tranches françaises, conscient du fait que les dépôts au-dessus de la plaque tubulaire
étaient la principale cause de corrosion, on a amélioré la géométrie autour des pieds
de tube, pour augmenter la circulation de l’eau en pied et éviter toute zone stagnante
(suppression d’ouvertures en partie basse de la chemise du faisceau, augmentation de
la recirculation en supprimant les plaques diaphragmées dans le down-comer, modification
des prises de purges pour les rendre plus efficaces, chemise de faisceau abaissée
pour augmenter la vitesse latérale de pénétration de l’eau dans le riser. . . ).
D’autre part, des problèmes de fissuration des tubes sont clairement apparus sur
le palier P4, avec des solutions apportées sur les méthodes de dudgeonnage des pieds
de tubes, et le passage à l’Inconel 690 (NC 30 Fe) 15, très peu sensible à la corrosion,
car mieux protégé par sa haute teneur en chrome, pour le palier N4.
La striction des tubes GV au droit des plaques entretoises (phénomène appelé
« denting », Figure 6.33), est apparue sur les GVs dont les plaques étaient en acier au
carbone. On constate un étranglement progressif du tube par effet mécanique lié à la
formation d’oxyde se développant autour du trou de la plaque entretoise. L’oxyde a
un volume plus important que l’acier de base, ce qui comprime le tube GV. La parade
à ce problème a consisté à utiliser pour les plaques entretoises un acier plus résistant
à la corrosion (13 % de chrome), et des trous de passage des tubes GV en forme de
feuille de trèfle, obtenus par brochage. Cette forme assure un balayage plus intense
de l’eau secondaire au droit du tube.
De l’accumulation de boues, principalement constituées de magnétite (Fe3O4),
apparaît dans la zone à basse vitesse de la jambe chaude côté secondaire. Ces boues
activent une corrosion en pied de tube. La solution à ce problème est d’optimiser
la géométrie de cette zone pour augmenter les vitesses locales de l’eau secondaire
par l’installation d’une plaque de répartition de débit. Des pratiques de nettoyage
par « lançage » par effet karcher (Figure 6.34) ou attaque chimique permettent de
nettoyer ces zones pendant les arrêts.
Le nettoyage chimique des GVs (6.14.2) a été rendu nécessaire pour attaquer
les dépôts locaux de produits de corrosion 16. Ces dépôts conduisent à des zones
d’ébullition sous dépôts qui forment des milieux chimiques concentrés, très agressifs
et corrodants, en particulier sur l’Inconel 600. EDF a mis au point un procédé chimique
qui comprend plusieurs phases successives. En premier lieu, une dissolution des oxydes
15 Quelques propriétés de base : Rp 0,2 (20 ◦C) >
275, Rp 0,2 (35 ◦C) >
215, Rm (20 ◦C)
> 630, A % > 30.
16 Didier Noel, Henri-Bernard Psychala, Jean-Marie Fiquet : Le nettoyage chimique des générateurs
de vapeur, EPURE, n ◦44, octobre 1994, pp. 46-54.

<!-- page 731 (PDF 747) -->
Fig. 6.33 – Effet de « denting » sur un tube GV.
de fer et de zinc par de l’acide citrique 17 et gluconique 18 à pH 3,3 à 85 ◦C sous azote
(au moins 170 heures). Puis une dissolution du cuivre par une solution identique
à celle utilisée précédemment, mais alcalinisée à PH > 9,5 et rendue oxydante par
bullage d’oxygène, à 50 ◦C (au moins 20 heures). Enfin, une solution de finition
d’acide citrique à pH 3,5 inhibée pour éliminer le souffre contenu dans l’inhibiteur
de la solution précédente pendant 5 heures à 40 ◦C. Cette phase acide est suivie
d’une phase basique pour un deuxième décuivrage et pré-passivation avec une solution
alcaline à pH > 9,5, rendue oxydante par bullage d’oxygène (5 heures à 40 ◦C). Le
tout avant rinçage. Cette tactique est très efficace comme le montre la Photo 6.4. Elle
a été mise en place industriellement à partir de 1988 sur une centrale en Belgique,
puis en France.
17 L’acide citrique (C6H8O7) est un acide faible qu’on trouve dans le citron (d’où son nom), isolé
en 1784 par le chimiste suédois Carl Sheele, dont l’action détartrante est bien connue des ménagères.
18 L’acide gluconique (C6H12O7) est un acide soluble dans l’eau très répandu aussi bien chez les
animaux que dans les plantes. Il est le plus souvent intégré dans une molécule plus grande comme
c’est le cas dans diverses gommes (Wikipédia).

<!-- page 732 (PDF 748) -->
Fig. 6.34 – Nettoyage des dépôts de magnétite du secondaire d’un GV par lançage
(technique Framatome). On injecte de l’eau à haute pression (200 bars) par des orifices
d’inspection.
Photo 6.4 – Nettoyage chimique du GV : avant (gauche), après (droite) (d’après
Noel et al., op. cit.).
