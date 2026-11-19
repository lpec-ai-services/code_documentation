# Chapitre 6 Le circuit secondaire — 6.8 Le condenseur — 6.8.6 Principe physique du condenseur … 6.8.7 Les pompes d’extraction du condenseur
<!-- source PDF pages 793-801 -->

<!-- page 777 (PDF 793) -->
Tab. 6.6 – Type de condenseur par palier. Les tubes en laiton imposent un conditionnement
à la morpholine à bas pH, ce qui est plutôt mauvais vis-à-vis du risque de colmatage
des GVs [Hutin, 2016] p. 600. A contrario, des tubes en titane ou en inox permettent un
conditionnement à fort pH, plus propice aux GVs, mais pouvant exacerber des problèmes de
corrosion. Le laiton semble le matériau présentant au final le plus de problèmes (relâchement
de cuivre vers les GVs, corrosion-érosion. . . ). Par contre, le cuivre du laiton a des propriétés
bactéricides intéressantes si on ne veut pas rajouter un additif bactéricide qu’on retrouverait
aux rejets.
CP1
CP2
P4-P’4
N4
Volume de la cavité (m3)
2 500
2 500
3 130
7 10034
Nombre de tubes échangeurs
74 004
72 032
95 208
128 856
Longueur des tubes échangeurs
(m)
10,818
14,656
14,412
15,000
Diamètre externe des tubes
(mm)
Épaisseur des tubes (mm)
0,5
1,0
0,5
0,5
Matériau des tubes
Titane35
Laiton 70/30
Titane
Inox 304L
Masse volumique (kg/m3)
7 900
8 500
7 900
7 900
Capacité thermique (J/kg)
Conductivité thermique
(W/m/K)
34Incluant les tuyauteries de liaison moyenne pression vers basse pression.
35Le titane résiste bien à la corrosion de l’eau de mer (centrale sur mer), mais est un mauvais
conducteur thermique, ce qui impose une faible épaisseur de tube (0,5 à 0,7 mm). Le risque
d’incendie du titane est aussi à prendre en compte (lors des opérations de retubage par
exemple).
de retour vers l’arrêt à froid, d’atteindre la connexion au RRA (32 bars au primaire).
Bien entendu, la seule contrainte est que le condenseur, et d’une manière générale le
circuit CEX, soient disponibles. Nous reviendrons par la suite sur le contournement
total de la turbine et la décharge à l’atmosphère (GCTa).
La vapeur provient du barillet GV d’où partent les tuyauteries d’alimentation
normale de la turbine, et deux collecteurs de contournement (avec désurchauffe ou
sans désurchauffe). Chaque collecteur se divise en 2 voies, puis chaque voie se répartit
en 4 soupapes de réglage de débit (Figure 6.76). La vapeur pénètre ensuite dans les
caissons de détente (Figure 6.77, Figure 6.78) situés dans la manchette du condenseur.

### 6.8.6 Principe physique du condenseur

Au niveau de la physique, il y a quatre grands phénomènes à prendre en compte. D’une
part la thermohydraulique du mélange vapeur et eau condensée dans la cavité de la
cuve du condenseur. Ensuite la thermohydraulique du liquide de refroidissement dans
les faisceaux tubulaires, les échanges thermiques à la paroi des faisceaux de tubes, et
enfin la transmission de chaleur à travers les faisceaux.
Dans une approche simplifiée, on peut considérer que la cavité du condenseur est
divisée en deux zones superposées : la zone supérieure qui est occupée par la phase

<!-- page 778 (PDF 794) -->
Fig. 6.76 – Principe du contournement de la turbine vers le condenseur.
vapeur qui doit se condenser au contact de la face externe des faisceaux condenseur,
et la zone inférieure qui est constituée des condensats liquides. On supposera que les
échanges thermiques vers l’extérieur de la cuve du condenseur sont négligeables, qu’il
y a équilibre thermodynamique entre les phases liquide et vapeur, que chaque phase
est homogène en pression et en température et qu’on néglige les incondensables dans
la vapeur d’entrée. Dans ce cas, on peut écrire les équations de conservation des deux
phases :
d(Ml + Mv)
dt
= Wv +WGCT +Wdrainage−Wl out−Wlrgulation−Wvvide+Wrecirculation
(6.1)

<!-- page 779 (PDF 795) -->
Fig. 6.77 – Profil des caissons du condenseur. La manchette du condenseur contient les
caissons de détente de la vapeur. La détente est constituée de deux circuits indépendants :
un circuit avec désurchauffe et un circuit sans désurchauffe. Le circuit avec désurchauffe
comporte deux groupes de 4 soupapes qui débitent dans 4 caissons de détente divisés en
3 étages. Le premier étage (A sur la figure) est constitué d’une chambre cylindrique où on
injecte l’eau de désurchauffe à 2,5 bars (prélevée au refoulement des pompes d’extraction du
condenseur). Le deuxième étage (B) est un caisson rectangulaire gavé par le premier étage
par deux plaques perforées faisant office de diaphragme de détente. Le troisième étage (C)
est un étage de séparation de l’eau situé en dessous des deux autres étages et en liaison
avec l’étage B et avec le condenseur par des ouvertures latérales (pression 0,16 bar avec une
température finale d’entrée au condenseur de 60 ◦C). Le circuit sans désurchauffe comporte
deux groupes de 4 soupapes qui débitent dans 4 caissons cylindriques (adapté de [Circuit
secondaire, 1977]).
d(MlHl+MvHv)
dt
−Vcavit
dp
dt = WvHvout + WGCT HGCT + WdrainageHdrainage
−WloutHl −Wlr´egulationHl −WvvideHv + WrecirculationHrecirculation −Qv→tubes
(6.2)
Dans ces notations, les indices l et v représentent le liquide et la vapeur, H les
enthalpies (J/kg), l’indice GCT indique le contournement turbine, OUT pour la sortie
du condenseur, vide pour le débit de vapeur extrait par la création de vide, drainage est

<!-- page 780 (PDF 796) -->
Fig. 6.78 – Refroidissement du contournement vapeur. Toute la partie inférieure au
contournement sans désurchauffe, est commune avec le refroidissement de la vapeur issue de
la turbine.
autoportant, ainsi que recirculation. La puissance échangée entre le fluide de la cavité
et les parois du faisceau tubulaire est notée Qv→tubes. Par l’hypothèse d’équilibre
thermodynamique entre phases dans la cavité, on déduit que les propriétés liquide et
vapeur sont prises à saturation :
Ml = ρlsatVl
Mv = ρvsat (Vcavite −Vv)
En résolvant ces équations de bilan pas par pas, on peut calculer le volume d’eau
liquide dans la cavité donc son niveau, d’où une gestion possible de la régulation du
niveau d’eau pour ne pas engorger le condenseur.

<!-- page 781 (PDF 797) -->
En ce qui concerne le fluide refroidisseur dans le faisceau tubulaire, on peut considérer
que tous les tubes en parallèle sont représentés par un seul tube équivalent de
section de passage égale à la somme de toutes les sections de chaque tube, d’une
longueur égale à la moyenne de celle des tubes et de même diamètre hydraulique.
On peut aussi supposer que la masse volumique et la pression sont constantes le long
du tube. On discrétise les tubes en un nombre limité de cellules axiales notées i de
longueur L et de volume V (i). Cela se traduit par une modélisation très simple si le
débit est supposé constant pour toutes les cellules axiales d’un même tube :
Wlrefroid(i) = Wlrefroid(i −1) = Wlrefroid
ρlrefroidV (i)dH(i)
dt
= Wlrefroid(H(i −1) −H(i)) + Qirefroid(i)
Le terme Qirefroid(i) est la puissance échangée entre les parois du faisceau et le fluide
de la cellule i. La section droite du tube équivalent est donnée par :
Arefroid = NπR2
internetube
où N est le nombre de tubes.
La chaleur échangée par les parois des tubes respecte la conservation de l’énergie :
Nπ(R2
externetube −R2
internetube)LρtubeCp,tube
dTtube(i)
dt
= Qext(i) −Qint(i)
La puissance échangée avec le fluide de la cellule i de la cavité est donnée par :
Qext(i) = N2πRexternetubeLhext(Tsat −Ttube(i))
La puissance échangée par la paroi du tube de la cellule i avec le fluide refroidisseur
est donnée par :
Qint(i) = N2πRinternetubeLhint(Ttube(i) −Tlrefroid(i))
Tlrefroid(i) est la température moyenne de l’eau de la maille i, dont on peut donner
une bonne approximation par :
Tlrefroid(i) ≡0, 3 × Tlrefroid(i −1) + 0, 7 × Tlrefroid(i)
La corrélation de Dittus-Boelter représente correctement les échanges entre le fluide
de refroidissement et la paroi interne des tubes :
hint = 0, 023Re0,8Pr0,4
λlrefroid
2Rinternetube
λlrefroid est la conductibilité thermique de l’eau de refroidissement en W/m/K. Le
nombre de Reynolds est donné par :
Re = Wlrefroid × 2Rinternetube
πR2
internetube × μlrefroid
Le nombre de Prandtl est donné par :
Pr = ρlrefroid × Cp,lrefroid
λlrefroid

<!-- page 782 (PDF 798) -->
En ce qui concerne le coefficient d’échange entre la paroi externe des tubes et la cavité,
on peut l’approximer par :
hext ≈25000 W/m2/K
On pourra simplifier les calculs en considérant le régime permanent où Qext(i) =
Qint(i), d’où un calcul simple avec des hypothèses réalistes de la puissance échangée
en fonction de la température du fluide de refroidissement et de celle de la cavité.

### 6.8.7 Les pompes d’extraction du condenseur

[Hutin, 2016] p. 631, [Ricard, 1953] p. 385
Les pompes d’extraction du condenseur sont des motopompes qui ont pour fonction
la reprise de l’eau du secondaire condensée en sortie des corps BP de la turbine. Trois
pompes puissantes (environ 3 500 kW par pompe) assurent l’extraction de l’eau secondaire
du condenseur. Il faut avoir en tête que les débits à extraire sont considérables,
de l’ordre de 2 000 m3/h pour un CPY et 2 800 m3/h pour un P4. Comme la pression
dans le condenseur est très basse (de l’ordre de 50 mbar), pour disposer d’un NPSH 36
suffisant, ces pompes sont positionnées dans des puits d’une dizaine de mètres de profondeur
, soit l’équivalent d’environ un bar de pression statique uniquement récupéré
par gravité. Ces pompes se présentent comme un corps d’aspiration avec une roue
double suivi de 4, 5 ou 6 étages de pression identiques. Ces pompes sont basées sur
l’utilisation de bulbes, et d’un étage de refoulement qui intègre le dispositif d’étanchéité
de l’arbre de pompe (Photo 6.9, caractéristiques Tableau 6.7, Figure 6.79).
Les limites maximales des régimes normaux de fonctionnement correspondent aux
situations suivantes avec deux pompes en service (recirculations fermées) et la troisième
en secours (recirculation en service ouvert) :
• un régime nominal, chaudière à 2 905 MWth avec pompe de reprise de condensats
en service ;
• un régime dit « maximal » à 2 905 MWth, débit majoré de 5 % et pompe de
reprise de condensats hors service. Dans ce cas, les purges (surchauffeur. . . )
sont drainées vers le condenseur et les pompes d’extraction assurent, côté basse
pression, la totalité du débit alimentaire.
Notons que le condenseur peut être partiellement isolé, assurant un service réduit
lorsque 3 des 6 faisceaux ont été isolés côté eau de circulation. De même, on peut
fonctionner en mettant en parallèle les trois pompes CEX, par exemple pour assurer
la permutation de la pompe de secours ou en cas de NPSH insuffisant à l’aspiration
des pompes alimentaires ARE.

### 6.8.8 Réglage du niveau du condenseur

Il existe d’inévitables fuites d’eau secondaires au niveau du condenseur (purges,
fuites. . . ) qui nécessite un système d’appoint d’eau déminéralisée. Ces appoints sont
fournis par une bâche d’eau déminéralisée et les rejets sont évacués vers les égouts (on
rappelle que cette eau n’est pas radioactive, sauf éventuellement en situation de RTGV
36 Net Positive Suction Head. Il s’agit de la différence de pression en un point d’un circuit et la
pression de vapeur saturante. Voir le chapitre sur les pompes primaires pour plus de détail sur cette
notion.

<!-- page 783 (PDF 799) -->
Photo 6.9 – Levage par le pont polaire de la salle des machines d’une pompe
d’extraction d’eau du condenseur de son puits de logement (photo EDF). La dimension
axiale de cette pompe très longiligne est imposante.
Tab. 6.7 – Palier CP1 : caractéristiques des pompes Jeumont-Schneider asynchrones
triphasées motorisées par du 6,6 kV (1 000 tours/minute, 3 550 kW).
Caractéristiques des
Unité
Régime
Régime
pompes d’extraction
nominal
maximal
Température de l’eau à l’aspiration
◦C
Vitesse
tr/min
N.P.S.H. requis au niveau de la 1ère roue
mCF
4,5
5.6
Hauteur manométrique totale
mCF
Débit
m3/h
1 980
3 010
Puissance absorbée à l’accouplement
kW
2 900
3 600
Rendement
%
Pression absolue d’alimentation du
presse-étoupe
bar
2.2
2.2
où on arrêterait les rejets). La régulation du niveau d’eau du condenseur (Figure 6.80,
Figure 6.81) joue sur une vanne d’appoint réglante qui gave le condenseur si le niveau
est trop bas, et d’une vanne de rejet Tout Ou Rien (TOR) qui s’ouvre sur niveau très
haut du condenseur.

<!-- page 784 (PDF 800) -->
Fig. 6.79 – Caractéristique hydraulique d’une pompe CEX (CP1).

<!-- page 785 (PDF 801) -->
Fig. 6.80 – Principe de la régulation du niveau condenseur et du niveau de la
bâche d’eau alimentaire ADG.
Fig. 6.81 – Réglage du niveau d’eau dans le condenseur (adapté de [Circuit
secondaire, 1977]).
