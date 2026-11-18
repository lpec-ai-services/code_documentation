# Les formes dérivées des équations fondamentales
<!-- source PDF pages 13-18 -->

<!-- page 55 (PDF 13) -->
# Les formes dérivées des équations fondamentales

Dans les systèmes sous flux considérés ici, le processus
d’émission de neutrons lié à la fission spontanée des
nucléides est parfaitement négligeable. Il est donc écarté.

## Les calculs de transport stationnaires

La plupart du temps, un réacteur fonctionne en régime stationnaire
, c’est-à-dire à puissance constante. Il s’ensuit que sa
population de neutrons est constante : à chaque génération,
on a le même nombre de neutrons qu’à la génération précédente
. On dit alors que le réacteur est critique*.Dans un réacteur
sur-critique, le nombre de neutrons augmente avec le
temps, et, a contrario, dans un réacteur sous-critique, le
nombre de neutrons diminue avec le temps.
Pour décrire un réacteur critique, on cherche une solution stationnaire
de l’équation de Boltzmann, où les sources de neutrons
sont limitées aux sources de fission induite. Pour décrire
cette source, on utilise le nombre total de neutrons émis (neutrons
prompts* et neutrons retardés*) et le spectre d’émission
des seuls neutrons prompts qui représentent la quasitotalité
des neutrons émis par fission. On fait donc abstraction
de l’impact du spectre d’émission des neutrons retardés, après
s’être assuré du bien-fondé de cette hypothèse.

### Forme intégro-différentielle de l’équation de Boltzmann stationnaire

On est, par conséquent, conduit à résoudre l’équation :
(1)
• ν,C (/) : nombre moyen de neutrons (prompts et retardés)
émis de manière isotrope à la suite d’une fission induite sur
un noyau C par un neutron incident d’énergie /.
L’équation (1) décrit un équilibre parfait entre productions et
disparitions des neutrons, qui seul peut conduire à un état stationnaire
.

### Forme intégrale de l’équation de Boltzmann stationnaire

On peut écrire l’équation de Boltzmann stationnaire sous une
forme telle que toutes les variables de l’espace des phases
apparaissent dans des opérateurs intégraux.Cette forme intégrale
de l’équation de Boltzmann est utilisée dans deux types
de traitements du transport des neutrons : la méthode des probabilités
de collision et la méthode de Monte-Carlo.
La forme intégrale de l’équation de Boltzmann peut soit se
déduire de l’équation (1) établie dans le chapitre traitant des
équations fondamentales de la neutronique, soit s’établir
directement.
La figure 20 (page suivante) montre que le flux angulaire
= (), E, 
→) cherché au point de l’espace des phases
(), E, 
→) résulte de deux termes :
• Les neutrons émis en )= )– s
→à l’énergie E et dans la
direction 
→, S ()– s
→, E, 
→). Ces neutrons ont une probabilité
d’arriver en (), E, 
→) sans
subir de collision. En intégrant sur toutes les distances s
séparant le point d’émission ) et le point ) d’arrivée, on
obtient le premier terme qui contribue au flux angulaire
= (), E, 
→) :
• les neutrons d’énergie / et de direction 
→ qui subissent une
diffusion en )= )– s
→qui leur confère une énergie / et une
direction 
→:
Les méthodes de la neutronique

<!-- page 56 (PDF 14) -->
### Équation critique – Introduction du coefficient de multiplication effectif

Pour avoir une solution stationnaire à l’équation, quel que soit
l’état réel du système (critique, sur-critique ou sous-critique),
on modifie l’équation (1) en divisant les sources de fission par
un facteur qui permet de rétablir l’équilibre entre productions et
disparitions.Ce facteur est appelé « facteur de multiplication
effectif*» ou CLL. L’équation (1) devient alors l’équation (3),
qui est une équation aux valeurs propres.On peut montrer que
CLL est la plus grande valeur propre et que = (), E, 
→) est la
fonction propre associée.
On appelle (3) le problème critique associé et la solution
= (), E, 
→) est dénommée flux critique. On peut aussi montrer
que le CLL introduit dans l’équation s’accorde avec la définition
de facteur de multiplication comme le rapport entre les
neutrons de génération (4 + 1) et les neutrons de génération 4.
Le problème aux valeurs propres (3) est résolu par une
méthode connue sous le nom d’« itération de la puissance
* » : on commence avec une distribution d’essai de la
source (habituellement une constante en espace et un spectre
de Watt en énergie) et on résout le problème à source fixe qui
en résulte. Avec le flux ainsi calculé, on met à jour la distribution
des sources de fissions, et ainsi de suite, selon le schéma
itératif :
(4)
En régime stationnaire, l’équation intégrale du transport s’écrit donc :
(2)
Fig. 20. Établissement de l’équation intégrale de Boltzmann en régime stationnaire. Le flux angulaire = (), E, 
→) résulte des neutrons provenant
de la source S ()– s
→, E, 
→) et de la source de diffusion Σs ()– s
→, /→E, 
→→
→) = ()– s
→, /, 
→).
Par le même raisonnement que précédemment, on obtient le second terme qui contribue au flux angulaire ψ (), E, 
→) :
)= )– P
→
(/, 
→)
s =|) – )|
s : distance à franchir sans subir de collision
probabilité associée :
Point source ou point de diffusion
Point de calcul du flux angulaire
= (), /, 
→)
Neutrons source
S ()– P
→, E, 
→)
Flux de neutrons incidents
= ()–s
→, /
→)
Neutrons diffusés
(E, 
→)
)

→
(3)

<!-- page 57 (PDF 15) -->
Analogie formelle entre les équations intégrales de Boltzmann et de Bateman
Tableau 9
Analogie formelle entre le transport en régime stationnaire et la transmutation
Transport stationnaire
Évolution en un point
Espace : )
Temps : t
Énergie : E (variable continue)
Espèce de nucléide : C (variable discrète)
Direction : 
→
Irréversibilité du temps : t > 0
Flux en phase : = (), E, 
→)
Concentration en radionucléides : NC (), ,)
Section efficace macroscopique totale : Σ (), /)
Taux de transmutation microscopique total : μC ())
Densité de collision : ζ (), E, 
→) = Σ (), E) = (), E, 
→)
Activité généralisée : AC (), ,) = μC ()) NC (), ,)
Source de neutrons : S (), E, 
→)
Activité source : S = UC(), ,)
Équation intégrale du transport : ζ = TCζ + TS
Équation intégrale de la transmutation : A = TCA + TS
T opérateur intégral de déplacement en espace :
T opérateur intégral de déplacement en temps :
C opérateur de diffusion :
C opérateur de transmutation : CA vecteur dont
la Ce composante est donnée par :
Références
P. H. WILSON, “Analog Monte Carlo Methods for Simulating Isotopic
Inventories
in
Complex
Systems”,
Nuclear
Science
and
Engineering, 152, 3, pp. 243-255, March 2006.
C. M. DIOP, “Integral form of nuclide generation and depletion equations
for Monte-Carlo simulation. Application to perturbation calculations
”, Annals of Nuclear Energy, 35, pp. 2156-2159, 2008.
Dans le cas où le flux provoquant les transmutations de nucléides est indépendant du temps, les équations de Bateman peuvent
être réécrites sous la forme intégrale suivante :
• μC()) = λC +̋
C())
• μC←I()) = λC←I +̋
C←I ())
• UC(),,) : taux de production du nucléide C au point ) et à l’instant ,.
On définit l’« activité généralisée » de l’ensemble des nucléides comme le vecteur dont la composante k est donnée par la relation :
L’« activité généralisée » satisfait l’équation intégrale suivante :
En faisant apparaître la densité de collision ζ (), E, 
→) = Σ (), E) ψ (), E, 
→), l’équation intégrale de Boltzman en régime stationnaire
pour un problème à source fixe dans un milieu non multiplicateur s’écrit :
L’analogie formelle entre le transport en régime stationnaire et la transmutation en un point ) donné est explicitée dans le tableau
ci-dessous :

<!-- page 58 (PDF 16) -->
Flux adjoint, importance et fonction de Green
L’équation adjointe* de l’équation de Boltzmann est également
largement utilisée en neutronique. Le flux adjoint* est la
solution de cette équation. Il s’interprète comme le nombre
moyen de neutrons issus de l’histoire d’un neutron initial d’une
énergie fixée, placé en un point donné de l’espace. En régime
sous-critique, ce nombre est fini. Par contre, en régime critique
ou sur-critique, la somme des descendants des générations successives
est infinie, ce qui pose un problème d’interprétation.On
est donc amené « à refuser la notion de flux adjoint pour un système
sur-critique et à considérer que le flux adjoint d’un cas critique
est la limite du flux adjoint du cas sous-critique, lorsque sa
réactivité (négative) tend vers zéro… Dans un système critique,
une fraction infinitésimale des neutrons a une descendance infinie
: l’évaluation de la limite pose donc un problème du type
“ 0 × ∞”. » [1]
Ce nombre moyen de descendants mesure l’importance* [2]
du neutron initial considéré pour l’entretien de la réaction en
chaîne. D’où
son
alias
d’importance
souvent
utilisé.
Contrairement au flux sa nature mathématique est une fonction
et non une densité.
Le flux adjoint intervient pour traiter différents problèmes de neutronique
, par exemple :
• En cinétique où il sert à définir des coefficients cinétiques effectifs
utilisés pour la cinétique d’un réacteur point ;
• en cinétique et neutronique expérimentale pour faire des calculs
de perturbation et concevoir/interpréter des mesures de
réactivité [3] ;
• en transport et en évolution pour calculer les profils de sensibilité
permettant d’effectuer des calculs d’incertitude sur des
grandeurs physiques d’intérêt par propagation des incertitudes
existant sur les données physiques du problème à résoudre
(sections efficaces…) ;
• en transport Monte-Carlo pour accélérer la simulation ;
• en transport pour réaliser des études paramétriques telles que
celles relatives à la détermination des réponses de détecteurs
en fonction de la distribution de la puissance du cœur du réacteur
, ainsi qu’il est montré ci-après.
On considère un détecteur C occupant une zone d’espace Z,
caractérisé par une fonction réponse ou sensibilité sk (section
efficace macroscopique, par exemple). La réponse associée au
flux scalaire de neutrons ? (-), où P représente le couple de
variables (), /), s’écrit :
(1)
Le flux ? (-) résulte d’une source de neutrons S(-) circonscrite
dans un domaine  de l’espace.Supposons que l’on veuille étudier
le comportement de la réponse Rk() en fonction de
diverses distributions de sources S(-). Il est toujours possible
de faire un calcul de transport pour chacune des distributions de
sources à considérer. Une autre voie de calcul consiste à
résoudre l’équation adjointe du transport en prenant pour terme
source la sensibilité du détecteur sk(-) pour P ∈Z. La résolution
de cette équation fournit le flux adjoint ψ+(-) et l’on peut montrer
que RC() est également donnée par :
(2)
L’intérêt de cette expression pour des calculs paramétriques est
manifeste, puisqu’il suffit de n’effectuer qu’un unique calcul de
transport adjoint et de convoluer le flux adjoint obtenu avec les différentes
distributions de sources envisagées pour déterminer les
réponses RC() correspondantes.
On notera le lien du flux adjoint avec les fonctions de Green
G(-→-) :
et donc en comparant avec (2) :
(3)
Références
[1] P. REUSS, Précis de neutronique, p. 370, Les Ulis, EDP
Sciences/INSTN, 2003.
[2] J. LEWINS, Importance – The Adjoint Function, Pergamon Press,
1965.
[3] J. BUSSAC, P. REUSS, Traité de Neutronique, chapitre XXV : “Théorie
des perturbations”, pp. 403-415, Paris, Hermann, 1985.

<!-- page 59 (PDF 17) -->
Le facteur de multiplication à l’étape (<) est calculé comme le
rapport entre le flux à l’étape (<) et le flux à l’étape (< – 1). Le
problème aux valeurs propres est ainsi résolu comme une
succession de problèmes à source fixe, jusqu’à la convergence
numérique.
L’équation (3) nécessite une résolution numérique souvent
complexe, en raison du nombre très élevé d’inconnues, lié à
la dimension 6 de l’espace des phases (), E, 
→). Elle a pour
solution le flux angulaire = (), E, 
→), alors que l’on pourrait
se contenter de la connaissance du flux scalaire pour calculer
les taux de fission.

## Les équations de la cinétique spatiale

Pour traiter de façon générale un problème dépendant du
temps, il faut partir du système d’équations couplées établi au
chapitre traitant des équations fondamentales de la neutronique.
Il est d’usage de distinguer l’évolution temporelle du cœur du
réacteur sur une gamme allant de la fraction de seconde à
quelques minutes (changements de puissance, phases de
démarrage et d’arrêt du réacteur, situations accidentelles) et
l’évolution du combustible par modification de sa composition
isotopique sur des échelles de temps allant de quelques
heures à plusieurs mois. Ce dernier aspect est partiellement
traité infra, p.107-113, dans le chapitre intitulé : « Méthodes de
résolution des équations de Bateman généralisées ».
La cinétique consiste à prédire l’évolution de la population de
neutrons aux échelles de temps où le phénomène d’émission
des neutrons retardés joue un rôle déterminant sur l’évolution
de la réactivité. Elle est cruciale pour le pilotage des réacteurs
en situation normale et accidentelle.
Comme la source de neutrons retardés s’exprime en fonction
des concentrations des noyaux précurseurs, il faut connaître
l’évolution en temps de ces nucléides particuliers. En
revanche, l’échelle de temps étant relativement courte, on peut
négliger, pour le transport des neutrons, l’évolution en fonction
du temps des concentrations des nucléides.
On note P l’ensemble des noyaux précurseurs de neutrons
retardés. Il est important de rappeler que ces noyaux ont la
propriété de pouvoir décroître par la voie (2–, <), décroissance
2– suivie de l’émission immédiate d’un neutron.Mais cette voie
n’est pas leur unique mode de décroissance. Dans le cas particulier
du brome 87, qui est un des principaux précurseurs de
neutrons retardés, sa décroissance par la voie (2–, <) n’a lieu
que dans 0,02 % des cas.
Si on note F l’ensemble des nucléides fissiles qui est disjoint
de l’ensemble P, on peut écrire l’équation d’évolution des
concentrations des précurseurs, relativement au seul phénomène
d’émission de neutrons retardés. Pour distinguer cette
équation de celle dérivée de l’équation de Bateman, où toutes
les causes d’évolution seraient prises en compte, on note Cp
la concentration d’un précurseur p.
La contribution principale à la production des précurseurs est
la fission induite. La contribution principale à la disparition des
précurseurs, relativement au seul phénomène d’émission de
neutrons retardés, est leur décroissance radioactive par la voie
(2–, <).En négligeant les autres causes de variation, on obtient,
pour un précurseur p de l’ensemble - l’équation suivante :
(5)
C’est un bilan au point ) et à l’instant t d’un quelconque
nucléide précurseur p. Dans cette équation,
• λd,p : constante partielle de décroissance radioactive du
nucléide p, correspondant à la voie (2–, <),
• νt,C (E) : nombre total moyen de neutrons émis lors d’une fission
induite par un neutron incident d’énergie / sur le
nucléide C,
• 2p
(C)νt,C (/) : nombre de neutrons retardés issus d’un précurseur
p né de la fission induite à l’énergie / sur le nucléide C,
• NC ()) 2p
(C) ∫0
∞d/ νt,C (/) σL,C (/) ' (), /, ,) : production du
précurseur p par fission induite sur le nucléide C, sachant
qu’à un neutron retardé émis correspond un noyau précurseur
formé.
Habituellement, on paramétrise l’émission en temps des
neutrons retardés, pour chaque noyau fissile k ∈F, en
regroupant les processus d’émission par les noyaux précurseurs
(environ cent cinquante) en six ou huit familles notées
par le couple d’indices (C, 4). À chaque famille sont associées
une constante de décroissance moyenne λi
(C) rendant compte
du rythme avec lequel sont produits les neutrons retardés
issus de cette famille (elle correspond donc à la pondération
des constantes de décroissance partielle λd,p des différents
noyaux précurseurs regroupés dans la famille) et une proportion
de neutrons retardés 2i
(C). La concentration des « précurseurs
» de la famille (C, 4) est notée i
(C). Elle est donnée par
l’équation :
(6)

<!-- page 60 (PDF 18) -->
En utilisant la paramétrisation des précurseurs, nous pouvons
écrire la source de neutrons retardés de l’équation du transport
sous la forme :
où χd,4
(C)(/) est la proportion de neutrons retardés de la famille
(C, 4) émis à l’énergie E.
L’équation du transport se réécrit alors sous la forme :
Les équations couplées (6) et (7) sont appelées « équations
de la cinétique spatiale ».
Mireille COSTE-DELCLAUX, Cheikh M. DIOP,
Fausto MALVAGI et Anne NICOLAS
Département de modélisation des systèmes et structures
(7)
