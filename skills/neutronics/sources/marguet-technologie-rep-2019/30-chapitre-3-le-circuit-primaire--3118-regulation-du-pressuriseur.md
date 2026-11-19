# Chapitre 3 Le circuit primaire — 3.11 Le pressuriseur — 3.11.8 Régulation du pressuriseur … 3.11.11 Aspects sûreté du pressuriseur
<!-- source PDF pages 400-407 -->

<!-- page 384 (PDF 400) -->
en mode dégradé), mais elle a de fait trompé les opérateurs qui n’ont pas détecté la
véritable ouverture des soupapes de décharge, pensant qu’elles étaient fuitardes mais
fermées.

### 3.11.8 Régulation du pressuriseur

La régulation d’un pressuriseur est complexe et fine (Figure 3.88, Figure 3.89,
Figure 3.90), étant donné l’importance de ce composant sur la physique du circuit
primaire. Deux questions essentielles se posent : comment régler la pression, l’objectif
primal du pressuriseur, et comment maintenir le niveau de l’eau dans une gamme
acceptable, permettant de laisser un volume libre compatible avec la régulation de
pression. Nous avons vu précédemment qu’une variation de niveau affecte la pression.
Dans les faits, la régulation de niveau, qu’on établit fortement temporisée pour laisser
les équilibres s’établir, influe finalement peu sur la pression, et c’est la régulation de
pression qui sera prépondérante. En ce qui concerne le niveau d’eau, une augmentation
du volume d’eau liquide du primaire conduit naturellement à une augmentation
du niveau. De même, une baisse du volume primaire induit une baisse de niveau.
Donc, si l’on se donne un point de consigne de niveau (pour fixer les idées, disons à
mi-hauteur du pressuriseur), c’est en jouant sur les débits de charge et de décharge du
RCV qu’on pourra maintenir le niveau. Ces actions d’injection et de retrait sont par
conception lentes. En ce qui concerne la pression, l’idée est de faire baisser la pression
quand elle est trop forte par aspersion d’eau plus froide qui condense la vapeur
dans le matelas de vapeur et, a contrario, de chauffer par des résistances électriques
chauffantes noyées dans l’eau du pressuriseur pour augmenter la pression si celle-ci
est trop basse (notons que ces résistances doivent rester noyées pour être efficaces).
Du fait des pertes calorifiques au travers du corps du pressuriseur, il est nécessaire de
chauffer constamment pour compenser ces pertes.
En conclusion, une augmentation du niveau d’eau conduit à une compression du
matelas de vapeur et une augmentation de la pression, ce qui induit une ouverture de
la vanne d’aspersion du pressuriseur, de la condensation d’une partie de la vapeur et
d’une ouverture de la décharge du RCV (dont l’effet est négligeable sur la pression).
Les résultats de ces actions sont une limitation de l’augmentation de pression (par
rapport à une situation libre sans action), puis une réduction de la pression. A contrario
, une baisse du niveau provoque une détente de la vapeur dans le volume libre du
pressuriseur et une baisse de la pression, ce qui va être contré par un chauffage accru
des chaufferettes, une vaporisation d’une partie de l’eau liquide et une ouverture de la
charge RCV (dont l’effet est négligeable sur la pression). Les résultats de ces actions
sont une limitation de la baisse de pression, puis une augmentation de celle-ci.
La puissance électrique totale d’un pressuriseur de CPY est au total de 1 440 kW,
délivrés par 60 chaufferettes, réparties en 4 groupes de chaufferettes Tout Ou Rien et
2 groupes de chaufferettes variables proportionnelles. Selon la valeur de la pression,
on engage les chaufferettes TOR (Tout Ou Rien, 1 008 kW) ou des chaufferettes
proportionnelles (432 kW), selon la régulation présentée dans la Figure 3.89. La vitesse
maximale de l’échauffement est de 112 ◦C/heure et le taux moyen pour compenser
les pertes thermiques et chauffer l’eau du pressuriseur est de 56 ◦C/heure.
L’aspersion est assurée par une douche d’eau prélevée d’une branche froide et injectée
par une « pomme de douche » qui micronise l’eau en gouttelettes offrant une
grande surface d’échange. En cas de montée anormale de la pression, un circuit de

<!-- page 385 (PDF 401) -->
Fig. 3.88 – Principe de la régulation de pression et de niveau du pressuriseur
(adapté d’après [Pressuriseur, 1977] p. 27).
Fig. 3.89 – Principe de la régulation du pressuriseur.

<!-- page 386 (PDF 402) -->
Fig. 3.90 – Régulation détaillée du pressuriseur.
décharge de vapeur permet d’évacuer rapidement la vapeur vers le réservoir de décharge
pressuriseur (RDP), où elle est condensée. La régulation du niveau d’eau se fait
par l’intermédiaire d’une consigne de niveau qui augmente avec la charge linéairement
en fonction de la moyenne de température des branches chaudes et froides (on fait la
moyenne branche par branche et on prend la plus élevée). Le niveau est impacté par
les appoints de charge et les rejets de décharge (qui est bloquée sur niveau très bas du
pressuriseur) grâce au RCV, et à l’action des chaufferettes TOR qui évaporent l’eau
excédentaire.
En ce qui concerne la mesure de la pression, un transmetteur de pression différentielle
est relié à une balance manométrique située hors enceinte. La pression différentielle
entre le primaire et le capillaire de la balance fournit l’induction de pression

<!-- page 387 (PDF 403) -->
pressuriseur en salle de commande. Cette mesure est une composante très importante
de la régulation automatique de pression. Cette régulation règle l’intensité du chauffage
pour une pression inférieure à la consigne ou bien le débit d’aspersion pour une
pression supérieure à la consigne, et ce, quelle que soit la charge du réacteur.
En ce qui concerne la protection du réacteur, l’arrêt automatique réacteur (AAR)
peut être engagé par pression trop basse ou pression trop haute, sur niveau trop haut
et l’injection de sécurité sur niveau bas et pression basse.

### 3.11.9 La ligne d’expansion du pressuriseur

Le pressuriseur communique avec le circuit primaire (branche chaude) via la ligne
d’expansion du pressuriseur (LEP), dont le circuit sinueux permet d’encaisser des
variations rapides de pression (Figure 3.91). Les différences de température entre la
branche chaude et le pressuriseur engendrent une stratification thermique dans la
LEP. Des fluctuations de cette stratification, en particulier pendant les transitoires
de charge, créent des variations de contraintes, d’où une fatigue thermique et un
dommage potentiel localisé au niveau des soudures en acier inoxydable en position
Fig. 3.91 – Ligne d’expansion du pressuriseur.

<!-- page 388 (PDF 404) -->
basse du coude de la LEP, en particulier les surfaces internes des soudures du coude
qui relient les parties horizontale et verticale du circuit, mais aussi la soudure de
raccordement de la LEP sur l’embout du pressuriseur. Ces zones présentent des particularités
géométriques (« délardage », bourrelets de soudure) qui augmentent les
contraintes. À la conception, on a déjà pris des mesures pour limiter ces contraintes.
Ainsi, un débit d’aspersion et un chauffage continu sont maintenus en permanence
dans le pressuriseur, et ce, afin d’éviter par un brassage continu une stratification
plus intense dans le pressuriseur. Une scrutation continue par fatigue-mètre menée
sur Dampierre a d’ailleurs montré que cette technique permettait de réduire d’un
facteur 10 le facteur d’usage de la LEP. Différents moyens de contrôle des soudures
incriminées existent. La plus classique, la radiographie permet de détecter des fissures
d’un minimum de 7 mm de hauteur lorsqu’on dispose de radiogrammes de référence
de la soudure neuve. Des études poussées ont montré qu’on pouvait aussi utiliser la
technique par ultrasons (code ULTSON 2D de EDF/R&D, Figure 3.92). Le principe
est de détecter les échos de diffraction ultrasonore, créés par les défauts et de les
différencier des échos de transformation d’onde habituels du fait des changements de
matériaux. On arrive ainsi à détecter des défauts supérieurs à 5 mm.

### 3.11.10 Éléments simplifiés de thermohydraulique du pressuriseur

Une aspersion par de l’eau froide en tête de pressuriseur permet de condenser la vapeur
de la bulle. La thermohydraulique du pressuriseur met donc en œuvre une interface
liquide/vapeur. Les équations de bilan des masses dans la zone inférieure liquide et la
zone supérieure vapeur doivent prendre en compte les échanges par cette interface.
Le bilan des masses de la zone liquide (liq) et vapeur (vap) s’écrit :
□
dmliq
dt
= Wle + Wcond,spray + Wcond,nat + Wspray −Wevap
dmvap
dt
= Wevap + Wsebim + Wscurit −Wcond,spray −Wcond,nat −Wspray
où Wle est le débit liquide de la ligne d’expansion du pressuriseur (en kg/s),
Wcond,spray le débit de condensation de l’aspersion, Wcond,nat le débit de condensation
par convection naturelle à l’interface, Wspray le débit d’aspersion et Wevap le
débit d’évaporation à l’interface. Le bilan enthalpique s’écrit :
⎧
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎩
d(mliqhliq)
dt
= Wlehle + Wcond,sprayhliq,sat + Wcond,nathliq,sat
+Wsprayhliq,sat −Wevaphvap,sat + Qtor + Qprop + Vliq
dp
dt −Qliq,fuite
d(mvaphvap)
dt
= Wevaphvap,sat −Wcond,sprayhliq,sat −Wcond,nat
(hvap −hvap,sat + Lliq→vap) −(Wscurit + Wsebim) hvap + Vvap
dp
dt −Qvap,fuite
où Qliq,fuite est la puissance perdue à travers l’enveloppe du pressuriseur par la zone
liquide, Qvap,fuite la puissance perdue par la zone vapeur, Qtor + Qprop la puissance
des chaufferettes tout ou rien et proportionnelles. Lliq→vap ≡hvap,sat −hliq,sat est la
chaleur latente de vaporisation. Ce modèle simple 31 suppose que l’eau d’aspersion,
P.E. Lebeau : Monte-Carlo estimation of generalized unreliability in probabilistic dynamics
– 1 : Application to a pressurized water reactor pressurizer, Nuclear Science and Engineering, vol.
126, pp. 131-145 (1997).

<!-- page 389 (PDF 405) -->
Fig. 3.92 – Analyse par ultrasons d’une soudure sur maquette (Villard et al., 2001,
EDF/R&D).
qui est prise depuis la branche froide du primaire, passe d’une enthalpie hspray à
l’enthalpie liquide à saturation hliq,sat en condensant de l’eau du volume de vapeur
selon un débit Wcond,spray, de telle sorte qu’à l’équilibre :
Wspray (hliq,sat −hspray)
=
Wcond,nat (hvap −hvap,sat + Lliq→vap)
=
Wcond,nat (hvap −hliq,sat)
Ceci explique que l’apport d’enthalpie de l’eau de l’aspersion est donné par
Wsprayhliq,sat. Le débit dans la ligne d’expansion doit compenser le débit total d’aspersion
et les variations de volume du primaire au cours du temps, à savoir :
Wle = −Wspray −Vprimaire
∂ρliq
∂Tprimaire
∂Tprimaire
dt
+ ∂ρliq
∂p
∂p
dt
□

<!-- page 390 (PDF 406) -->
Fig. 3.93 – Modélisation du pressuriseur
Si le débit dans la ligne d’expansion est positif, l’eau provient de la branche chaude
et hle = h(TBC, p), dans le cas contraire, c’est l’eau du pressuriseur qui se vide et
hle = hliq. On peut modéliser assez simplement la condensation et la vaporisation en
supposant que le débit est proportionnel à la masse en présence, à l’écart d’enthalpie à
la saturation et en introduisant un temps caractéristique de condensation τcondensation
ou de vaporisation τvaporisation
□
Wcond,nat =
m2(hvap,sat−h2)
τcondensationLliq→sat
si
hvap,sat ≥h2
Wevap,nat =
m2(h1−hliq,sat)
τevaporationLliq→sat
si
hliq,sat ≤h1
Ces débits sont nuls si les enthalpies ne permettent pas le phénomène. Il existe aussi
un débit d’évaporation propre au bilan net du chauffage et des fuites :
Wevap,chauffe =
⎧
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎩
Qtor+Qprop−Qliq,fuite−Qvap,fuite
hvap,sat−h1
si bilan de puissance positif et h1 < hliq,sat
Qtor+Qprop−Qliq,fuite−Qvap,fuite
Lliq→sat
si bilan de puissance positif et h1 ≥hliq,sat
si bilan de puissance n´egatif

### 3.11.11 Aspects sûreté du pressuriseur

Si la perforation du pressuriseur est un événement particulièrement peu crédible du
fait du casematage le protégeant d’éventuels missiles, les « points faibles » d’un

<!-- page 391 (PDF 407) -->
pressuriseur sont ses pénétrations naturelles. Les soupapes ressorts de dépressurisation
, placées en tête de pressuriseur ont historiquement posé des problèmes par
non-fermeture après plusieurs sollicitations. Le cas historique particulièrement sévère
est le cas de l’accident de TMI-2. Nous ne reprendrons pas ici les aspects sûreté liés
à cette problématique. L’autre point faible est la ligne d’expansion (LEP) qui relie
le pressuriseur à sa branche chaude. Pour ménager les contraintes thermiques qui s’y
appliquent, les STEs limitent le ΔT aux bornes de la ligne. Des situations paradoxales
ont pu conduire à dépasser inconsciemment ces limites.
L’incident du 17 septembre 1999 sur Civaux 2 en est l’illustration. Alors que le réacteur
est en arrêt à froid, les chaufferettes du pressuriseur ont été laissées en service
sans que cela soit détecté. Alors que les opérateurs commencent leur procédure de
redémarrage, procédure qui requiert que les prises de courant des chaufferettes soient
embrochées, la procédure est ensuite abandonnée pour traiter une indisponibilité sur
le RRI, sans que le débrochage soit effectué, les laissant donc actives. Au même moment
, le niveau d’activation du panneau auxiliaire, un panneau de secours du panneau
KIC de commande principale, n’était pas adéquat et donnait l’ordre de mise en service
automatique des chaufferettes. Cet ordre reste maintenu et prioritaire quand on
revient en commande par le KIC sans que l’opérateur en soit averti. Le chauffage par
les chaufferettes a donc été maintenu après l’arrêt de la procédure de redémarrage, et
ce, pendant 21 heures avec un gradient de 10 ◦C/h. C’est là que l’erreur humaine intervient
car de nombreux dispositifs (4 !) permettent de vérifier ce problème, mais leur
pouvoir d’alerte était faible, et l’attention des opérateurs était puissamment détournée
par l’indisponibilité du RRI. L’eau du pressuriseur s’est donc totalement vaporisée en
moins d’une heure et l’alarme Niveau très bas dans le pressuriseur a disparu prématurément
(et anormalement !), conduisant à une erreur d’orientation dans la procédure
d’approche par état (APE), pourtant sans incidence dans le cas présent. C’est ce qui
arrive lorsque des capteurs fournissent des indications hors de leur plage de mesure,
ce qui est le cas du niveau d’eau lorsque le pressuriseur est vide. Ce problème du
niveau d’eau dans le pressuriseur a déjà été une des causes principales de l’accident
de TMI-2. Conscient du peu de crédibilité de l’information donnée par ce capteur,
l’opérateur de Civaux, disposant de la version la plus récente de salle de commande
informatisée du parc, a choisi une orientation de conduite différente de celle proposée
par le calculateur d’APE. La situation s’est rapidement rétablie lorsqu’on a compris
que les chaufferettes étaient en marche, ce qu’indiquait pourtant le synoptique du
primaire. Force est de constater que l’opérateur n’a pas fait confiance au synoptique
dans la mesure où des essais avaient lieu sur le circuit secondaire. Clairement dans
cette affaire, c’est la méconnaissance du passage en automatique de la commande de
chauffage du pressuriseur lors du basculement de contrôle commande automatisé KIC
vers le panneau Auxiliaire, et le fait que l’action retour laisse le chauffage en marche,
qui sont les causes de l’incident. L’opérateur pensait que le chauffage était arrêté et
que le synoptique n’était pas conforme à la situation réelle. Néanmoins, l’informatisation
de la conduite APE a été mise en défaut par la prise en compte de valeur
hors gamme (ici le niveau d’eau dans le pressuriseur) de certains capteurs. Comme
toujours, la perception par l’opérateur de la globalité d’une tranche nucléaire reste
difficile. On notera aussi que l’aide informatique de l’APE peut être mise en défaut
par des valeurs de capteurs hors gamme.
Un incident à peu près identique s’est déroulé sur Gravelines 6 le 30 septembre 1999
où la détection d’air dans des tuyauteries du RIS, pendant le chauffage (à 70 ◦C à cet
