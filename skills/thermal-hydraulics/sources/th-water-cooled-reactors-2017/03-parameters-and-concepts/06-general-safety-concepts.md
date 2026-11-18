# General safety concepts
<!-- source PDF pages 35-40 -->

<!-- page 123 (PDF 35) -->
## 3.6.9 Verification and validation

Verification and Validation are concepts used in many engineering fields. In a first
approach, such concepts can be applied to any product, service, or system. In this context
to verify is to check that the product, service, or system is built as intended and to
validate is to check whether it works.
In the context of thermal hydraulics (D’Auria et al., 2012b; IAEA, 2015), verification
of a model is the process of confirming that the model is correctly implemented
with respect to its theoretical principles and equations. Similarly, validation of a
model is the process of checking its accuracy in the representation of the real system.
Also in the context of thermal hydraulics, verification and validation could be
applied to nodalizations (models or input decks) (Bonuccelli et al., 1993; Revento´s
et al., 2007a). The verification of a nodalization is the process of confirming that
the nodalization is implemented using the documentation that properly describes
the facility or the plant. Similarly, validation of a nodalization is the process of checking
its accuracy in the representation of the dynamic behavior of the real plant. Methodologies
exist to guide such processes.
3.7
General safety concepts

## 3.7.1 Safety objectives/safety culture

Fundamentals of safety of NPPs are explained in available documents of IAEA
(International Atomic Energy Agency) (IAEA 2000, 2002, 2006).
The fundamental safety objective is to protect people and the environment from
harmful effects of ionizing radiation. This means to guarantee that risk added by technology
is affordable and avoiding fission products release is assured. To do so, it is
necessary to establish and execute the engineering procedures devoted to accomplish
the mentioned objective.
Safety culture is that type of organizational culture, where safety is a value of
utmost priority, considered essential for the long-term success of the organization.
The issue is to make that safety culture strong and sustainable so that safety becomes
a primer responsibility of main focus for all types of activities. Nuclear safety has to be
highly integrated in nuclear business.
3.7.2
Accident management/emergency operating procedures/
severe accident management guidelines
AM is the systematic treatment or handling accident-related conditions with the purpose
of preventing it, avoiding its escalation to more serious event and mitigating its
consequences. In order to fulfill its goals AM establishes policies and plans that are
identified as strategies, guidelines, and procedures. Procedures describe actions
intending to be as concise as feasible. They establish a sequence of actions to be
followed step by step. Guidelines are less strict since actions to be taken are needed

<!-- page 124 (PDF 36) -->
of some evaluation. Strategies establish the general aspects of safety functions
recovery.
Emergency operating procedures (EOPs) are designed with the goal of avoiding or
delaying the accident progression to severe accident conditions. Bringing the plant to
an optimal plant state is their general goal.
Severe accident management guidelines (SAMGs) are designed with the goal of
mitigating severe accident consequences, by means of maintaining containment
functions and minimizing radiation relief (inside and outside). Reaching a secure
and stable plant condition at long term is their main goal.

## 3.7.3 Heat extraction safety relevance

The correct heat extraction from fuel keeps the integrity of the first safety barrier and
avoids accidental radioactivity release. As a general statement when damage is
avoided, accidental radioactivity release cannot progress.

## 3.7.4 Energy sources

Since damage can be produced by the failure of heat extraction, to predict the accident
progression, complete studies of energy sources are needed. Some different energy
sources have to be taken into account; among them are fission energy, stored energy,
residual energy, and energy due to core degradation.
Fission energy is produced by fission reaction. Its calculation is usually performed
by a neutron physics model. Such model can be rather simple as the so-called point
kinetics (or zero-D) model or quite complete as those based on neutron diffusion, neutron
transport, or Monte Carlo theories. The thermal-hydraulic analyst must decide on
the need of coupling the involved code with any neutron-kinetics model and also on
how detailed the related neutron physics model has to be.
Energy stored in fuel and structures is nonnegligible in some transient analyses.
The amount of stored energy depends on materials’ heat capacity and on temperature.
As a general statement, stored energy is the most significant heat source at the early
stages of most accidents. The blowdown dry-out in a LBLOCA is an example of core
heat-up produced by energy stored in the fuel. Another situation that has to do with
stored energy is the injection of rather cold water in a way that it contacts hot structures
of pipes and vessel. The energy stored in such structures will be partially
absorbed by injected water that will increase its temperature, hence decreasing the
cooling capability of the safety system.
Residual energy or decay heat is the energy produced by fission products within the
fuel rods. When fission chain is stopped due to reactor scram, decay heat starts
decreasing but it never becomes zero. Despite being a decreasing function, decay heat
could produce damage by itself. The accurate evaluation of decay heat could be performed
analyzing the built up and decay of fission products. Such calculation is connected
with fuel burn-up, historical power, and also the time after scram. In practice
some look-up tables are available and helpful to produce results that are good enough
for safety and design purposes.

<!-- page 125 (PDF 37) -->
During core degradation many different chemical reactions could occur among
fuel, structures, and degradation materials. Some of these reactions could be
exoenergetic and become significant in powering core degradation. Among such
reactions oxidation is the most relevant one. Oxidation could combine oxygen or
water with zirconium, stainless steel, or other materials. Zirconium oxidation is
exoenergetic at high temperature (more than 1000 K) and produces hydrogen that
when combined with air could produce explosions. Safety limits are set to avoid such
interactions.

## 3.7.5 Damage

Besides its essential goals of fulfilling acceptance criteria, thermal-hydraulic analysis
of DBA is devoted to assure that damage is not involved in the progression of such
scenarios. Although definitions are not fully established, authors use to distinguish
between failure and damage when facing fuel behavior in an accident scenario. In
most of technical literature, core damage occurs when strong degradation starts. Such
degradation could include mechanical and chemical transformation (including strong
cladding oxidation), components melting, and fission products release. All this would
occur at high or very high temperatures. The value of 1200°C (or 2200°F) as cladding
temperature, that is traditionally related with a well-known acceptance criterion in
licensing basis, is indirectly used as the threshold of damage. In this sense, it is also
accepted that other incipient degradation phenomena, for example, cladding oxidation
at lower temperatures, are usually not pointed out core damage.

## 3.7.6 Safety functions

Safety functions are specific purposes that must be accomplished to assure the general
safety objective. The accomplishment has to be performed in operational states, during
and following DBAs and, to the extent practicable, during and following the considered
plant conditions beyond DBA. The fulfillment of such functions is
continuously checked in emergency operation. They constitute an important guideline
for DBA and for emergency operation guide and procedures. General safety functions
are the following: subcriticality, heat extraction, and radioactivity confinement.
Subcriticality is the safety function related to reactivity control. It is used and
developed in the DB of systems dealing with reactivity control like control rods system
, reactor protection system, and safety injection. In emergency operation, it generates
the need of checking the ability to scram the reactor.
Heat extraction is the safety function related to removing heat from the core. It is
used and developed in the DB of systems established to do so in any operational situation
, like emergency core cooling. In emergency operation, it generates the need of
checking the capability of doing so.
Radioactivity confinement is the safety function related to radioactivity control. It
is used and developed in the DB of systems dealing with containment integrity and
radioactivity extraction like containment building systems. In emergency operation,
it generates the need of checking the availability of such systems.

<!-- page 126 (PDF 38) -->
## 3.7.7 Defense in depth

Following IAEA definition: defense in depth is a comprehensive approach to safety
that has been developed by nuclear power experts to ensure with high confidence that
the public and the environment are protected from any hazards posed by the use of
nuclear power for the generation of electricity. The concepts of defense in depth
and safety culture have served the nuclear power industry well as a basic philosophy
for the safe design and operation of NPPs.
In such approach, it is established that the general objective of safety will be
accomplished making provisions at different levels and considering different physical
barriers to confine radioactivity.

## 3.7.8 Defense in depth levels

The five levels of actuation in defense in depth approach are the following:
Level 1 Prevention of abnormal operation and failures (provisions are made to avoid abnormal
behavior).
Level 2 Control of abnormal operation and detection of failures (provisions are made to
recover normal behavior).
Level 3 Control of accidents within the DB (provisions are made to avoid damage)
Level 4 Control of severe plant conditions, including prevention of accident progression
and mitigation of the consequences of severe accidents (provisions are made to limit
damage)
Level 5 Mitigation of radiological consequences of significant releases of radioactive materials
(provisions are made to limit radioactivity release)

## 3.7.9 Safety barriers

Safety barriers are physical obstructions or walls established to confine the radioactive
material at specified locations. Typically for water reactors, the considered barriers
are the fuel cladding, the reactor coolant system pressure boundary, and the containment
building. Some authors consider the fuel matrix as an additional safety barrier.

## 3.7.10 Safety systems/safety-related systems

Two kinds of systems are pointed out as important for safety: safety systems and
safety-related systems.
Safety systems are systems directly necessary to assure the performance of safety
functions. They are designed following specific codes and include protections and
safeguards.
Protection systems use to monitor the operation of a component (usually the reactor
) following the values of relevant parameters. Once any abnormal condition is
detected through a critical value of the surveilled parameter, the system automatically
initiates actions to prevent an unsafe situation. The most significant preventive action
is usually to stop the equipment (to scram the reactor).

<!-- page 127 (PDF 39) -->
Engineered safeguards are SSCs designed to keep the safety functions. There are
safeguards of different natures, among them: containment systems, emergency core
cooling systems, secondary side safeguards, systems related to control room habitability
and complementary systems.
In spite of control systems (or controls) contributing to levels 1 and 2 of defense in
depth, they are not considered safety systems.
Safety-related systems are systems whose failure has a safety impact. They are
classified in three categories: Safety Class 1, 2, and 3.
Safety Class 1 Systems are those whose failure could produce a LOCA (Category 3 or 4)
Safety Class 2 Systems are the rest of SSCs belonging to Reactor Coolant System pressure
boundary.
Safety Class 3 Systems include those whose failure could produce a release to environment,
those that support other safety systems and those controlling radioactivity.

## 3.7.11 Inherent safety/passive safety/active safety

Safety is highly integrated in design and performs properly because of many different
implementations.
Among the different ways to perform safety in a plant, inherent safety is maybe
the most effective. Inherent safety features are those that bring the plant to safe situation
based on the initiator itself without the need of designing any additional
safety system. Fail-safe designs are in this category. Current plants have only a
few inherent safety features. Inherent safety is in the conceptual design of some
future plants.
Passive safety is the one that brings the plant to safe situation-based passive
systems actuation. A passive system performs its function without any manual action
and without the need of electrical power. Second generation power plants have some
passive safety system. Some of the third generation power plants are fully passive
(Batet, 2004; IAEA, 2009).
So, safety in current plants, having a few inherent safety features and some passive
safety system, is basically active. This means that to perform safety in current plants
electrical power is needed in short term and manual actions are also needed at midterm
. Some engineered features are needed to help availability of safety systems and
thus avoid plant vulnerability. IAEA identifies and gives the definition (see below) of
three of such features: redundancy, diversity, and independence. Design robustness is
an additional feature connected with usual design practices.
Redundancy is the use of more than the minimum number of sets of equipment to
fulfill a given safety function; it is an important design principle for achieving high
reliability in systems important to safety and for meeting the single failure criterion
for safety systems. Redundancy enables failure or unavailability of at least one set of
equipment to be tolerated without loss of the function.
Diversity is applied to redundant systems or components that perform the same
safety function by incorporating different attributes into the systems or components.
Such attributes could be different principles of operation, different physical variables,

<!-- page 128 (PDF 40) -->
different conditions of operation, or production by different manufacturers. Diversity
helps minimize the risk of common cause failure.
Independence is accomplished in the design of systems by using functional isolation
and physical separation:
l
Functional isolation that should be used to reduce the likelihood of adverse interaction
between equipment and components of redundant or connected systems resulting from normal
or abnormal operation or failure of any component in the systems.
l
Physical separation and layout of plant components that should use physical separation as far
as practicable to increase assurance that independence will be achieved, particularly in relation
to certain common cause failures.
Design practices consider robustness as an important additional feature that needs to
be taken into account especially when reliability of systems involved is a first priority.
The adequate size of safeguards is an example of design robustness.

## 3.7.12 International institutions

The Nuclear Energy Agency (NEA) is an OECD institution which strategic areas are
the following:
l
Serve as a forum for sharing and analyzing information and experience among member
countries
l
Foster international cooperation in the nuclear field
l
Help member countries to pool and maintain their technical expertise and human infrastructure
, and support their nuclear activities.
l
Provide member countries with nuclear policy analyses
Activities and projects, conferences or specialist meetings (OECD/NEA/CSNI, 1992,
2000, 2011), and state-of-the-art reports (OECD/NEA/CSNI, 1989, 2016a) are the initiatives
used for developing such strategic areas.
In EURATOM’s tasks definition one can find statements related to research and
safety such as promoting research and ensuring the dissemination of technical information
; and establishing uniform safety standards to protect the health of workers and
of the general public and ensure that they are applied.
And also, other statements related to: equitable supply of nuclear fuels (making
certain, by appropriate supervision, that nuclear materials are not diverted to purposes
other than those for which they are intended); exercise the right of ownership conferred
upon it with respect to special fissile materials; exercise the right of ownership
conferred upon it with respect to special fissile materials; establish with other countries
and international organizations such relations as will foster progress in the
peaceful uses of nuclear energy, and so on.
The former group results in the network of joint research centers all over Europe:
Petten (Netherlands), Geel (Belgium), Karlsruhe (Germany), Ispra (Italy), and Sevilla
(Spain). The latter results in all activities related with nuclear materials and peaceful
uses of nuclear energy.
In the tasks definition of the IAEA one can find also statements related to research,
science and technical information like: to encourage and assist research…; to make
provision,…, for materials, services, equipment, and facilities to meet the needs; to
