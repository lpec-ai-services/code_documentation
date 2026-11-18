# Les méthodes de la neutronique
<!-- source PDF pages 1-2 -->

<!-- page 43 (PDF 1) -->
# Les méthodes de la neutronique

## Sur les fondements de l’équation du transport

La propagation des neutrons dans un milieu donné relève
d’une famille de processus de transport rassemblant des phénomènes
aussi variés que la propagation de la lumière (photons
) dans la matière stellaire ou dans l’atmosphère terrestre,
la dynamique des gaz raréfiés, la physique des plasmas,
l’orientation dans l’espace des macromolécules, le trafic autoroutier
, etc., comme l’exposent J. J. Duderstadt et W. R.
Martin dans leur Transport Theory [1]. Ces processus sont
régis par les équations de la théorie cinétique (à ne pas
confondre ici avec les équations de la cinétique des réacteurs
nucléaires). On reprend, dans ce qui suit, les grandes lignes
de l’exposé que font ces deux auteurs sur le lien entre la théorie
du transport et la théorie cinétique, car il présente l’intérêt
de replacer l’équation du transport dans un cadre plus général
et d’en saisir les fondements. Par ailleurs, il montre la
connexion existant entre les formulations stochastique et
déterministe du problème du transport reliant celles-ci aux
mesures d’une grandeur physique d’intérêt effectuées lors
d’une expérience.
L’équation de Boltzmann et l’équation du transport des
neutrons sont deux exemples d’équations de la théorie cinétique
. En fait, l’équation du transport des neutrons est un cas
particulier de l’équation de Boltzmann dans lequel un « gaz »
de neutrons se déploie dans un « gaz » de nucléides.Les processus
de transport des neutrons sont caractérisés par le fait
que les particules (molécules de gaz ou neutrons) ont des
libres parcours moyens* bien plus grands que la portée du
potentiel d’interaction entre particules (réaction nucléaire, voir
infra, p. 9), qui dès lors, est supposé ponctuel.
L’équation de Boltzmann, que l’on établit souvent directement,
peut être dérivée, de plusieurs manières, d’une équation aux
dérivées partielles de la mécanique statistique plus générale,
l’équation de Liouville, elle-même établie à partir des équations
de Hamilton. On passe ainsi des équations microscopiques
qui gouvernent le mouvement de chacune des particules
d’un système physique donné aux équations de la théorie
cinétique permettant d’accéder à des grandeurs macroscopiques
« moyennes » et mesurables expérimentalement.
La discipline cadre théorique de ce passage du microscopique
au macroscopique est la mécanique statistique de nonéquilibre
(“Nonequilibrium Statistical Mechanics”).
Pour préciser le lien entre ces deux niveaux de description
de l’état d’un système physique, on considére un système
physique constitué de N particules. Chaque particule i de cet
ensemble est caractérisée, à un instant donné t, par sa position
)4(t) et sa vitesse v4(t). On note ΓN(t) l’ensemble des
positions et des vitesses des N particules à l’instant t :
ΓN(t)  {)4(,), v4(,)}4=1,N où les )4(,) et les v4(,) sont gouvernées
par les lois de la mécanique. Soit G une grandeur physique
macroscopique caractérisant le système et donc
dépendant de son état : à un instant , fixé la grandeur G
prend la valeur G (ΓN(,)). Une mesure de G consiste à en calculer
la moyenne <G> sur une durée T d’observation :

<!-- page 44 (PDF 2) -->
À présent, considérons non plus un système unique de N particules
, mais une collection de systèmes macroscopiquement
identiques de N particules. Soit ΓN une configuration possible
dans l’espace des phases de ces systèmes. À ΓN nous pouvons
alors associer une densité de probabilité ρ(ΓN) ; la valeur
moyenne de G, <q>, est alors obtenue par :
r q s =tD(Γ()q(Γ() uΓ(
Le postulat fondamental de la mécanique statistique est que
les moyennes <G> sont identifiées comme des mesures de la
grandeur macroscopique G qui ne sont autres que les
moyennes temporelles <G>T.Par conséquent, nous pouvons
écrire l’égalité :
Très schématiquement, cette égalité représente l’hypothèse
d’ergodicité introduite par W. Gibbs (il semble cependant que
Boltzmann [2], [3] ait été le premier à introduire le concept
d’ergodicité). Cette hypothèse stipule que l’on peut remplacer
l’étude d’un système unique par celle d’une collection de
systèmes macroscopiquement identiques affectés de conditions
initiales arbitraires différentes.
La densité de probabilité D(ΓN) est obtenue via l’équation de
Liouville mentionnée plus haut.
On est ainsi passé de l’espace à 6 × N dimensions du
niveau microscopique à l’espace à 6 dimensions (celui
d’une configuration « moyenne ») du « niveau cinétique ».
En fait, dans le cas d’une population de neutrons, dont le comportement
est markovien et dont un certain nombre peut disparaître
par absorption, par exemple, la densité D(ΓN) se
déduit des équations de Chapman-Kolmogorov.
En « contractant » encore une fois les dimensions pour ne
retenir que les trois dimensions d’espace, on atteint le
« niveau hydrodynamique » auquel appartiennent les équations
de Navier-Stokes et l’équation de la diffusion des
neutrons.
C’est donc une grandeur moyenne (le flux en phase) qui
satisfait l’équation de Boltzmann ou du transport. Les
méthodes déterministes mises en œuvre pour la résolution
de cette équation ne donnent plus accès à l’histoire individuelle
de chaque particule du système étudié.
La méthode probabiliste de Monte-Carlo, appliquée à la
résolution de l’équation du transport, simule explicitement la
collection des systèmes physiques équivalents considérés
plus haut, dans le cadre de l’hypothèse ergodique, puis opère
en fin de simulation la moyenne statistique de l’ensemble des
résultats produits par chacune des simulations, à l’image d’un
ensemble de mesures qui seraient faites et « moyennées »
dans un cadre purement expérimental.Cette moyenne est une
estimation statistique du résultat recherché. Le niveau microscopique
est préservé, en ce sens que les caractéristiques
(positions, énergies, événements) de l’histoire simulée de chacune
des particules des systèmes peuvent être stockées, analysées
, retraitées.
On remarquera que l’approche déterministe donne a priori en
tout point de l’espace des phases la valeur (moyenne) de
la grandeur physique d’intérêt. Ce ne peut être le cas, dans la
pratique, avec une simulation naturelle probabiliste, pour une
simple raison de statistique : la probabilité pour qu’une particule
simulée donne lieu à un événement en un point donné
de l’espace est quasiment nulle.
Références
[1] J. J. DUDERSTADT, W. R. MARTIN, Transport Theory, New York, John
Wiley & Sons, USA, 1979.
[2] L.BOLTZMANN, « Weitere Studien über das Wärmegleicgewicht unter
Gasmolekülen », Wiener Berichte, 66, pp. 275-370, 1872.
[3] L. BOLTZMANN, Théorie cinétique des gaz, Trad. française, Éditions
Jacques Gabay, 1987.
