# Chapitre 7 Les principaux circuits — 7.1 Généralités — 7.1 Généralités … 7.2.1 Généralités
<!-- source PDF pages 859-870 -->

<!-- page 843 (PDF 859) -->
# Chapitre 7 Les principaux circuits

La circuiterie d’un REP est par nature complexe et il ne s’agit pas ici de décrire
l’ensemble des milliers de vannes, clapets, réservoirs. . . que constitue une tranche.
Néanmoins, il est utile de connaître les principaux circuits et leur rôle tant au niveau
du fonctionnement normal qu’ incidentel.

## 7.1 Généralités

[Drevon et al., 1983] p. 261
Outre le circuit secondaire auquel nous consacrons un chapitre entier, les circuits
annexes du circuit primaire (Figure 7.1) sont tous nomenclaturés par la lettre R.
Citons le circuit de refroidissement à l’arrêt (RRA), uniquement utilisé en dessous de
32 bars pour le CPY ou 25 bars pour le P4. Le RRA est lui-même refroidi par un
système tampon entre la source froide, le circuit de réfrigération intermédiaire (RRI).
Le RRI échange sa chaleur au circuit SEC qui prend son eau à la source froide, mer ou
rivière. C’est le circuit RCV qui assure l’appoint en eau du primaire (ou le trop-plein)
et le conditionnement chimique de ce dernier.
Les circuits principaux de sauvegarde (Figure 7.2) sont constitués de l’injection de
sécurité (RIS), du secours en eau des GVs (ASG) remédiant à une déficience de l’eau
normale (circuit ARE), et du circuit d’aspersion de l’enceinte (EAS) dont le rôle est
de refroidir l’enceinte.

## 7.2 Le circuit de contrôle volumétrique et chimique (RCV)

[Système de contrôle volumétrique et chimique, 1978], [Coppolani et al., 2004] p. 144,
[Tong, 1988] p. 189
Le circuit RCV est situé en partie dans le BR (partie dite « haute énergie »), et
l’autre partie (« basse énergie ») est située dans le BAN. Pour se prémunir du risque
d’incendie au niveau des pompes de charge RCV (huile auto-inflammable à 220 ◦C),
celles-ci sont placées dans des locaux séparés à détection d’incendie et dispositif fixe
d’extinction à poste. Les organes d’isolement peuvent être commandés à distance. Les
voies d’alimentation électriques (voie A et voie B) sont aussi séparées.

<!-- page 844 (PDF 860) -->
Fig. 7.1 – Les principaux circuits annexes du circuit primaire (adapté d’après
[Présentation générale des centrales PWR du palier 900 MWe, Fascicule 302] p. 13).

### 7.2.1 Généralités

Le circuit RCV a plusieurs fonctions. En premier lieu, il permet de contrôler le
volume d’eau dans le primaire, par ses connexions avec le primaire (Figure 7.3). Les
importantes variations de températures de l’eau du primaire, lorsqu’on passe de l’état
à froid à l’état en attente à chaud, puis en puissance, créent par dilatation de l’eau
des variations importantes de volume. Par un rapide calcul (Figure 7.7), à 20 ◦C, le
primaire d’un CPY (274 m3) contient 274 tonnes d’eau. En arrêt à chaud (286 ◦C),
ces 274 tonnes occuperaient un volume de 370 m3 du fait de la dilatation de l’eau.
Ces 96 m3 excédentaires ne peuvent être encaissés par le pressuriseur ; d’où la fonction
d’extraction du RCV. C’est pourquoi il faut soutirer de l’eau pour contrôler
la pression. Le problème est inverse lorsqu’on revient à froid. Le RCV (Figure 7.4)
extrait de l’eau par la ligne de décharge (en boucle 2 des tranches paires, boucle 3 des

<!-- page 845 (PDF 861) -->
Fig. 7.2 – Les principaux circuits de sauvegarde (adapté d’après [Présentation générale
des centrales PWR du palier 900 MWe, Fascicule 302] p. 73).
Fig. 7.3 – Connexion entre le RCP et le RCV (CPY).

<!-- page 846 (PDF 862) -->
Fig. 7.4 – Le RCV du palier P4 (adapté de [Centrales Nucléaires EDF de 1 300 MW,
1991] p. 29).
tranches impaires) et en injecte par la ligne de charge (Figure 7.8) (en boucle 1 pour
les tranches paires, boucle 2 pour les tranches impaires). Notons qu’une ligne de soutirage
excédentaire, reliée au primaire par l’intermédiaire d’une ligne de drainage de la
boucle 2, permet d’effectuer de la décharge lorsque le circuit normal de décharge n’est
pas disponible ou lorsque le débit à soutirer serait trop important pour ce dernier. En
ce qui concerne la décharge principale, l’eau est prélevée par un collecteur de deux
pouces (CPY) pouvant extraire jusqu’à 28,6 m3/heure. L’eau traverse le casematage
anti-missile, un échangeur régénérateur d’où elle sort refroidie à moins de 180 ◦C,
des orifices de détente pour abaisser sa pression, un sectionnement d’isolement à la
traversée de l’enceinte du BR, un nouvel échangeur régénérateur qui abaisse sa température
à environ 50 ◦C (alarme à 57 ◦C, bipasse automatique à 60 ◦C) de façon à
être compatible à son passage au travers des résines d’épuration (qui fondraient à une
température plus élevée en polluant par effet « caramel mou » l’ensemble des lignes
de charge du RCV !). La ligne de soutirage excédentaire possède un débit plus faible
(de l’ordre de 3,4 tonnes/heure) et n’est utilisée que rarement dans des situations
de démarrage (fin de la phase de chauffage), d’avarie de la ligne principale (rupture
ou isolement intempestif par la fermeture d’une vanne pneumatique, de la ligne de
décharge), ou lors de la formation de la bulle au pressuriseur.
Pour éviter des transitoires thermohydrauliques, les actions de charge et de
décharge sont en fait continues, et c’est le différentiel entre charge et décharge qui
définit l’appoint positif ou négatif d’eau selon le besoin. Les liaisons permanentes

<!-- page 847 (PDF 863) -->
assurant cette fonction sont appelées charge et décharge. Une ligne dite d’aspersion
auxiliaire permet également d’injecter de l’eau du RCV dans la phase vapeur du pressuriseur
, lorsque l’aspersion normale du pressuriseur n’est pas disponible à l’arrêt des
pompes primaires (c’est le différentiel de pression dû à la pompe primaire qui fait
fonctionner l’aspersion normale du pressuriseur). Les lignes de décharge, de charge et
d’injection aux joints des pompes primaires sont ouvertes en fonctionnement normal.
Réciproquement, les lignes de soutirage excédentaire et d’aspersion auxiliaire sont
fermées en situation normale.
Le débit RCV dépend du palier considéré et du mode de fonctionnement à un ou
deux orifices :
CPY ⇒13, 6 tonnes d′eau/heure ≤QRCV ≤27 tonnes d′eau/heure
1300MWe et N4 ⇒18 tonnes d′eau/heure ≤QRCV ≤36 tonnes d′eau/heure
Le ballon RCV (Figure 7.5, Figure 7.6) joue le rôle de réservoir tampon (8,5 m3
dont 3,4 m3 de liquide) entre charge et décharge. Il est connecté par des liaisons
hydrauliques au niveau des branches froides du circuit primaire. Le RCV ne peut
absorber à lui seul les plusieurs dizaines de mètres cubes d’eau dans certains cas
d’expansion ou de contraction. De fait, le RCV sera obligé de produire des effluents
vers d’autres systèmes de traitement (TEP, TEG).
Fig. 7.5 – Schéma de principe du RCV.
En fonction normale, l’eau est prélevée par un piquage dans une branche froide du
circuit primaire (à 286 ◦C) (Figure 7.8), et elle doit être refroidie à environ 45 ◦C sous
2 bars car l’eau doit rester liquide. Cette opération d’abaissement de la température

<!-- page 848 (PDF 864) -->
Fig. 7.6 – Schéma fonctionnel du RCV (adapté de [Système de contrôle volumétrique
et chimique, 1978] p. 32).
Fig. 7.7 – Volume spécifique de l’eau en fonction de la température (adapté de
[Système de contrôle volumétrique et chimique, 1978] p. 6).

<!-- page 849 (PDF 865) -->
Fig. 7.8 – Le circuit RCV : vue d’ensemble.
entraîne des pertes thermiques qu’on limite en utilisant un échangeur-régénérateur
qui permet de refroidir le prélèvement par l’eau refroidie déjà épurée et donc de récupérer
les calories. Cet échangeur-régénérateur est placé dans le bâtiment réacteur. Un
refroidisseur non régénérateur, situé lui dans le BAN, reste cependant nécessaire pour
amener l’eau à 45 ◦C. Du fait de la pression de service de 2 bars, il faut faire attention
à éviter la vaporisation de l’eau lors de la détente de 155 bars à 2 bars (Figure 7.9).
Pour rester en dessus de la courbe de vaporisation, on effectue la détente en deux
étapes en amont des deux étapes de refroidissement. On profite de cette épuration de
l’eau pour la faire dégazer des éventuels produits de fission gazeux incondensables qui
s’y trouveraient (du fait de défauts de gainage) dans le réservoir tampon du RCV.
Une fois traitée, on y adjoint le bore et les différents additifs liés à la chimie de l’eau
(Figure 7.10). L’eau est ensuite réchauffée dans l’échangeur-régénérateur (de type tube
en U et virole) puis réinjectée dans une autre branche froide que celle du prélèvement.
La fonction « épuration » (Figure 7.11) permet aussi d’effectuer un balayage à
l’azote pendant les opérations préliminaires au réchauffage du circuit, c’est-à-dire
pendant la phase de retrait de l’oxygène de l’eau du RCV (par mises sous vide successives
en vidangeant le réservoir). Ce balayage d’azote est aussi utilisé pour diminuer
la concentration d’hydrogène de l’eau du primaire lors des arrêts avec ouverture du
circuit primaire.
Notons aussi qu’au démarrage, c’est le RCV qui assure le remplissage et la pressurisation
du circuit primaire jusqu’à 25 bars où se forme la bulle dans le pressuriseur
(Figure 7.11). À partir de cette pression, ce sont les chaufferettes du pressuriseur qui
font monter la pression.

<!-- page 850 (PDF 866) -->
Fig. 7.9 – Parcours des détentes de l’eau primaire à travers les refroidisseurs
(d’après [Système de contrôle volumétrique et chimique, 1978] p. 18).
Fig. 7.10 – Contrôle chimique du RCV.

<!-- page 851 (PDF 867) -->
Fig. 7.11 – Utilisation du RCV (adapté d’après [Système de contrôle volumétrique et
chimique, 1978] p. 27).

<!-- page 852 (PDF 868) -->
Les principaux éléments du RCV (exemple du CP2, Figure 7.12, Figure 7.13,
Figure 7.14) sont :
• les pompes de charge RCV 001 à 003 P0. Ces pompes sont puissantes et assurent
une hauteur manométrique comprise entre 450 m CE et 1 700 m CE. Rappelons
qu’elles doivent pousser l’eau dans le circuit primaire qui est à 155 bars au
nominal ;
• la ligne de débit nul des pompes de charge ;
• les échangeurs RCV 001 EX (régénérateur), RCV 002 RF, RCV 003 RF et
RCV 021 RF (non régénérateurs) ;
• la ligne de décharge, munie de vannes réglantes (RCV 013 VP, RCV 030 VP)
et les orifices de détente HP RCV 001 à 003 DI ainsi que les vannes d’isolement
RCV 002 VP et RCV 003 VP ;
• la ligne de charge munie de la vanne réglante RCV 045 VP et la vanne d’isolement
RCV 050 VP. Le débit de charge du RCV est régulé par la chaîne
RCV 046 RG lorsque le pressuriseur est diphasique via la vanne réglante
RCP 014 RG. La mesure du débit de charge est donnée par un capteur situé en
amont de la vanne RCV 046 VP ;
• la ligne d’aspersion de secours munie de la vanne d’isolement RCV 227 VP ;
• la liaison RRA-RCV munie de la vanne RCV 310 VP ;
• la ligne d’étanchéité des pompes primaires, munie de la vanne réglante
RCV 061 VP ;
• la ligne de soutirage excédentaire munie des vannes réglantes RCV 258 et
259 VP ;
• le piquage sur la ligne de décharge vers le circuit TEP, muni de la vanne
RCV 030 VP ;
• le piquage sur l’aspiration des pompes de charge, correspondant à la liaison avec
le système PTR, via le RIS avec les vannes RIS 012 et 013 VP. Les pompes de
charge peuvent aspirer l’eau du réservoir RCV jusqu’à un niveau de 3 % du
ballon, ensuite l’aspiration bascule sur la bâche PTR pour éviter la cavitation
et assurer la fonction de charge ;
• le piquage à l’amont des pompes de charge, représentant la liaison avec le système
REA, avec le clapet RCV 142 VP ;
• le réservoir RCV 002 BA. Le niveau de ce réservoir est réglé par une régulation,
piloté par un capteur (RCV 011 MN), qui pilote la vanne réglante RCV 030 VP
qui dirige une fraction du débit de décharge vers le circuit TEP, si le niveau
dépasse la consigne. Sur seuil bas, on initie l’appoint automatique en eau REA,
par les vannes RCV 154 VP et RCV 117 VP. Sur seuil très bas, l’opérateur isole
le réservoir du circuit de charge et connecte l’aspiration des pompes de charge
au circuit PTR.

<!-- page 853 (PDF 869) -->
Fig. 7.12 – Lignage stéréoscopique du RCV.
Fig. 7.13 – Les différentes fonctions du RCV.

<!-- page 854 (PDF 870) -->
Fig. 7.14 – Situation du RCV en phase de rechargement, démarrage ou réacteur
en puissance (adapté de [PWR 900 MWe, Signification physique des STE], p. A14).
En mode monophasique, une chaîne de régulation (RCV 013 RG) règle la pression
à l’aspiration RRA (par la vanne réglante RCV 013 VP). En mode diphasique,
cette vanne règle la pression en aval des orifices de détente HP. La pression est alors
donnée par un capteur situé en aval de l’échangeur non régénérateur RCV 002 RF.
La température en aval de cet échangeur est régulée en agissant sur le débit d’eau de
réfrigération.
Le RCV assure aussi d’autres fonctions annexes comme l’aspersion auxiliaire du
pressuriseur (pour le palier 900 MWe), en cas de non-fonctionnement des pompes primaires
(dans la fin de la phase de refroidissement lors de l’arrêt des pompes primaires).
Le circuit RCV assure aussi l’injection d’eau aux joints de pompes primaires, pour
faire contre-pression à la pression primaire (voir le chapitre sur les pompes primaires).
Un certain nombre de grandeurs physiques du circuit RCV sont régulées : le niveau
du pressuriseur via le débit de charge/décharge, le niveau du réservoir tampon du RCV
via le débit entrant/sortant du réservoir tampon 1, la pression amont de détente basse
pression (pour éviter une vaporisation pendant la détente HP) via le débit d’eau de
détente BP, la température amont de détente haute pression via de débit d’eau de
refroidissement de l’échangeur-régénérateur, et la concentration en hydrogène de l’eau
primaire via la pression de réservoir tampon RCV (réglage du détendeur d’admission
d’hydrogène au réservoir).
Différentes sécurités protègent le circuit RCV, à savoir l’isolement de la décharge
par très bas niveau dans le pressuriseur, le contournement des déminéraliseurs par
1 Par l’intermédiaire d’un régulateur P.I.D. (Proportionnel, Intégral, Dérivé).
