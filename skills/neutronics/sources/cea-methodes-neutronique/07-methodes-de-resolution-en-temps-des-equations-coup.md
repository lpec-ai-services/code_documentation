# Méthodes de résolution en temps des équations couplées de la cinétique spatiale
<!-- source PDF pages 73-82 -->

<!-- page 115 (PDF 73) -->
# Méthodes de résolution en temps des équations couplées de la cinétique spatiale

Rôle des neutrons retardés dans le pilotage
des réacteurs
On prend l’exemple d’un réacteur à neutrons thermiques et on
ne considére dans un premier temps, que la population des
neutrons prompts qui représentent plus de 99 % de la population
totale des neutrons (neutrons prompts + neutrons retardés
). La durée de vie moyenne, , d’un neutron dans le
domaine d’énergie thermique est de l’ordre de  ≈10–5 s.
On montre alors que le flux de neutrons en tout point du cœur
du réacteur évolue exponentiellement en fonction du temps
comme
où δk est l’excédent du facteur de multiplication
des neutrons, par rapport à l’unité : δC = CLL –1. On définit la
réactivité*, notée ρ, par
. L’état stable
ou critique* du réacteur correspond à δC = 0 ou ρ = 0.
La grandeur
est la constante de temps qui caractérise
l’évolution de la population des neutrons dans le réacteur
considéré ; on la nomme « période du réacteur ».
Si δC = 10–4 alors T = 0,1 s, et en une seconde, le flux initial
de neutrons se trouve multiplié par le facteur e10 ≈2,2 104 rendant
impossible le pilotage du réacteur.
Bien que peu nombreux en proportion (moins de 1 %), les
neutrons retardés ont pour effet d’allonger très sensiblement
la période du réacteur.Par exemple, les neutrons retardés dus
à la fission induite sur l’uranium 235 font passer la période du
réacteur de T = 0,1 s à T = 866 s.
En une seconde, le flux initial de neutrons se trouve donc multiplié
par le facteur
≈1,00116 rendant, par conséquent,
possible le pilotage du réacteur.
Circonscrite au cadre de la neutronique, l’équation générale
de Boltzmann régissant le flux de neutrons en tout point du
cœur du réacteur à tout instant ,, a été précédemment présentée
supra, p. 60.Cette équation possède deux termes sources
de neutrons correspondant respectivement aux neutrons
prompts* et aux neutrons retardés*. Le rôle crucial joué par
les neutrons retardés pour le pilotage d’un réacteur nucléaire
a déjà été évoqué. Il est illustré par l’encadré ci-contre.
En fonctionnement normal, on cherche à maintenir le réacteur
dans un état d’équilibre caractérisé par un bilan nul entre les
neutrons qui sont créés (essentiellement par fission induite
par neutron) et les neutrons disparaissant par absorption et
fuites hors du cœur du réacteur.Même en fonctionnement normal
, le cœur d’un réacteur a ses propriétés physiques (composition
isotopique, température, dimensions…) en constante
modification du fait des processus physiques qui s’y déroulent
de sorte que, dans la pratique, cet état critique est maintenu
en agissant sur des dispositifs capables à tout moment de
réduire à 0 l’écart à la criticité (δC = 0).Ce pilotage du réacteur
est effectué en particulier grâce à des barres de contrôle dont
l’insertion plus ou moins profonde dans le cœur du réacteur
permet de maîtriser la valeur du paramètre δC.
Le présent chapitre est consacré à la cinétique des réacteurs
nucléaires aux temps « courts » sur lesquels les neutrons
retardés jouent un rôle particulièrement important.
Comme cela a été expliqué dans « La démarche du neutronicien
», voir supra, p. 51, la complexité des configurations physiques
réelles (hétérogénéités, grandes dimensions…) à étudier
conduit à introduire des hypothèses raisonnablement
simplificatrices pour résoudre les équations du transport et
d’évolution. Le modèle dit « de la cinétique ponctuelle* des
réacteurs nucléaires* », décrit ci-après, découle de cette
démarche. Il est caractérisé par deux équations différentielles
linéaires du premier ordre couplées régissant respectivement
l’évolution temporelle de la population totale des neutrons
dans le réacteur et celle des précurseurs des neutrons retardés
; elles sont supposées valables en tout point du cœur du
réacteur en faisant abstraction des variables d’espace et
d’énergie. Sa présentation est précédée de l’énoncé des principes
généraux guidant le passage des équations de la cinétique
spatiale décrite supra, p. 59 et 60, à celles de la cinétique
ponctuelle. C’est au cours de ce passage que sont
introduites des grandeurs qualifiées d’« effectives » : elles
jouent un rôle clé, car elles permettent de « préserver la physique
» de la configuration réelle.
Enfin, un distinguo doit être opéré entre la réactivité statique
qui mesure l’écart à la criticité d’un système fissile
« figé » de référence et la réactivité dynamique qui inclut
un terme supplémentaire résultant d’une pertubation du système
de référence.
Les méthodes de la neutronique

<!-- page 116 (PDF 74) -->
## Les principes généraux

On reprend, dans cette section, les grandes lignes de l’exposé
fait sur ce sujet par J. Lewins dans la référence [1].
Conformément à ce qui a été dit plus haut, l’objectif est ici
de décrire le comportement du réacteur nucléaire uniquement
en fonction du temps. Pour cela, on repart des équations
de la cinétique spatiale (supra, p. 59 et 60), en y faisant
apparaître la densité totale de neutrons à la place du flux de
neutrons :
(1)
(2)
Dans un souci de clarté de l’exposé, on ne considére pas de
source externe et on suppose l’existence d’un seul noyau fissile
noté C0.
Par ailleurs, on néglige la dépendance, en fonction de l’énergie
du neutron incident, du nombre de neutrons émis par fission
et du spectre de fission. Sous ces hypothèses, l’équation
(1) se réécrit :
(3)
On utilise les notations simplifiées suivantes :
• <  <(), E, 
→, ,)
• χp  χp,C0 (/) : spectre énergétique d’émission des neutrons
prompts de fission.
• χd,4  χd,4 (/) : spectre énergétique des neutrons retardés
de la famille 4.
• β4  β4
: fraction de neutrons retardés de la famille 4.
• λ4  λ4
: constante de décroissance de la famille 4.
• C4  C4
(), ,) :concentration des précurseurs de la famille 4.
• β = Σ4 β4 : fraction totale de neutrons retardés.
• 1 – β : fraction de neutrons prompts.
On définit les grandeurs suivantes :
• taux de disparition et de transfert des neutrons noté de façon
simplifiée &< :
• taux de production des neutrons par fission noté de façon
simplifiée F< :
En remarquant que le taux de production des neutrons
prompts s’écrit :
On réécrit les équations (3) et (2) sous la forme :
(5)
(6)
On introduit l’opérateur de production totale de neutrons:
(7)
On dérive, finalement, le système d’équations suivant :
(8)
(9)
Pour décrire le comportement du réacteur nucléaire uniquement
en fonction du temps, on intègre les équations (8) et (9)
en angle, en énergie et en espace sur tout le cœur du réacteur
. Au préalable, on multiplie la seconde équation par le
spectre en énergie des neutrons retardés χd,4, puis les deux
équations par une fonction poids à définir w.
(C0)
(C0)
(C0)
(C0)

<!-- page 117 (PDF 75) -->
On définit, à présent, les grandeurs cinétiques « effectives
» suivantes :
• nombre pondéré de neutrons dans le réacteur :
• nombre pondéré de précurseurs dans le réacteur :
• nombre moyen de neutrons produits dans le réacteur :
• fraction effective de neutrons retardés pour la famille 4 :
• fraction effective de neutrons retardés :
• nombre moyen de neutrons transférés d’un point de l’espace
des phases à un autre dans le réacteur :
• réactivité :
La réactivité apparaît comme la différence entre le terme de
production et le terme de disparition et de transfert des neutrons
normalisé par le terme de production.
• temps moyen de reproduction des neutrons dans le réacteur
:
[Λ]LL est de l’ordre de 25 microsecondes dans un réacteur de
puissance à neutrons thermiques.
Les deux équations (11) et (12) prennent alors les formes
simples suivantes :
(13)
(14)
Par ailleurs, on peut montrer que la fonction poids w déduite
de la résolution de l’équation adjointe de l’état critique :
(15)
est un choix optimal [1].
Du point de vue physique, cette pondération en angle, en
énergie et en espace par la quantité adjointe <+
0 de la densité
critique <0 signifie que tous les neutrons n’apportent pas la
même contribution à la réactivité : cette contribution varie selon
leur position dans l’espace des phases ; les neutrons qui naissent
dans les régions où la densité neutronique est la plus élevée
« pèsent » plus que ceux qui naissent en périphérie du
cœur, ces derniers ayant une probabilité de fuite hors du réacteur
plus élevée que les premiers.
La résolution directe des équations de cinétique spatiales (1)
et (2) reste encore peu courante, en raison de son coût élevé
en temps de calcul. Cependant, les puissances de calcul
actuelles et futures permettent de l’envisager, tant par la voie
déterministe que par la voie stochastique, comme le montrent
les références [2] et [3].
Les équations (13) et (14) permettent de déterminer l’évolution
temporelle, en fonction de la réactivité, du nombre pondéré
de neutrons et de précurseurs dans le réacteur. Les quantités
[ρ]LL, [βi]LL et [Λ]LL intervenant dans ces équations sont
généralement déterminées en remplaçant dans leurs définition
respectivement l et < par <+
0 et <0, ce qui nécessite la résolution
de l’équation critique et celle de son équation adjointe.
Ces équations peuvent être établies directement dans le cadre
de la théorie de la cinétique ponctuelle, souvent utilisée en
physique des réacteurs nucléaires.
(11)
(12)

<!-- page 118 (PDF 76) -->
## Les équations de la cinétique ponctuelle

Dans le cadre de la cinétique ponctuelle, la population neutronique
est modélisée uniquement du point de vue temporel,
en « moyennant » en angle, en espace et en énergie les propriétés
du réacteur. Le modèle de la cinétique ponctuelle
revient donc à supposer que tout le réacteur est concentré en
un même point d’espace et que tous les neutrons ont le même
vecteur vitesse.
L’évolution du nombre total de neutrons dépend de trois types
de paramètres :
• Le facteur de multiplication effectif CLL ;
• le temps de vie moyen des neutrons dans le réacteur  ;
• les paramètres de neutrons retardés.
On a vu, au paragraphe établissant les équations de la cinétique
spatiale (supra, p. 59 et 60) que les précurseurs de neutrons
retardés ne sont pas traités individuellement : leurs
contributions à la production de neutrons retardés sont réparties
en quelques groupes ou familles de noyaux précurseurs
. On note O ce nombre de familles.Les calculs classiques
de réacteurs impliquent aujourd’hui six ou huit de ces familles,
dont les caractéristiques sont, pour chacune (repérée par l’indice
4, 1≤4 ≤O) :
• La quantité totale de neutrons retardés issus des noyaux
appartenant à cette famille, notée 24 ;
• une constante de décroissance, notée λ4 (ou la vie moyenne
associée, notée τ4) rendant compte du rythme avec lequel
sont produits les neutrons retardés issus de cette famille.
Ces caractéristiques, issues du lissage de mesures menées
après activation de matériaux fissiles sont, dans le cas de
l’uranium 235, regroupées dans le tableau 17, ci-dessous. On
y trouve également, à la ligne « Valeur moyenne », les caractéristiques
qu’il conviendrait d’utiliser, si l’on souhaitait réaliser
un traitement de la production des neutrons retardés plus
grossier, en regroupant l’ensemble des noyaux précurseurs
en une seule famille.
On peut établir directement les équations de la cinétique ponctuelle
en effectuant un bilan du nombre total de neutrons <(,)
et du nombre de précurseurs dans chaque famille C4(,).
Pendant un intervalle de temps dt,
neutrons disparaissent
, donnant naissance par fission à, en moyenne,
neutrons prompts. Dans ce même intervalle
de temps, Σ4 λ4C4(,) neutrons retardés naissent consécutivement
à la décroissance des précurseurs.
Par ailleurs, pendant un intervalle de temps dt, λ4C4(,) précurseurs
de la famille 4 disparaissent alors que
apparaissent.
On obtient ainsi les équations de la cinétique ponctuelle :
(16)
En exprimant le facteur de multiplication effectif en fonction de
la réactivité ρ,
, le système (16) se réécrit :
(17)
On remarque que ce système a la
même forme que celui donné par les
équations générales (13) et (14), les
quantités effectives paramétrant ces
équations, [ρ]LL, [β4]LL et [Λ]LL, étant
ici remplacées par les grandeurs ρ, 2, et
. Cette dernière grandeur, généralement
notée *, correspond au temps
de vie des neutrons dans un réacteur
critique.
Tableau 17
Constantes de décroissance, vies moyennes et proportions
de neutrons retardés pour la fission de l’uranium 235
(données issues de JEFF3.1)
Groupes
λ4 (s-1)
~4 = – (s)
24 (pcm)
de précurseurs
1,247 10-2
8,021 101
2,829 10-2
3,535 101
4,252 10-2
2,352 101
1,330 10-1
7,516
2,925 10-1
3,419
6,665 10-1
1,500
1,635
6,117 10-1
3,555
2,813 10-1
Valeur moyenne
7,681 10-2
1,302 101
λ4

<!-- page 119 (PDF 77) -->
En première approche, on peut considérer que le fonctionnement
normal des réacteurs s’opère par succession de plages
où la réactivité demeure constante (barres de contrôle, plus
ou moins insérées, à des cotes maintenues pendant un certain
temps).
Le système d’équations différentielles (17) est donc un système
linéaire homogène à coefficients constants dont la solution
est une combinaison linéaire de (O+1) solutions particulières
. On recherche ces solutions particulières, pour la
population neutronique et pour la population des précurseurs,
sous la forme :
où ¸ est un paramètre à déterminer.
La solution générale s’écrit donc :
On montre que les ¸ sont solution d’une équation en ¸ appelée
« équation de Nordheim* » :
(18)
Une fois les valeurs possibles des ¸ trouvées, la résolution
du problème complet s’achève par la détermination des
constantes ¹ et Y4 à partir des conditions initiales <(, = 0) et
4(, = 0).
Une façon pratique de procéder est de résoudre graphiquement
l’équation de Nordheim.On met en évidence ses racines
en traçant l’horizontale ρ dans un diagramme représentant la
fonction L (ω) figurant au second membre de l’équation (18)
(fig. 54).
On constate, sur ce graphe, que l’on trouve toujours (I + 1)
racines, si I est le nombre de familles de neutrons retardés.
Parmi ces (I + 1) racines, I sont toujours négatives et correspondent
à des transitoires, tandis que la dernière, du signe de
la réactivité, correspond au mode dominant asymptotiquement.
Pour le cas des très grandes réactivités (qui correspondent à
des conditions accidentelles), des considérations simples
d’ordres de grandeur permettent d’expliciter l’expression de la
plus grande racine de l’équation de Nordheim, notée ω0. De
manière approchée :
Cette expression peut encore s’écrire :
où CLL (1 – β) représente la contribution des seuls neutrons
prompts au facteur de multiplication.
Cette formule montre que si CLL (1 – 2) > 1 (ou ρ > 2), le réacteur
diverge en neutrons prompts seulement, la population de
neutrons se multipliant alors avec la période :
donc extrêmement rapidement, selon la loi :
Le réacteur est, dans un tel cas, dit « critique prompt » et la
valeur ρ = β (β de l’ordre de 665 pcm pour l’uranium 235,
d’après le tableau 17) apparaît comme une limite supérieure,
au-delà de laquelle le comportement du réacteur est régi par
les neutrons prompts.
En revanche, lorsque la réactivité est très petite et inférieure
à β, le comportement du réacteur est décrit par :
où
Le temps τ est caractéristique du noyau fissile et vaut de
l’ordre de 0,0866 s, dans le cas de l’uranium 235.
La population de neutrons se multiplie alors avec la période :
Fig. 54. Résolution graphique de l’équation de Nordheim. Cas d’une
réactivité négative.
- λ2
- λ5
- λ6
- λ1
ω
ω0
β
ω1
ω5
ω6
- β
ρ < 0
L(ω)
*

<!-- page 120 (PDF 78) -->
selon la loi :
Le pilotage du réacteur est donc tout à fait possible, lors de
l’introduction de petites réactivités.
On peut aussi remarquer que l’arrêt complet de la réaction en
chaîne n’est effectif qu’à la fin de l’émission de neutrons retardés
, soit après quelques minutes.

## La cinétique tridimensionnelle

La modélisation de situations incidentelles ou accidentelles
d’un cœur de réacteur nécessite de prendre en compte la
variation rapide de la population neutronique au sein du cœur
du réacteur. L’accident enveloppe retenu pour le dimensionnement
, vis-à-vis de l’évolution incontrôlée de la fission
nucléaire, est l’éjection d’une grappe de commande*. Cette
éjection est provoquée par la rupture du mécanisme de commande
de la grappe et est due à la différence de pression
entre la cuve et l’enceinte. Elle entraîne un emballement local
très violent de la fission nucléaire (quelques millisecondes),
cependant limité par les contre-réactions neutroniques qui permettent
l’arrêt immédiat du réacteur. On conçoit que ce type
d’accident, pour être étudié avec précision, nécessite un
modèle 3D de neutronique et de thermo-hydraulique associé.
Les équations de la cinétique neutronique spatiale ont été présentées
supra, p. 59 et 60.
Usuellement, on les résout sous la forme simplifiée suivante :
(19)
avec :
On travaille ici avec un spectre de fission prompt moyen indépendant
de l’énergie du neutron incident, un nombre moyen
de neutrons prompts émis et des familles de précurseurs indépendantes
du système fissile.
Après intégration de l’équation (2), la concentration C (), t) du
précurseur 4 s’exprime en fonction du flux scalaire par :
(20)
La résolution d’une telle équation est très coûteuse du fait
qu’elle s’exprime dans un espace de dimension sept. On peut
estimer les temps d’un calcul typique en supposant que l’espace
est discrétisé en 103x103x102 points, que l’angle nécessite
de l’ordre de 50 directions, que l’énergie est discrétisée
en une vingtaine de groupes et que la discrétisation temporelle
nécessite de l’ordre de 103 pas de 10-2s. À cela, il faut
rajouter les itérations nécessaires pour prendre en compte les
contre-réactions thermo-hydrauliques.On obtient de l’ordre de
1011 inconnues.Chaque inconnue est couplée par un système
matriciel. En estimant à 100 le taux de remplissage du système
matriciel, on obtient une estimation de l’ordre de 1016
opérations flottantes pour une simulation cinétique tridimensionnelle
.
Pour pallier ce coût important en temps de calcul, différentes
approximations ont été proposées au cours des années, en
fonction de la puissance disponible sur les ordinateurs.

### Modèles de simplification

Le premier modèle simplificateur repose sur la discrétisation
angulaire. On utilise le plus souvent un opérateur de diffusion
(–
→.D
→) pour lequel l’inconnue devient le flux scalaire :
?(), E, ,). Plus récemment, on a introduit l’opérateur SPN
(voir supra, p.74) pour lequel l’inconnue est alors un ensemble
d’harmoniques parmi lesquels le flux scalaire et le courant. À
l’heure actuelle, grâce à la puissance des nouvelles machines
parallèles, on peut résoudre des problèmes de cinétique en
transport complet, les inconnues étant alors les flux angulaires.
Le second modèle concerne le modèle en temps. Il a conduit
à de nombreuses variantes (méthodes adiabatique, quasi statique
, quasi statique améliorée, quasi statique locale, quasi
statique généralisée, multi-échelles, tridimensionnelle « monostep
» ou « multisteps », etc.). Les approximations portent sur
l’état initial ou sur le comportement dans le temps du système,
ce qui peut, bien sûr, entraîner une perte en précision du
modèle.L’utilisateur doit donc trouver un juste compromis pour
le ratio temps/précision.
On a déjà décrit le modèle de la cinétique ponctuelle. Ce
modèle ne permet d’obtenir que le comportement moyen du
cœur. Il ne fournit donc pas d’informations locales en espace,
ce qui le limite uniquement à la problématique du fonctionnement
global du cœur et ne lui permet pas de traiter la problématique
d’accidents graves.

<!-- page 121 (PDF 79) -->
Les premiers modèles 3D en temps, ont été développés à partir
des années 60 [4, 5]. Ils s’appuient sur un principe de factorisation
en espace et en temps avec une fonction de forme
dépendant de l’espace et éventuellement du temps et une
fonction d’amplitude dépendant du temps et éventuellement
de l’espace :
?(), E, ,) =  (), E, ,) L (), E, ,)
(21)
La méthode peut être vue comme une séparation des variations
rapides et lentes du flux (par rapport au temps). Ainsi
(), E, ,) est une fonction qui représente le comportement
rapide en temps, et L(), E, ,) est un flux de forme (en
n/cm2/s) qui varie lentement en fonction du temps.

### La méthode quasi statique (QS)

Le principe de la méthode quasi statique a été proposé par
Henry en 1958. Dans ce modèle, seule l’amplitude  (,) est
calculée en fonction du temps et la forme L est conservée à sa
valeur initiale L (), E, t0) :
?(), E, ,) =  (,) L (), E, t0)
L’amplitude, ne dépendant que du temps, est solution d’une
équation de cinétique ponctuelle dont les coefficients s’obtiennent
par projection de la forme sur une fonction de pondération
qui est, de façon optimale, le flux adjoint. Le calcul de la
forme peut être refait au cours du transitoire, pour un état statique
donné, au prix du recalcul des coefficients de la cinétique
ponctuelle.

### La méthode quasi statique améliorée (IQS)

La séparation de variable effectuée dans la méthode quasi
statique est une hypothèse forte. Rapidement, on la fit donc
évoluer sous la forme Quasi Statique Améliorée (IQS). L’idée
est d’introduire une dépendance lente en temps notée g pour
la forme, tout en conservant une amplitude ponctuelle à variation
rapide :
 (), E, ,) =  (,) et L (), E, ,) = L (), E, g)
Il faut cependant, du fait de la dépendance de L en temps,
ajouter une condition de normalisation pour garantir l’unicité
de la factorisation. Usuellement, dans la méthode IQS, on
impose :
Cette condition valide a posteriori l’hypothèse de variation
lente en temps de la fonction de forme. Des fonctions de pondération
autres que le flux adjoint ?*(), E, t0) sont possibles.
Cependant, on montre, par un raisonnement variationnel,
qu’en utilisant le flux adjoint initial on minimise l’erreur sur le
calcul.
On introduit donc deux échelles de discrétisation en temps,
une première grossière T ∈[T4 T4+1], sur laquelle on évalue la
forme et une deuxième fine (subdivision de la précédente)
Δ,C ∈[,C ,C+1] sur laquelle on n’évalue que l’amplitude.
On résout alternativement :
• Un problème de cinétique ponctuelle donnant  en connaissant
L ;
• un problème de cinétique 3D sur le pas de temps grossier
donnant L en connaissant .
La résolution se fait de la façon suivante. On considère les
équations 3D où ? est substitué par le produit L. Pour obtenir
la première équation sur l’amplitude , on condense ces
équations en espace et en énergie, après multiplication par le
flux adjoint initial. La dérivée en temps du flux de forme disparaît
grâce à la condition de normalisation. Pour obtenir les
équations sur la forme, le traitement des équations est identique
à celui d’un système complet 3D. Un terme supplémentaire
apparaît pour prendre en compte la variation de l’amplitude
, ce qui conduit à un système couplé avec l’amplitude qui
peut être résolu par une méthode itérative de point fixe (dans
la pratique une seule itération est effectuée). Pour la discrétisation
en temps, la variation étant lente, on peut utiliser des
schémas de bas niveau.Tous les plus grands codes de calcul
de cœur (diffusion et transport) appliquent au moins une des
méthodes quasi statiques (en général le quasi statique amélioré
).
La méthode quasi statique améliorée est disponible par
exemple pour le solveur en éléments finis MINOS du code
CRONOS2 [6]. L’intégration de la méthode IQS dans le
contexte MINOS a permis de bénéficier des avantages de la
rapidité du solveur. Néanmoins, en pratique, pour obtenir une
précision équivalente à celle d’une résolution 3D, on doit discrétiser
très finement en temps [7].

### La méthode quasi statique locale

Le défaut de la méthode précédente se situe dans la supposition
forte d’une amplitude constante en espace et en énergie
. Ainsi sur les pas de temps fins, on ne prend pas assez en
compte les variations spatiales et énergétiques, liées par
exemple à une forte hétérogénéité du milieu. Pour pallier ce
défaut, on recherche d’autres approches reprenant en partie
l’idée du quasi statique, pour son gain en temps de calcul,
mais avec une condensation plus locale de la forme.
L’idée est de décomposer le domaine spatial en sousdomaines
et de transposer localement les hypothèses globales
du quasi statique. Sur les sous-domaines, on retrouvera
donc une décomposition amplitude/forme quasi statique
(amplitude ne dépendant que du temps et forme faiblement
dépendante en temps). En adaptant, par exemple, ces sous
domaines aux propriétés du milieu, on espère obtenir un
modèle plus réaliste.

<!-- page 122 (PDF 80) -->
### L’approche multi-échelle (ME)

On cherche ici à étendre le principe de la méthode quasi statique
locale de façon à améliorer la précision du modèle tout
en gardant les avantages d’une approximation locale. L’idée
est de conserver la factorisation à deux échelles de temps,
mais en introduisant, pour la fonction amplitude, une variation
grossière en espace (sur un maillage spatial grossier, surmaillage
du maillage fin de résolution) [8].
Dans cette approche, on est conduit à résoudre deux problèmes
simultanés de cinétique sur des échelles différentes
et en utilisant un même solveur.Dans le contexte MINOS, étudié
par S. Chauvet [8], la représentation discontinue du flux
facilite l’implémentation (il faut cependant imposer la continuité
du courant normal). De plus, on profite pleinement des outils
existants et optimisés dans l’environnement du code disponible
, (MINOS par exemple).La problématique se situe essentiellement
sur l’optimisation du ratio temps/précision.
Cette méthode permet, à partir des méthodes existantes, et
en optimisant localement les méthodes de résolution adaptées
au contexte (pas de temps grossier ou maillage spatial
large) de gagner en temps de calcul par rapport à une
méthode 3D complète.

### La méthode de synthèse modale

La méthode de synthèse modale est une extension de la
méthode quasi statique originale dans laquelle on cherche une
solution sous forme d’une superposition de fonctions de forme
connues (modes) et précalculées, notées LI.Pour la méthode
avec condensation en énergie, on utilise un développement
sous la forme:
Les équations donnant les coefficients I(,) sont obtenues
par condensation en pondérant par des fonctions poids et en
intégrant sur le domaine spatial et énergétique. Il faut au préalable
éliminer les équations différentielles de précurseurs
grâce aux équations (20).
On obtient un système couplé d’équations intégro-différentielles
sur les fonctions I(,) qui se résout à l’aide d’une discrétisation
en temps et d’un schéma «monostep» ou «multisteps
».
Pour que la solution du système existe, il faut que les différents
modes soient linéairement indépendants. Un choix possible
est d’utiliser les harmoniques en espace et énergie de
l’opérateur statique ; le meilleur choix au sens variationnel pour
les fonctions poids est alors d’utiliser les harmoniques
adjointes.

### La méthode de cinétique tridimensionnelle

Les premières applications des méthodes de cinétique tridimensionnelle
datent des années 1970. Elles furent dans un
premier temps appliquées sur une discrétisation en différences
finies pour la variable d’espace (utilisation de l’opérateur
de diffusion), une discrétisation multigroupe pour la
variable d’énergie et un schéma «monostep»pour la variable
temps. Pour les calculs tridimensionnels, la méthode aux différences
finies s’est avérée trop coûteuse en mémoire et a été
remplacée par des méthodes d’éléments finis qui conduisent
à des matrices plus condensées et permettent une reconstruction
facile à l’intérieur des mailles. On décrira cette
approche tout d’abord utilisée dans le code CRONOS [6], puis
dans le code APOLLO3® en SPN (solveur MINOS [9]), et plus
récemment en transport (solveur MINARET [10]) avec éléments
finis discontinus (voir supra, p. 81).
On considère l’équation de la cinétique dans laquelle on a
préalablement intégré les équations de précurseurs comme
présenté plus haut et on utilise une discrétisation en énergie
multigroupe.
On choisit, comme opérateur spatial, l’opérateur de diffusion
et on considère un pas de temps [Te Te+1] sur lequel on effectue
une intégration en temps. L’équation de la cinétique
devient, en supposant ÀT constante sur un pas de temps :
Fig. 54. Schéma de principe des modélisations en quasi statique, quasi statique amélioré et multi-échelle.
Du quasi statique au multi-échelle
QS
? (), ,) =
 (,)
×
LT ())
indépendant de )
indépendant de t
IQS
? (), ,) =
 (,)
×
LT (), T)
indépendant de )
grossier en temps
ME
? (), ,) =
T (&→, ,)
×
LT (), T)
grossier en espace
grossier en temps
T0=t0
T0=t0
T1=t4
T2=t8
T1=t4
T2=t8
T0=t0
t1
t2
t3
t4
t5
t6
t7
t8
Temps grossiers et fins
Maillages grossiers et fins
Temps grossiers et fins
Maillages grossiers et fins
Temps grossiers et fins
Maillages grossiers et fins
t1
t2
t3
t5
t6
t7
t1
t2
t3
t5
t6
t7
t
t
t
}
}
}
}
}
}

<!-- page 123 (PDF 81) -->
où on a posé :
et
.
On fait ensuite des hypothèses sur les variations en temps des
sections efficaces, du coefficient de diffusion et du flux que
l’on écrit sous la forme :
avec :
Différents choix sur les fonctions ¸e(,) et Áe(,) sont possibles.
Les sections efficaces et le coefficient de diffusion sont supposés
à variations linéaires sur le pas de temps. Pour le flux,
le choix d’une variation linéaire en , conduit au schéma classique
de Crank-Nikolson et le choix d’une représentation parabolique
en , permet, en autres, d’obtenir le schéma implicite.
Dans les simulations de transitoires accidentels, les deux
schémas peuvent être utilisés successivement : le schéma de
Crank-Nikolson plus précis est utilisé au cours de l’excursion
de puissance et le schéma implicite plus stable est utilisé dans
la phase de chute de la puissance due à la chute des barres
de contrôle.
On considère ensuite une représentation spatiale sur une
base d’éléments finis. Le flux est alors décomposé sous la
forme :
On remplace les
par leur représentation dans l’équation
de la cinétique, intégrée sur le pas de temps. Après multiplication
par des fonctions poids - ()) (méthode de Galerkin), on
intègre sur le domaine complet en espace.On obtient alors un
système matriciel d’ordre (×q (( étant le nombre de nœuds
dans la base d’éléments finis et q le nombre de groupes
d’énergie). À chaque pas, on est conduit à résoudre un système
linéaire:
Le système précédent est résolu par itérations en utilisant différentes
méthodes d’accélération. La méthode de «rebalancing
» par condensation sur les groupes d’énergie est très efficace
; elle est équivalente à un préconditionnement par une
méthode quasi statique.
L’extension de la méthode au solveur SPN MINOS (géométrie
cartésienne et hexagonale) suit le même principe. Cependant
du fait de l’approximation mixte utilisée, on introduit deux
représentations différentes sur le pas de temps pour les flux
pairs (scalaires) et les flux impairs (vectoriels). Le système
matriciel à résoudre sur le pas de temps est écrit en termes de
flux impairs. Le solveur permet, au choix de l’utilisateur, de
prendre en compte le terme différentiel
de l’équation (19) uniquement sur le flux scalaire, sur le flux et
le courant ou sur toutes les harmoniques.
La cinétique en transport SN permet d’améliorer la modélisation
dans les configurations fortement hétérogènes. Le code
TORT-TD [11] permet d’effectuer de tels calculs pour des géométries
cartésiennes et cylindriques.Le schéma en temps est
un schéma implicite et la discrétisation en espace est de type
différences finies. Plus récemment, la cinétique en transport
SN a été implémentée pour le solveur MINARET du code
APOLLO3®. L’algorithme en temps est également «monostep
»implicite, la discrétisation spatiale utilise des éléments
finis discontinus d’ordre quelconque et le maillage est déstructuré
en radial et cylindrique en axial.L’utilisateur peut, au choix,
prendre en compte le terme différentiel en temps
pour le flux scalaire uniquement ou pour toutes les composantes
du flux angulaire. Le balayage en angle est parallélisé.
Un exemple d’application de la cinétique 3D est donné dans
cette monographie dans le cas de l’accident de rupture d’un
tube générateur de vapeur (voir infra, p. 225).
Références
[1] J. LEWINS, Nuclear Reactor Kinetics and Control, Oxford, Pergamon
Press, 1978.
[2] B. L. SJENITZER and J. E. HOOGENBOOM, “A Monte Carlo method for
calculation of the dynamic behaviour of nuclear reactors”, Progress in
Nuclear Science and Technology, vol. 2, pp. 716-721, 2011.
[3] B. L. SJENITZER and J. E. HOOGENBOOM, “General purpose dynamic
Monte Carlo with continuous energy for transient analysis”, in
Proceedings PHYSOR (Knoxville), 2012.
[4] G. R. KEEPIN, Physics of Nuclear Kinetics, Addison-Wesley,
Massachussetts, 1965.

<!-- page 124 (PDF 82) -->
[5] A.HENRY, “The application of reactor kinetics to the analysis of experiments
”, Nuclear Science and Engineering, 3, pp. 52-70, 1958.
[6] J.J. LAUTARD, S. LOUBIÈRE and C. FEDON-MAGNAUD, “CRONOS a
Modular Computational System for Neutronic Core Calculations”,
Specialist IAEA meeting, Advanced Calculational Methods for Power
Reactors, Cadarache, France, 1990.
[7] M. DAHMANI, A.M. BAUDRON, J.J. LAUTARD and L. ERRADI, “Application
of the nodal mixed dual technique of spatial reactor kinetics using the
improved quasi static method”, Proc. ANS Topical Mtg., Mathematics
and Computation, Reactor Physics and Environmental Analysis in
Nuclear Applications, vol. 1, Madrid, Spain, 1999.
[8] S. CHAUVET, A. NACHAOUIA, A.M. BAUDRON and J.J LAUTARD, “A Multi-
Scale Quasi-static Method for the Neutronic Kinetics”, International
Conference on the Physics of Reactors, Casino-Kursaal Conference
Center, Interlaken, Switzerland, September 14-19, 2008.
[9] D. SCHNEIDER, J.C. LE PALLEC, A.M. BAUDRON “Mixed dual finite element
method for the solution of the 3D kinetic simplified PN transport
equations”, Nuclear Mathematical and Computational Sciences,
Gatlinburg, Tennessee, April 6-11, 2003.
[10] A.M. BAUDRON, J.J. LAUTARD, Y. MADAY, and O. MULA, “Towards a
time-dependent neutron transport parallel solver” submitted to Proc
SNA/MC conf. Paris, 2013.
[11] A. SEUBERT, A. SUREDA, J. BADER, J. LAPINS, M. BUCK, E. LAURIEN,
“The 3-D time-dependent transport code TORT-TD and its coupling
with the 3D thermal-hydraulic code ATTICA3D for HTGR applications”,
Nuclear Engineering and Design, 251, pp. 173-180, 2012.
Anne-Marie BAUDRON, Patrick BLANC-TRANCHANT,
Mireille COSTE-DELCLAUX, Cheikh M. DIOP,
Jean-Jacques LAUTARD et Anne NICOLAS
Département de modélisation des systèmes et structures
