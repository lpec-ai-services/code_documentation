# Les équations fondamentales de la neutronique
<!-- source PDF pages 3-8 -->

<!-- page 45 (PDF 3) -->
# Les équations fondamentales de la neutronique

Dans le cœur d’un réacteur nucléaire, la propagation des
neutrons est couplée à la transmutation des milieux dans lesquels
ceux-ci se propagent. En effet, l’irradiation neutronique
et la température du combustible, du modérateur et de l’ensemble
des structures existantes présentent des variations
spatiales et temporelles significatives. Il s’ensuit que la composition
en nucléides des milieux irradiés varie en espace et
en temps. Cela explique que la neutronique traite deux équations
fondamentales couplées, régissant dans l’espace et
dans le temps, l’une le déplacement des neutrons, et l’autre
l’évolution des compositions isotopiques.

## L’équation intégro-différentielle de Boltzmann : le transport des neutrons

La solution de l’équation de Boltzmann donne la densité de la
population des neutrons en fonction du temps et de l’espace.
Cette équation s’applique aussi au transport des photons qui
interviennent également dans les études de réacteurs, en particulier
dans les calculs de protection contre les rayonnements
et les calculs d’échauffement des matériaux.
Le comportement quantique des neutrons se manifeste lors
des collisions avec les noyaux, mais, pour le neutronicien, ces
collisions peuvent être considérées comme des événements
ponctuels et instantanés, dont seules les conséquences l’intéressent
. Selon l’énergie du neutron incident et le noyau avec
lequel il interagit, différents types de réactions peuvent se produire
: le neutron peut être absorbé*, diffusé* ou encore provoquer
la fission* du noyau. On rappelle que la probabilité de
chaque réaction est caractérisée par une grandeur appelée
«section efficace microscopique*». Entre deux collisions,
les neutrons se comportent comme des particules classiques,
décrites par leur position et leur vitesse. Non chargés (particules
neutres), ils se déplacent en ligne droite, au moins pour
les courtes distances pour lesquelles on peut négliger l’effet de
la gravitation.
L’établissement de l’équation de Boltzmann en neutronique
repose sur les hypothèses et simplifications suivantes :
• Le nombre de neutrons dans le système considéré est suffisamment
important pour pouvoir définir une densité de neutrons
. Les conditions d’un réacteur nucléaire, avec un ordre de
grandeur de 108 neutrons par cm3, satisfont cette hypothèse ;
• les interactions neutron-neutron peuvent être négligées visà
-vis des interactions neutron-matière. Le rapport entre la
densité des neutrons et la densité du milieu de propagation
(eau, oxyde d’uranium…) est de l’ordre de 10-15, ce qui justifie
cette approximation. Cette hypothèse est d’une grande
importance, puisqu’elle conduit à une formulation linéaire de
l’équation de Boltzmann, beaucoup plus simple que la version
non linéaire utilisée dans la théorie cinétique des gaz ;
• les effets relativistes sont négligés. Dans un réacteur, les
neutrons produits par fission ont une énergie cinétique maximale
de l’ordre de 20 MeV, correspondant à 2 % de leur
masse au repos ;
• la
décroissance
radioactive
du
neutron
en
proton
(< →e +□– + ν̅□) peut être négligée, dans la mesure où son
temps de vie dans le réacteur, avant d’être absorbé, est
beaucoup plus faible que son temps de décroissance. En
effet, son temps de vie est compris entre 10-5 et 10-3
secondes selon les filières et sa période de décroissance
radioactive est de l’ordre de 10 minutes.
L’équation de Boltzmann exprime le bilan du nombre des neutrons
dans un volume élémentaire D ≡d)□.dE.d□
→autour du
point -≡()□, E, □→) de l’espace des phases et dans l’intervalle
de temps élémentaire dt, autour de l’instant t.
Six termes sont impliqués dans ce bilan :
a) La disparition algébrique des neutrons du domaine D par
fuite à travers les surfaces délimitant le volume élémentaire
autour du point )□ (bilan net des neutrons entrant et sortant)
dans l’intervalle de temps dt :
• =()□, E, □→, ,) : flux en phase en ()□, E, □→, ,) [voir introduction].
b) La disparition des neutrons du domaine D, par absorption et
diffusion, les absorptions faisant disparaître les neutrons et les
diffusions les faisant passer à une autre énergie et les envoyant
dans une autre direction, dans l’intervalle de temps dt :
• NC()□,,) : concentration des nucléides C au point )□ et à l’instant
t,
• σC(/) : section efficace microscopique totale du nucléide C
pour un neutron incident d’énergie E.
Les méthodes de la neutronique

<!-- page 46 (PDF 4) -->
c) L’arrivée de neutrons dans le domaine D résultant des diffusions
. Il s’agit des neutrons qui, avant la collision, étaient à
une autre énergie et se déplaçaient dans une autre direction,
et qui sortent de la collision à l’énergie E et dans la direction
□
→dans l’intervalle de temps dt :
• σs,C(/□→E, □
→□→□
→) : section efficace microscopique de transfert
faisant passer le neutron de l’énergie /□ à l’énergie E et
de la direction □
→□ à la direction □
→, lors d’une diffusion sur un
nucléide C.La nature isotrope des matériaux vis-à-vis des neutrons
implique que dans le processus de diffusion, pour un
angle de déviation donné après collision, les directions
d’émergence qui forment un cône de révolution autour de l’axe
défini par la direction d’incidence, sont toutes équiprobables.
C’est la raison pour laquelle les sections efficaces différentielles
de diffusion peuvent être réécrites avec un produit scalaire
: σs,C(/□→E, □
→□→□
→) = σs,C(/□→/, □
→□. □
→).
Pour les méthodes de traitement de l’équation du transport, il
est usuel de représenter ces sections efficaces différentielles
sous la forme d’un développement sur la base des polynômes
de Legendre P<(μ) :
d) La source de neutrons prompts* émis par fission induite
ou par fission spontanée dans le domaine D et dans l’intervalle
de temps dt :
• σL,C(E□) : section efficace microscopique de fission du
nucléide C, pour un neutron incident d’énergie /□,
• νp,C(E□) : nombre moyen de neutrons prompts émis à la suite
d’une fission induite sur un noyau C par un neutron incident
d’énergie /□,
• χp,C(E□→/) : spectre en énergie des neutrons prompts émis
de manière isotrope à la suite d’une fission induite sur un
noyau k par un neutron incident d’énergie E□,
• ?()□, /□, ,) : flux scalaire en ()□, /□, ,) [voir introduction],
• νp,Ls,C : nombre moyen de neutrons prompts émis par fission
spontanée du nucléide C,
• λLs,C : constante de décroissance radioactive de fission spontanée
du nucléide C,
• χp,Ls,C(/) : spectre des neutrons prompts émis de manière
isotrope par fission spontanée du nucléide k.
e) La source de neutrons retardés émis par fission induite ou
spontanée dans le domaine D et dans l’intervalle de temps dt.
Ces neutrons proviennent de produits de fission* radioactifs
particuliers, supposés émis au moment de la fission,
dénommés précurseurs*.Ces noyaux ont la propriété de pouvoir
décroître par la voie (2–,<), décroissance 2– suivie de
Espace des phases, densité et flux de neutrons
En physique des réacteurs, les populations de neutrons font l’objet
d’un traitement statistique. On les décrit en faisant appel à la
notion de densité neutronique, qui représente le nombre moyen
de neutrons observé par unité de volume. Cette densité neutronique
est cependant une notion plus générale que la notion de
densité usuelle, car le volume élémentaire à considérer n’est pas
seulement un volume dans l’espace physique.
Il faut, en effet, décompter les neutrons non seulement dans
l’espace, mais aussi selon leur vitesse qui n’est pas la même
pour tous et qui joue un rôle fondamental sur leur devenir. Cette
densité est également, en général, fonction du temps. Au total,
pour décrire complètement une population de neutrons, il faut
donc faire intervenir trois variables d’espace, trois variables de
vitesse et la variable temps. Dans la pratique, les matériaux utilisés
dans les réacteurs sont isotropes. Leurs propriétés (en
particulier, leurs sections efficaces) ne dépendent alors que du
module de la vitesse (ou de l’énergie) des neutrons incidents,
et non pas de leur direction. C’est pourquoi on distingue souvent
le module de la vitesse (ou directement l’énergie cinétique
des neutrons) et la direction des neutrons. Cette distinction est
réalisée en introduisant le vecteur unitaire bâti sur le vecteur
vitesse :
Au final, la densité (qualifiée de « densité en phase ») est notée
< ()□, /, □
→, ,).Elle permet d’exprimer le nombre moyen de neutrons
compris, à l’instant ,, dans un volume élémentaire d’un
espace à six dimensions appelé l’« espace des phases*».
De surcroît, il est souvent plus aisé de travailler avec la grandeur
= ()□, /, □
→, ,) = *< ()□, /, □
→, ,), appelée « flux angulaire» ou
« flux en phase », qui représente le nombre de neutrons d’énergie
E traversant à l’instant t, au point )□, une surface unitaire perpendiculaire
à la direction de propagation □
→. On définit aussi le
flux scalaire φ ()□, E, ,) comme l’intégrale sur toutes les directions
du flux angulaire : ' ()□, /, ,) = |4S = ()□, /, □
→, ,)u□
→.
L’intérêt de connaître le flux scalaire est que le nombre de réactions
nucléaires produites par unité de volume et de temps,
appelé « taux de réaction*», noté ~()□, E, ,), est calculé comme
le produit du flux scalaire et de la section efficace macroscopique
correspondant à la réaction nucléaire considérée, de section
efficace microscopique σ(/) :
~ ()□, /, ,) = ( ()□, ,)%(/)'()□, /, ,) = 6 ()□, /, ,)'()□, /, ,)
où N()□,,) représente la concentration du nucléide cible des neutrons
au point )□ et à l’instant ,.

<!-- page 47 (PDF 5) -->
l’émission immédiate d’un neutron. Comme la décroissance
radioactive d’un noyau précurseur, suivant cette voie, conduit
à l’émission d’un neutron unique, la source de neutrons retardés
s’écrit :
• λd,k : constante partielle de décroissance radioactive du
nucléide C, correspondant à la voie (2–,<),
• χd,C(/) : spectre en énergie des neutrons retardés émis de
manière isotrope par le nucléide C.
f) Les sources de neutrons externes :
La variation du flux en phase dans le temps :
est égale à la somme algébrique des six quantités précédemment
recensées. Cette égalité conduit à l’équation intégro-différentielle
de Boltzmann satisfaite par le flux angulaire des
neutrons, = ()□, /, □
→, ,) :
(1)
Cette écriture de l’équation de Boltzmann est générale, car
elle ne préjuge pas de la nature des nucléides. C’est ainsi
que, dans son application à une configuration physique donnée
, la section efficace de fission σL,C(/□), par exemple, prendra
une valeur nulle, si le nucléide k n’est pas fissile, ou que
la constante partielle de décroissance λd,C prendra une
valeur nulle si le nucléide C n’est pas précurseurs de neutrons
retardés.
On pourrait écrire une dépendance en temps pour les sections
efficaces microscopiques qui correspondrait à une variation
de la température. Elle est omise ici.
L’équation de Boltzmann existe aussi sous une forme intégrale
, forme qui constitue le point de départ de certaines
méthodes numériques, en particulier les méthodes de type
Monte-Carlo (voir le sous-chapitre sur les formes dérivées des
équations fondamentales).
Dans des situations particulières (études de criticité et de
radioprotection conduites dans le cadre du cycle du combustible
, par exemple) d’autres sources de neutrons sont prises
en considération, parmi lesquelles :
a) La source de neutrons issus de réactions nucléaires de type
(α, <) :
•
: rendement de production de neutrons d’énergie
E par les réactions (α, <) engendrées par les particules alpha
émises par décroissance radioactive du noyau C,
• λα,k : constante de décroissance radioactive α du noyau C.
b) La source de neutrons provenant de réactions photonucléaires
(γ, <), (γ, 2<), (γ, L), etc. :
• σγ,q,C(/□γ→E,□
→□γ→□
→) : section efficace différentielle de production
de neutrons à l’énergie E dans la direction □
→par la
réaction photonucléaire de type q du nucléide C,
• =$()□, /□$, □
→□γ, ,) : flux de gammas (particules neutres) dont
l’obtention se fait également en résolvant une équation de propagation
analogue à celle établie pour les neutrons.On notera
que :
- dans le domaine d’énergie des réacteurs nucléaires les
gammas émis ont des énergies situées dans l’intervalle (0,
20 MeV) et, par conséquent, leur propagation dans la
matière est gouvernée par l’effet Compton, l’effet photoélectrique
et l’effet de paires (électron-positons),
- ce terme de source de neutrons couple la propagation des
neutrons et celle des gammas.

<!-- page 48 (PDF 6) -->
L
udwig Eduard Boltzmann est né à
Vienne le 20 février 1844.Son diplôme de
doctorat, obtenu en 1866, sanctionne ses
travaux de thèse consacrés à la théorie cinétique
des gaz. Celle-ci avait été dirigée par
Joˇzef Stefan, physicien et homme de lettres
réputé, de culture slovène, auquel on doit la loi sur le rayonnement
du corps noir, loi de Stefan-Boltzmann. C’est, en effet,
L. E. Boltzmann qui en fournira la justification théorique. À la
fois expérimentateur et théoricien, ce dernier contribue au développement
de la plupart des domaines de la physique de son
temps.
Cependant, son apport majeur réside dans la révolution qu’il
opère dans la conception atomiste de la matière. Une des
grandes questions posées est la suivante : comment prédire
les propriétés macroscopiques d’un système physique donné
en partant de la myriade d’atomes qui le composent ? Afin d’y
répondre, L. E. Boltzmann pose les bases de la mécanique
statistique issue d’une idée géniale, audacieuse et courageuse
: celle d’allier la mécanique analytique issue des travaux
antérieurs de Newton, D’Alembert, Lagrange, Hamilton…
au calcul des probabilités dont les fondements théoriques
seront plus tardivement établis par des mathématiciens comme
Émile Borel, Henri Lebesgue, dans le cadre de la théorie de
la mesure [1, 2].
Il peut sembler aujourd’hui étrange que la mécanique statistique
de Boltzmann soit apparue, aux yeux de tous ses homologues
contemporains, comme ayant une orientation passéiste,
pour ne pas dire ringarde. Cela s’explique peut-être, en partie,
par deux facteurs :
• L’ambiance philosophique dominante du positivisme promu
entre autres par Ernst Mach et Auguste Comte, marquée
par une attitude de défiance vis-à-vis du calcul
des probabilités [3] ;
• la notion d’énergie elle-même, à cette
époque, objet d’une véritable révolution
conceptuelle, au point que, pour un Wilhelm
Ostwald, chimiste et physicien de renom,
ami proche de Ludwig Boltzmann, tout est
énergie. Cette entité devint synonyme de
modernité, détrônant, dès lors, l’entité
« archaïque » matière. La physique du
continu se devait de supplanter la physique
du discontinu.
Les traces du combat scientifique et épistémologique
tragique mené par Ludwig Boltzmann
pour installer, au sein de la communauté scientifique
européenne de la fin du XIXe siècle, le
Ludwig Eduard Boltzmann (1844-1906 )
nouveau paradigme de recherche associé à la mécanique statistique
sont nettement visibles sur plusieurs des pages ses
Leçons sur la théorie des gaz.
Intellectuellement marginalisé, sujet à des accès de mélancolie
et d’angoisse, d’une santé fragile, L. Boltzmann, presque paradoxalement
, n’a pas su ou pas pu saisir l’opportunité de l’émergence
de deux nouvelles physiques, la physique nucléaire et
la mécanique quantique, qui auraient pu l’aider à défendre,
face au monde savant, sa vision de la Nature.
Ludwig Boltzmann met fin à ses jours le 5 septembre 1906 à
Duino, près de la ville de Trieste où il passait des vacances. La
postérité lui donnera formidablement raison, au-delà, sans
doute, de ce qu’il était en mesure d’imaginer.
□Quelques références
[1] L. BOLTZMANN, « Weitere Studien über das Wärmegleichgewicht
unter Gasmoilekülen », Wiener Berichte, 66, pp. 275-370, 1872.
[2] L. BOLTZMANN, Leçons sur la théorie des gaz, Parties I et II, édition
française : Éditions Jacques Gabay, 1987, réimpression de l’édition
originale de la traduction française publiée en 1902 pour la partie
I et 1905 pour la partie II par Gauthier-Villars.
[3] S. CALLENS, Les Maîtres de l’erreur – Mesure et probabilité au
XIXe siècle, Paris, Presses Universitaires de France, 1997.
http://www.ipnl.in2p3.fr/delphi/laktineh/monitorat/public_html/boltz
mann/boltzmann.htm
Il a enseigné la physique expérimentale,
la physique théorique, les mathématiques
dans plusieurs universités : Munich, Leipzig,
Graz, Vienne. Excellent professeur,
son auditoire vient aussi d’Angleterre,
des États-Unis et du Japon.
Tombe de Ludwig Boltzmann
dans le cimetière central
(Zentralfriedhof) à Vienne
en Autriche.
L. E. Boltzmann a établi l’équation qui porte
son nom, généralisant du même coup la loi
de distribution des vitesses de Maxwell.
Il donne une interprétation statistique
de l’entropie que résume la loi S = k Log W,
écrite en épitaphe sur le haut de sa pierre
tombale, unifiant ainsi la mécanique
et la thermodynamique, et reliant le peu
probable au plus probable.
Source : http://fr.wikipedia.org/wiki/Ludwig_Boltzmann#Biographie

<!-- page 49 (PDF 7) -->
L’expression de la variation par unité de temps du nombre de
nucléides NC ()□,t), au point )□ et au temps , conduit à un système
d’équations différentielles couplées, appelées « équations
d’évolution» :
(2)
Elles sont aussi connues sous le nom d’équations de
Bateman* généralisées, du nom du mathématicien anglais
Harry Bateman [1] ayant fait sa carrière aux États-Unis, qui a
fourni une solution générale aux équations différentielles de
décroissance radioactive.
L’établissement
présenté
ci-dessus
de
l’équation
de
Boltzmann (1) et de celles de Bateman (2) montre qu’elles
sont couplées, formant un système neutroniquement fermé.
□Bibliographie
[1] BATEMAN (H.), “The solution of a system of differential equations
occurring in the theory of radioactive transformations”, Proceedings
Cambridge Philosophical Society, vol. 15, pp. 423-427, 1910.
Mireille COSTE-DELCLAUX, Cheikh M. DIOP,
Fausto MALVAGI et Anne NICOLAS
Département de modélisation des systèmes et structures

## Les équations de Bateman généralisées : évolution des nucléides

Les équations générales gouvernant l’évolution temporelle de
la concentration N k()□,,) des noyaux atomiques des
nucléides C, au cours de l’irradiation, dérivent du bilan au point
)□, et dans l’intervalle de temps élémentaire dt autour de l’instant
t, des nucléides C qui :
a) apparaissent par réactions nucléaires :
•̋
C←I ()□,,) : taux de réaction microscopique relatif à la formation
du nucléide C à partir du nucléide I :
• σq,C←I (/) : section efficace microscopique de la réaction q
induite par neutron d’énergie / sur le nucléide m conduisant
à la formation du nucléide C,
b) apparaissent par désintégration radioactive :
• λC←I : constante de décroissante radioactive d’un nucléide
de type I vers le nucléide C considéré,
c) disparaissent par réactions nucléaires :
•̋
k ()□,,) : taux de réaction microscopique relatif à la disparition
du nucléide C :
• σq,k (/) : section efficace microscopique de la réaction q
induite par neutron d’énergie E sur le nucléide C, conduisant
à la disparition du nucléide C,
d) disparaissent par désintégration radioactive :
• λC : constante de décroissante radioactive totale du nucléide
de type C (tous noyaux d’arrivée confondus).

<!-- page 50 (PDF 8) -->

