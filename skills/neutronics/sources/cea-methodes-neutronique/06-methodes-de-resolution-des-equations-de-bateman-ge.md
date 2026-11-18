# Méthodes de résolution des équations de Bateman généralisées
<!-- source PDF pages 65-72 -->

<!-- page 107 (PDF 65) -->
# Méthodes de résolution des équations de Bateman généralisées

## Les principes généraux

Un milieu irradié par un flux de neutrons a sa composition en
nucléides qui évolue au cours du temps par transmutation*,
soit du fait des réactions nucléaires, soit à cause de la
décroissance* radioactive des radionucléides formés.
Le tableau 15 regroupe les principaux phénomènes nucléaires
responsables de la modification de la composition du milieu
irradié. À la suite d’une réaction nucléaire ou d’un processus
radioactif (indiqués en rouge), le noyau A
ZX, de numéro atomique
Z et de nombre de masse A, est transmuté en un autre noyau.
Tableau 15
Réactions nucléaires et processus radioactifs
concourant à la modification de la composition
isotopique dans un réacteur nucléaire
A – 4
Z – 2X
α
A – 3
Z – 2X
(n,α)
A – 2
A – 2
Z – 1X
Z X
(n,t)
(n,3n)
A – 1
A – 1
Z – 1X
ZX
(n,d)
n,(n,2n)
A
A
A
Z – 1X
ZX
Z + 1X
C.E., β+,(n,p)
(n,n),(n,n’)
β-
A + 1
Z X
(n,γ)
Ces phénomènes nucléaires sont responsables de l’évolution
spatiale et temporelle de la composition isotopique en
noyaux lourds (NL) et en produits de fission* (PF) d’un
combustible irradié par les neutrons. Il en est de même de
l’évolution des produits d’activation* (PA) formés dans les
structures d’un réacteur et de l’évolution des produits de
spallation (PS) formés dans un système hybride accélérateur
-réacteur*, par exemple.
Ainsi, l’évaluation JEFF-3.1.1* comporte l’ensemble de ces
nucléides dont un classement en noyaux lourds et produits de
fission est donné par le tableau 16, page suivante :
Tableau 16
Répartition des nucléides de l’évaluation
des données nucléaires JEFF-3.1.1 [1], [2]
dans les catégories : noyaux lourds,
produits de fission et systèmes fissiles
Nombre total de nucléides
3 852 (226 stables)
Noyaux lourds
863 (Z > 80 : Hg)
Produits de fission
1 314
Noyaux fissiles* (ou « systèmes fissiles ») 39
L’ensemble de ces nucléides pères et fils sont décrits sous
forme de chaînes de filiation plus ou moins longues, suivant
les cas. Ainsi, les chaînes de filiation des noyaux lourds et des
produits de fission sont utilisées pour le calcul d’un réacteur
nucléaire, en y opérant, le cas échéant, un certain nombre de
simplifications, liées, par exemple, aux périodes des noyaux
radioactifs ou à leur pouvoir capturant.
Plusieurs grandeurs physiques sont dérivées des concentrations
(4 (), ,) des nucléides 4 : taux de réaction macroscopiques
*, puissances résiduelles* gamma, bêta, alpha et
sources de rayonnements correspondantes.
La dimension spatiale apparaissant dans les équations de
Bateman généralisées est imposée à la fois par la distribution
spatiale des concentrations des nucléides présents avant l’irradiation
(concentrations initiales), et par le flux de neutrons
via les différents taux de réaction. Ces équations doivent donc
être résolues en cohérence avec le schéma numérique en
espace (maillage spatial) adopté dans la résolution de l’équation
du transport.
Dans le cas du combustible nucléaire où il y a une forte interdépendance
entre le flux neutronique et les concentrations, les
pas de temps de la discrétisation sont définis de telle sorte que
le flux neutronique puisse y être supposé constant.Dans la pratique
, ce n’est pas toujours le temps qui est utilisé comme
variable, mais deux grandeurs qui sont représentatives de l’irradiation
des éléments (voir le tableau 5, supra, p. 13) :
• La fluence neutronique* exprimée en neutrons par kilobarn
(n/kb) ;
• le taux de combustion* exprimé en mégawatt jour par
tonne (MWj/t).
Z
A
Les méthodes de la neutronique

<!-- page 108 (PDF 66) -->
Par exemple, une irradiation d’un combustible UOx enrichi à
4,5 % de 45 000 MWj/t sera subdivisée en une cinquantaine
de paliers d’irradiation, correspondant à une présence en
réacteur de trois à quatre ans.
La résolution des équations de Bateman généralisées présentées
supra, p. 49, est effectuée par diverses méthodes dont le
choix est dicté par la nature du problème considéré :
• Recherche d’une solution analytique sous la forme d’une
combinaison linéaire d’exponentielles ;
• méthode de l’exponentielle de matrice utilisant un développement
limité de la fonction exponentielle ;
• méthodes numériques utilisant une discrétisation du temps
(ou de la variable qui y est associée).
Les principes de la résolution analytique et de la résolution par
la méthode numérique de type Runge-Kutta sont exposés ciaprès
. Suivent les résultats d’un calcul d’évolution illustrant,
d’une part, la modification significative de composition du combustible
en noyaux lourds au cours de son séjour dans le cœur
du réacteur et, d’autre part, l’empoisonnement du cœur par
deux produits de fission : le xénon* 135 et le samarium* 149.

## La solution analytique des équations de Bateman

Lorsque la chaîne de filiations* est décrite de manière à ne
contenir aucun chemin fermé, il est toujours possible d’ordonner
les nucléides de manière que le calcul du 4ème nucléide ne
fasse intervenir que des nucléides déjà calculés.
Soit c4C le coefficient conduisant au nucléide 4 depuis le
nucléide C par décroissance et / ou par réaction nucléaire et b4
un terme source – fission induite par neutron en l’occurence –
alimentant le nucléide 4. Les coefficients c4C et b4 sont supposés
constants sur le palier d’irradiation considéré.
U 235
U 236
U 237
U 238
U 239
Np 237
6,8 j
Np 238
Np 239
Pu 238
Pu 239
Pu 240
Pu 241
Pu 242
Pu 243
Am 241
Am 242m
Am 242
Am 243
Am 244
Cm 242
Cm 243
Cm 244
Cm 245
2,1 j
2,3 j
163 j
14,4 a
18 a
29 a
23,5 mn
5 h
84 % (16 h)
16 % (16 h)
89 %
11 %
10 h
(n, γ)
β–
α
C.E.
(n, 2n)
Fig. 49. Extrait d’une chaîne de filiation simplifiée de noyaux lourds
présents dans un cœur de réacteur REL. Ce schéma montre
comment se forment les actinides, et en particulier le plutonium,
par le jeu combiné des réactions nucléaires et des désintégrations
radioactives.

<!-- page 109 (PDF 67) -->
En omettant par raison de simplicité la variable spatiale,
l’équation à résoudre donnant la concentration du nucléide 4
en fonction du temps , compté à partir du début du palier d’irradiation
s’écrit :
(1)
La solution se met sous la forme :
(2)
où les coefficients N s
4 et F4C sont définis par :
(3)
en supposant c44 ≠0
(4)
en supposant c44≠cCC
(5)
où N4(0) = N4 (t = 0)
On notera qu’en l’absence de flux, cette résolution est toujours
moins onéreuse qu’une résolution par discrétisation numérique
.

## La résolution numérique des équations de Bateman

Lorsque l’on est en présence de chemins fermés, on a recours
à un schéma de résolution numérique.Celui présenté ici est de
type Runge-Kutta d’ordre 4, cet ordre étant choisi comme un
bon compromis entre la précision et le coût du calcul.
Les équations d’évolution à résoudre peuvent s’écrire sous la
forme matricielle générale suivante :
(6)
• N (,) : vecteur des concentrations des nucléides considérés ;
• S (,) : vecteur terme source ;
• A (,) : matrice d’évolution dont les éléments non diagonaux
contiennent les termes d’alimentation et les éléments
diagonaux les termes de disparition des nucléides par
radioactivité et / ou réaction nucléaire.
Les coefficients de la matrices sont définis par :
(7)
(8)
où les termes λ4, λ4←, relatifs respectivement à la décroissance
des nucléides 4 et , et̋ 4(,) et̋ 4←(,), correspondant aux
taux de réaction microscopiques associés aux nucléides 4 et
, ont été précédemment définis (voir supra, p. 49).
Nous voyons que, d’après les expressions (7) et (8), la matrice
d’évolution dépend essentiellement du temps par l’intermédiaire
du flux qui est une donnée fournie par les codes de
transport.Ses valeurs peuvent être connues à chaque instant,
soit parce qu’elles sont tabulées, soit parce qu’elles peuvent
être interpolées à partir des valeurs tabulées. Si l’on effectue
un calcul sur une plage d’irradiation « pas trop grande », on
peut supposer la matrice d’évolution constante et égale à son
expression au point milieu du palier.
Dans la pratique, lorsque le point milieu du palier n’est pas un
point correspondant à un résultat tabulé, on calcule les éléments
de la matrice d’évolution à partir des valeurs interpolées
entre deux points de tabulation encadrant le point milieu
d’évolution.
Cette hypothèse, conjuguée à la possibilité de connaître la
matrice d’évolution à différentes valeurs du taux de combustion
, peut justifier l’utilisation d’un schéma numérique de type
Runge-Kutta sans re-calcul de la matrice d’évolution entre
deux pas de temps élémentaires.Ce type de technique numérique
doit effectivement son nom aux deux mathématiciens
allemands qui l’ont mise au point, Carl David Tolmé Runge
(1856-1927) et Martin Wilhelm Kutta (1867-1944).
Ce schéma numérique repose sur l’utilisation conjointe de la
méthode d’Euler de résolution d’équations différentielles du
premier ordre et du développement de Taylor à un ordre fixé
de N (,) et de sa dérivée. On pose :
(9)
Le schéma Runge-Kutta d’ordre 4 s’écrit alors :
(10)
où µ, est la largeur du pas de discrétisation en temps.

<!-- page 110 (PDF 68) -->
L’erreur associée à ce schéma numérique est proportionnelle
à Δ,4.
On a implicitement supposé que l’historique du flux neutronique
était connu. Dans les calculs de cœur, le flux de neutrons
n’est pas connu à l’avance : l’équation du transport et les
équations d’évolution doivent être résolues simultanément.
Dans les faits, elles sont résolues séquentiellement par pas
de temps (ou de fluence neutronique ou de taux de combustion
), en adjoignant au procédé numérique précédemment
décrit une procédure de « prédiction-correction » qui anticipe
la variation du flux neutronique sur l’intervalle de discrétisation
considéré ; cette technique permet un calcul affiné des
concentrations à la borne supérieure de cet intervalle.

## Exemples de calculs d’évolution typiques en physique des réacteurs : l’évolution des noyaux lourds et des produits de fission

### Évolution des noyaux lourds

Le combustible utilisé dans les réacteurs français actuels est
soit du combustible à base d’uranium appelé UOx, soit un
mélange uranium-plutonium appelé «MOx». On peut distinguer
dans ces combustibles, d’une part, les noyaux fissiles*
tels que l’uranium 235, le plutonium 239, le plutonium 241,
d’autre part, les noyaux « fertiles* » qui donnent par capture
neutronique un noyau fissile ; l’uranium 238 qui, par capture
d’un neutron suivie de désintégrations radioactives, donne un
noyau fissile, le plutonium 239, est un exemple de noyau «fertile
».
Au cours de l’irradiation, des produits de fission* se forment
dans le combustible, comme nous le verrons plus loin, ainsi
que de nouveaux noyaux lourds* qui sont issus majoritairement
des réactions de capture neutronique.Les nucléides produits
et leur quantité dépendent de la composition initiale du
combustible, ainsi que du spectre des neutrons. Les figures
50 et 51 illustrent respectivement, en fonction de l’irradiation,
la formation ou la disparition des isotopes de l’uranium (U) et
du plutonium (Pu) dans un combustible REP-UOx enrichi à
4,5 % et dans un combustible MOx à teneur initiale moyenne
en plutonium de 5,6 %.

### Empoisonnement par les produits de fission

L’effet principal lié à l’apparition des produits de fission* dans
le combustible est l’éventuelle perte de réactivité* due à leur
capture neutronique. C’est ce que l’on appelle l’empoisonnement
*. Les poisons* les plus importants dans les réacteurs
à neutrons thermiques, et dont nous examinerons les effets
dans ce qui suit, sont le xénon 135 et le samarium 149.
En fin d’irradiation, l’empoisonnement de l’ensemble des produits
de fission atteint une dizaine de milliers de pcm* dans les
réacteurs à eau. Les quinze produits de fission les plus absorbants
constituent à eux seuls plus de 80 % de la capture totale
des produits de fission. Parmi eux figurent les nucléides suivants
: Rh 103, Gd 155, Cs 133, Nd 143, Nd 145, Sm 151,
Eu 153.
Cette anti-réactivité, pénalisante dans les réacteurs, peut
cependant devenir un atout dans les études liées au cycle du
combustible et, en particulier, dans le domaine de la sûreté-criticité
. De nombreuses études ont été menées ces dernières
0.0E+00
2.0E+25
4.0E+25
6.0E+25
8.0E+25
1.0E+26
1.2E+26
1.4E+26
Fig. 50. Évolution des principaux noyaux U, Pu dans un combustible UOx.
Concentration (at/tMLi)
Taux de combustion (GWj/t)
U 235
Pu 239
U 236
Pu 240
Pu 241
Pu 242
Pu 238
0.E+00
1.E+25
2.E+25
3.E+25
4.E+25
5.E+25
6.E+25
7.E+25
8.E+25
Fig. 51. Évolution des principaux noyaux U, Pu dans un combustible MOx.
Concentration (at/tMLi)
Taux de combustion (GWj/t)
U 235
Pu 239
U 236
Pu 240
Pu 241
Pu 242
Pu 238

<!-- page 111 (PDF 69) -->
### Empoisonnement par le samarium 149

La chaîne d’évolution conduisant au samarium* 149 est présentée
en figure 53. Cet isotope est stable et a une section
efficace d’absorption de 60 000 barns dans le domaine thermique
. Après quelques semaines de fonctionnement, à l’équilibre
, c’est-à-dire lorsqu’il y a autant de samarium formé que
détruit, l’anti-réactivité apportée par le samarium 149 est d’environ
600 pcm.
Si l’on arrête brusquement le réacteur fonctionnant avec un
flux constant depuis plusieurs semaines, la quantité de samarium
stable demeure dans le réacteur et augmente, en raison
de la décroissance du prométhéum 149 de période 53 heures
(fig. 52). Cela conduit à un surcroît d’empoisonnement qui
atteint une valeur limite proportionnelle au flux qui régnait dans
le réacteur avant l’arrêt ; contrairement à l’effet xénon, il n’y a
pas de passage par un maximum d’anti-réactivité. La quantité
de samarium ne diminue que lorsque le réacteur redémarre,
par absorption neutronique.
Références
[1] A. SANTAMARINA et al., The JEFF-3.1.1 Nuclear Data Library –
Validation Results from JEF-2.2 to JEFF-3.1.1, JEFF Report 22,
OECD 2009 NEA no 6807, 2009.
[2] M.A. KELLETT, O. BERSILLON, R.W. MILLS, The JEFF-3.1/-3.1.1 radioactive
decay data and fission yields sub-libraries, JEFF Report 20,
OECD 2009 NEA No. 6287, 2009.
années sur ce qu’on nomme le « crédit burn-up* » et qui
consiste à prendre en compte l’usure du combustible dans les
études de sûreté-criticité.

### Empoisonnement par le xénon 135

Le xénon* 135 est un gaz rare provenant de la fission suivant
la chaîne présentée dans la figure 52.
C’est l’un des principaux poisons dans les réacteurs à neutrons
thermiques, compte tenu d’une part de son rendement
de fission important pour l’uranium 235 et le plutonium 239
(6,5 % et 7,2 %, respectivement) et d’autre part, de son exceptionnelle
section efficace de capture dans le domaine thermique
(σc = 3.106 barns). En fonctionnement normal, l’empoisonnement
xénon est de l’ordre de 3 000 pcm dans un REP ;
cette anti-réactivité asymptotique (la production et la disparition
du xénon s’équilibrent) est obtenue au bout d’un jour ou
deux de fonctionnement à flux constant.
En cas d’arrêt du réacteur, l’iode 135 n’est plus produit par fission
et le xénon 135 ne disparaît plus par capture neutronique.
La réserve d’iode 135 accumulée en fonctionnement décroît
en formant du xénon 135 et le niveau de celui-ci augmente
pour atteindre un maximum au bout d’environ dix heures,
avant de décroître à nouveau. Dans un REP, l’anti-réactivité
maximale due à ce « pic xénon » est d’environ 3 700 pcm, ce
qui peut empêcher le réacteur de redémarrer instantanément.
Il est donc indispensable de prendre en compte, dans la
conception des cœurs, l’existence de ce phénomène.
De surcroît, cet effet xénon peut être à l’origine de perturbations
de la répartition de puissance dans le cœur, du fait de
sa section efficace de capture particulièrement élevée.
Fig. 52. Chaîne d’évolution du xénon 135.
Décroissance β–
Fission
Sn 135
Sb 135
Te 135
I 135
Xe 135
Cs 135
Ba 135
Période
0,85 s
1,70 s
19,0 s
6,61 h
9,09 h
2.3 106 ans
Stable
Rendement cumulé (pour un neutron thermique induisant la fission)
U 235
9,3 10–4
1,8 10–1
3,68
6,32
6,58
6,58
6,58
Pu 239
5,9 10–5
3,9 10–2
1,92
6,19
7,23
7,24
7,24
Fig. 53. Chaîne d’évolution du samarium 149.
Décroissance β–
Fission
Ba 149
La 149
Ce 149
Pr 149
Nd 149
Pm 149
Sm 149
Période
0,35 s
1,20 s
5,20 s
2,27 mn
1,73 h
53, 00 h
Stable
Rendement cumulé (pour un neutron thermique induisant la fission)
U 235
1,5 10–3
1,0 10–1
8,3 10–1
1,04
1,05
1,05
1,05
Pu 239
1,8 10–4
3,9 10–2
7,1 10–1
1,21
1,25
1,25
1,25

<!-- page 112 (PDF 70) -->
Ernest Rutherford, est un physicien et chimiste, né en Nouvelle-
Zélande et ayant vécu en Angleterre. Expérimentateur exceptionnel
, il élucide la structure de l’atome : noyau atomique chargé
positivement entouré d’un cortège d’électrons chargés négativement
. Il découvre les rayonnements alpha et bêta issus de l’uranium
, en étudiant l’ionisation de l’air induite par ces rayonnements.
Travaillant avec le chimiste Frederick Soddy, il établit, en 1902, le
lien entre radioactivité et changement d’espèce chimique [1].
F. Soddy identifiera, un peu plus tard, des nucléides radioactifs
de masses différentes ayant néanmoins les mêmes propriétés chimiques
, ce qui a conduit à la notion d’isotope.
E. Rutherford et F. Soddy étudient, en particulier, la famille radioactive
du Thorium et établissent la loi de décroissance exponentielle
qui régit les chaînes de décroissance radioactive [1],
[5].
La conséquence de la découverte de cette loi dans la reconstitution
de l’histoire de la Terre s’avéra considérable. Buffon (1707-
1788), avec ses 80 000 ans, un moment révisés à quelques millions
d’années, avait déjà mis à mal, par d’astucieuses
expériences, l’âge de quelques milliers d’années que l’on attribuait
communément à la Terre, en Europe. La géologie en essor du
milieu du XIXe siècle annonça plusieurs centaines de millions d’années
. Au début du XXe siècle, avec la radioactivité, l’âge de la Terre
dépassa le milliard d’années, au grand dam du tout-puissant et
« anti-darwinien » physicien Lord Kelvin (1824- 1907) qui resta
longtemps arc-bouté sur un âge de cent millions d’années qu’il
avait déduit de l’application
de lois de
la diffusion de la
chaleur [3].
À la suite de la
Ernest Rutherford
1871-1937
Prix Nobel de Chimie en 1908
Frederick Soddy
1877-1956
Prix Nobel de Chimie en 1921
Aux sources des Équations d’évolution

<!-- page 113 (PDF 71) -->
théorie de l’évolution de Charles Robert Darwin (1809-1882)
(et aussi d’Alfred Russel Wallace [1823-1913]), la physique
nucléaire naissante contribuait ainsi à installer durablement un
nouveau paradigme de l’histoire naturelle de la Terre, du système
solaire, de l’Univers : diachronique, évolutif, filiatif.
C’est à Harry Bateman, mathématicien d’origine anglaise ayant
émigré aux États-Unis, fortement intéressé par la physiquemathématique
, que l’on doit la solution générale des équations
différentielles régissant au cours du temps les concentrations
des nucléides appartenant à des filiations radioactives [4], [5].
Ces équations sont couramment appelées « équations de
Bateman ». Les équations de Bateman généralisées – ou
équations d’évolution – qui tiennent compte, de surcroît, de
l’irradiation par un flux de neutrons, à l’instar de ce qui se produit
dans le cœur d’un réacteur nucléaire en fonctionnement, ont été
résolues pour la première fois, en 1949, par William Rubinson,
scientifique
travaillant
au
Département
de
Chimie
du
Brookhaven National Laboratory, aux États-Unis [6].
Références
[1] E. RUTHERFORD, F. SODDY, “Radioactive Change”, Philosophical
Magazine and Journal of Science, Jan-Jun, pp. 576-591, 1903.
[2] http://www.larecherche.fr/idees/histoire-science/quel-age-a-terre-
01-10-2009-86743
[3] Charles DARWIN, On the Origin of Species by Means of Natural
Selection, or the Preservation of Favoured Races in the Struggle for
Life, London, John Murray, 1859.
[4] H. BATEMAN, “The solution of a system of differential equations
occurring in the theory of radioactive transformations”, Proceedings
Cambridge Philosophical Society, vol. 15, pp. 423-427, 1910.
[5] R. D. EVANS, The Atomic Nucleus, NewYork, Mac Graw-Hill Book
Company, 1955.
[6] W. RUBINSON, “The Equations of Radioactive Transformation in a
Neutron Flux”, Journal of Chemical Phvsics, vol. 17, number 6,
pp. 542-547, June 1949.
Charles Robert
Darwin
1809-1882
Harry Bateman
1882-1946
Cheikh M. DIOP,Tan Dat HUYNH,
Anne NICOLAS, Aimé TSILANIZARA
Département de modélisation des systèmes et structures
et Bénédicte ROQUE
Département d’études des réacteurs

<!-- page 114 (PDF 72) -->

